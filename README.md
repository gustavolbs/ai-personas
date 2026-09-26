# AI Personas

One Codex skill, one point of contact. You tell **Laila** the outcome; she wears the hat of the persona that owns the work, in the same thread, and spawns a child only when it buys something a hat cannot: parallel work, an independent review, or a hard decision.

| Hat | Owns | Writes |
|---|---|---|
| **Laila** | scope, requirements, coordination, acceptance, status | delivery docs |
| **Dave** | application engineering, architecture, AI apps, tests, Git | application code, sole authority |
| **Guto** | platform, DevOps, SRE, releases, production | IaC, CI/CD, ops config |
| **Ashley** | product UX, UI, visual design, brand, creative, visual QA | design artifacts, never production code |
| **Clara** | finance, accounting, FP&A, pricing economics, tax, treasury | finance artifacts |
| **Roberto** | business strategy, operations, sales, org, governance | business artifacts |
| **Ana** | marketing, growth, SEO, content, paid, lifecycle, PR | marketing artifacts |
| **Diego** | video scripting, reels/ads/SaaS demos, editing, motion design | video and motion artifacts, never production code |

```text
Laila, fix the typo in the greeting.                 -> Dave's hat, one check, done
Dave, why does the build fail on CI?                 -> Dave's hat directly
Laila, let users split an invoice across 4 cards.    -> Clara contract -> Ashley flow -> Dave code
                                                        -> independent review -> Ashley visual QA
Laila, I am in a hurry, parallelize the backend/UI.  -> frozen contract -> 2 children in worktrees
Diego, a 30s reel announcing the new export feature. -> Diego's hat: beat sheet, edit spec, cover, Ana handoff
```

## Why this shape

A persona is a file, not a process. Reading a hat costs about 800 tokens; a child agent costs a full boot plus a second read of the repository. So the coordinator stays resident on the cheap **Luna** tier, hats cost almost nothing, and money is spent only where judgment must be independent: a read-only reviewer on a different model, or one reusable read-only **Sol** decision packet at a real decision gate. FAST and STANDARD work uses zero Sol. Rationale in [docs/DESIGN.md](docs/DESIGN.md).

## Layout

```text
team/                      the installable skill
  SKILL.md                 Laila: routing table, modes, child rules, capsule, report format
  personas/*.md            seven hats, read on demand
  lenses/<domain>/*.md     domain depth, read only when the task needs it
  lenses/shared/           evidence states, memory rules
  templates/docs/          project memory docs (engineering, design, delivery)
  scripts/project-context.py   repository snapshot cache shared by all worktrees
  scripts/init-project.sh      creates docs/<domain>/ from the templates
evals/                     six behaviors with mechanical assertions over Codex traces
scripts/                   validate, install, run-evals, eval-assert
docs/                      design rationale, Penpot and pen.dev setup
```

## Install

```bash
npx skills add gustavolbs/ai-personas --skill team -g -a codex -y
```

or from a clone:

```bash
bash scripts/install.sh
```

Restart Codex. Say `Laila, <outcome>`. Set `AI_PERSONAS_REMOVE_LEGACY=1` when running the installer to remove the previous seven separate persona skills.

## Project setup (optional)

```bash
bash ~/.agents/skills/team/scripts/init-project.sh --context      # snapshot cache in <git-common-dir>/ai-personas
bash ~/.agents/skills/team/scripts/init-project.sh --engineering  # docs/engineering/ templates
bash ~/.agents/skills/team/scripts/init-project.sh --all
```

The cache never touches the working tree and is shared by every worktree of the repository. `FRESH` means no rediscovery; `STALE` means reconcile the listed delta only.

## Validate and evaluate

```bash
bash scripts/validate.sh    # structure, size caps, dangling references, cache tests, assertion selftest (CI)
bash scripts/run-evals.sh   # live: runs six prompts through codex exec and asserts on the traces (uses quota)
```

## Third-party

Optional external skills and tools Ashley and Dave know how to use are listed in [THIRD_PARTY.md](THIRD_PARTY.md). Nothing is installed automatically.
