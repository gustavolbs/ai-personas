# Changelog

All notable changes to AI Personas are documented here.

## [5.0.0] — 2026-09-26

### Breaking: one skill, hats instead of processes
- the seven persona skills collapse into one installable `team/` skill; Laila is the single entry point;
- personas are hat files in `team/personas/` read in the same thread on demand; children exist only for disjoint parallel work, an independent read-only review, or one reusable read-only Sol decision;
- the five shared contracts and the per-persona boilerplate become a 12-rule SKILL.md; nothing is mandatory reading at boot except the context snapshot;
- `references/` reorganize into `team/lenses/<domain>/`; the seven copies of evidence, memory and orchestration references merge into `lenses/shared/` and SKILL.md;
- specialist installers, per-persona installers, `sync-shared-contracts.sh`, `PERSONAS.json` and the string-grep static evals are removed.

### Added
- **Diego**, video scripting, editing and motion design hat, with `lenses/video/` (scripting, production, editing, motion design, packaging and distribution); inspired by the Agency Agents Short-Video Editing Coach, Video Optimization Specialist, Visual Storyteller and Ad Creative Strategist.

### Fixed
- the project-context cache lives in `--git-common-dir`, so every worktree shares one snapshot instead of rediscovering the repository;
- freshness no longer depends on the branch name; HEAD, tree fingerprint and summary hash decide;
- the snapshot cap drops from 12 KiB to 4 KiB;
- installed references no longer point at repository-root `docs/` files.

### Evals
- six cases with mechanical assertions over `codex exec --json` traces (`scripts/eval-assert.py`), with a model-free selftest in CI; the 47 narrative scenarios are retired.

## [4.0.0] — 2026-09-26

### Breaking orchestration change
- persistent persona sessions now default to Luna: **Luna runs, Sol decides**;
- Sol is an ephemeral read-only decision advisor rather than the resident
  orchestration/control loop;
- STANDARD work no longer automatically earns a Sol planning pass;
- Laila must never be the persistent Sol orchestrator.

### Breaking authority change
- Laila, Roberto, Clara and Ana are explicitly non-coding personas;
- Ashley cannot write production application code;
- Dave is the sole application-programming authority;
- Guto owns infrastructure/IaC/CI/CD/production mutations and cannot change
  application behavior owned by Dave;
- write-capable tools do not expand persona authority.

### Added
- shared Mutation Authority Contract packaged into every persona;
- Sol quota budgets and regression eval;
- cross-persona mutation-boundary eval.

## [3.7.0] — 2026-09-26

### Added
- deployment-free local Project Context Cache shared by all personas;
- branch/HEAD/working-tree fingerprinting so new chats can prove whether prior
  project understanding is still current without rereading the repository;
- FRESH / STALE / NEEDS_CONTEXT boot states and incremental delta reconciliation;
- deterministic cache regression tests;
- optional pinned Graphify 0.9.68 installer for local multi-hop code
  dependency/impact navigation.

### Changed
- every repository-aware persona checks the local context cache before broad
  discovery;
- Laila no longer rediscovers an unchanged repository at the beginning of each
  chat;
- project initialization can explicitly bootstrap local context with --context;
- Graphify output, when used, lives in Git metadata and requires no server,
  vector database, MCP deployment or remote service.

## [3.6.0] — 2026-09-26

### Changed
- every installed persona now carries packaged shared routing, execution-mode and
  anti-slop contracts instead of depending on repository-root docs;
- SKILL files use stronger progressive disclosure and narrower discovery descriptions;
- Sol/Luna routing defines parent-is-Sol, parent-is-Luna and reusable-planner transitions;
- specialist installers use one canonical roster and a pinned Agency Agents commit;
- installed verification compares the full persona package;
- root architecture/usage docs describe the complete seven-persona suite;
- root project initialization is explicit by domain.

### Added
- shared-contract synchronization/check script;
- static behavior-contract eval and opt-in live Codex JSON-trace eval runner;
- eval-trace summary and SKILL context-size audit;
- CI checks for packaged contract drift, JSON validity and routing invariants.

### Removed
- tracked macOS .DS_Store artifacts.

## [3.5.0] — 2026-09-26

### Changed
- model routing now treats GPT-6 Sol as the control plane for investigation,
  orchestration, architecture and consequential decisions;
- GPT-6 Luna is the default execution plane for bounded implementation,
  production work, calculations, variants, routine diagnostics and review
  fixes;
- all seven personas now apply the same Sol/Luna boundary with domain-specific
  decision and execution lanes;
- FAST low-risk work may bypass Sol and execute directly on Luna;
- Sol-to-Luna handoffs use compact execution packets so Sol does not continuously
  consume implementation logs/context.

### Added
- explicit Luna-to-Sol re-escalation criteria for new decisions, contradictory
  evidence, repeated acceptance failure and high-consequence gates;
- cross-persona and provider-local regression coverage for the new routing
  contract.

## [3.4.0] — 2026-09-26

