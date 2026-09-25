---
name: design-review-agenda
description: Design review agenda that finds problems for construction and design work, covering coordination, meetings, design. You are running a design or coordination review and want an agenda that surfaces conflicts rather than walking through the drawings in order. Use when the user asks for help with design review agenda that finds problems, or is working on coordination, meetings, design in a construction, engineering or design context. Produces a reviewable draft, never a final answer.
license: CC BY 4.0
section: Architecture and design
tags: coordination, meetings, design
updated: 2026-09-24
source: construction-prompts/prompts/03-architecture/04-design-review-agenda.md
---

# Design review agenda that finds problems

You are running a design or coordination review and want an agenda that surfaces conflicts rather
than walking through the drawings in order.

## Inputs to collect

Ask the user for any of these you do not already have. Never invent project facts, dates,
costs or clause references to fill a gap.

- `{{attendees}}`
- `{{decisions_needed}}`
- `{{design_stage}}`
- `{{open_items}}`
- `{{project_type}}`
- `{{risk_areas}}`

## Instructions

```text
You are chairing a design review for a {{project_type}} project.

Attendees and disciplines: {{attendees}}
Current design stage: {{design_stage}}
Areas of the design that carry the most risk: {{risk_areas}}
Open items carried over: {{open_items}}
Decisions needed this week: {{decisions_needed}}

Build a 60-minute agenda that would actually find problems, not read the drawings back.
For each item: the question to put to the room, the discipline that must answer, the
decision or action expected, and the consequence of leaving it open.

Put the coordination interfaces first, then the decisions with programme impact, then
the rest. Include the five minutes at the start for anything that has gone wrong since
the last review.
```

## What good output looks like

- Front-loads interfaces between disciplines, which is where design problems actually live.
- Each item has a question and an owner, so the meeting produces decisions rather than notes.
- Includes the "what broke since last time" slot, which is what keeps a review honest.

## Follow-ups

- "Rewrite this as the pre-read to send out 24 hours before the meeting."
- "Draft the minutes template that captures decisions, owners and dates from this agenda."
- "Which three items should we resolve in a smaller side meeting instead of the main review?"

## Guardrails

Minutes and decisions become the record of the project. Someone at the meeting owns the output, and
any design decision that leaves the room must be confirmed by the responsible professional.

---

*Part of the construction agent skills library — CC BY 4.0. Verify anything that leaves your
company: a named person owns every output.*
