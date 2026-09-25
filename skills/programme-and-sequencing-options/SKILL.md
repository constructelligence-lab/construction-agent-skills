---
name: programme-and-sequencing-options
description: Programme and sequencing options for construction and design work, covering preconstruction, programme, sequencing. You have a target completion date and a rough scope, and you want the plausible sequencing options on the table before you build a CPM schedule. Use when the user asks for help with programme and sequencing options, or is working on preconstruction, programme, sequencing in a construction, engineering or design context. Produces a reviewable draft, never a final answer.
license: CC BY 4.0
section: Preconstruction
tags: preconstruction, programme, sequencing
updated: 2026-09-24
source: construction-prompts/prompts/01-preconstruction/03-programme-and-sequencing-options.md
---

# Programme and sequencing options

You have a target completion date and a rough scope, and you want the plausible sequencing options
on the table before you build a CPM schedule.

## Inputs to collect

Ask the user for any of these you do not already have. Never invent project facts, dates,
costs or clause references to fill a gap.

- `{{construction_type}}`
- `{{floor_area}}`
- `{{long_lead_items}}`
- `{{occupancy_requirements}}`
- `{{project_type}}`
- `{{seasonal_constraints}}`
- `{{site_access}}`
- `{{target_duration}}`

## Instructions

```text
You are a planner preparing options for {{project_type}} with {{floor_area}} of
{{construction_type}} construction.

Constraints:
- Site access: {{site_access}}
- Target duration: {{target_duration}} from start on site
- Long-lead items: {{long_lead_items}}
- Seasonal or weather constraints: {{seasonal_constraints}}
- Occupied areas or phased handover: {{occupancy_requirements}}

Give me three genuinely different sequencing strategies, not one strategy with three
labels. For each: the sequence in five to eight steps, the duration drivers, what it
costs in money and risk, and the conditions under which it is the right choice.

Then tell me which option you would pick, and which single assumption in my brief would
change that answer if it turned out to be wrong.
```

## What good output looks like

- Options that differ in *strategy* — a different critical path — rather than in wording.
- Long-lead procurement treated as the pace-setter where it genuinely is one.
- An honest statement of which assumption the recommendation hangs on.

## Follow-ups

- "Turn the chosen option into a first-pass activity list with predecessors and rough durations."
- "What would this sequence look like if the long-lead item slipped by {{slip_weeks}} weeks?"
- "Which of these options is most robust to labour shortages in the first three months?"

## Guardrails

This is a planning conversation, not a schedule. Durations must be replaced with your own
production rates and real lead times before anybody commits to a date, and any dates that reach a
client must be checked against the contract programme.

---

*Part of the construction agent skills library — CC BY 4.0. Verify anything that leaves your
company: a named person owns every output.*
