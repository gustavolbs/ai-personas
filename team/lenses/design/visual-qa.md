# Visual QA

High-fidelity design must be evaluated as pixels, not only as structure.

## Mandatory loop

For consequential visual work:

```text
create/edit
→ export/render representative artifact
→ inspect pixels
→ critique
→ fix
→ render again
→ pass/fail
```

A successful MCP/tool call is not a QA result.

## Observation hierarchy

Prefer:
1. rendered/exported frame at target size;
2. screenshot of the actual canvas/artifact;
3. host-provided preview/image.

For pen.dev, prefer `TakeScreenshot()`/`Export()` through the canvas tooling or `pen --in <file>.pen --export <preview>.png`; for Penpot, use `export_shape` where appropriate.

If no pixel-level observation is available, explicitly mark the visual gate as unverified.

## Inspect at intended consumption size

Examples:
- product UI: representative desktop/mobile viewport;
- social: actual feed/story/thumbnail size;
- logo: 16/24/32px plus normal display size;
- one-pager: whole page and reading zoom;
- campaign: mobile feed and larger composition.

## Visual QA checklist

### Macro
- first read;
- hierarchy;
- composition;
- balance;
- whitespace;
- density;
- product/message specificity.

### Typography
- wrapping;
- truncation;
- line length;
- optical scale;
- weight hierarchy;
- numeric/data legibility.

### Geometry
- alignment;
- spacing rhythm;
- radius consistency;
- border/shadow noise;
- icon optical balance.

### Color
- contrast;
- semantic consistency;
- over-saturation;
- unintended color competition.

### Real-content stress
Use realistic:
- long names;
- large numbers;
- missing values;
- multi-line copy;
- error states;
- dense lists.

## Independent critique

For important launches/brand systems, Ashley may ask a read-only critic subagent to evaluate the exported artifact independently.

The critic returns observable issues and rationale. Ashley decides what to change.

## Pass criteria

Visual QA passes only when:
- no known critical visual defect remains;
- the artifact works at intended consumption size;
- hierarchy matches the task/message;
- accessibility implications are acceptable;
- the result matches approved brand/system rules;
- remaining issues are consciously accepted tradeoffs.
