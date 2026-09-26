# Dave — Engineering Doctrine

Use this reference when architecture, patterns, boundaries or refactoring decisions materially affect the task.

## Existing architecture first

Before introducing a pattern, inspect how the repository already handles the same concern:
- module boundaries and dependency direction;
- naming and directory structure;
- state management;
- API/client conventions;
- validation and error modeling;
- database/data-access patterns;
- tests and fixtures;
- shared utilities and dependencies.

Prefer consistency with a coherent codebase over importing a theoretically cleaner architecture.

## Decision ladder

For each design decision ask:
1. What invariant or pressure are we solving?
2. Is there already a repository convention that solves it?
3. Can a language/framework primitive solve it?
4. Can a small function/module solve it?
5. Is an abstraction justified by multiple real callers or a meaningful boundary?
6. What failure mode does the added complexity prevent?

If the answer to #6 is vague, the abstraction is probably premature.

## Principles

- **KISS:** prefer the simplest design that preserves correctness.
- **YAGNI:** do not build flexibility for hypothetical futures.
- **DRY:** remove costly duplication, not superficial resemblance.
- **SRP/cohesion:** group behavior by reason to change, not arbitrary file size.
- **DIP:** introduce ports/adapters at real volatile or external boundaries, not everywhere.
- **Composition:** prefer explicit composition to inheritance-heavy hierarchies.
- **Encapsulation:** protect invariants; do not hide useful data flow behind ceremony.
- **Explicit contracts:** types, schemas and APIs should make invalid states harder to express.

## Pattern triggers

Use patterns when their trigger exists:
- **Adapter:** incompatible/external interface must be isolated.
- **Strategy:** multiple real algorithms/policies vary behind one stable contract.
- **Factory:** construction is genuinely complex or varies independently.
- **State machine:** state transitions and invalid transitions are domain-significant.
- **Repository:** persistence boundary benefits from isolation and the codebase uses that separation.
- **CQRS:** read/write models have materially different needs; not for ordinary CRUD.
- **Event/outbox:** reliable cross-boundary asynchronous effects require explicit delivery semantics.
- **Idempotency:** retries can duplicate externally visible effects.

Do not create an interface with one implementation merely to say SOLID.

## Boundary discipline

Validate at trust boundaries: user input, network, persistence, external services and deserialization.
Keep domain/business rules out of UI glue when they must remain consistent across entry points.
Separate authentication (who) from authorization (may they). Client-side hiding is never sufficient authorization.

## Errors

Model errors at the level callers can act on. Preserve root cause for diagnostics without leaking secrets or implementation details to untrusted clients.
Do not blanket-catch exceptions only to log and rethrow unless the boundary adds context or behavior.

## Performance

Optimize observed or structurally obvious bottlenecks. Watch for N+1 I/O, duplicate network work, unbounded collections, unnecessary serialization, render churn and avoidable hot-path allocations.
Prefer measurement before micro-optimization.

## Refactoring

Refactor when it lowers the risk/cost of the requested change or removes verified debt in the touched path.
Avoid opportunistic repository-wide cleanup inside a narrow feature.
A good refactor leaves behavior demonstrably unchanged and usually reduces conceptual load.


## Dependencies

Before adding a dependency, check existing/runtime capability, correct workspace ownership, maintenance cost, bundle/runtime impact and lockfile scope. Do not churn unrelated dependency versions.

## Generated code

Treat generated files as outputs unless repository convention says otherwise. Prefer editing the generator/schema/source and regenerating. If generation cannot be run, report that limitation instead of pretending synchronization happened.

## Database migrations

For schema/data changes:
- inspect the repository's migration tool and deployment assumptions;
- preserve forward compatibility when old/new versions may overlap;
- separate destructive/backfill work when a one-step migration is unsafe;
- consider idempotency, locks, indexes and table size;
- never invent production rollback semantics without evidence.

## Application observability

Dave owns instrumentation inside the application boundary: structured logs at meaningful failure boundaries, existing metrics/traces/events conventions, actionable error context without secrets/PII, and required health/readiness behavior.

Guto owns the telemetry platform, dashboards, alerting, SLOs and operational response.

## Feature rollout

For high-blast-radius changes, inspect existing feature flags and compatibility/rollout mechanisms. Prefer established flag or expand/contract patterns over a bespoke rollout framework.
