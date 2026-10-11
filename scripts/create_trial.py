#!/usr/bin/env python3
"""Create a disposable Git repository for blind skill trials."""
import argparse
import json
from pathlib import Path
import shutil
import subprocess


ROOT = Path(__file__).resolve().parents[1]


def git(repo, *args):
    return subprocess.run(["git", "-C", str(repo), *args], check=True, capture_output=True, text=True).stdout.strip()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--destination", type=Path, required=True)
    args = parser.parse_args()
    destination = args.destination.expanduser().resolve()
    if destination.exists():
        parser.exit(2, "Destination already exists; choose a new disposable path.\n")
    if destination == ROOT or ROOT in destination.parents:
        parser.exit(2, "Choose a destination outside the skills repository.\n")
    shutil.copytree(ROOT / "fixtures/checkout", destination, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    (destination / ".gitignore").write_text("__pycache__/\n*.pyc\n")
    git(destination, "init", "-b", "main")
    git(destination, "config", "user.name", "PEH Trial")
    git(destination, "config", "user.email", "trial@example.invalid")
    git(destination, "add", ".")
    git(destination, "commit", "-m", "Add checkout behavior and contract")
    base = git(destination, "rev-parse", "HEAD")
    git(destination, "checkout", "-b", "reorganize-checkout")
    service = destination / "app/service.py"
    service.write_text(service.read_text().replace(
        "        reserve_stock(db, sku, quantity)\n        db.execute(",
        "        reserve_stock(db, sku, quantity)\n    with db:\n        db.execute(",
    ))
    git(destination, "add", "app/service.py")
    git(destination, "commit", "-m", "Separate checkout transaction blocks")
    head = git(destination, "rev-parse", "HEAD")
    print(json.dumps({
        "repository": str(destination), "base": base, "head": head,
        "contract": str(destination / "CONTRACT.md"),
        "review_prompt": f"Use peh-review to review {base}...{head} in {destination}. Read CONTRACT.md for intent. Do not read review-comments.md or other review outputs. Do not edit source, post, or merge.",
        "study_prompt": f"Use peh-trace-system in study mode in {destination}. I have 25 minutes and want to learn the checkout flow so I can support a teammate. Explain one boundary clearly, with concrete values and code anchors, and one optional prediction question. Do not edit source.",
        "triage_prompt": f"Use peh-interrogate in {destination} to verify the supplied independent review and review-comments.md at {head}. Do not add another blind reviewer, fix source, post, or merge.",
    }, indent=2))


if __name__ == "__main__":
    main()
