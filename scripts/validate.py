#!/usr/bin/env python3
"""Validate the skill library: Agent Skills front-matter, structure, and index sync."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import build_index as bi  # noqa: E402

REQUIRED_FILES = [
    "README.md",
    "index/skills.json",
    ".claude-plugin/marketplace.json",
    ".claude-plugin/plugin.json",
    "docs/how-skills-work.svg",
    "docs/skill-anatomy.svg",
    "docs/skill-map.svg",
    "scripts/build_index.py",
    "scripts/import_prompts.py",
    "scripts/validate.py",
    ".github/workflows/validate.yml",
]
REQUIRED_HEADINGS = [
    "## Inputs to collect",
    "## Instructions",
    "## What good output looks like",
    "## Follow-ups",
    "## Guardrails",
]
NAME_PATTERN = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
PLACEHOLDER = re.compile(r"\{\{[a-z0-9_]+\}\}")

errors: list[str] = []


def check_files() -> None:
    for rel in REQUIRED_FILES:
        if not (ROOT / rel).exists():
            errors.append(f"missing required file: {rel}")


def check_skill(path: Path) -> None:
    rel = path.relative_to(ROOT).as_posix()
    text = path.read_text(encoding="utf-8")
    meta = bi.parse_front_matter(text)
    name = str(meta.get("name", ""))

    if not name:
        errors.append(f"{rel}: front-matter is missing 'name'")
    elif not NAME_PATTERN.match(name):
        errors.append(f"{rel}: name must be lowercase words separated by hyphens, got {name!r}")
    elif name != path.parent.name:
        errors.append(f"{rel}: name {name!r} must match the directory {path.parent.name!r}")

    description = str(meta.get("description", ""))
    if not description:
        errors.append(f"{rel}: front-matter is missing 'description'")
    elif len(description) > 1024:
        errors.append(f"{rel}: description is {len(description)} characters; the limit is 1024")
    elif "Use when" not in description:
        errors.append(f"{rel}: description should say when to trigger ('Use when ...')")

    if not meta.get("license"):
        errors.append(f"{rel}: front-matter is missing 'license'")
    for key in ("section", "tags", "updated", "source"):
        if not meta.get(key):
            errors.append(f"{rel}: front-matter is missing '{key}'")

    for heading in REQUIRED_HEADINGS:
        if heading not in text:
            errors.append(f"{rel}: missing section '{heading}'")
    if not PLACEHOLDER.search(text):
        errors.append(f"{rel}: no input variables listed")
    follows = text.split("## Follow-ups", 1)[-1].split("## Guardrails", 1)[0]
    if len([ln for ln in follows.splitlines() if ln.strip().startswith("-")]) < 2:
        errors.append(f"{rel}: give at least two follow-up prompts")


def check_sections(entries: list[dict]) -> None:
    for section in bi.SECTION_ORDER:
        count = len([e for e in entries if e["section"] == section])
        if count < 2:
            errors.append(f"section '{section}' has {count} skill(s); at least 2 required")


def check_index(entries: list[dict]) -> None:
    if not bi.INDEX.exists():
        errors.append("index/skills.json is missing; run scripts/build_index.py")
        return
    data = json.loads(bi.INDEX.read_text(encoding="utf-8"))
    if data.get("count") != len(entries):
        errors.append(f"index/skills.json says {data.get('count')} skills; there are {len(entries)}")
    if f"skills-{len(entries)}-" not in bi.README.read_text(encoding="utf-8"):
        errors.append("README badge count does not match the number of skills")


def check_readme(entries: list[dict]) -> None:
    text = bi.README.read_text(encoding="utf-8")
    if bi.BEGIN not in text or bi.END not in text:
        errors.append("README.md: generated index markers are missing")
        return
    block = text.split(bi.BEGIN, 1)[1].split(bi.END, 1)[0].strip("\n")
    if block.strip() != bi.render(entries).strip("\n"):
        errors.append("README.md: skill index is out of date; run scripts/build_index.py")
    for entry in entries:
        if entry["name"] not in block:
            errors.append(f"README.md: {entry['name']} is missing from the index")


def check_marketplace(entries: list[dict]) -> None:
    path = ROOT / ".claude-plugin" / "marketplace.json"
    if not path.exists():
        return
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        errors.append(f".claude-plugin/marketplace.json is not valid JSON: {exc}")
        return
    for key in ("name", "owner", "plugins"):
        if key not in data:
            errors.append(f".claude-plugin/marketplace.json: missing '{key}'")
    if not data.get("plugins"):
        errors.append(".claude-plugin/marketplace.json: no plugins listed")
    for plugin in data.get("plugins", []):
        for key in ("name", "source", "description"):
            if key not in plugin:
                errors.append(f".claude-plugin/marketplace.json: plugin missing '{key}'")
    del entries  # the marketplace points at the repo, not at individual skills


def main() -> int:
    check_files()
    entries = bi.load_skills()
    if not entries:
        errors.append("no skills found under skills/")
    for path in sorted(bi.SKILLS.glob("*/SKILL.md")):
        check_skill(path)
    check_sections(entries)
    check_index(entries)
    check_marketplace(entries)
    if bi.README.exists():
        check_readme(entries)

    if errors:
        print(f"FAIL: {len(errors)} problem(s)\n")
        for error in errors:
            print(f"  - {error}")
        return 1
    sections = len({e["section"] for e in entries})
    print(f"OK: {len(entries)} skills in {sections} sections, index and README in sync")
    return 0


if __name__ == "__main__":
    sys.exit(main())
