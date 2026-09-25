---
name: toolbox-talk-from-near-miss
description: Toolbox talk from a real near miss for construction and design work, covering safety, training, briefing. Something nearly went wrong on this site and you want a five-minute talk that lands with the crew, rather than a generic briefing they have heard ten times. Use when the user asks for help with toolbox talk from a real near miss, or is working on safety, training, briefing in a construction, engineering or design context. Produces a reviewable draft, never a final answer.
license: CC BY 4.0
section: Safety and compliance
tags: safety, training, briefing
updated: 2026-09-24
source: construction-prompts/prompts/08-safety/02-toolbox-talk-from-near-miss.md
---

# Toolbox talk from a real near miss

Something nearly went wrong on this site and you want a five-minute talk that lands with the crew,
rather than a generic briefing they have heard ten times.

## Inputs to collect

Ask the user for any of these you do not already have. Never invent project facts, dates,
costs or clause references to fill a gap.

- `{{audience}}`
- `{{changes_made}}`
- `{{location_and_time}}`
- `{{near_miss_description}}`
- `{{potential_outcome}}`

## Instructions

```text
You are a site safety lead writing a five-minute toolbox talk about something that
actually happened.

What happened: {{near_miss_description}}
Where and when: {{location_and_time}}
What could have happened: {{potential_outcome}}
What we changed afterwards: {{changes_made}}
Audience: {{audience}}

Write the talk in plain language, in this order:
1. What happened, told straight, including how ordinary the start of it was.
2. What would have had to be different for someone to be hurt.
3. The two things this crew should do differently, stated as actions rather than rules.
4. One question to ask the crew, so they talk rather than listen.

Keep it under 250 words, spoken language, no jargon and no blaming anyone. Do not name
the individual involved.
```

## What good output looks like

- Tells the story of how ordinary the conditions were, which is what makes a crew see themselves
- Gives two concrete actions rather than a list of rules.
- Ends with a question, turning a briefing into a conversation.

## Follow-ups

- "Add three follow-up questions for a crew that goes quiet on safety discussions."
- "Write the record of the briefing, including the attendance line and the points raised."
- "What might this near miss be telling us about our method or our equipment rather than our people?"

## Guardrails

Talks must reflect what actually happened on this site and must not identify individuals or imply
blame. Investigations and disciplinary matters follow your own procedures, and anything reportable
must be handled through the required channels before it becomes training material.

---

*Part of the construction agent skills library — CC BY 4.0. Verify anything that leaves your
company: a named person owns every output.*
