---
name: schedule-narrative-for-owner
description: Schedule narrative for the owner for construction and design work, covering schedule, reporting, communication. The monthly schedule update is done and needs the narrative section: what moved, why, what you are doing about it, and what you need — without excuses and without jargon. Use when the user asks for help with schedule narrative for the owner, or is working on schedule, reporting, communication in a construction, engineering or design context. Produces a reviewable draft, never a final answer.
license: CC BY 4.0
section: Scheduling and planning
tags: schedule, reporting, communication
updated: 2026-09-24
source: construction-prompts/prompts/06-scheduling/01-schedule-narrative-for-owner.md
---

# Schedule narrative for the owner

The monthly schedule update is done and needs the narrative section: what moved, why, what you are
doing about it, and what you need — without excuses and without jargon.

## Inputs to collect

Ask the user for any of these you do not already have. Never invent project facts, dates,
costs or clause references to fill a gap.

- `{{actions}}`
- `{{asks}}`
- `{{causes}}`
- `{{overall_status}}`
- `{{recovery_plan}}`
- `{{schedule_movement}}`

## Instructions

```text
You are a project manager writing the narrative for a schedule update to an owner.

Status: {{overall_status}}
Movement since last period: {{schedule_movement}}
Causes: {{causes}}
Actions taken: {{actions}}
Recovery or mitigation plan: {{recovery_plan}}
What we need from the owner: {{asks}}

Write the narrative in this order, under 500 words:
1. Where the programme stands against the baseline, in one sentence, honestly.
2. What moved this period and by how much.
3. Why, stated factually, with no blame and no defensiveness.
4. What we have done and what we are doing.
5. What we need from the owner, with dates.

Separate the delay we can recover from the delay that changes the completion date. Do not
use scheduling jargon without explaining it in the same sentence. Do not overstate
progress: if the date is at risk, say so plainly in the first paragraph.
```

## What good output looks like

- Says the difficult thing in the first paragraph instead of burying it in section four.
- Distinguishes recoverable slippage from a change to the completion date, which is the
- Ends with dated asks, which converts a report into a request.

## Follow-ups

- "Cut it to 200 words for the owner's executive summary."
- "Rewrite section three so it is factual and still does not read as an excuse."
- "Draft the covering email, and a one-paragraph version for the owner's board pack."

## Guardrails

Never let a generated narrative state a cause that the records do not support — contemporaneous
records govern, not a well-written paragraph. Any statement about time entitlement must be checked
against the contract before it leaves the company.

---

*Part of the construction agent skills library — CC BY 4.0. Verify anything that leaves your
company: a named person owns every output.*
