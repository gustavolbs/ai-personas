# Design Systems

A design system is a decision system, not a component inventory.

## Foundations

Define only what the product needs:
- color primitives + semantics;
- type roles;
- spacing;
- layout/grid;
- radius;
- borders;
- elevation;
- iconography;
- motion;
- z-index/layers where relevant;
- density modes if necessary.

## Token architecture

When complexity warrants:

```text
primitive → semantic → component
```

Example:
`gray-950 → text-primary → button-primary-label`.

Do not introduce three token layers for a tiny product with no benefit.

## Semantic naming

Prefer role over appearance.

Weak:
`blue-500`

Strong:
`action-primary-bg`
`text-muted`
`status-danger-bg`

Raw palette primitives remain useful underneath.

## Components

Create a component when:
- visual/interaction behavior repeats;
- consistency reduces user learning;
- implementation benefits from shared contract.

Do not create components purely to satisfy a checklist.

## State contract

For interactive components consider:
- default;
- hover;
- focus-visible;
- pressed;
- selected;
- disabled;
- loading;
- invalid/error;
- success where relevant.

## Patterns

Systems include compositions:
- data table;
- filter bar;
- detail panel;
- empty state;
- confirmation;
- wizard;
- command menu;
- permission block;
- bulk action.

A library of atoms alone does not solve product consistency.

## Density

Some products need:
- comfortable;
- compact.

If density variants exist, define what changes:
- row height;
- control height;
- gap;
- typography;
- not arbitrary scaling of everything.

## Governance

Record:
- intended use;
- anti-patterns;
- variant rationale;
- deprecation;
- replacement.

Avoid variant explosion.

## Handoff

Before implementation:
- name components consistently in Penpot;
- use reusable tokens/styles;
- define responsive behavior;
- define state behavior;
- preserve decision rationale in DESIGN_SYSTEM.md.


## Materializing an implemented component library

When an existing codebase already contains a component system, the inventory is evidence, not a brainstorming prompt.

Use `component-library-materialization.md`.

For each component, capture:
- source file / registry item;
- public variants;
- sizes;
- interaction states;
- composition/subcomponents;
- token dependencies;
- icons;
- content slots;
- responsive behavior if relevant;
- accessibility semantics that affect design.

Do not create visual variants that the implementation does not support unless they are explicitly proposed as design-ahead changes.

For large systems, build a reusable design library and a specimen/catalog page separately.
