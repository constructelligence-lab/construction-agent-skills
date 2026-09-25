---
name: design-brief-from-conversation
description: Design brief from a client conversation for construction and design work, covering brief, client, architecture. You have come out of a client meeting with scattered notes and need a written brief that the client can confirm or correct before design work starts. Use when the user asks for help with design brief from a client conversation, or is working on brief, client, architecture in a construction, engineering or design context. Produces a reviewable draft, never a final answer.
license: CC BY 4.0
section: Architecture and design
tags: brief, client, architecture
updated: 2026-09-24
source: construction-prompts/prompts/03-architecture/01-design-brief-from-conversation.md
---

# Design brief from a client conversation

You have come out of a client meeting with scattered notes and need a written brief that the client
can confirm or correct before design work starts.

## Inputs to collect

Ask the user for any of these you do not already have. Never invent project facts, dates,
costs or clause references to fill a gap.

- `{{budget_signals}}`
- `{{client_organisation}}`
- `{{meeting_notes}}`
- `{{programme_signals}}`
- `{{project_type}}`
- `{{site_context}}`

## Instructions

```text
You are an architect's project lead writing up a first meeting with a client.

Project: {{project_type}} for {{client_organisation}}
Notes from the meeting: {{meeting_notes}}
Site and planning context: {{site_context}}
Budget signals: {{budget_signals}}
Programme signals: {{programme_signals}}

Write a design brief with these sections, and keep it under one page:
1. What the client is trying to achieve, in their words rather than ours.
2. Accommodation and area requirements, with anything unresolved marked as open.
3. Constraints we know about: site, planning, budget, programme.
4. Decisions taken, decisions deferred, and who owns each.
5. The three questions that most need an answer before we design.

Mark anything you inferred rather than heard with [to confirm].
```

## What good output looks like

- Separates what the client said from what you assumed, with the assumptions labelled.
- Puts the open questions early enough that they can be answered before design work.
- Reads like something a client can edit in the margin, which is the point of sending it.

## Follow-ups

- "Turn the [to confirm] items into a numbered list of questions for the client email."
- "Rewrite section one so it could be pasted into a fee proposal without further editing."
- "What did the client not talk about that projects like this always need to discuss?"

## Guardrails

Check anything client-confidential before pasting, and do not let a generated brief become the
record of an agreement. The client confirms the brief in writing; the model only arranged what you
already heard.

---

*Part of the construction agent skills library — CC BY 4.0. Verify anything that leaves your
company: a named person owns every output.*
