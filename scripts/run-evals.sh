#!/usr/bin/env bash
# Live evals: each case runs through `codex exec --json` against a throwaway fixture repo, then the trace is asserted.
# Costs real model quota. Requires the team skill installed (scripts/install.sh).
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
CTX="$ROOT/team/scripts/project-context.py"
CASES_DEFAULT="fast-path sol-budget hat-before-write context-fresh parallel-disjoint program-mode no-fake-validation"
command -v codex >/dev/null || { echo "codex CLI required" >&2; exit 2; }
[[ -f "$HOME/.agents/skills/team/SKILL.md" ]] || { echo "install the team skill first: bash scripts/install.sh" >&2; exit 2; }
OUT="${AI_PERSONAS_EVAL_OUT:-$ROOT/.eval-results}"; rm -rf "$OUT"; mkdir -p "$OUT"
fixture(){
  local d=$1; rm -rf "$d"; mkdir -p "$d/src"
  ( cd "$d"; git init -q; git config user.email eval@example.com; git config user.name Eval
    printf '# Demo\n\nA small TypeScript demo. Entry point: src/app.ts.\n' > README.md
    printf '{"name":"demo","scripts":{"test":"node --test","typecheck":"tsc --noEmit"}}\n' > package.json
    printf 'export const add=(a:number,b:number)=>a+b;\nexport const greet=(n:string)=>`Helo ${n}`;\n' > src/app.ts
    git add . && git commit -qm init )
}
fail=0
for c in ${*:-$CASES_DEFAULT}; do
  d="$OUT/fixture-$c"; fixture "$d"
  if [[ $c == context-fresh ]]; then
    python3 "$CTX" --root "$d" bootstrap >/dev/null; p=$(python3 "$CTX" --root "$d" path)
    sed -i.bak -e '/AI_PERSONAS_CONTEXT_PENDING/d' -e 's/- TODO:.*/- see README.md and src\/app.ts/' "$p"; rm -f "$p.bak"
    python3 "$CTX" --root "$d" checkpoint >/dev/null
  fi
  prompt="$(sed -n '/^## Prompt/,/^## /p' "$ROOT/evals/cases/$c.md" | sed '1d;$d')"
  echo "== $c"; codex exec --json -C "$d" "$prompt" > "$OUT/$c.jsonl" || true
  python3 "$ROOT/scripts/eval-assert.py" "$c" "$OUT/$c.jsonl" || fail=1
done
exit $fail
