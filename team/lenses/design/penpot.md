# Penpot MCP Workflow

Penpot is Ashley's primary editable design canvas.

Use Penpot Cloud unless the user explicitly chooses self-hosting.

## Connection model

```text
Codex + Ashley
      ↓ MCP
Penpot remote MCP
      ↓
active Penpot file/page
```

The secret MCP URL/token belongs in the user's Codex configuration, not the product repo.

## Setup

In Penpot:
1. enable MCP integration in account/integration settings;
2. generate/copy the MCP server URL;
3. add it to Codex as a remote MCP server named `penpot`;
4. open the design file;
5. connect the active file/page to MCP.

Exact UI labels can change; consult current Penpot docs if needed.

## Before editing

For an unfamiliar file:
1. inspect active page;
2. identify frames;
3. identify components;
4. identify styles/tokens;
5. identify naming;
6. identify approved design authority.

Do not immediately rewrite.

## Concept exploration

Create a dedicated exploration page when appropriate:

```text
01 — Directions
  A — ...
  B — ...
  C — ...
02 — Brand
03 — Foundations
04 — Components
10 — Product / ...
```

Exact naming can adapt to the product.

Keep comparison frames:
- same viewport;
- same representative content;
- comparable fidelity.

## Writing

Make coherent batches:
- foundations;
- a whole component family;
- one screen/flow;
- one concept variant.

Avoid dozens of unrelated micro-writes if a coherent change is possible.

## Inspection loop

After a write:
- re-read the page/object structure;
- visually inspect if vision/screenshot is available;
- verify no unintended element changed;
- compare against project memory.

A successful MCP response is not proof of good layout.

## Design-system hygiene

When direction is approved:
- convert repeatable properties to tokens/styles;
- create components/variants;
- name semantically;
- avoid local overrides unless justified.

Exploration can be looser; approved production design should become systematic.

## Safety

Before broad/destructive edits:
- state intended scope internally/briefly;
- preserve approved alternatives;
- duplicate exploration if uncertainty is high.

Do not destroy A/B/C concepts before the user chooses unless asked.

## Handoff to implementation

Before implementation:
- approved frames identified;
- design-system foundations documented;
- responsive behavior documented;
- states documented;
- components named coherently;
- unresolved questions recorded.

Penpot + `docs/design/` together are the design source of truth:
- Penpot = visual artifact;
- docs = rationale/contracts.


## Rendered visual QA

For high-fidelity work, layer/structure inspection is necessary but not sufficient.

Use the best available visual path:
1. `export_shape` for the relevant frame/artifact when available;
2. screenshot/preview from the connected environment when available;
3. another host-provided image observation path.

Then inspect:
- hierarchy at intended viewing size;
- clipping/overflow;
- optical alignment;
- text wrapping/truncation;
- contrast;
- density;
- visual noise;
- brand coherence;
- thumbnail/feed legibility where relevant.

After fixes, inspect again.

Remote MCP exposes `export_shape`, but remote mode may not write directly to arbitrary local file paths. Work with the representation/path the client exposes.

If pixels cannot be observed, mark visual QA as **not verified** rather than claiming completion.

## Design ↔ code sync

Penpot MCP can inspect tokens/styles, export assets and map design components to code concepts.

When syncing:
- inspect implemented tokens/components first;
- identify authoritative source per layer;
- align semantic names/identifiers;
- document intentional differences;
- do not overwrite production conventions merely to make Penpot tidy.

Read `design-code-sync.md`.
