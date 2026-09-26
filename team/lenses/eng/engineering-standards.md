# Engineering Standards Contract

This is the review contract for application code. Dave and the independent
reviewer apply the sections matching the detected stack; they do not impose
Next.js conventions on an Expo app or rewrite a coherent repository merely to
match a preferred architecture.

Use [`EXECUTION_MODES.md`](EXECUTION_MODES.md) to avoid running the full
verification matrix for low-risk, narrow changes.

The contract is intentionally opinionated at boundaries where defects are
expensive: types, trust boundaries, server/client separation, async work,
component composition, accessibility, visual runtime evidence and tests.

Primary references:
[React purity](https://react.dev/learn/keeping-components-pure),
[TypeScript strict](https://www.typescriptlang.org/tsconfig/strict),
[TypeScript TSConfig reference](https://www.typescriptlang.org/tsconfig/),
[Next.js data security](https://nextjs.org/docs/15/app/guides/data-security),
[Next.js data fetching](https://nextjs.org/docs/app/getting-started/fetching-data),
[Tailwind class detection](https://tailwindcss.com/docs/detecting-classes-in-source-files),
[shadcn/ui composition](https://ui.shadcn.com/docs),
[Expo Router](https://docs.expo.dev/router/introduction/),
[Expo Router core concepts](https://docs.expo.dev/router/basics/core-concepts/), and
[Expo testing](https://docs.expo.dev/develop/unit-testing/).
For daily tooling, see [ESLint configuration](https://eslint.org/docs/latest/use/configure/configuration-files),
[Prettier options](https://prettier.io/docs/options),
[Biome getting started](https://biomejs.dev/guides/getting-started/) and
[Husky hooks](https://typicode.github.io/husky/get-started.html).

## Universal rules

### Before editing

- Read repository instructions, package scripts, lockfile, tsconfig and the
  nearest analogous implementation.
- Identify the runtime boundary: browser, server, worker, native device, build
  step and external services.
- Write functional, security and UI acceptance criteria before implementation.
- Preserve existing coherent conventions unless the change explicitly includes
  a migration.

### Type and boundary rules

- Treat external input as `unknown` until validated at the boundary.
- Prefer schemas and discriminated unions over casts and prose assumptions.
- `any`, `as`, `@ts-ignore`, `@ts-expect-error` and non-null assertions require
  a local justification and the smallest possible scope.
- Do not pass database rows, secrets, tokens or internal error objects directly
  into UI/client payloads.
- Keep authentication separate from authorization; enforce authorization on the
  server or trusted runtime for every protected operation.
- Model errors callers can act on. Preserve diagnostic causes without leaking
  secrets or internal topology.

### Async and resource rules

- Set timeouts and cancellation for network, filesystem, child-process and
  long-running operations where the runtime supports them.
- Bound concurrency, retries, queues, collection sizes and request bodies.
- Make retried external mutations idempotent; do not retry non-idempotent work
  blindly.
- Avoid N+1 I/O, duplicate fetches, render churn and unbounded memory growth.
- Do not perform synchronous filesystem/crypto/process work on a hot server
  path without evidence that it is safe.

### Tests and evidence

- Add a regression test for a bug when practical.
- Test behavior and boundary failures, not only implementation details.
- Run the narrowest relevant typecheck, lint, unit/integration, build and E2E
  checks; report skipped checks.
- For UI, render the exact route/state and inspect pixels at target viewports.
- For native apps, verify the target platform; web evidence does not prove
  iOS/Android.

## Daily developer tooling

Detect the repository's existing tools first. Do not add Prettier, ESLint,
Biome, Husky or a second test runner merely because this contract mentions
them. A project has one source of truth for formatting and one primary
semantic linter per file family.

### Package manager and scripts

- Use the package manager indicated by the existing lockfile:
  `pnpm-lock.yaml`, `yarn.lock`, `package-lock.json`, `bun.lock` or the
  repository's documented tool.
- Do not mix package managers or rewrite lockfiles unnecessarily.
- Pin Node/package-manager versions through the repository's existing
  `.nvmrc`, `.node-version`, `engines`, Corepack or toolchain convention.
- Keep canonical scripts discoverable in `package.json`:
  `format`, `format:check`, `lint`, `typecheck`, `test`, `build` and
  `check` when the project has those concerns.
- `check` should compose cheap deterministic checks; CI remains the authority
  for the full matrix and integration/runtime checks.
- Never replace a failing check with `|| true`, broad ignores or a disabled
  rule without recording why and what boundary remains.

### Formatting

- Use the repository's configured Prettier or Biome; do not run both against
  the same files.
- Keep formatting configuration in a committed config file, not personal
  editor settings or one-off CLI flags.
- Use LF line endings, a final newline and the repository's `.editorconfig`.
- Format only changed files during implementation; avoid unrelated
  repository-wide formatting churn.
- Use `format:check` in CI and `format`/`--write` locally.
- Generated code, snapshots and vendored files must be excluded or use the
  repository's explicit generated-file convention. Do not hand-format output
  that will be regenerated.
- A formatter does not replace code review: it cannot validate security,
  architecture, accessibility, runtime behavior or business correctness.

When available, AIslop may add a deterministic changed-code quality signal for
narrative comments, speculative abstractions, dead code, unsafe casts, weak
tests and related AI-assisted failure modes. It is advisory until a project
baseline is calibrated and never replaces ESLint/Biome, TypeScript, tests,
security analysis or runtime evidence.

Prettier's configured options are the source of truth for its CLI and editor
integrations. Biome can combine formatting, linting and import organization;
when Biome is adopted, use its pinned project version and `biome ci` in CI
instead of maintaining a duplicate formatter stack.

### Linting and static analysis

- Run the existing ESLint flat config or Biome configuration; do not create a
  second competing configuration.
- Keep rules grouped by purpose: correctness, TypeScript safety, React/hooks,
  accessibility, imports/dependencies, security and project conventions.
- Prefer type-aware rules for TypeScript when the repository can afford them.
- Treat new warnings as findings. Do not lower severity globally to make CI
  green.
- Suppress a rule only at the narrowest line/file scope with a reason; review
  suppressions as debt.
- Use import sorting/organization from the configured tool, not manual
  alphabetization that conflicts with it.
- Lint generated files only when the generator owns the lint contract; otherwise
  exclude them and verify the source/generator.

### Typecheck, tests and build

Run, in the repository's own command names and scope:

1. formatter check;
2. linter;
3. TypeScript/typecheck;
4. targeted unit/component/API tests;
5. integration/E2E tests for the changed boundary;
6. build or Expo native build when the changed surface requires it;
7. rendered UI/device verification for user-visible changes.

Do not claim `check` passed when only `test` ran. Do not treat a snapshot-only
test as proof of interactions, accessibility or native behavior.

### Git hooks and CI

- Use Husky/lint-staged only when the repository already uses them or a change
  explicitly establishes them.
- Pre-commit hooks should be fast and scoped to staged files: formatting check,
  lint fix/check and lightweight type/tests where practical.
- CI must rerun authoritative checks from a clean checkout; hooks are developer
  ergonomics, not a security boundary.
- Do not bypass hooks with `--no-verify` except for an explicitly documented
  emergency, and report the skipped checks.
- CI should use frozen lockfile installs and the repository's pinned Node
  version.

### Dependencies and configuration

- Add the smallest dependency that fits the existing toolchain; pin/update the
  lockfile in the same change.
- Review package provenance, lifecycle scripts, permissions, license and
  vulnerability output when adding or upgrading dependencies.
- Keep secrets in the approved runtime secret mechanism; never add them to
  `.env` committed files, fixtures, snapshots or logs.
- Separate developer-only tooling from production dependencies.
- Keep lint/format/type/test configuration close to the package it governs in
  a monorepo and make root orchestration explicit.

### Commit and diff hygiene

- Keep behavior changes, formatting-only changes and dependency migrations
  separate when possible.
- Do not hide a large formatting diff inside a feature or security fix.
- Use the repository's Conventional Commit convention when one exists.
- Include the exact checks run in the review/commit handoff.

## TypeScript

- Enable `strict`; enable `noUncheckedIndexedAccess` and
  `exactOptionalPropertyTypes` for new code or when the repository can absorb
  them without an unrelated migration.
- Prefer `unknown` plus narrowing at external boundaries; never use `any` to
  silence an error.
- Use `noImplicitReturns`, `noImplicitOverride`, `noUnusedLocals` and
  `noUnusedParameters` when compatible with the existing project.
- Prefer `type` for unions and aliases, `interface` for extendable public
  object contracts, and discriminated unions for state machines.
- Keep public function inputs and outputs explicit. Infer local values.
- Use exhaustive `switch` handling for discriminated unions.
- Avoid enums when string literal unions or existing repository conventions are
  clearer; do not invent a new convention mid-file.
- Keep type-only imports type-only when the toolchain supports it.
- Parse JSON, environment variables and API responses into validated types;
  `JSON.parse()` returns `unknown` at the boundary, not a trusted domain object.

TypeScript's `strict` mode is the baseline; the compiler documents it as the
wide type-checking mode for stronger correctness guarantees. Use stricter
options deliberately rather than sprinkling assertions.

## React

- Components and hooks are pure during render. Side effects belong in event
  handlers or effects that synchronize with an external system.
- Keep state minimal; derive values from props/state rather than storing
  duplicated derived state.
- Keep effects narrow and explain their external synchronization responsibility.
  Do not use `useEffect` as a general data-fetching or event pipeline when the
  framework/server boundary provides a better path.
- Use stable keys from domain identity, never array indexes for reorderable or
  stateful lists.
- Keep client components small and leaf-oriented; do not move a whole tree to
  the client to use one hook.
- Expose semantic HTML/native controls, labels, focus behavior, keyboard/touch
  behavior and loading/error/empty/disabled states.
- Avoid prop drilling by default only when a real shared boundary exists; do
  not introduce context or a state library for one consumer.
- Memoization (`memo`, `useMemo`, `useCallback`) needs a measured or
  structurally obvious render-cost reason.

React's purity rule is a correctness constraint: render must be predictable for
the same inputs and must not mutate external state.

## Next.js App Router

- Prefer Server Components by default; add `'use client'` only at the smallest
  interactive boundary.
- Keep secrets, database clients and privileged logic in server-only modules.
  Mark sensitive data-access modules with `import 'server-only'` where useful.
- Use a data-access layer for new production code when the repository does not
  already have an equivalent; authenticate and authorize inside that boundary.
- Treat Server Actions as public HTTP endpoints: validate input, authenticate,
  authorize and rate-limit as applicable even when the action is only imported
  by one component.
- Fetch data close to its source in Server Components; avoid making the server
  call its own Route Handler merely to reach internal data.
- Make caching/revalidation explicit for request-sensitive data. Do not assume
  a cached response is safe for user-specific or permission-sensitive data.
- Use `loading.tsx`, `error.tsx`, `not-found.tsx` and `Suspense` for meaningful
  route states, not a single global spinner.
- Start independent async work together; avoid sequential waterfalls without a
  dependency.
- Pass a minimal sanitized DTO to Client Components, never an entire database
  row or session object.
- Use `next/navigation` in App Router code; never mix `next/router` into an
  App Router route.
- Never pass unsanitized user-controlled URLs to `router.push` or
  `router.replace`.
- Keep route handlers thin: validate, authorize, call domain/data code, map
  errors and return the contract.

These rules follow the Next.js data-security guidance: Server Components can
keep secrets server-side, but data must still be authenticated, authorized and
sanitized before crossing to the client.

## Node.js

- Use the repository's module system and package manager; do not mix ESM/CJS
  conventions casually.
- Use `node:` imports for built-ins and keep process/environment access at a
  small configuration boundary.
- Validate environment variables at startup and fail with actionable messages;
  never log secrets.
- Prefer async APIs, streams and backpressure for server I/O. Bound body size,
  upload size and parsed input.
- Pass `AbortSignal`/timeouts to outbound requests and clean up timers,
  listeners, workers and child processes.
- Handle promise rejection and process shutdown deliberately. Do not swallow
  errors or use blanket catch-and-log.
- Keep CPU-heavy work off the event loop; use worker threads/queues only when
  the measured workload justifies it.
- Do not trust filesystem paths, archive entries, URLs, serialized objects or
  subprocess arguments from users.
- Test handlers with malformed input, upstream timeout/error, cancellation and
  partial failure.

## Tailwind CSS

- Use the project's theme tokens for color, spacing, typography and radii.
  Arbitrary values require a reason and should become a token when repeated.
- Use complete statically detectable class names. Map variants to complete
  strings; do not build `bg-${color}-500` dynamically.
- Do not place conflicting utilities on the same element. Use a variant map or
  `cn`/class merge helper at the component boundary.
- Keep responsive, hover, focus-visible, disabled and reduced-motion states
  explicit for interactive components.
- Prefer layout primitives (`flex`, `grid`, `gap`, container constraints) over
  coordinate nudges and negative-margin patching.
- Keep class strings readable; extract a component or variant map when a
  repeated class contract has semantic meaning.
- Verify the generated CSS source paths include monorepo/shared component
  locations.

Tailwind scans source as text; dynamic class construction can silently produce
missing styles. Complete class names are a correctness requirement, not merely
a style preference.

## shadcn/ui

- Treat shadcn/ui as open component source, not an opaque dependency. Inspect
  and adapt the copied component to the repository's design tokens.
- Preserve the primitive's accessible semantics, keyboard behavior, focus
  management and ARIA contract when customizing it.
- Follow the documented composition tree. Do not flatten required wrappers or
  nest interactive controls invalidly.
- Prefer composition and explicit variants over forks with one-off overrides.
- Keep `cn`/class merging at the component boundary and avoid conflicting
  utility classes from consumers.
- Do not add a second component library for a component shadcn already covers
  without a documented capability gap.
- Add interaction tests for dialogs, menus, comboboxes, forms and destructive
  confirmation; add screenshot checks for meaningful visual changes.
- Update the local component source when behavior changes; do not patch a
  generated copy elsewhere and leave the source of truth ambiguous.

## Expo / React Native

- Prefer the repository's established navigation; for new Expo projects use
  Expo Router when it fits. Keep `src/app` (or `app`) for routes and layouts
  only; put components, hooks and utilities outside the route tree.
- Enable typed routes when using Expo Router and preserve deep-link behavior.
  Treat route params as untrusted input and validate them.
- Use `npx expo install`/the repository's Expo package manager path so SDK
  versions remain compatible. Do not hand-upgrade native packages casually.
- Keep platform-specific behavior explicit with `.ios`, `.android`, `.native`
  and `.web` boundaries instead of runtime branching spread across components.
- Handle safe areas, keyboard avoidance, touch targets, accessibility labels,
  focus/press states, reduced motion and loading/error/offline states.
- Keep secrets out of the client bundle and secure storage boundaries; do not
  treat obfuscation or app config as secret storage.
- Test with the repository's `jest-expo`/React Native setup for logic and
  component behavior, and use E2E/device evidence for navigation and native
  behavior. Snapshot tests alone do not prove a screen works.
- Verify the actual iOS/Android runtime when the reported defect is native;
  Expo Web evidence is not a substitute.

Expo Router's file-based routes are also deep links. Moving a route is an API
change for links, analytics and tests; review it as such.

## Reviewer output

The independent reviewer reports:

- stack detected and standards applied;
- P0-P3 findings with exact evidence;
- security boundary and exploit/failure scenario;
- type/test/build/runtime/UI evidence;
- accessibility and responsive findings for user-visible changes;
- smallest remediation and re-check command;
- explicit unverified areas.

No P0/P1 finding may remain open. A standard is not marked passed when its
corresponding evidence was not run.
