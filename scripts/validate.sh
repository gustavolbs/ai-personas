#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"; S="$ROOT/team"
fail(){ echo "validate: $1" >&2; exit 1; }
[[ ! -f "$ROOT/SKILL.md" ]] || fail "root SKILL.md would shadow team/"
grep -q '^name: team$' "$S/SKILL.md" || fail "SKILL.md frontmatter name"
b=$(wc -c < "$S/SKILL.md"); (( b <= 8704 )) || fail "SKILL.md is $b bytes (cap 8704: it loads on every session)"
for p in dave ashley diego guto clara roberto ana; do
  f="$S/personas/$p.md"; [[ -f $f ]] || fail "missing $f"
  b=$(wc -c < "$f"); (( b <= 5120 )) || fail "$f is $b bytes (cap 5120: it loads on every hat switch)"
  grep -q "personas/$p.md" "$S/SKILL.md" || fail "SKILL.md does not route to $p"
done
while read -r ref; do [[ -f "$S/$ref" ]] || fail "dangling reference $ref"; done \
  < <(grep -ohE 'lenses/[a-z]+/[a-z-]+\.md' "$S/SKILL.md" "$S"/personas/*.md | sort -u)
for f in "$S"/lenses/*/*.md; do
  [[ $(basename "$(dirname "$f")") == shared ]] && continue
  grep -q "$(basename "$f")" "$S/SKILL.md" "$S"/personas/*.md "$S"/lenses/*/*.md || fail "orphan lens $f (no persona or lens points to it)"
done
! grep -rnE '(^|[^a-z_])docs/[A-Z_]+\.md|references/[a-z]|_shared/' "$S" || fail "installed skill points at repository-root files"
for f in "$ROOT"/scripts/*.sh "$S"/scripts/*.sh; do bash -n "$f"; done
python3 -c 'import ast,sys; [ast.parse(open(f).read(),f) for f in sys.argv[1:]]' "$S/scripts/project-context.py" "$ROOT"/scripts/*.py
python3 "$ROOT/scripts/test-project-context.py"
python3 "$ROOT/scripts/eval-assert.py" --selftest
for c in $(sed -n 's/^CASES_DEFAULT="\(.*\)"/\1/p' "$ROOT/scripts/run-evals.sh"); do [[ -f "$ROOT/evals/cases/$c.md" ]] || fail "eval case file missing: $c"; done
echo "validate: ok ($(find "$S" -type f | wc -l | tr -d ' ') skill files, SKILL.md $(wc -c < "$S/SKILL.md" | tr -d ' ') B)"
