#!/usr/bin/env bash
# Installs the single `team` skill for Codex. Set AI_PERSONAS_REMOVE_LEGACY=1 to also remove the old seven persona skills.
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
bash "$ROOT/scripts/validate.sh"
DEST="$HOME/.agents/skills/team"
if ! (command -v npx >/dev/null 2>&1 && npx -y skills add "$ROOT" --skill team -g -a codex -y --copy); then
  echo "npx skills unavailable; copying directly"; rm -rf "$DEST"; mkdir -p "$(dirname "$DEST")"; cp -R "$ROOT/team" "$DEST"
fi
[[ -f "$DEST/SKILL.md" ]] || { echo "install failed: $DEST/SKILL.md missing" >&2; exit 1; }
cmp -s "$ROOT/team/SKILL.md" "$DEST/SKILL.md" || echo "warning: installed SKILL.md differs from the repository copy"
if [[ "${AI_PERSONAS_REMOVE_LEGACY:-0}" == "1" ]]; then
  for p in ashley dave guto roberto clara ana laila; do rm -rf "$HOME/.agents/skills/$p" "$HOME/.codex/skills/$p"; done
  echo "removed legacy persona skills"
else
  for p in ashley dave guto roberto clara ana laila; do [[ -d "$HOME/.agents/skills/$p" ]] && echo "note: legacy skill still installed: ~/.agents/skills/$p (AI_PERSONAS_REMOVE_LEGACY=1 removes it)"; done
fi
echo "installed: $DEST. Restart Codex and say: Laila, <outcome>"
