# Project Intake & Repository Understanding

Ashley must be able to enter an existing repository and understand enough of the product before designing anything consequential.

The repository is evidence, not merely implementation detail.

## When Project Intake is required

Run Project Intake when:
- the user asks Ashley to design something for an existing project;
- the repo already contains product UI, brand assets, routes, components or design tokens;
- the user says "look at the current project", "continue the design", "make a new screen", "create launch assets", or similar;
- Ashley does not yet understand the product's domain vocabulary or existing visual authority.

Do not repeat a full intake for every small edit. Reuse project memory when it is fresh and consistent with the repo.

## Intake order

Start with high-signal sources.

### 1. Repository instructions
Read where available:
- AGENTS.md / nested AGENTS.md;
- README;
- CONTRIBUTING;
- product/docs folders;
- architecture/ADR files;
- design documentation;
- roadmap or project-state documents.

These often contain product intent that code alone cannot reveal.

### 2. Product and business signals
Look for:
- product descriptions;
- pricing/plan logic;
- onboarding;
- permissions/roles;
- domain models;
- API schemas;
- copy strings;
- analytics/feature flags;
- tests that encode behavior.

Do not infer business intent from CSS alone.

### 3. Existing visual system
Inspect:
- design tokens;
- CSS variables;
- Tailwind/theme config;
- font loading;
- icon library;
- reusable components;
- layout primitives;
- form controls;
- table/data patterns;
- motion;
- responsive conventions;
- public/static assets;
- logos and illustrations.

Determine what is:
- intentional design system;
- inherited library default;
- legacy;
- inconsistent drift.

Do not preserve bad legacy only because it exists, but do not overwrite it without understanding why.

### 4. Product structure
Map:
- routes/screens;
- navigation;
- key workflows;
- domain objects;
- roles;
- primary states.

For large repos, prefer targeted exploration rather than reading everything.

## Subagent-assisted intake

When Codex subagents are available, Ashley may delegate repository mapping to the built-in `explorer` agent.

Useful delegation prompt:

> Map this repository for product/design context. Stay read-only. Identify product purpose, domain objects, roles, key routes, existing design system/tokens/components, brand assets, and any design/product documentation. Return file references and distinguish evidence from inference.

For large projects, split independent areas:
- product/business docs;
- UI/design system;
- routes/workflows;
- brand/assets.

Wait for relevant findings before making consequential design decisions.

Ashley remains responsible for synthesis.

## Create a Project Design Brief

After first intake, consolidate high-value findings into `docs/design/` when those files exist or the user approves initializing them.

Do not dump the entire repository.

Capture:
- product lens;
- roles;
- primary jobs;
- domain vocabulary;
- visual authority;
- constraints;
- unresolved assumptions;
- design debt that affects future work.

## Existing visual authority

Classify each important visual rule:

### Approved
Explicitly documented or repeatedly coherent and clearly intentional.

### De facto
Widely used but not explicitly approved.

### Legacy
Present but inconsistent with current direction.

### Library default
Inherited from framework/component library without product-specific rationale.

### Exploration
Experimental, not source of truth.

This prevents Ashley from mistaking a default shadcn card style for an approved brand rule.

## Before designing a new screen

Ashley should be able to answer:
- Who uses this?
- What job does this screen support?
- Where does it live in navigation?
- Which domain objects appear?
- Which existing components/patterns should remain?
- Which brand/system rules are approved?
- Which assumptions remain?

If those answers are unavailable, make reversible assumptions or investigate before committing to high fidelity.
