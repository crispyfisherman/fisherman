#!/usr/bin/env python3
"""Install personal skills for Codex and/or Claude Code using owned symlinks."""
import argparse
import json
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]


def available_skills():
    return sorted(p.name for p in (ROOT / "skills").iterdir() if (p / "SKILL.md").is_file())


def link_matches(link, source):
    return link.is_symlink() and link.resolve() == source.resolve()


def claude_content(name):
    content = (ROOT / "skills" / name / "SKILL.md").read_text()
    match = re.match(r"\A---\n(.*?)\n---\n", content, re.S)
    if not match:
        raise ValueError(f"Invalid skill frontmatter: {name}")
    extra = "\ndisable-model-invocation: true"
    if name == "peh-review":
        extra += "\ncontext: fork\nagent: general-purpose\nbackground: false\neffort: high"
    return "---\n" + match.group(1) + extra + "\n---\n" + content[match.end():] + (
        "\n## Invocation inputs\n\nUse the following task scope and instructions:\n\n$ARGUMENTS\n"
    )


def generate_claude(name):
    canonical = ROOT / "skills" / name
    generated = ROOT / ".generated/claude/skills" / name
    if generated.is_symlink():
        raise ValueError(f"Refusing generated-directory symlink: {generated}")
    marker = generated / ".peh-generated"
    if generated.exists() and not marker.is_file():
        raise ValueError(f"Unmanaged generated directory: {generated}")
    generated.mkdir(parents=True, exist_ok=True)
    marker.write_text("Managed by personal-engineering-harness/scripts/install.py\n")
    (generated / "SKILL.md").write_text(claude_content(name))
    for source in canonical.iterdir():
        if source.name == "SKILL.md":
            continue
        dest = generated / source.name
        if dest.exists() or dest.is_symlink():
            if not link_matches(dest, source):
                raise ValueError(f"Unmanaged generated resource: {dest}")
        else:
            dest.symlink_to(source, target_is_directory=source.is_dir())
    return generated


def plan_for(target, selected, home):
    plan = []
    for host in (["codex", "claude"] if target == "both" else [target]):
        location = home / (".agents/skills" if host == "codex" else ".claude/skills")
        for name in selected:
            source = ROOT / "skills" / name if host == "codex" else ROOT / ".generated/claude/skills" / name
            plan.append((host, location / name, source))
    return plan


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", choices=["codex", "claude", "both"], default="both")
    parser.add_argument("--home", type=Path, default=Path.home(), help="Override user home for a sandbox installation")
    parser.add_argument("--skills", nargs="+", choices=available_skills())
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--uninstall", action="store_true")
    args = parser.parse_args()
    selected = list(dict.fromkeys(args.skills or available_skills()))
    plan = plan_for(args.target, selected, args.home.expanduser().resolve())
    conflicts = [str(dest) for _, dest, source in plan
                 if (dest.exists() or dest.is_symlink()) and not link_matches(dest, source)]
    if conflicts:
        parser.exit(2, "Refusing to overwrite or remove other skills:\n" + "\n".join(conflicts) + "\n")
    # Check generation conflicts before touching installed links.
    if not args.uninstall:
        for host, _, source in plan:
            if host == "claude" and source.exists() and not (source / ".peh-generated").is_file():
                parser.exit(2, f"Unmanaged generated directory: {source}\n")
    try:
        if not args.dry_run and not args.uninstall and args.target in ("claude", "both"):
            for name in selected:
                generate_claude(name)
        for host, dest, source in plan:
            action = "remove" if args.uninstall else "link"
            if not args.dry_run:
                if args.uninstall:
                    if link_matches(dest, source):
                        dest.unlink()
                else:
                    dest.parent.mkdir(parents=True, exist_ok=True)
                    if not link_matches(dest, source):
                        dest.symlink_to(source, target_is_directory=True)
            print(json.dumps({"host": host, "action": action, "destination": str(dest), "source": str(source), "dry_run": args.dry_run}))
    except (OSError, ValueError) as exc:
        parser.exit(2, f"Installation failed: {exc}\n")
    if not args.dry_run:
        print("Restart the CLI if the skill list has not refreshed. Keep this repository at its current path.")


if __name__ == "__main__":
    main()
