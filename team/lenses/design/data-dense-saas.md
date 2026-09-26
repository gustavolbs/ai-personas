# Data-Dense SaaS & Operational Interfaces

Operational software is a special design context.

## Optimize information throughput

Ask:
- what must be scanned repeatedly?
- what indicates urgency?
- what must be compared across rows?
- what changes frequently?
- what action repeats?
- what information is only occasionally needed?

Prefer:
- alignment;
- columns;
- compact hierarchy;
- persistent context;
- saved filters/views;
- keyboard efficiency;
- list-detail patterns;
- sticky headers/columns when justified.

## Dashboard skepticism

A dashboard is useful when users need an overview/decision surface.

Do not create:
- four KPI cards;
- three charts;
- recent activity;
simply because the product is SaaS.

A daily operator may need an **inbox/queue**, not a dashboard.

## Tables

Design real table behavior:
- sorting;
- filtering;
- search;
- pagination/infinite load;
- row actions;
- selection;
- bulk actions;
- expandable/contextual detail;
- long data;
- missing data;
- pinned columns;
- responsive strategy;
- loading/partial/error.

Prioritize comparison columns.

## Exception-driven design

Many operational products are about handling exceptions.

Consider:
- "needs attention" queue;
- severity;
- SLA/deadline;
- blocker;
- owner;
- next action;
- reason.

Users should not inspect every object to discover the few that need action.

## List-detail

Useful when users repeatedly:
1. scan many items;
2. inspect one;
3. act;
4. move to next.

Preserve list context and selection.

## Filters

Frequent filters may deserve first-class controls.
Rare filters can enter an advanced panel.

Show active filter state and provide clear reset.

"0 results because there is no data" and "0 results because filters exclude everything" need different empty states.

## Density does not mean clutter

Dense UI still requires:
- alignment;
- grouping;
- controlled type hierarchy;
- consistent row rhythm;
- whitespace at meaningful boundaries.

Use whitespace strategically rather than uniformly.
