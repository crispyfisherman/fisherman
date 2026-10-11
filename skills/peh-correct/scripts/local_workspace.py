#!/usr/bin/env python3
"""Resolve an external personal workspace without changing the target repo."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess


def workspace_for(repo, base_dir=None):
    repo = Path(repo).expanduser().resolve(strict=True)
    result = subprocess.run(
        ["git", "-C", str(repo), "rev-parse", "--show-toplevel"],
        check=True, capture_output=True, text=True,
    )
    repo = Path(result.stdout.strip()).resolve(strict=True)
    default = Path(os.environ.get("XDG_DATA_HOME", Path.home() / ".local/share"))
    base = Path(base_dir).expanduser().resolve() if base_dir else (
        default / "personal-engineering-harness/projects"
    ).expanduser().resolve()
    label = re.sub(r"[^a-zA-Z0-9._-]", "-", repo.name)[:48] or "repository"
    digest = hashlib.sha256(os.fsencode(repo)).hexdigest()[:16]
    workspace = (base / f"{label}-{digest}").resolve()
    if workspace == repo or repo in workspace.parents:
        raise ValueError("Personal workspace must be outside the target repository")
    # Worktrees share repository metadata. Keep personal state outside that too.
    common = subprocess.run(
        ["git", "-C", str(repo), "rev-parse", "--git-common-dir"],
        check=True, capture_output=True, text=True,
    ).stdout.strip()
    common_dir = (repo / common).resolve() if not Path(common).is_absolute() else Path(common).resolve()
    if workspace == common_dir or common_dir in workspace.parents:
        raise ValueError("Personal workspace must be outside git metadata")
    return {"repo": str(repo), "project_key": f"{label}-{digest}", "workspace": str(workspace)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", required=True)
    parser.add_argument("--base-dir", help="Optional external personal destination")
    parser.add_argument("--create", action="store_true", help="Create the external directory")
    args = parser.parse_args()
    try:
        info = workspace_for(args.repo, args.base_dir)
        if args.create:
            Path(info["workspace"]).mkdir(parents=True, exist_ok=True, mode=0o700)
        print(json.dumps(info, indent=2))
    except (OSError, ValueError, subprocess.CalledProcessError) as exc:
        parser.exit(2, f"Cannot resolve personal workspace: {exc}\n")


if __name__ == "__main__":
    main()
