# Accessibility & Inclusive Design

Accessibility is part of the design contract.

Use current WCAG/platform guidance when exact criteria matter.

## Core checks

### Perceivable
- sufficient text/UI contrast;
- information not dependent on color alone;
- meaningful images have alternatives in implementation;
- layouts survive zoom/text scaling;
- content remains understandable without animation.

### Operable
- keyboard access;
- visible focus;
- logical focus order;
- adequate touch targets;
- no hover-only essential interaction;
- no inaccessible drag-only action;
- escape/dismiss behavior.

### Understandable
- predictable controls;
- clear labels;
- consistent vocabulary;
- errors explain cause/recovery;
- destructive consequences are explicit;
- forms preserve context.

### Robust implications
Design components so implementation can carry:
- semantic roles;
- accessible names;
- table semantics;
- live-status announcements;
- dialog focus management.

## Cognitive accessibility

Reduce:
- unnecessary choices;
- ambiguous language;
- hidden mode changes;
- inconsistent controls;
- recall burden;
- long unstructured forms.

Recognition over recall does not mean showing everything at once.

## Motion

Provide a reduced-motion path for nonessential animation.

Avoid:
- motion required to understand state;
- high-amplitude unnecessary parallax;
- repeated autoplay motion in task surfaces.

## Data visualization

Do not rely on:
- hue alone;
- tiny legends far from data;
- inaccessible hover-only tooltips.

Use:
- labels;
- patterns/shapes where needed;
- adequate contrast;
- text/table alternatives for important data.

## Accessibility versus aesthetics

Do not "solve" accessibility by flattening all brand character.

Find alternatives:
- darker/lighter semantic token;
- stronger type weight/size;
- redundant cue;
- better focus treatment;
- different surface relation.

Good accessibility and strong visual identity are compatible.