### Added
- explicit `FAST`, `STANDARD` and `HIGH_RISK` execution modes;
- fast-path budgets and escalation rules to prevent unnecessary delegation,
  research, full-matrix checks and reviewer waits;
- regression eval for low-risk task latency and over-orchestration.

### Changed
- external review is now conditional on shared/public behavior or risk, not
  mandatory for every small change;
- visual QA is targeted to visual/layout/interaction changes;
- all personas classify execution speed before building a child graph.

## [3.3.1] — 2026-09-25

### Fixed
- Dave 1.1.1 documents the version-scoped NativeWind style-callback regression,
  the className boundary for native-only bypasses, and the Jest interop blind spot.
- Adds a mobile regression eval requiring rendered-style assertions and native
  visual evidence instead of cache assumptions or helper-only tests.

## [3.3.0] — 2026-09-25

### Added
- universal anti-slop quality contract for code, UI, prose, strategy, finance,
  operations and delivery;
- AIslop deterministic code-quality integration for TypeScript, JavaScript,
  Expo/React Native and other supported stacks;
- optional SkillSpector supply-chain scanning before external skill/MCP installs;
- optional Reticle runtime-verification guidance for web/desktop projects;
- selective ibelick UI Skills routing for Ashley;
- project helpers for explicit external-skill and changed-code scans.

### Deliberately not included
- silent global tool/MCP installation;
- a blocking anti-slop score without a project baseline;
- replacing native formatter, linter, tests, security review or visual QA.

## [3.2.0] — 2026-09-24

### Added
- selective ECC-inspired workflows for Dave and Laila: proportional TDD,
  verification, browser E2E, AI workflow evals, research/source discipline,
  agent-failure recovery and strategic context compaction;
- an explicit ECC integration note and regression eval.

### Deliberately not included
- the full ECC plugin/catalog, global hooks, MCP configuration, credentials,
  fixed model recommendations or a universal 80% coverage gate.

## [3.1.4] — 2026-09-23

### Fixed
- the canonical global persona location is `~/.agents/skills/<persona>`;
- the installer removes only stale persona shadows from `~/.codex/skills`;
- verification now fails when a deprecated shadow exists instead of accepting both
  copies as one installation.

## [3.1.3] — 2026-09-23

### Hardened
- the installer now mirrors every persona to the canonical Codex path `~/.codex/skills/<persona>` after the skills CLI runs;
- post-install verification checks every existing Codex/Agents skill copy and fails on stale shadow copies instead of silently succeeding.

## [3.1.2] — 2026-09-23

### Hardened
- moved delegated-child lifecycle enforcement into every persona's always-loaded `SKILL.md`, not only on-demand references;
- installation now runs repository validation before copying skills;
- installation now verifies the exact installed `SKILL.md` copies and lifecycle marker after install, failing loudly on stale/mismatched copies;
- structural CI now rejects any persona kernel that loses the lifecycle contract.

## [3.1.1] — 2026-09-23

### Fixed
- made subagent lifecycle explicit across every persona that delegates work;
- a successful `spawn_agent` or “message sent” acknowledgement no longer counts as completed delegation;
- coordinators retain child ids, wait for required children, collect terminal results and distinguish completed/failed/cancelled work before synthesis;
- an empty active-agent list is no longer treated as success without a returned result;
- duplicate retries are forbidden while the original child's state is unknown; 429 recovery collapses concurrency and retries at most once when justified;
- fallbacks must be reported explicitly instead of implying that a persona/specialist participated.

### Added
- regression eval for child lifecycle, 429 recovery and cross-persona synthesis.

## [3.1.0] — 2026-09-23

### Added
- evidence-first anti-hallucination protocol across all seven personas;
- explicit evidence states: PROPOSED, CHANGED, BUILT, RUN, VERIFIED and UNVERIFIED;
- Expo/React Native runtime-verification rules preventing source diffs from being reported as visual fixes;
- regression eval for the "CSS changed but Expo app did not" failure mode;
- Clara existing financial-flow audit mode with financial invariants and VERIFIED vs UNVERIFIED transitions;
- suite + per-persona semantic versioning via `VERSION`, `PERSONAS.json` and `skills/<persona>/VERSION`;
- Dave system-architecture mode with Software Architect routing, C4/ADR/protocol/data/failure semantics;
- expanded domain coverage and team-routing evals.

### Changed
- Ashley and Dave use smaller progressive-disclosure kernels with domain depth in references;
- Laila is the primary cross-functional control plane and cannot accept worker claims as proof;
- CI validates skill/reference integrity, persona versions and evidence-protocol participation.

### Release note
This version is currently on the feature branch/PR. Create tag `v3.1.0` only after the relevant PRs are merged.

## [3.0.0] — 2026-09-23

### Added
- seven-persona operating team: Laila, Roberto, Clara, Ana, Ashley, Dave and Guto;
- persona-first orchestration and domain-specific durable memory;
- cross-functional product, finance, marketing, engineering, design and platform workflows.
