# Component Library Materialization

This protocol is for creating a reusable component library in either of two modes:

- **mirror mode** — an implementation/registry already exists and design mirrors it;
- **design-first mode** — the product is being designed before the implementation exists.

Both are more deterministic than normal open-ended creative work.

## 1. Establish mode and authority

Before drawing, classify the task.

### Mirror mode
Use when code/components already exist.

Authority:
- code/registry = behavior + variants;
- approved project tokens = visual contract;
- design canvas = visual representation and design-ahead proposals.

### Design-first mode
Use when the component library does not exist yet.

Authority:
- product jobs/flows = component-need evidence;
- approved brand and design tokens = visual contract;
- current official target-library docs/registry = implementation-feasibility reference;
- design canvas = initial component specification.

In design-first mode Ashley is allowed to define the future component API/variants, but only when they are justified by product needs and remain implementable with the intended library.

Do not create a huge component inventory merely because the upstream library offers it.

## 2. Build a manifest

Do not begin by drawing.

Create an inventory table containing at least:
- component;
- source/evidence;
- family;
- product use cases;
- planned variants;
- planned sizes;
- required states;
- subcomponents;
- token dependencies;
- implementation target/reference;
- status.

In design-first mode, every component must answer: **which product flow/job needs this?**

Suggested statuses:
- pending;
- materializing;
- structure-verified;
- visual-QA-passed;
- blocked;
- intentional-drift.

Store the manifest in design memory or a task-local artifact as appropriate.

## 3. Foundations first

Before components, materialize:
- color variables;
- typography variables/styles;
- spacing;
- radii;
- borders;
- elevation;
- icon approach;
- density/control heights.

Use variables rather than hardcoded repeated values where the canvas supports them.

## 4. Use a real design library

For pen.dev/Pencil, prefer:
`design/ui.lib.pen`

Keep a separate specimen/catalog document if useful:
`design/ui-catalog.pen`

The library contains reusable origins. The catalog demonstrates variants, states and compositions.

Do not turn a screenshot/catalog into the design system itself.

## 5. Batch by dependency

A useful order:

1. foundations;
2. primitive controls;
3. selection controls;
4. feedback/status;
5. overlays;
6. navigation;
7. data display;
8. forms/composites;
9. complex patterns.

Build parent/compound components from already verified primitives.

## 6. Batch size

Default maximum:
- 1 complex component; or
- 2–4 simple related components.

Reduce batch size after any tool error or visual failure.

Never process "all components" in one tool call or one unverified generation pass.

## 7. Per-component contract

Before writing, Ashley must know:
- exact component name;
- source contract;
- required variants;
- required sizes;
- required states;
- content/slot needs;
- token mappings.

After writing:
- inspect object structure;
- verify reusability;
- verify instances/slots where needed;
- render/screenshot;
- visual QA;
- update manifest status.

## 8. Stop conditions

Stop the batch and repair before continuing if:
- tool/schema operation fails;
- origin is not actually reusable;
- instances do not inherit;
- tokens are hardcoded unexpectedly;
- screenshot is visually wrong;
- states/variants are missing;
- the canvas has drifted from the code contract.

Do not bury errors under more generated components.

## 9. Final completion

A materialized library is not complete until:
- manifest is fully resolved;
- reusable origins exist;
- required variants/states are represented;
- tokens are mapped;
- compound components use verified primitives;
- representative screenshots pass visual QA;
- design↔code mapping is documented.


## Design-first planning

When no implementation exists yet:

1. map core product flows;
2. derive needed interaction primitives/patterns;
3. map those needs to the intended implementation library;
4. prefer reusable primitives that cover multiple flows;
5. avoid materializing low-probability upstream components prematurely;
6. mark speculative components separately from committed ones.

Suggested manifest classes:
- **core** — needed by known high-frequency flows;
- **supporting** — likely needed by secondary/administrative flows;
- **deferred** — upstream capability that may be useful later but has no current product evidence.

The design library should be complete for the product phase, not necessarily exhaustive for the upstream ecosystem.
