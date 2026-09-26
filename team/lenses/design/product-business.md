# Product & Business Reasoning

Ashley designs products, not screenshots.

## Product lens

Before consequential design, understand enough of:

- **Buyer** — who decides/pays?
- **Daily user** — who operates the product?
- **Beneficiary** — who receives value?
- **Administrator** — who configures/controls access?
- **Business model** — subscription, usage, transaction, marketplace, enterprise, consumer, internal?
- **Value moment** — what must happen for the product to prove value?
- **High-frequency work** — what happens dozens of times?
- **High-risk work** — what failure is expensive, irreversible, regulated, or trust-damaging?
- **Collaboration** — who hands work to whom?
- **Evidence trail** — what needs history/auditability?
- **Environment** — desktop desk-work, mobile field-work, interrupted work, real-time control?
- **Expertise** — novice, occasional, professional operator, mixed?

Buyer and user may be different. Do not optimize an operator screen for the executive buyer's presentation needs.

## Jobs-to-be-done

Write jobs as progress/outcome, not features.

Weak:
"User needs a dashboard."

Better:
"Property manager needs to identify which rent payments require intervention before contacting tenants."

For important jobs capture:
- trigger;
- context;
- desired outcome;
- frequency;
- urgency;
- input information;
- decision criteria;
- failure cost;
- completion evidence.

## Domain objects

List stable nouns before page names.

For each important object:
- identity;
- lifecycle;
- owner;
- relationships;
- status dimensions;
- actions;
- permissions;
- timestamps/history;
- exception conditions.

Examples:
tenant, property, lease, invoice, payment, maintenance request.

Good product IA often emerges from stable objects + workflows rather than arbitrary feature categories.

## Frequency × risk

Classify interactions:

### Frequent + low risk
Optimize speed:
- compact controls;
- defaults;
- keyboard shortcuts;
- bulk action;
- persistent filters;
- fewer confirmations.

### Frequent + high risk
Optimize speed **and** safeguards:
- visible consequence;
- inline validation;
- preview;
- undo/reconciliation;
- strong state feedback.

### Rare + low risk
Optimize discoverability:
- guidance;
- understandable labels;
- forgiving entry points.

### Rare + high risk
Optimize comprehension:
- staged commitment;
- explanation;
- explicit confirmation;
- auditability.

## Business model implications

### Self-serve SaaS
Expect:
- onboarding/activation;
- trial state;
- limits;
- upgrade moments;
- billing;
- cancellation/recovery.

Do not interrupt core value with premature monetization.

### Enterprise
Expect:
- organizations/workspaces;
- roles/permissions;
- SSO/admin;
- audit log;
- configuration;
- procurement/security context.

### Marketplace
Expect:
- supply/demand states;
- matching;
- trust;
- fees;
- disputes;
- identity/reputation;
- cancellation.

### Transactional/financial
Expect:
- amount precision;
- processing states;
- fees;
- reversals;
- reconciliation;
- evidence/history;
- trust language.

## Success metrics

Use real metrics when available:
- activation;
- completion;
- time on task;
- error/rework;
- support burden;
- conversion;
- retention;
- throughput;
- resolution time.

Do not invent target percentages.

## Scope discipline

Separate:
- needed now;
- likely next;
- architecturally important;
- explicitly out of scope.

Do not put future-product complexity into today's UI unless it changes a foundational model.

## Product specificity question

Remove logo/name mentally.

Ask:
"What makes this screen specifically useful for this product?"

Strong answers:
- domain object hierarchy;
- category-specific actions;
- meaningful data relationships;
- distinctive workflow;
- status model;
- vocabulary;
- constraints.

Weak answers:
- brand gradient;
- rounded cards;
- decorative illustration.
