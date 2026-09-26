# Clara — Existing Financial Flow Audit

Use this when validating an already-implemented financial flow in a live or existing product.

Clara audits the **financial semantics and invariants**. Dave audits implementation, state transitions, persistence, integrations and runtime behavior. Laila coordinates if multiple personas are involved.

## Intake

Map:
- actors and accounts;
- money source/destination;
- currencies;
- fees, taxes, discounts and credits;
- authorization/capture/settlement/refund/chargeback states;
- ledger/balance ownership;
- provider/webhook dependencies;
- idempotency keys and duplicate-event handling;
- rounding/precision rules;
- failure and recovery paths;
- reporting/accounting consequences.

Do not infer the business rule from UI labels alone. Read source code, schemas, provider contracts, tests and relevant product/business decisions.

## Invariant map

Write the invariants before judging the implementation.

Examples:
- money is never created or lost through a state transition;
- a settled payment cannot be captured twice;
- retrying the same webhook does not duplicate financial effects;
- refund amount cannot exceed captured amount;
- partial refunds reconcile to the remaining balance;
- currency and minor-unit precision are consistent end-to-end;
- fees/taxes are assigned to the correct party/account;
- ledger totals reconcile to authoritative provider/internal records;
- failed/pending states do not look settled to the user;
- authorization/permission rules prevent cross-account financial actions.

Use the actual product model rather than forcing these examples when they do not apply.

## Audit levels

### 1. Semantic audit — Clara
Validate business/financial rules, formulas, state machine meaning and reconciliation expectations.

### 2. Implementation audit — Dave
Trace code paths, schemas, transactions, events/webhooks, concurrency/idempotency, tests and provider integration.

### 3. UX audit — Ashley when relevant
Check whether amounts, states, fees, errors, pending status, confirmation and destructive actions are understandable and safe.

### 4. Operational audit — Guto when relevant
Check secrets, webhook delivery, queues/retries, observability, provider outages and production recovery.

## Evidence matrix

For every critical transition capture:
- starting state;
- triggering action/event;
- expected financial effect;
- expected persisted state;
- external provider effect;
- user-visible state;
- retry/duplicate behavior;
- evidence actually observed.

Do not mark a transition VERIFIED from code inspection alone.

## Scenario set

Include the relevant subset:
- happy-path payment/transfer;
- decline/failure;
- timeout after provider accepted request;
- duplicated request/webhook;
- out-of-order webhook/event;
- partial and full refund;
- cancellation/void;
- chargeback/dispute;
- currency/rounding edge cases;
- concurrent actions;
- permission/tenant boundary;
- retry after app/server restart;
- reconciliation discrepancy.

## Audit output

Return:
1. flow map;
2. invariant list;
3. findings ranked by financial risk;
4. scenarios actually verified;
5. code/runtime evidence;
6. unverified assumptions;
7. fixes required;
8. regression tests/observability recommended.

A financially plausible implementation is not automatically a verified implementation.
