# shadcn/ui Materialization

Use this when shadcn/ui is the intended implementation system, whether or not shadcn has already been installed.

shadcn evolves, so Ashley must not rely on a memorized catalog.

## Choose the operating mode

### A. Design-first shadcn mode

Use when shadcn is **not installed yet** and the user wants Ashley to prepare the future component system.

Inputs:
1. product/domain/flows;
2. approved brand and visual foundations;
3. current official shadcn component catalog/docs/registry;
4. accessibility and platform constraints.

Output:
- planned component manifest;
- reusable design variables;
- `design/ui.lib.pen`;
- optional `design/ui-catalog.pen`;
- future implementation contract in DESIGN_SYSTEM.md/HANDOFF.md.

In this mode, design is the initial visual specification.

Do not require `components.json` or local shadcn source because they do not exist yet.

### B. Mirror mode

Use when shadcn is already installed.

Inputs:
1. `components.json`;
2. actual installed/local component source;
3. project theme/tokens;
4. current official docs only when local code is insufficient.

Local code wins over upstream examples.

## Current upstream evidence

When planning before installation, consult the current official shadcn docs/registry at task time.

Do not fabricate the catalog.

The current official component directory is the authoritative discovery surface. Use current CLI/docs/registry commands when exact anatomy/behavior/availability matters.

Read/view/search operations are preferred over installing components merely for inspection.

## Design-first selection: product needs first

Do not start with "draw every shadcn component."

Start with product flows and derive a planned set.

For a B2B operations product, likely families may include:

### Foundations / basic display
- Typography
- Button
- Button Group when product actions justify it
- Badge
- Separator
- Avatar
- Skeleton
- Spinner

### Form controls
- Label
- Field/Form composition
- Input
- Input Group when justified
- Textarea
- Checkbox
- Radio Group
- Switch
- Select / Native Select as appropriate
- Slider only when a real use case exists
- Date Picker / Calendar when workflows require dates

### Feedback / empty states
- Alert
- Progress when asynchronous progress exists
- Toast/Sonner
- Empty

### Navigation / disclosure
- Tabs
- Accordion
- Breadcrumb
- Pagination
- Sidebar only if the IA actually uses one
- Command only if command/search workflows justify it

### Overlays
- Dialog
- Alert Dialog
- Sheet/Drawer when narrow-screen or contextual workflows need them
- Popover
- Tooltip
- Dropdown Menu
- Context Menu only when the product interaction model requires it

### Data-heavy operations
- Table
- Data Table pattern
- Scroll Area
- Card only for bounded semantic groups, not as a default layout primitive

This list is planning guidance only. The live official shadcn catalog and product needs decide the final manifest.

## Do not overbuild

Classify planned components:

- **core** — clearly needed by known product flows;
- **supporting** — likely needed in secondary flows;
- **deferred** — available upstream but not justified yet.

Materialize core first.

Do not spend time building Carousel, Chart, OTP, Resizable, Aspect Ratio, etc. unless the actual product needs them.

## Foundations

In design-first mode, create the project's future semantic variables from approved brand/design foundations.

Typical shadcn-compatible semantic roles may include:
- background;
- foreground;
- card;
- popover;
- primary;
- secondary;
- muted;
- accent;
- destructive;
- border;
- input;
- ring;
- chart-* when needed.

These names are implementation-alignment aids. Their values come from the product identity, not shadcn defaults.

Also define:
- typography;
- radius;
- spacing/control heights;
- focus treatment;
- icon sizing/stroke conventions;
- elevation/border behavior;
- density.

## Component contract in design-first mode

For each planned component Ashley decides and documents:
- product use cases;
- anatomy/subcomponents;
- variants justified by the product;
- sizes justified by density/context;
- visual states;
- interactive states that affect appearance;
- content slots;
- token dependencies;
- intended shadcn counterpart;
- accessibility implications.

Do not copy every upstream example/variant blindly.

The goal is a product-specific system that can later be implemented cleanly using shadcn primitives.

## pen.dev target

Prefer:

```text
design/
├── ui.lib.pen
└── ui-catalog.pen
```

The library contains reusable origins and variables.
The catalog contains labeled specimens and state/variant demonstrations.

Use actual reusable components/instances/slots, not flattened drawings.

## Batch order

A useful design-first order:

1. foundations;
2. Button / Badge / Separator / Avatar;
3. Input / Textarea / Label or Field;
4. Checkbox / Radio Group / Switch;
5. Select / Popover / Tooltip;
6. Dialog / Alert Dialog / Sheet/Drawer as needed;
7. Tabs / Breadcrumb / Pagination;
8. Table / Data Table;
9. product-specific composed patterns.

This order is not mandatory. Product dependencies win.

## Batch discipline

Default:
- 1 complex component; or
- 2–4 tightly related simple components.

After each batch:
- inspect structure/reusability;
- screenshot;
- visual QA;
- compare to approved product foundations;
- fix before continuing;
- update manifest.

## Later implementation

When shadcn is eventually initialized:
- compare the code implementation to this design-first contract;
- map tokens;
- implement only the approved variants/states;
- document intentional implementation differences;
- switch future sync work to mirror mode.
