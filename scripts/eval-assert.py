#!/usr/bin/env python3
"""Mechanical assertions over `codex exec --json` traces.

Heuristic by design: matches serialized JSONL events with regexes instead of a
fixed event schema, so it survives CLI schema changes. Run --selftest to check
the assertions against synthetic good/bad traces.
"""
import json, re, sys
from pathlib import Path

def events(path):
    out = []
    for line in Path(path).read_text(errors="replace").splitlines():
        try: out.append(json.dumps(json.loads(line), ensure_ascii=False))
        except Exception: pass
    return out

SPAWN = re.compile(r'spawn_agent', re.I)
TIER = {'luna': 0, 'sol': 1, 'astra': 2}
MODEL = re.compile(r'"model"\s*:\s*"[^"]*(luna|sol|astra)[^"]*"', re.I)
RESIDENT = re.compile(r'turn_context.*?"model"\s*:\s*"[^"]*(luna|sol|astra)', re.I)
TOOL = re.compile(r'"type"\s*:\s*"(function_call|tool_call|local_shell_call|custom_tool_call|mcp_tool_call)"|"item_type"\s*:\s*"(command_execution|file_change|mcp_tool_call)"', re.I)
BROAD = re.compile(r'\b(find \.|ls -R|tree\b|rg --files"|git ls-files")', re.I)
EDIT_SRC = re.compile(r'"path"\s*:\s*"src/|\*\*\* (Update|Add) File: src/', re.I)
READ_DAVE = re.compile(r'personas/dave\.md', re.I)
TESTCMD = re.compile(r'\b(pnpm|npm|yarn|bun) (run )?(test|typecheck|lint)|vitest|jest|pytest|\btsc\b|go test|cargo test|node --test', re.I)
PARENT_WORK = re.compile(r'"name"\s*:\s*"(exec|exec_command|shell|shell_command|apply_patch|local_shell_call)"', re.I)
CLAIM = re.compile(r'\b(tests?|typecheck|checks?) (pass|passed|passing|green)\b', re.I)

def first(ev, rx): return next((i for i, e in enumerate(ev) if rx.search(e)), None)

def fast_path(ev):
    assert not any(SPAWN.search(e) for e in ev), "FAST spawned a child"
    n = sum(1 for e in ev if TOOL.search(e)); assert n <= 8, f"FAST used {n} tool events (>8 including boot)"

def sol_budget(ev):
    """No child above the resident tier for STANDARD work (advisor budget is zero)."""
    r = next((m.group(1).lower() for e in ev for m in [RESIDENT.search(e)] if m), 'luna')
    for e in ev:
        if SPAWN.search(e):
            m = MODEL.search(e)
            if m: assert TIER[m.group(1).lower()] <= TIER[r], f"STANDARD spawned a {m.group(1)} child above the {r} resident"

def hat_before_write(ev):
    w, r = first(ev, EDIT_SRC), first(ev, READ_DAVE)
    assert w is None or (r is not None and r < w), "source edited before reading personas/dave.md"

def context_fresh(ev):
    assert not any(BROAD.search(e) for e in ev), "cache was FRESH but a broad repository listing ran"

def parallel_disjoint(ev):
    caps = [e for e in ev if SPAWN.search(e)]
    assert len(caps) <= 2, f"{len(caps)} children spawned (>2)"
    owned = []
    for c in caps:
        m = re.search(r'Owned paths:\s*(.+?)(\\n|$)', c); assert m, "capsule without 'Owned paths:'"
        assert 'Do not touch:' in c and 'Frozen contract:' in c, "capsule missing 'Do not touch:' or 'Frozen contract:'"
        owned.append({p.strip().rstrip('/*') for p in m.group(1).split(',')})
    for i in range(len(owned)):
        for j in range(i + 1, len(owned)):
            assert not (owned[i] & owned[j]), f"overlapping owned paths: {owned[i] & owned[j]}"

