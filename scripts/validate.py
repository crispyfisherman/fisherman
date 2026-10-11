#!/usr/bin/env python3
"""Validate portable skill metadata, resources, and generated adapter contracts."""
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]


def main():
    errors = []
    skills = sorted((ROOT / "skills").glob("*/SKILL.md"))
    if len(skills) != 6:
        errors.append(f"Expected six skills, got {len(skills)}")
    for path in skills:
        content = path.read_text()
        front = re.match(r'\A---\nname: ([a-z0-9-]+)\ndescription: "([^\n]+)"\n---\n', content)
        if not front or front.group(1) != path.parent.name:
            errors.append(f"Invalid canonical frontmatter: {path}")
            continue
        if len(front.group(1)) > 64 or len(front.group(2)) > 1024:
            errors.append(f"Metadata exceeds portable limits: {path}")
        if "[TODO:" in content:
            errors.append(f"Unfinished skill: {path}")
        if len(content.splitlines()) >= 500:
            errors.append(f"Skill needs progressive disclosure: {path}")
        for reference in re.findall(r'\]\(([^)]+)\)', content):
            if not reference.startswith(("https:", "http:", "#")) and not (path.parent / reference).is_file():
                errors.append(f"Missing reference {reference}: {path}")
        metadata = path.parent / "agents/openai.yaml"
        meta = metadata.read_text() if metadata.is_file() else ""
        for required in ('display_name:', 'short_description:', f'${path.parent.name}', 'allow_implicit_invocation: false'):
            if required not in meta:
                errors.append(f"Missing {required}: {metadata}")
        print(f"{path.parent.name}: {len(content.split())} words, {len(content.splitlines())} lines")
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    print("Six canonical skills and standalone references validated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
