---
name: proposal-tailoring
description: Tailoring a proposal to the client's actual concerns for construction and design work, covering proposals, bidding, bd. You have a standard proposal structure and a specific client, and you want the document to answer what *they* are worried about instead of repeating your company history. Use when the user asks for help with tailoring a proposal to the client's actual concerns, or is working on proposals, bidding, bd in a construction, engineering or design context. Produces a reviewable draft, never a final answer.
license: CC BY 4.0
section: Business development
tags: proposals, bidding, bd
updated: 2026-09-24
source: construction-prompts/prompts/10-business-development/02-proposal-tailoring.md
---

# Tailoring a proposal to the client's actual concerns

You have a standard proposal structure and a specific client, and you want the document to answer
what *they* are worried about instead of repeating your company history.

## Inputs to collect

Ask the user for any of these you do not already have. Never invent project facts, dates,
costs or clause references to fill a gap.

- `{{brief_summary}}`
- `{{client_history}}`
- `{{client_priorities}}`
- `{{evaluation_criteria}}`
- `{{our_approach}}`
- `{{our_experience}}`
- `{{project_type}}`

## Instructions

```text
You are a bid manager responding to an invitation for {{project_type}}.

What the client said they care about: {{client_priorities}}
What is in the ITT or brief: {{brief_summary}}
Evaluation criteria if published: {{evaluation_criteria}}
Our relevant experience: {{our_experience}}
Our proposed approach: {{our_approach}}
Known concerns or history with this client: {{client_history}}

Structure the response so that the sections answering the client's stated priorities come
first and are the longest. For each of the top four concerns:
- the concern in the client's words
- what we will do about it specifically
- the evidence from our experience that shows we can
- what we would want them to hold us to

Then tell me which parts of our standard proposal should be cut because they do not
answer this client's questions.
```

## What good output looks like

- Reorders the document around the client's stated priorities rather than your usual structure.
- Recommends cutting material, which is the hardest and most useful part of tailoring.
- Turns claims into commitments a client can hold you to, which reads as confidence.

## Follow-ups

- "Rewrite the executive summary in the client's language, using their terms for their project."
- "What are the three questions this client is most likely to ask at interview, and how should we answer them?"
- "Draft the one-page cover letter that goes with the submission."

## Guardrails

Do not paste another client's confidential brief or evaluation feedback into a consumer tier tool,
and never make a commitment on programme, price or resources that the delivery team has not
confirmed. Proposals are contractual documents once submitted.

---

*Part of the construction agent skills library — CC BY 4.0. Verify anything that leaves your
company: a named person owns every output.*
