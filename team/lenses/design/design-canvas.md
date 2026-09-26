# Design Canvas Routing

Ashley is canvas-agnostic. The user should not lose design capability because one MCP host is flaky.

## Capability check

Before consequential visual production, identify which capabilities are actually available:

- writable editable canvas;
- file-backed/versionable design source;
- screenshot/render capability;
- export capability;
- component/token inspection;
- browser/implementation preview;
- image generation/editing;
- shell/CLI access.

Choose the most reliable path that satisfies the task.

## Preferred routing

### 1. pen.dev / Pencil
Prefer when:
- the `pencil` MCP is available;
- a project-owned `.pen` file exists or is appropriate;
- the user wants versionable design artifacts;
- headless export/resilience is valuable.

Use `pen-dev.md`.

### 2. Penpot
Use when:
- the project already lives in Penpot;
- the MCP connection is stable;
- collaboration in Penpot is important.

Use `penpot.md`.

### 3. Other writable canvas
A different canvas is acceptable if the current harness exposes real read/write tools plus visual inspection/export.

Do not assume a connector is writable just because it can read design metadata.

### 4. Code/browser visual sandbox
Use when no editable canvas is available and the task is product UI/web exploration.

Create an isolated, clearly non-production sandbox or temporary route/component, render it in the browser, inspect screenshots and preserve the user's dirty worktree.

Do not present this as the canonical vector design source.

## Failover

If the active canvas disconnects mid-task:
1. preserve completed work;
2. do not repeatedly retry a flaky connection without progress;
3. switch to another available writable path;
4. if a project-owned `.pen` file exists and `pen` CLI is authenticated, use the headless path;
5. otherwise continue reasoning/docs and mark visual production/QA as blocked.

## Source of truth

Record the selected visual source in `docs/design/HANDOFF.md`.

Examples:
- `design/product.pen` — visual source of truth;
- Penpot file/page — visual source of truth;
- code implementation — current production truth, with design canvas exploratory.

Do not maintain two supposedly authoritative visual systems silently.
