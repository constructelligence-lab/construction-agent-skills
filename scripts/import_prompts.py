#!/usr/bin/env python3
"""Generate Agent Skills from the construction prompt library.

Each prompt file becomes skills/<slug>/SKILL.md with Agent Skills front-matter
(name, description, license) plus the sections an agent needs: when to use it,
inputs to collect, instructions, expected output, follow-ups and guardrails.

Usage:
  python3 scripts/import_prompts.py [--source ../../construction-prompts/prompts]

The generated files are committed, so this only needs to run when the prompt
library changes. It never overwrites a SKILL.md that has been edited by hand
unless --force is passed.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_SOURCE = ROOT.parent / "construction-prompts" / "prompts"
SKILLS = ROOT / "skills"

FRONT_MATTER = re.compile(r"\A---\n(.*?)\n---\n", re.S)
PLACEHOLDER = re.compile(r"\{\{([a-z0-9_]+)\}\}")


def parse_front_matter(text: str) -> dict:
    match = FRONT_MATTER.match(text)
    if not match:
        return {}
    data: dict[str, object] = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        value = value.strip()
        if value.startswith("[") and value.endswith("]"):
            data[key.strip()] = [item.strip() for item in value[1:-1].split(",") if item.strip()]
        else:
            data[key.strip()] = value
    return data


def section_body(text: str, heading: str, stop_headings: list[str]) -> str:
    marker = f"## {heading}"
    if marker not in text:
        return ""
    body = text.split(marker, 1)[1]
    for stop in stop_headings:
        if stop in body:
            body = body.split(stop, 1)[0]
    return body.strip()


def bullets(text: str) -> str:
    return "\n".join(line for line in text.splitlines() if line.strip().startswith("-")).strip()


def first_sentence(text: str) -> str:
    flat = " ".join(text.split())
    match = re.search(r"(.+?[.?!])(?:\s|$)", flat)
    return match.group(1) if match else flat


def description_for(title: str, use_when: str, tags: list[str]) -> str:
    """The description is the trigger: it is the only thing loaded before a skill matches."""
    triggers = ", ".join(tags) if tags else "construction work"
    text = (
        f"{title} for construction and design work, covering {triggers}. "
        f"{first_sentence(use_when)} "
        f"Use when the user asks for help with {title.lower()}, or is working on "
        f"{triggers} in a construction, engineering or design context. "
        f"Produces a reviewable draft, never a final answer."
    )
    return " ".join(text.split())[:1000]


def build_skill(source: Path, force: bool) -> tuple[str, bool]:
    text = source.read_text(encoding="utf-8")
    meta = parse_front_matter(text)
    slug = str(meta.get("slug") or source.stem)
    title = str(meta.get("title") or slug.replace("-", " ").title())
    section = str(meta.get("section") or "Construction")
    tags = [str(t) for t in meta.get("tags", [])]
    updated = str(meta.get("updated") or "")

    use_when = section_body(text, "Use it when", ["## The prompt"])
    prompt_body = section_body(text, "The prompt", ["## What good output looks like"])
    prompt_block = re.search(r"```text\n(.+?)```", prompt_body, re.S)
    prompt = prompt_block.group(1).strip() if prompt_block else prompt_body
    good = bullets(section_body(text, "What good output looks like", ["## Follow-ups"]))
    follow_ups = bullets(section_body(text, "Follow-ups", ["## Guardrails"]))
    guardrails = section_body(text, "Guardrails", [])

    placeholders = sorted(set(PLACEHOLDER.findall(prompt)))
    inputs = "\n".join(f"- `{{{{{name}}}}}`" for name in placeholders) or "- No fixed inputs"

    out = SKILLS / slug
    target = out / "SKILL.md"
    if target.exists() and not force:
        return slug, False
    out.mkdir(parents=True, exist_ok=True)

    body = f"""---
name: {slug}
description: {description_for(title, use_when, tags)}
license: CC BY 4.0
section: {section}
tags: {", ".join(tags)}
updated: {updated}
source: {source.relative_to(ROOT.parent).as_posix()}
---

# {title}

{use_when}

## Inputs to collect

Ask the user for any of these you do not already have. Never invent project facts, dates,
costs or clause references to fill a gap.

{inputs}

## Instructions

```text
{prompt}
```

## What good output looks like

{good}

## Follow-ups

{follow_ups}

## Guardrails

{guardrails}

---

*Part of the construction agent skills library — CC BY 4.0. Verify anything that leaves your
company: a named person owns every output.*
"""
    target.write_text(body, encoding="utf-8")
    return slug, True


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--force", action="store_true", help="overwrite skills that already exist")
    args = parser.parse_args(argv)

    source: Path = args.source
    if not source.exists():
        sys.exit(f"FAIL: prompt source not found at {source}")

    created, skipped = [], []
    for path in sorted(source.rglob("*.md")):
        slug, written = build_skill(path, args.force)
        (created if written else skipped).append(slug)

    print(f"wrote {len(created)} skills, skipped {len(skipped)} that already existed")
    if skipped:
        print(f"  skipped: {', '.join(skipped)}")
        print("  re-run with --force to regenerate them")
    return 0


if __name__ == "__main__":
    sys.exit(main())
