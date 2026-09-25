---
name: productivity-assumption-stress-test
description: Productivity assumption stress test for construction and design work, covering productivity, labour, risk. An estimate depends on production rates you have assumed rather than measured, and you want to know how much of the margin is riding on them. Use when the user asks for help with productivity assumption stress test, or is working on productivity, labour, risk in a construction, engineering or design context. Produces a reviewable draft, never a final answer.
license: CC BY 4.0
section: Estimating and takeoff
tags: productivity, labour, risk
updated: 2026-09-24
source: construction-prompts/prompts/02-estimating/04-productivity-assumption-stress-test.md
---

# Productivity assumption stress test

An estimate depends on production rates you have assumed rather than measured, and you want to
know how much of the margin is riding on them.

## Inputs to collect

Ask the user for any of these you do not already have. Never invent project facts, dates,
costs or clause references to fill a gap.

- `{{assumed_rates_and_quantities}}`
- `{{basis}}`
- `{{crew_plan}}`
- `{{historical_rates}}`
- `{{trade_scope}}`

## Instructions

```text
You are a labour planner for {{trade_scope}} work.

Our estimate assumes:
{{assumed_rates_and_quantities}}

Basis for those assumptions: {{basis}}
Our own history on similar work: {{historical_rates}}
Crew composition planned: {{crew_plan}}

Stress test the assumptions:
1. Which assumption does the most damage if it is wrong by 15 percent?
2. Which are most likely to be wrong on this job given the conditions I described?
3. For each, what is the early indicator that would tell me within four weeks?
4. What would the labour cost be at 85 percent, 100 percent and 115 percent of the
   assumed productivity, all else equal?

Give me the sensitivity as a table, then the two assumptions worth measuring on site
rather than arguing about.
```

## What good output looks like

- Identifies which assumption drives the outcome rather than treating all as equally risky.
- Proposes measurable early indicators, which is what turns a risk into a managed one.
- Shows the arithmetic so you can check it, and does not pretend to know your rates.

## Follow-ups

- "Build me the weekly tracking sheet for the two indicators you chose."
- "What crew change would recover the 85 percent case, and what would it cost?"
- "Rewrite the sensitivity table as something I can show a client without exposing our margin."

## Guardrails

Labour rate and margin information should stay out of consumer tier tools. The sensitivity is only
as good as the range you supply, and it must be rebuilt with your own measured rates once the job
has four weeks of data.

---

*Part of the construction agent skills library — CC BY 4.0. Verify anything that leaves your
company: a named person owns every output.*
