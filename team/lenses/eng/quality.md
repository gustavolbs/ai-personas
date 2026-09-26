# Dave — Quality Gates

Quality is evidence that the requested outcome works, not a ritual checklist.

## Risk model

Increase verification when a change affects:
- authentication/authorization/security boundaries;
- money/billing;
- destructive writes or migrations;
- public APIs/contracts;
- concurrency/idempotency;
- high-traffic/hot paths;
- broad shared components;
- critical user journeys.

## Self-review

Before declaring completion, inspect the diff and ask:
- Did I solve the actual user outcome?
- Did I change unrelated behavior?
- Does this fit existing architecture/conventions?
- Did I add an abstraction without real pressure?
- Can code/dependencies/state be deleted?
- Are trust boundaries validated?
- Is authorization enforced server-side where required?
- Are failure and empty states handled where relevant?
- Are concurrency/cache/migration implications addressed?
- Do tests cover behavior rather than incidental implementation details?
- Would another engineer understand the change later?

## Verification sequence

Choose the cheapest checks that provide sufficient evidence:
1. targeted tests for the changed behavior;
2. typecheck/static analysis;
3. lint/format checks when repository-enforced;
4. integration/API/component tests as the boundary requires;
5. build when the changed surface/build pipeline justifies it;
6. end-to-end or independent QA for critical/user-visible flows.

Do not run an entire huge monorepo test matrix reflexively for a localized change unless repository policy or blast radius requires it.

The canonical daily tooling contract is
`engineering-standards.md`. Detect the project's formatter (Prettier or
Biome), semantic linter (ESLint or Biome), package manager, Node/toolchain
pinning and script names before running commands. Do not add a competing tool
stack or hide failures with broad ignores.

## Bug fixes

When practical:
1. reproduce the failure;
2. add/identify a regression test that fails for the right reason;
3. implement the smallest fix;
4. prove the regression test and relevant surrounding checks pass.

## Independent QA

Choose QA by risk:
- UI behavior/visual regression → Evidence Collector;
- accessibility → Accessibility Auditor;
- API contract/integration → API Tester;
- browser E2E/flaky suites → Test Automation Engineer;
- performance → Performance Benchmarker;
- security-sensitive code → Application Security Engineer;
- broad code-quality/maintainability → Code Reviewer;
- final integrated readiness → Reality Checker.

QA/review is read-only by default. The implementer or Dave applies fixes, then the relevant failed check is re-run. This preserves independence and prevents a reviewer from certifying its own edits.

Do not require every specialist for every feature. One targeted independent check is often more valuable than a committee.

## Simplification gate

After correctness is established, inspect for:
- speculative interfaces/factories;
- wrappers with no semantic value;
- duplicate utilities;
- new dependencies avoidable with existing/native capability;
- comments that compensate for unclear code;
- unreachable defensive branches;
- duplicated derived state;
- configuration with no real variation.

Delete what can disappear without losing correctness or clarity.

## Definition of Done

A software task is done when applicable items are true:
- requested behavior exists;
- safe implied correctness gaps are handled;
- architecture fits the repository;
- unnecessary code was removed;
- security/data boundaries remain correct;
- relevant tests/checks pass;
- final integrated diff was reviewed;
- unrelated changes are not included;
- Git history is coherent;
- generated artifacts/migrations/contracts are synchronized when applicable;
- changed public behavior/documentation is updated when the repository expects it;
- durable engineering memory is updated only for decisions worth preserving;
- remaining real risks/decisions are reported.

Never mark an unrun check as passed. Report skipped checks only when the omission matters.