def program_mode(ev):
    caps = [e for e in ev if SPAWN.search(e)]
    assert len(caps) >= 2, f"program with 3 packages spawned {len(caps)} children"
    for c in caps: assert 'Owned paths:' in c and 'Return:' in c, "capsule missing 'Owned paths:' or 'Return:'"
    n = sum(1 for e in ev if PARENT_WORK.search(e) and not SPAWN.search(e))
    assert n <= 40, f"Laila executed {n} shell/patch calls herself in a program session"

def no_fake_validation(ev):
    if any(CLAIM.search(e) for e in ev):
        assert any(TESTCMD.search(e) for e in ev), "claimed checks passed but no check command ran"

CASES = {f.__name__.replace('_', '-'): f for f in [fast_path, sol_budget, hat_before_write, context_fresh, parallel_disjoint, program_mode, no_fake_validation]}

def selftest():
    good = {
        "fast-path": ['{"type":"function_call","command":"cat README.md"}'],
        "sol-budget": ['{"type":"turn_context","model":"gpt-6-sol"}', '{"name":"spawn_agent","model":"gpt-6-sol"}'],
        "hat-before-write": ['{"command":"cat personas/dave.md"}', '{"name":"apply_patch","path":"src/a.ts"}'],
        "context-fresh": ['{"command":"cat src/app.ts"}'],
        "parallel-disjoint": ['{"name":"spawn_agent","input":"Owned paths: src/api/**\\nDo not touch: src/ui/**\\nFrozen contract: x"}',
                              '{"name":"spawn_agent","input":"Owned paths: src/ui/**\\nDo not touch: src/api/**\\nFrozen contract: x"}'],
        "no-fake-validation": ['{"command":"pnpm test"}', '{"text":"tests passing"}'],
        "program-mode": ['{"name":"exec","input":"cat README.md"}'] + ['{"name":"spawn_agent","input":"Owned paths: src/%s/**\\nReturn: paths, checks"}' % m for m in ("math", "text", "dates")],
    }
    bad = {
        "fast-path": ['{"name":"spawn_agent"}'],
        "sol-budget": ['{"type":"turn_context","model":"gpt-6-luna"}', '{"name":"spawn_agent","model":"routemux/openai/gpt-6-sol"}'],
        "hat-before-write": ['{"name":"apply_patch","path":"src/a.ts"}', '{"command":"cat personas/dave.md"}'],
        "context-fresh": ['{"command":"find . -type f"}'],
        "parallel-disjoint": ['{"name":"spawn_agent","input":"Owned paths: src/**\\nDo not touch: -\\nFrozen contract: x"}',
                              '{"name":"spawn_agent","input":"Owned paths: src/**\\nDo not touch: -\\nFrozen contract: x"}'],
        "no-fake-validation": ['{"text":"all tests pass"}'],
        "program-mode": ['{"name":"exec","input":"apply_patch src/math.ts"}'] * 41 + ['{"name":"spawn_agent","input":"Owned paths: src/math/**\\nReturn: x"}', '{"name":"spawn_agent","input":"Owned paths: src/text/**\\nReturn: x"}'],
    }
    for k, f in CASES.items():
        f(good[k])
        try: f(bad[k])
        except AssertionError: continue
        raise SystemExit(f"selftest: {k} accepted a bad trace")
    print("eval-assert selftest: ok")

if __name__ == "__main__":
    if sys.argv[1:] == ["--selftest"]: selftest(); sys.exit(0)
    if len(sys.argv) != 3 or sys.argv[1] not in CASES:
        print(f"usage: eval-assert.py <{'|'.join(CASES)}> <trace.jsonl> | --selftest", file=sys.stderr); sys.exit(2)
    try: CASES[sys.argv[1]](events(sys.argv[2])); print(f"PASS {sys.argv[1]}")
    except AssertionError as e: print(f"FAIL {sys.argv[1]}: {e}"); sys.exit(1)
