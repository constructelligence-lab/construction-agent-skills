---
name: takeoff-review-checklist
description: Takeoff review checklist for construction and design work, covering takeoff, quantities, quality. A takeoff has been produced — by a person, by software, or by one of the tools in our [open source construction tools](https://github.com/constructelligence-lab/open-source-construction-tools) list — and it needs a review that is actually systematic. Use when the user asks for help with takeoff review checklist, or is working on takeoff, quantities, quality in a construction, engineering or design context. Produces a reviewable draft, never a final answer.
license: CC BY 4.0
section: Estimating and takeoff
tags: takeoff, quantities, quality
updated: 2026-09-24
source: construction-prompts/prompts/02-estimating/02-takeoff-review-checklist.md
---

# Takeoff review checklist

A takeoff has been produced — by a person, by software, or by one of the tools in our
[open source construction tools](https://github.com/constructelligence-lab/open-source-construction-tools)
list — and it needs a review that is actually systematic.

## Inputs to collect

Ask the user for any of these you do not already have. Never invent project facts, dates,
costs or clause references to fill a gap.

- `{{drawing_set_and_revision}}`
- `{{project_type}}`
- `{{stated_exclusions}}`
- `{{takeoff_summary}}`
- `{{trade_scope}}`

## Instructions

```text
You are a senior estimator reviewing a quantity takeoff for {{trade_scope}} on a
{{project_type}} project.

Takeoff summary:
{{takeoff_summary}}

Sources used: {{drawing_set_and_revision}}
Exclusions stated by the person who measured it: {{stated_exclusions}}

Build the review checklist I should work through, specific to this scope and this trade.
Cover:
- revision and superseded-sheet checks
- scope that is commonly double counted in {{trade_scope}}
- scope that is commonly missed in this project type
- measurement rules that need confirming against the specification
- the arithmetic and rounding traps

Format it as a checklist I can tick off with the source sheet for each item.
```

## What good output looks like

- Names the double-count traps for that specific trade, not a generic audit list.
- Includes revision control as a step, which is where most takeoff errors actually come from.
- Gives each check a place to write down the evidence, so the review leaves a record.

## Follow-ups

- "Which five checks would you run first if I only had an hour?"
- "Turn this into a one-page template I can reuse on every job."
- "What does this checklist look like for a design-build job where we own the quantities?"

## Guardrails

This is a process aid, not a measurement. Somebody competent still owns the quantities, and any
takeoff that feeds a bid must be reconciled against a known number before it is trusted.

---

*Part of the construction agent skills library — CC BY 4.0. Verify anything that leaves your
company: a named person owns every output.*
