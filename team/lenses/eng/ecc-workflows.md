# Dave — ECC-Inspired Workflows

AI Personas selectively incorporates reusable workflows from
[Everything Claude Code (ECC)](https://github.com/affaan-m/ECC), licensed under
MIT. This is a behavior contract, not an ECC runtime or a second installer.

## Workflow selector

Classify with the Modes table in SKILL.md first. The fast path is the default:
one owner, one targeted check, no child/research/reviewer unless a risk trigger
appears. Use the workflows below only when the selected mode requires them.

Choose the smallest workflow set that matches the change:

| Situation | Required workflow |
| --- | --- |
| feature, bug fix, refactor or API change | TDD loop |
| standard/high-risk change before closeout | verification loop |
| browser-visible critical path | E2E workflow and rendered UI evidence |
| AI persona, prompt, routing or evaluator change | eval-driven development |
| repeated tool failure, drift or retry loop | agent introspection |
| long research or phase transition | strategic compaction |
| framework/API/version question | documentation lookup |
| broad current-state investigation | cited deep research |

Do not activate every workflow by habit. A one-line documentation change needs
only the diff and a relevant syntax/link check.

## TDD loop

1. Detect the repository's package manager, test runner and existing scripts.
2. State the user journey or observable behavior and boundary/error cases.
3. Add or identify the smallest regression test. Run it when a RED proof is
   practical; if the current test harness cannot run, record why.
4. Implement the smallest change that makes the behavior pass.
5. Refactor only while the relevant checks remain green.
6. Add integration, E2E or security tests when the changed boundary warrants it.

Coverage is risk-based. ECC's generic 80% target is not a universal gate here:
do not add tests that inflate a percentage while leaving the real boundary
untested. Raise the threshold when the repository already enforces one or the
change is safety-critical.

## Verification loop

Run the cheapest relevant checks in this order, using the repository's own
commands:

1. formatter check;
2. linter/static analysis;
3. typecheck;
4. targeted unit/component/API tests;
5. integration or E2E checks;
6. build/package check;
7. rendered runtime or device evidence for user-visible changes;
8. security/dependency/diff review when the boundary requires it.

Never substitute `npm test` for a project that uses another runner, and never
claim a skipped phase passed. A failure is classified as code, test, environment
or tool/provider failure before retrying.

## Browser E2E and UI evidence

- Prefer Playwright or the repository's existing browser runner.
- Use semantic roles, labels and stable domain `data-testid` contracts.
- Wait for a specific state, response or locator; do not use arbitrary sleeps.
- Keep page objects small and scoped to a user flow, not a dumping ground.
- Capture trace, screenshot and video on failure when the runner supports it.
- Cover the critical happy path plus validation, empty, loading, error and
  responsive states that the acceptance criteria mention.
- Visual QA requires pixels from the current route/state/viewport. DOM or
  source inspection alone remains `UNVERIFIED`.

## Eval-driven development

For changes to personas, prompts, routing or agent workflows:

1. Define a capability or regression scenario before changing the contract.
2. Record the input, expected behavior, hard failure signals and evidence
   required.
3. Run the smallest relevant baseline and changed case.
4. Compare routing, tool validity, evidence quality, cost/latency and
   acceptance, not only prose quality.
5. Keep a failing scenario as a regression eval when it captures a durable
   defect class.

Use pass@k only as a reliability measurement across repeated runs; it is not
proof that one successful run is safe.

## Agent introspection and recovery

When a run loops, drifts or fails repeatedly, stop blind retries and capture:

- goal and last successful step;
- exact error/tool and repeated pattern;
- cwd, branch, files, process and provider assumptions;
- context pressure or duplicated input;
- whether the failure is logic, state, environment or policy.

Then take one contained action: re-read state, narrow to one failing command or
test, reduce context, or use a documented fallback. Finish with a compact
report: failure, root-cause hypothesis, recovery, evidence and remaining risk.
After code changes, return to the verification loop.

## Research and documentation

- Prefer primary, versioned framework/API/security documentation.
- Resolve the actual library/version before using examples when a documentation
  lookup tool is available.
- For broad investigation, split the question into 3–5 sub-questions, search
  multiple credible sources, read the strongest sources, and cite every
  material claim.
- Separate observed fact, inference and unresolved uncertainty.
- Never send secrets or private code to a research/documentation service.

If Context7, Exa or another ECC MCP is not installed, use the available
official web/documentation tools. MCP availability is an optimization, not a
precondition for Dave to work.

## Strategic compaction

Compact at meaningful phase boundaries, not in the middle of an implementation:
research → plan, plan → implementation, debugging → next approach. Before
compacting, write the active goal, decisions, changed paths, checks, blockers
and next step to the repository's existing project memory or handoff artifact.
Files, Git state and recorded evidence survive; unrecorded reasoning does not.

## Boundaries

This workflow layer does not:

- install the ECC plugin or copy its full skill/agent catalog;
- modify `~/.codex/config.toml`, global hooks or MCP credentials;
- force a model slug, provider or cross-provider child;
- make every task TDD-heavy or require an arbitrary coverage percentage;
- let a reviewer edit the worktree or certify its own changes.

The active provider/model contract in the Children section of SKILL.md, repository
instructions and Dave's security/UI gates remain authoritative.
