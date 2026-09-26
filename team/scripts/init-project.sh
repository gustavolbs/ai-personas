#!/usr/bin/env bash
set -euo pipefail
SKILL_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PROJECT_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
usage(){ echo "Usage: init-project.sh [--context] [--engineering] [--design] [--delivery] [--all]"; }
copy_docs(){
  local d=$1 f t; mkdir -p "$PROJECT_ROOT/docs/$d"
  for f in "$SKILL_ROOT/templates/docs/$d"/*.md; do
    t="$PROJECT_ROOT/docs/$d/$(basename "$f")"
    if [[ -e $t ]]; then echo "keep   docs/$d/$(basename "$f")"; else cp "$f" "$t"; echo "create docs/$d/$(basename "$f")"; fi
  done
}
[[ $# -gt 0 ]] || { usage; exit 0; }
for a in "$@"; do case $a in
  --context) python3 "$SKILL_ROOT/scripts/project-context.py" bootstrap ;;
  --engineering|--design|--delivery) copy_docs "${a#--}" ;;
  --all) python3 "$SKILL_ROOT/scripts/project-context.py" bootstrap; for d in engineering design delivery; do copy_docs "$d"; done ;;
  -h|--help) usage ;;
  *) echo "unknown option: $a" >&2; usage >&2; exit 2 ;;
esac; done
