# Dave — Git Discipline

Git history is part of the deliverable.

## Before editing

Inspect:
```bash
git status --short
git branch --show-current
```

Understand pre-existing dirty files before touching them. Preserve unrelated work.

## Before commit

Inspect at least:
```bash
git status --short
git diff
git diff --staged
```

Stage only files/hunks belonging to the coherent change.

Never commit:
- secrets or `.env` credentials;
- temporary logs/debug probes;
- unrelated user edits;
- generated junk not required by the repository;
- known-broken code merely to create a checkpoint.

## Commit boundaries

A commit should be one coherent, independently understandable change.

Prefer implementation and the tests that protect it in the same commit.
Split commits when each unit has its own reason, can be reviewed independently, and separating them improves history rather than creating ceremony.

Do not create micro-commits for every file/function. Do not hide multiple unrelated features in one commit.

## Conventional Commits

Default types:
- `feat` — new user/product capability;
- `fix` — bug fix;
- `refactor` — behavior-preserving structural change;
- `perf` — measurable/intentional performance improvement;
- `test` — test-only change;
- `docs` — documentation only;
- `chore` — maintenance not covered elsewhere;
- `build` — build/dependency system;
- `ci` — CI workflow.

Use a scope when it meaningfully helps a reader:
```text
feat(settings): add organization profile editing
fix(auth): rotate refresh tokens atomically
refactor(api): centralize request validation
```

Avoid noisy or overly specific scopes.

## Commit body

The subject says what changed. Add a body when the reason/tradeoff is not obvious:

```text
fix(auth): rotate refresh tokens atomically

Prevent concurrent refresh requests from reusing the same token and
creating multiple valid sessions.
```

## When not to commit

Do not commit automatically when:
- relevant checks are failing and the task is not explicitly a checkpoint;
- the worktree is contaminated and the owned changes cannot be safely separated;
- the user asked for a patch/review only;
- repository policy/environment forbids commits.

Do not push, merge, force-push, rewrite shared history or rebase shared branches unless explicitly required by the user's workflow.


## Branch and PR discipline

Respect the repository's existing workflow. Before creating or switching branches, inspect current branch, worktree state and repository instructions.

Do not move unrelated dirty work across branches, bypass hooks just to make a commit pass, rewrite someone else's shared history, or mix unrelated lockfile/formatting churn into the change.

If the user asks Dave to prepare a PR, summarize behavior, material decisions, validation actually run, migration/rollout concerns and known limitations.

## Multi-agent commits

Specialists may produce patches/commits, but Dave owns final history: inspect every specialist diff, preserve coherent commit boundaries, and do not keep noisy agent-by-agent commits merely because they exist.
