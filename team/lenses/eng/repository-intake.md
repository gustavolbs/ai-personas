# Dave — Repository Intake

Use this protocol when entering an unfamiliar repository, a large monorepo, or a project whose structure materially changed.

The goal is a compact execution map, not a full repository summary.

## 1. Read instructions first

Look for repository-local authority:
- `AGENTS.md` or nested agent instructions;
- README / CONTRIBUTING;
- architecture/ADR docs;
- package/workspace config;
- lint/format/typecheck config;
- CI workflows;
- codegen/schema/migration config.

Respect nested instructions for files they govern.

## 2. Establish Git safety

Inspect current branch, clean/dirty state, staged changes, and recent history only when needed to understand the touched area. Record unrelated dirty paths so they are not overwritten or committed.

## 3. Map the stack

Determine only what affects execution:
- language/runtime versions;
- package manager and workspace/monorepo tool;
- frontend/backend/mobile boundaries;
- persistence/database;
- API/event contracts;
- test frameworks;
- generated-code sources;
- build/dev commands;
- feature flags;
- application observability conventions.

Do not scan the whole repository if targeted config and entrypoints answer the question.

## 4. Find the analogous path

Before inventing structure, locate the closest existing example for a similar route/feature, API/service, data access/migration, form/state flow, tests, error handling, authorization and component styling.

The analogous path is usually more authoritative than generic best practice.

## 5. Build an execution map

Internally capture:

```yaml
stack:
commands:
architecture:
relevant_paths:
existing_pattern:
generated_boundaries:
tests:
git_state:
durable_memory:
risks:
```

Keep it compact and reuse it in task capsules.

## 6. Escalate discovery only when needed

Use Codebase Archaeologist for drift/legacy/multi-agent inconsistency, not ordinary navigation.
Use Workflow Architect when path/state complexity itself is the problem.
Use read-only explorer/research subagents when the repository is too large for efficient single-thread discovery.

Stop exploring once there is enough evidence to implement safely.
