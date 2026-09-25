---
name: bid-go-no-go
description: Bid qualification: go or no-go for construction and design work, covering bidding, risk, preconstruction. An invitation to bid lands and you need a defensible recommendation before you spend a week estimating it. Use when the user asks for help with bid qualification: go or no-go, or is working on bidding, risk, preconstruction in a construction, engineering or design context. Produces a reviewable draft, never a final answer.
license: CC BY 4.0
section: Preconstruction
tags: bidding, risk, preconstruction
updated: 2026-09-24
source: construction-prompts/prompts/01-preconstruction/01-bid-go-no-go.md
---

# Bid qualification: go or no-go

An invitation to bid lands and you need a defensible recommendation before you spend a week
estimating it. Best used with real numbers — your backlog, your crew availability, your history on
this kind of work — rather than an impression.

## Inputs to collect

Ask the user for any of these you do not already have. Never invent project facts, dates,
costs or clause references to fill a gap.

- `{{annual_revenue}}`
- `{{backlog_months}}`
- `{{bid_days}}`
- `{{bonding_impact}}`
- `{{client_type}}`
- `{{company_type}}`
- `{{competitors}}`
- `{{contract_terms}}`
- `{{estimator_hours}}`
- `{{experience}}`
- `{{known_risks}}`
- `{{project_name}}`
- `{{project_size}}`
- `{{project_type}}`
- `{{workload}}`

## Instructions

```text
You are a commercial manager at a {{company_type}} contractor with annual revenue of
about {{annual_revenue}} and a backlog of {{backlog_months}} months.

We are deciding whether to bid {{project_name}}, a {{project_size}} {{project_type}}
project for {{client_type}}, due in {{bid_days}} days, requiring approximately
{{estimator_hours}} estimating hours and {{bonding_impact}} of bonding capacity.

Facts you should weigh:
- Our experience with this project type: {{experience}}
- Our current workload and crew availability: {{workload}}
- Contract form and payment terms: {{contract_terms}}
- Known risks (site, programme, cash, client behaviour): {{known_risks}}
- Competitors likely to bid: {{competitors}}

Give me:
1. A go / no-go recommendation with the two strongest reasons for it.
2. The three questions I should answer before committing to bid.
3. The strongest argument for the opposite decision, so I can test it.
4. What would have to change for the recommendation to flip.

Be direct. Do not hedge into "it depends" without saying what it depends on. Return a
short table of decision factors with a rating (strong, neutral, weak) and a one-line
justification for each, then the recommendation in two sentences.
```

## What good output looks like

- Names the two decisive factors rather than listing ten considerations of equal weight.
- States explicitly what would change the answer, which is what makes it testable.
- Separates commercial risk from the things you cannot know yet, and says which is which.

## Follow-ups

- "Assume we bid and win. What are the three most likely reasons this job loses money?"
- "Rewrite this as the note I would send the owner if we decline, keeping the relationship warm."
- "Turn the three questions into a checklist with the person who should answer each one."

## Guardrails

Do not paste client pricing strategy, competitor bids, or another contractor's confidential
information. Treat the recommendation as an input to a decision the owners make, not the decision
itself — and check the bonding and cash assumptions against your real numbers before acting.

---

*Part of the construction agent skills library — CC BY 4.0. Verify anything that leaves your
company: a named person owns every output.*
