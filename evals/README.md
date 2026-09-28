# Evals

Seven behaviors that cost money or trust when they break. Each case is a prompt plus a mechanical assertion over the `codex exec --json` trace, implemented in `scripts/eval-assert.py`.

```bash
bash scripts/run-evals.sh                 # all cases, uses real model quota
bash scripts/run-evals.sh fast-path       # one case
python3 scripts/eval-assert.py --selftest # assertions only, no model (runs in CI)
```

Run them before a release and after any change to `team/SKILL.md` or `team/personas/`. The assertions are heuristics over the serialized trace; a PASS means the failure signal was absent, not that the output was good. Read the trace when a case matters.

| Case | Asserts |
|---|---|
| fast-path | no child spawned, ≤8 tool events |
| sol-budget | no child above the resident tier for STANDARD work |
| hat-before-write | `personas/dave.md` read before the first `src/` edit |
| context-fresh | no broad repository listing when the cache is FRESH |
| parallel-disjoint | ≤2 children, capsules carry owned paths, do-not-touch and frozen contract, owned paths disjoint |
| program-mode | ≥2 package children with capsules, Laila's own shell/patch calls ≤40 |
| no-fake-validation | a "tests pass" claim is backed by an actual check command |
