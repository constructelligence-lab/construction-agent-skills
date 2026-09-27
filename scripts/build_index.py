#!/usr/bin/env python3
"""Generate index/skills.json, the README skill tables and the badge from SKILL.md front-matter."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
README = ROOT / "README.md"
INDEX = ROOT / "index" / "skills.json"

BEGIN = "<!-- begin:index -->"
END = "<!-- end:index -->"
BADGE_BEGIN = "<!-- begin:badge -->"
BADGE_END = "<!-- end:badge -->"

SECTION_ORDER = [
    "Preconstruction",
    "Estimating and takeoff",
    "Architecture and design",
    "Visualisation and rendering",
    "Engineering",
    "Scheduling and planning",
    "Site and field operations",
    "Safety and compliance",
    "Contracts and commercial",
    "Business development",
    "Automation and analysis",
]

SECTION_BLURB = {
    "Preconstruction": "Qualifying work, framing the programme, finding risk before you price it.",
    "Estimating and takeoff": "Sanity checks, pricing narratives and takeoff review.",
    "Architecture and design": "Briefs, specifications, code topics and design review.",
    "Visualisation and rendering": "Image prompts, iteration and critique before a client sees it.",
    "Engineering": "Structural and MEP sense checks, with an engineer and never instead of one.",
    "Scheduling and planning": "Narratives, look-aheads and the records a delay claim is built from.",
    "Site and field operations": "Turning field notes into records somebody can act on.",
    "Safety and compliance": "Task-specific safety documents, written with a competent person.",
    "Contracts and commercial": "Notices, risk reviews and payment narratives, drafted for review.",
    "Business development": "Case studies, proposals and the writing that wins the next job.",
    "Automation and analysis": "For the person who would rather script it than retype it.",
}

FRONT_MATTER = re.compile(r"\A---\n(.*?)\n---\n", re.S)


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
        if key.strip() == "tags":
            data["tags"] = [item.strip() for item in value.split(",") if item.strip()]
        else:
            data[key.strip()] = value
    return data


def title_and_summary(text: str) -> tuple[str, str]:
    """The H1 and the first sentence of the paragraph under it: short enough for a table row."""
    body = FRONT_MATTER.sub("", text, count=1)
    title = next((line[2:].strip() for line in body.splitlines() if line.startswith("# ")), "")
    after = body.split(f"# {title}", 1)[-1].strip() if title else body.strip()
    paragraph = " ".join(after.split("\n\n", 1)[0].split())
    sentence = re.split(r"(?<=[.!?])\s+(?=[A-Z])", paragraph, maxsplit=1)[0]
    return title, sentence


def load_skills() -> list[dict]:
    entries = []
    for path in sorted(SKILLS.glob("*/SKILL.md")):
        text = path.read_text(encoding="utf-8")
        meta = parse_front_matter(text)
        title, summary = title_and_summary(text)
        entries.append(
            {
                "name": str(meta.get("name", path.parent.name)),
                "title": title,
                "summary": summary,
                "description": str(meta.get("description", "")),
                "section": str(meta.get("section", "")),
                "tags": meta.get("tags", []),
                "license": str(meta.get("license", "")),
                "updated": str(meta.get("updated", "")),
                "source": str(meta.get("source", "")),
                "path": path.relative_to(ROOT).as_posix(),
            }
        )
    return entries


def render(entries: list[dict]) -> str:
    out: list[str] = []
    for section in SECTION_ORDER:
        group = [e for e in entries if e["section"] == section]
        if not group:
            continue
        # Same order as the numbered files in the prompts library, so the two indexes read alike.
        group.sort(key=lambda e: (e["source"], e["name"]))
        out.append(f"### {section}")
        out.append("")
        out.append(f"*{SECTION_BLURB.get(section, '')}*")
        out.append("")
        out.append("| Skill | Use it when | Tags |")
        out.append("| --- | --- | --- |")
        for entry in group:
            tags = " ".join(f"`{tag}`" for tag in entry["tags"])
            label = f"[**{entry['title'] or entry['name']}**]({entry['path']})<br>`{entry['name']}`"
            out.append(f"| {label} | {entry['summary']} | {tags} |")
        out.append("")
    return "\n".join(out).rstrip() + "\n"


def render_badge(count: int, sections: int) -> str:
    return (
        f"![skills](https://img.shields.io/badge/skills-{count}-1f6feb) "
        f"![sections](https://img.shields.io/badge/sections-{sections}-2ea043) "
        "![licence](https://img.shields.io/badge/licence-CC%20BY%204.0-2ea043) "
        "![validated](https://img.shields.io/badge/index-validated%20in%20CI-6e7781)"
    )


def replace_block(text: str, begin: str, end: str, block: str) -> str:
    if begin not in text or end not in text:
        print(f"note: markers {begin} / {end} not found, skipped")
        return text
    head, rest = text.split(begin, 1)
    _, tail = rest.split(end, 1)
    return f"{head}{begin}\n{block}\n{end}{tail}"


def main() -> int:
    entries = load_skills()
    unknown = {e["section"] for e in entries} - set(SECTION_ORDER)
    if unknown:
        print(f"FAIL: skills in unknown sections: {sorted(unknown)}")
        return 1
    sections = len({e["section"] for e in entries})

    INDEX.parent.mkdir(parents=True, exist_ok=True)
    INDEX.write_text(
        json.dumps(
            {"generated_on": max((e["updated"] for e in entries), default=""), "count": len(entries), "sections": sections, "skills": entries},
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )

    if README.exists():
        text = README.read_text(encoding="utf-8")
        text = replace_block(text, BEGIN, END, render(entries))
        text = replace_block(text, BADGE_BEGIN, BADGE_END, render_badge(len(entries), sections))
        README.write_text(text, encoding="utf-8")

    print(f"indexed {len(entries)} skills across {sections} sections")
    return 0


if __name__ == "__main__":
    sys.exit(main())
