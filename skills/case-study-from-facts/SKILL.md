---
name: case-study-from-facts
description: Project case study from the facts for construction and design work, covering marketing, case-study, bd. You have finished a job worth writing about and need a case study for the website, a proposal or a prequalification pack — without inventing anything and without breaching confidentiality. Use when the user asks for help with project case study from the facts, or is working on marketing, case-study, bd in a construction, engineering or design context. Produces a reviewable draft, never a final answer.
license: CC BY 4.0
section: Business development
tags: marketing, case-study, bd
updated: 2026-09-24
source: construction-prompts/prompts/10-business-development/01-case-study-from-facts.md
---

# Project case study from the facts

You have finished a job worth writing about and need a case study for the website, a proposal or a
prequalification pack — without inventing anything and without breaching confidentiality.

## Inputs to collect

Ask the user for any of these you do not already have. Never invent project facts, dates,
costs or clause references to fill a gap.

- `{{approach}}`
- `{{challenges}}`
- `{{client_and_sector}}`
- `{{company_type}}`
- `{{outcomes}}`
- `{{project_name_descriptor}}`
- `{{reference_permission}}`
- `{{scope}}`
- `{{value_and_duration}}`

## Instructions

```text
You are a bid writer at a {{company_type}} contractor writing a project case study.

Project: {{project_name_descriptor}}
Client type and sector: {{client_and_sector}}
Value band and duration: {{value_and_duration}}
Scope we delivered: {{scope}}
Constraints and challenges: {{challenges}}
What we did that was different: {{approach}}
Outcome with evidence: {{outcomes}}
Client agreement to reference: {{reference_permission}}

Write the case study in this structure, 400 to 600 words:
1. The project in three lines a busy reader can absorb.
2. The challenge, described in terms the client would recognise.
3. What we did, specific and concrete, no superlatives.
4. The outcome, using only the numbers I gave you.
5. A short closing line identifying who this work is relevant for.

Rules: no invented statistics, no client name if permission was not given (use a
descriptor), and no claims about performance I have not evidenced. Flag anything in my
brief that reads like a claim without proof.
```

## What good output looks like

- Specific and modest: numbers only where you supplied them, and named claims flagged.
- Reads as a record of work rather than marketing, which is what makes it credible to a
- Ends by telling the reader whether this is relevant to them, which is what a case study is for.

## Follow-ups

- "Cut this to 150 words for a prequalification submission, keeping the specifics."
- "Rewrite the challenge section from the client's point of view rather than ours."
- "List every claim in this text that needs evidence before we publish it."

## Guardrails

Never publish another party's name, figures or images without written permission. Commercial
sensitivity matters too: values, margins and programme details are often confidential even when the
project is public knowledge, so check what the contract allows before publishing.

---

*Part of the construction agent skills library — CC BY 4.0. Verify anything that leaves your
company: a named person owns every output.*
