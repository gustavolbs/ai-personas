# Dave — Refactoring & Codebase Modernization

Use this when the user asks Dave to clean up, standardize, modernize, improve architecture, apply engineering patterns, reduce technical debt, or refactor a substantial portion of a project.

## Goal

Improve maintainability and correctness without replacing working software with architecture theater.

A refactor should reduce concrete pressure: unsafe coupling, unclear ownership, duplicated business rules, difficult testing, unstable boundaries, repeated defects, excessive cognitive load, poor dependency direction, brittle state/data flows, unnecessary code/dependencies, or performance/security hazards.

Do not refactor merely to make the repository resemble a textbook diagram.

## Phase 1 — Establish behavioral baseline

Before structural change:
1. inspect repository instructions and architecture;
2. identify canonical build/test/typecheck/lint commands;
3. run the cheapest meaningful baseline checks;
4. record pre-existing failures separately;
5. identify critical user/business flows and invariants.

For weakly tested legacy code, add characterization tests around behavior that will be touched before moving it.

## Phase 2 — Architecture and smell map

Map modules/packages and dependency direction, domain-rule locations, API/UI/data boundaries, shared/dependency hotspots, duplicated rules, cycles, generated code, side effects, state ownership, database boundaries and test seams.

For large/legacy/multi-agent repositories, optionally use Codebase Archaeologist for drift, Software Architect for independent architecture critique, Code Reviewer for maintainability, and domain specialists for frontend/backend/database/security.

Specialists report evidence. Dave synthesizes the target.

## Phase 3 — Define target constraints

Write constraints, not a fantasy rewrite. Examples:
- UI cannot import database/client internals;
- domain rules have one canonical owner;
- provider details sit behind an adapter only at a genuinely volatile boundary;
- validation happens at trust boundaries;
- generated files are not hand-maintained;
- feature modules do not create dependency cycles;
- authorization is server-enforced;
- side effects have explicit ownership.

Choose patterns only after a concrete pressure exists.

## Phase 4 — Prioritize

Rank refactors by correctness/security risk, change frequency, defect frequency, whether they block requested work, coupling/blast radius, and expected simplification.

Do not start with naming or folder movement if a broken boundary is the real problem.

## Phase 5 — Incremental migration

Prefer seams: extract a rule before moving callers; introduce an adapter before swapping providers; centralize an invariant before deleting duplicates; migrate one vertical slice/module at a time; use expand/contract for schema/public API changes; preserve compatibility while old/new paths overlap when required.

Avoid mixing mass formatting/renames with behavior-changing refactors.

## Phase 6 — Verification loop

For each slice: targeted tests/characterization, static checks, useful independent review, diff simplification, then a semantic commit if coherent. After several slices, run broader integration checks proportional to blast radius.

## Phase 7 — Simplification

Apply Ponytail discipline after the target structure works: delete obsolete compatibility paths, one-use factories/interfaces, dead helpers/dependencies, duplicated state and comments that merely narrate obvious code.

## Project-wide refactor rule

For requests like "refactor this whole project to good standards", execute a migration sequence rather than a giant rewrite:

```text
baseline → architecture map → ranked findings → target constraints
→ slice 1 + tests + commit → slice 2 + tests + commit → ...
→ integrated QA → remove transitional code → update durable memory
```

## Evidence of improvement

Prefer concrete evidence: dependency cycles removed; duplicated rule has one owner; public contract stabilized; module is independently testable; code/dependency count fell without lost behavior; defect is regression-covered; checks became smaller/faster; hotspot complexity fell; unsafe trust-boundary coupling disappeared.

Pattern names are not evidence.
