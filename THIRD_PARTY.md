# Third-party intelligence

AI Personas does not vendor these projects. They remain optional independently installed skills/resources. Persona instructions may absorb durable principles while keeping upstream tools independently updateable.

## Agency Agents
https://github.com/msitarzewski/agency-agents

Used as inspiration for professional competency decomposition, especially:
- UI Designer
- UX Architect
- UX Researcher
- Brand Guardian
- UI Finish-Gate Reviewer

Ashley absorbs the role boundaries and useful workflows but does not inherit every opinionated default.

## UI/UX Pro Max
https://github.com/nextlevelbuilder/ui-ux-pro-max-skill

Role inside Ashley:
**searchable design intelligence** — styles, product patterns, palettes, typography, UX guidelines, charts, stacks.

Install through its own CLI so its datasets/scripts remain intact and updateable.

## Taste
https://github.com/tasteskill/tasteskill

Role inside Ashley:
**creative pressure / anti-generic frontend taste**.

The safe general skill is preferred. The stricter GPT/Codex variant is useful only when deliberate visual divergence is appropriate.

Its highly opinionated rules are never universal Ashley rules.

## Impeccable
https://github.com/pbakaus/impeccable

Role inside Ashley:
**design red-team, critique, audit and finish gate**, especially after implementation.

Impeccable remains an independently updateable skill.

## Standards and foundational sources

Ashley uses established design principles as constraints/reasoning tools, not as a catalog to mechanically apply:
- WCAG / WAI accessibility guidance
- Nielsen Norman Group usability heuristics
- Apple Human Interface Guidelines
- mature design-system practices and platform conventions

When a current standard/version materially matters, research the latest source rather than relying on a frozen note in this repository.


## pen.dev / Pencil
https://pen.dev
https://docs.pencil.dev/

Role inside Ashley:
**preferred editable design canvas and repo-local design artifact format**.

Ashley prefers project-owned `.pen` files when the workflow benefits from versioned design artifacts. The desktop/IDE MCP is used for live canvas work; the CLI provides headless editing, screenshots/exports and resilience when a GUI host is unavailable.

Ashley does not edit `.pen` JSON manually; it uses pen.dev tooling.


## Dave engineering intelligence

### AIslop
https://github.com/scanaislop/aislop

MIT-licensed deterministic code-quality and AI-slop scanner. AI Personas uses
its changed-file/CI mode as an optional signal for comments, speculative
abstraction, dead code, swallowed errors, unsafe casts, weak tests and related
patterns. It never replaces repository-native linting, tests, security review
or runtime evidence.

### NVIDIA SkillSpector
https://github.com/NVIDIA/skillspector

Apache-2.0 security scanner for third-party agent skills, MCPs and bundles.
AI Personas does not install the scanner and never treats a static clean result
as proof of safety; scan third-party skills yourself before installing them.

### Reticle
https://github.com/reticlehq/reticle

Project-local runtime verification for supported web/desktop apps. SDK packages
are Apache-2.0; server/test packages have their own source-available license,
so users must review the package license before commercial use. AI Personas
documents Reticle as a complement to Playwright and pixel inspection, not a
global automatic install.

### ibelick UI Skills
https://github.com/ibelick/ui-skills

MIT-licensed narrow design-engineering skills. Ashley selectively uses its
routing, accessibility, motion-performance, metadata, design-evidence and
baseline ideas without importing the entire registry or overriding project
design authority.

### Slop Cop
https://github.com/howshannon/slop-cop

MIT-licensed cross-artifact quality rubric for prose, UI/design and code. AI
Personas absorbs its evidence-first, voice-preserving and no-authorship-claim
principles into the Quality section of `team/SKILL.md`; it does not add another always-on reviewer
or humorous scorecard.

### Everything Claude Code (ECC)
https://github.com/affaan-m/ECC

AI Personas selectively adapts workflow ideas from ECC for Codex: TDD,
verification loops, stable E2E, eval-driven agent development, research/source
hygiene, failure introspection and context compaction. It does not vendor or
install ECC's full catalog, hooks, MCP configuration or model recommendations.
The adapted material lives in `team/lenses/eng/ecc-workflows.md` and
`team/lenses/delivery/ecc-workflows.md`. ECC is MIT licensed.

### Agency Agents
https://github.com/msitarzewski/agency-agents

Role decompositions (Frontend Developer, Backend Architect, Reality Checker,
Evidence Collector, API Tester, SRE, Financial Analyst, Growth Hacker and
others) inspired the persona hats and lenses. Diego's video lenses adapt the
Short-Video Editing Coach, Video Optimization Specialist, Visual Storyteller
and Ad Creative Strategist agents. AI Personas does not install the
roster: every installed custom agent adds its description to every session's
context, while a lens loaded on demand delivers the same perspective for free.
If you install Agency Agents yourself (upstream places them under
`~/.codex/agents/`), the hats may delegate bounded tasks to them; they remain
workers and reviewers, never authorities. Reviewed pin:
`053ddbbf392a1688fc7043d81529f47ef2cf86c8`.

### Ponytail
https://github.com/StarQuant/ponytail-skill

Role inside Dave:
**anti-overengineering discipline** — YAGNI, reuse existing code, prefer standard/native capabilities, avoid unnecessary dependencies and delete needless code after implementation.

Dave internalizes the principle rather than depending on Ponytail being installed. An installed Ponytail skill may be used as an additional simplification review.

### Caveman
https://github.com/JuliusBrussee/caveman

Role inside Dave:
**optional token-efficiency layer** — the skill compresses Dave's prose; the proxy can additionally shrink noisy tool/context traffic.

Dave does not depend on Caveman. Native context budgeting, targeted reads, read deduplication, compact task capsules and bounded tool output remain mandatory. If Caveman is installed, Dave uses it as an additive optimization without compressing exact code/contracts/errors or changing provider/RouteMux wiring.


## Pins

Optional external tools were reviewed at these versions. Upgrade deliberately:
review the upstream change, scan when appropriate, run `scripts/validate.sh`
and the evals, then update the recorded pin.

- Agency Agents: `053ddbbf392a1688fc7043d81529f47ef2cf86c8`;
- Taste: `37c8c376b92ebc02456f7c70776b514fddda88e1`;
- UI/UX Pro Max CLI: `2.15.0`;
- Impeccable: `4.1.0`;
- Graphify: `graphifyy==0.9.68`.

## Graphify

https://github.com/Graphify-Labs/graphify

Optional local code-graph accelerator for repository dependency/impact
navigation. AI Personas does not require it for session reuse: the native
project-context cache remains the default.

Install it yourself (`uv tool install graphifyy==0.9.68` or `pipx install
graphifyy==0.9.68`). `project-context.py graph-dir` gives the output location
inside the repository's Git metadata, so the graph never dirties the working
tree and needs no server or deployment.

The graph is navigation evidence. Current source, tests, schemas and
configuration remain authoritative.
