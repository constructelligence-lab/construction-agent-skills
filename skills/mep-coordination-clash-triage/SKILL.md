---
name: mep-coordination-clash-triage
description: MEP coordination and clash triage for construction and design work, covering mep, coordination, bim. You have a clash report or a coordination problem list and need to decide which clashes matter, in what order to resolve them, and who should move. Use when the user asks for help with mep coordination and clash triage, or is working on mep, coordination, bim in a construction, engineering or design context. Produces a reviewable draft, never a final answer.
license: CC BY 4.0
section: Engineering
tags: mep, coordination, bim
updated: 2026-09-24
source: construction-prompts/prompts/05-engineering/02-mep-coordination-clash-triage.md
---

# MEP coordination and clash triage

You have a clash report or a coordination problem list and need to decide which clashes matter, in
what order to resolve them, and who should move.

## Inputs to collect

Ask the user for any of these you do not already have. Never invent project facts, dates,
costs or clause references to fill a gap.

- `{{clash_list}}`
- `{{programme_notes}}`
- `{{project_type}}`
- `{{service_priorities}}`
- `{{special_zones}}`
- `{{void_depth}}`

## Instructions

```text
You are an MEP coordinator triaging a clash list for a {{project_type}} project.

Clashes or conflicts:
{{clash_list}}

Ceiling void available: {{void_depth}}
Zones with special requirements: {{special_zones}}
Services with priority established by specification: {{service_priorities}}
Programme pressure: {{programme_notes}}

Triage the list. For each item:
- which service should move, and why that service rather than the other
- whether it is a real clash or a modelling artefact
- the cost and programme consequence of resolving it in the field instead
- who should decide, and by when

Then give me the five items to resolve in the coordination meeting this week, and the
pattern you notice across the list that suggests an underlying cause.
```

## What good output looks like

- Applies consistent priority logic — gravity drainage and duct sizes usually constrain what can
- Separates real conflicts from modelling noise, which is where most of the list usually is.
- Names a cause pattern, which is the output that stops the same clash appearing next week.

## Follow-ups

- "Turn the top five into an agenda with the disciplines that must attend."
- "Draft the coordination note for a clash that requires a design change rather than a move."
- "What should we add to the coordination checklist so this pattern stops recurring?"

## Guardrails

Clash resolution is a design decision. Anything that changes a route, a size or a penetration needs
the responsible discipline's approval, and the required clearances and code-driven separations must
come from the specification, not from a model's suggestion.

---

*Part of the construction agent skills library — CC BY 4.0. Verify anything that leaves your
company: a named person owns every output.*
