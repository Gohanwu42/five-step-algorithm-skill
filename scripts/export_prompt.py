#!/usr/bin/env python3
"""Export the skill body as a standalone prompt, or check that it is current."""

import argparse
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Check without writing")
    args = parser.parse_args()
    skill_dir = Path(__file__).resolve().parents[1] / "five-step-algorithm"
    source = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
    parts = source.split("---\n", 2)
    if len(parts) != 3 or parts[0]:
        parser.error("SKILL.md must start with a complete YAML frontmatter block")
    expected = parts[2].lstrip("\n").rstrip() + "\n"
    target = skill_dir / "prompt.txt"
    if args.check:
        if not target.exists() or target.read_text(encoding="utf-8") != expected:
            parser.exit(1, "prompt.txt is out of date; run scripts/export_prompt.py\n")
        print("Standalone prompt matches SKILL.md.")
    else:
        target.write_text(expected, encoding="utf-8")
        print("Updated five-step-algorithm/prompt.txt")


if __name__ == "__main__":
    main()
