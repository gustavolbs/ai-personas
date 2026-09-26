# Design ↔ Code Sync

Ashley should prevent the editable design source and the product codebase from becoming independent realities.

## First decision: source of truth

Choose authority **per layer**, not necessarily one source for everything.

Example:
- semantic tokens: code authoritative;
- exploratory visual direction: design canvas authoritative;
- component names/contracts: shared mapping;
- brand source SVG: brand assets folder authoritative;
- product behavior: code/product spec authoritative.

Record in `docs/design/HANDOFF.md`.

## Existing project audit

Inspect:
- CSS variables;
- Tailwind/theme config;
- token packages;
- font loading;
- component primitives;
- variants;
- icon library;
- spacing/radius conventions;
- responsive breakpoints;
- state behavior;
- accessibility implementation.

Then inspect the selected design canvas:
- tokens/styles;
- components;
- variants;
- naming.

## Drift classes

Classify differences:

- **intentional** — documented design/code difference;
- **design ahead** — approved design not yet implemented;
- **code ahead** — implementation changed first;
- **legacy** — stale artifact;
- **unmapped** — relationship unknown.

Do not "fix" intentional divergence automatically.

## Mapping contract

For important primitives/components record:

```text
Design: Button / Primary / MD
Code:   packages/ui/Button variant=primary size=md
Tokens: action-primary-*
States: default hover focus pressed disabled loading
```

## Sync workflow

### Code → design
Use when implementation is current truth:
- extract tokens/styles;
- update design-canvas foundations;
- align component names/states;
- document exceptions.

### Design → code
Use after approved design:
- identify changed tokens/components;
- describe behavior/responsive changes;
- export required assets;
- map to existing implementation primitives before creating new ones.

## Avoid destructive "sync"

Sync is not:
- mass-renaming code to match design-canvas naming/taste;
- replacing accessible components with visual replicas;
- introducing new token families unnecessarily;
- treating screenshot similarity as sufficient behavior parity.

## Handoff

HANDOFF.md should include:
- source-of-truth matrix;
- component map;
- token map;
- approved frames;
- required states;
- responsive behavior;
- asset exports;
- known intentional drift;
- unresolved implementation questions.


## Component-library sync

When mirroring an implemented UI library into design:
- treat component source and registry metadata as the behavior/variant contract;
- treat approved project tokens as the visual contract;
- create a manifest before canvas work;
- mark each component as pending / materialized / QA-passed / drifted;
- do not claim parity from visual resemblance alone.

The design library should reference the code contract in HANDOFF.md.
