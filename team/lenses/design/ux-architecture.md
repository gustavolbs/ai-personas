# UX Architecture

## Start with the object/work model

Map:
- actors;
- domain objects;
- object relationships;
- lifecycles;
- queues/inboxes;
- projects/workspaces;
- approvals/handoffs;
- history/audit;
- search/filter needs.

Then choose information architecture.

## Navigation strategies

Possible models:
- object-based;
- task-based;
- workspace/project-based;
- inbox/queue-based;
- time-based;
- role-based;
- hybrid.

For navigation specify:
- global vs local;
- active context;
- selected state;
- return path;
- deep linking;
- breadcrumbs only when hierarchy benefits;
- permission-driven visibility;
- cross-object navigation.

Do not add top-level sections just because SaaS templates typically have them.

## Workflow map

For each critical flow:

```text
trigger
→ entry
→ required context
→ decision
→ action
→ system processing
→ result
→ recovery / next action
```

Map branches before high fidelity.

## State architecture

Separate state dimensions rather than collapsing them.

Examples:
- lifecycle: draft / active / archived;
- processing: queued / processing / complete / failed;
- payment: due / paid / overdue / reversed;
- permission: editable / read-only / blocked;
- data quality: fresh / stale / partial;
- selection: selected / not selected.

Avoid one overloaded "status" badge when users need different dimensions.

## Progressive disclosure

Hide information when:
- not needed for current decision;
- predictable to reveal;
- easy to recover.

Do not hide:
- frequent actions;
- critical status;
- information required before irreversible decisions.

Clean screenshots are not a design goal.

## Role/permission design

For consequential actions define:
- visibility;
- editability;
- approval;
- delegation;
- override;
- reason for block;
- escalation path.

Choose intentionally among:
- hidden;
- visible but disabled;
- visible with permission explanation.

Security authorization is backend responsibility; permission comprehension is UX responsibility.

## Search/filter/sort

For operational products ask:
- what users remember when searching?
- which filters repeat every day?
- must filter state persist/share?
- are saved views valuable?
- which sort defines urgency?
- what happens when filters return zero results?

## Responsive architecture

Preserve **the job**, not desktop geometry.

For narrow widths decide:
- what remains visible;
- what becomes detail;
- which controls collapse;
- what needs sticky context;
- touch interaction changes;
- table transformation strategy.

Do not mechanically transform each desktop row into a giant card.
