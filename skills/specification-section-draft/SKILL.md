---
name: specification-section-draft
description: Specification section draft for construction and design work, covering specification, documentation, quality. You need a first draft of a specification section structure so you are editing rather than staring at an empty document — with the understanding that the technical content is yours, not the model's. Use when the user asks for help with specification section draft, or is working on specification, documentation, quality in a construction, engineering or design context. Produces a reviewable draft, never a final answer.
license: CC BY 4.0
section: Architecture and design
tags: specification, documentation, quality
updated: 2026-09-24
source: construction-prompts/prompts/03-architecture/02-specification-section-draft.md
---

# Specification section draft

You need a first draft of a specification section structure so you are editing rather than staring
at an empty document — with the understanding that the technical content is yours, not the
model's.

## Inputs to collect

Ask the user for any of these you do not already have. Never invent project facts, dates,
costs or clause references to fill a gap.

- `{{discipline}}`
- `{{element_or_system}}`
- `{{exclusions}}`
- `{{jurisdiction}}`
- `{{materials}}`
- `{{performance_requirements}}`
- `{{project_type}}`
- `{{standards}}`
- `{{workmanship}}`

## Instructions

```text
You are a specification writer for {{discipline}} work.

I am writing a specification section for {{element_or_system}} on a {{project_type}}
project in {{jurisdiction}}.

What I know:
- Materials and products: {{materials}}
- Performance requirements: {{performance_requirements}}
- Standards and testing regime: {{standards}}
- Installation and workmanship expectations: {{workmanship}}
- What is excluded: {{exclusions}}

Build me an outline for the section using the standard three-part structure, with the
clauses I should cover and one line describing what each clause must decide.

Mark clearly:
- clauses where the requirement must come from the design team, not from general practice
- anything that varies by jurisdiction and must be checked locally
- the coordination items with other sections

Do not invent product names, standards numbers, or test values.
```

## What good output looks like

- Gives you the clause skeleton and the questions each clause answers, without fabricating content.
- Marks the items that must be jurisdiction-checked, instead of asserting a code requirement.
- Names the coordination interfaces, which is where specifications usually fail on site.

## Follow-ups

- "Turn the coordination items into a list of other sections I must cross-check."
- "Draft the submittal requirements clause using the three-part structure."
- "What in this section would a subcontractor be most likely to price as an exclusion?"

## Guardrails

Specifications are contractual. Every requirement, standard reference and test value must come from
an authoritative source you have checked, and the section must be reviewed by the designer
responsible for it before issue.

---

*Part of the construction agent skills library — CC BY 4.0. Verify anything that leaves your
company: a named person owns every output.*
