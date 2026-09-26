# Memory

The tracker and the repository are live truth. Persona memory is a pointer layer, never a second source of truth.

## Where
- `docs/engineering/` (Dave): CONTEXT, CONVENTIONS, DECISIONS, TESTING, HANDOFF, LEARNINGS
- `docs/design/` (Ashley): PRODUCT, UX, BRAND, DESIGN_SYSTEM, MESSAGING, RESEARCH, ASSETS, DECISIONS, HANDOFF, LEARNINGS
- `docs/delivery/` (Laila): CHARTER, SCOPE, PLAN, RISKS, DECISIONS, HANDOFFS, LEARNINGS
- business, finance and marketing artifacts: where the project already keeps them, otherwise `docs/<domain>/`
- `~/.ashley/PREFERENCES.md`, `~/.ashley/HEURISTICS.md`: cross-project design preferences only, created lazily when needed
- `<git-common-dir>/ai-personas/PROJECT_CONTEXT.md`: navigation snapshot shared by all worktrees, ≤4 KiB, managed by `scripts/project-context.py`

Create the project docs with `scripts/init-project.sh --engineering|--design|--delivery|--all`. An existing ADR system or AGENTS.md wins over new files: extend it instead.

## What
Store: approved decisions with rationale, rejected options and why, proven constraints, durable invariants, usability/finance/ops lessons with scope and exceptions.
Do not store: secrets, source dumps, logs, transient status a tracker owns, one-off wording, unresolved exploration, Sol-only reasoning, anything user-private.

## How
One approval is not a universal rule: encode scope, confidence, evidence and exceptions ("rejected editorial serif for this operational accounting surface", not "never serif"). New explicit feedback supersedes old preferences; when they conflict, record the context instead of deleting history. An approved project decision beats a global preference inside that project.

Never edit the installed skill as "learning". Propose changes in the ai-personas repository and run its evals.
