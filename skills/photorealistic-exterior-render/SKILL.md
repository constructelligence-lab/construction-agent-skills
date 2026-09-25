---
name: photorealistic-exterior-render
description: Photorealistic exterior render prompt for construction and design work, covering rendering, visualisation, marketing. You need a client-ready exterior visual quickly, before the model is advanced enough for a proper render, or to explore a façade direction. Use when the user asks for help with photorealistic exterior render prompt, or is working on rendering, visualisation, marketing in a construction, engineering or design context. Produces a reviewable draft, never a final answer.
license: CC BY 4.0
section: Visualisation and rendering
tags: rendering, visualisation, marketing
updated: 2026-09-24
source: construction-prompts/prompts/04-visualisation/01-photorealistic-exterior-render.md
---

# Photorealistic exterior render prompt

You need a client-ready exterior visual quickly, before the model is advanced enough for a proper
render, or to explore a façade direction. It is a communication tool, not a documentation tool.

## Inputs to collect

Ask the user for any of these you do not already have. Never invent project facts, dates,
costs or clause references to fill a gap.

- `{{building_type}}`
- `{{cladding_materials}}`
- `{{colour_palette}}`
- `{{context_description}}`
- `{{eye_level_or_angle}}`
- `{{focal_length}}`
- `{{focus}}`
- `{{glazing_description}}`
- `{{landscape_and_paving}}`
- `{{occupancy_signal}}`
- `{{season}}`
- `{{storeys}}`
- `{{time_of_day}}`
- `{{view_description}}`
- `{{weather}}`

## Instructions

```text
Photorealistic architectural photograph of {{building_type}}, {{storeys}} storeys,
{{cladding_materials}}, {{glazing_description}}.

View: {{view_description}} from {{eye_level_or_angle}}, framed to show {{focus}}.
Time and weather: {{time_of_day}}, {{weather}}, {{season}}.
Site context: {{context_description}}.
Foreground: {{landscape_and_paving}}.
People and activity: {{occupancy_signal}}.

Composition: architectural photography, {{focal_length}}mm equivalent look, level
verticals, natural perspective, deep depth of field, {{colour_palette}} palette.
Avoid: text, watermarks, signage, distorted geometry, extra windows, floating elements,
cartoon rendering, oversaturated skies.
```

## What good output looks like

- Reads as a photograph, with believable light direction and no geometry that would embarrass you
- Shows context — a building in a void is a diagram, not a visual.
- Is close enough to the design intent that you can use it to have a conversation, not to prove

## Follow-ups

- "Same building, dusk, interiors lit, wet paving, people arriving, warmer palette."
- "Same view at eye level from the street with more of the neighbouring context visible."
- "Change the cladding to {{alternative_material}} and keep everything else the same."

## Guardrails

Never present a generated image as a representation of what will be built. Label it clearly as an
illustrative visual, keep it out of planning submissions and contracts, and check that no
generated image contains a real building, brand or person that creates a rights problem.

---

*Part of the construction agent skills library — CC BY 4.0. Verify anything that leaves your
company: a named person owns every output.*
