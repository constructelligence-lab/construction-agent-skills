---
name: interior-render-iteration
description: Interior render: iteration prompt for construction and design work, covering rendering, interior, iteration. The first interior image is close but wrong — the light, the proportions or the materials — and you want to change one thing at a time rather than regenerate from scratch. Use when the user asks for help with interior render: iteration prompt, or is working on rendering, interior, iteration in a construction, engineering or design context. Produces a reviewable draft, never a final answer.
license: CC BY 4.0
section: Visualisation and rendering
tags: rendering, interior, iteration
updated: 2026-09-24
source: construction-prompts/prompts/04-visualisation/02-interior-render-iteration.md
---

# Interior render: iteration prompt

The first interior image is close but wrong — the light, the proportions or the materials — and you
want to change one thing at a time rather than regenerate from scratch.

## Inputs to collect

Ask the user for any of these you do not already have. Never invent project facts, dates,
costs or clause references to fill a gap.

- `{{change_one}}`
- `{{change_three}}`
- `{{change_two}}`
- `{{light_source}}`
- `{{lighting}}`
- `{{materials}}`
- `{{room_size}}`
- `{{room_type}}`
- `{{what_to_change}}`
- `{{what_to_keep}}`

## Instructions

```text
Refine the previous interior image. Change only what is listed; keep the geometry,
camera and mood otherwise identical.

Room: {{room_type}}, approximately {{room_size}}.
What is right about the current image: {{what_to_keep}}.
What must change: {{what_to_change}}.
Materials to keep: {{materials}}.
Lighting to keep: {{lighting}}.

Specific changes:
1. {{change_one}}
2. {{change_two}}
3. {{change_three}}

Keep: realistic scale for {{room_type}}, believable ceiling height, no furniture
floating, consistent light direction from {{light_source}}, photographic exposure.
Avoid: text, logos, fisheye distortion, duplicated furniture, impossible joinery.
```

## What good output looks like

- Only the requested things changed, which is how you keep a client-approved image recognisable.
- Realistic daylight behaviour for the room type: an office at {{time}} should not look like a
- Believable scale cues — door heights, furniture, ceiling grid — because that is what clients

## Follow-ups

- "Now produce the same room at {{time_of_day}} with blinds half closed."
- "Give me the same image with a wider camera and the ceiling visible."
- "Describe the changes a client is most likely to ask for based on this image."

## Guardrails

Keep an approved version of any image a client has signed off, so an iteration cannot overwrite the
record. Never present an interior image as a specification of finishes — schedules and
specifications govern, not pictures.

---

*Part of the construction agent skills library — CC BY 4.0. Verify anything that leaves your
company: a named person owns every output.*
