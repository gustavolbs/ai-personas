#!/usr/bin/env python3
"""Deployment-free local project context cache shared by every worktree of a repository."""
from __future__ import annotations
import argparse, hashlib, json, os, subprocess, sys
from datetime import datetime, timezone
from pathlib import Path

SCHEMA_VERSION=1
PENDING="<!-- AI_PERSONAS_CONTEXT_PENDING -->"
MAX_BYTES=int(os.environ.get("AI_PERSONAS_CONTEXT_MAX_BYTES","4096"))
MAX_DELTA=int(os.environ.get("AI_PERSONAS_CONTEXT_MAX_DELTA_LINES","80"))
EXCLUDED={".git",".hg",".svn","node_modules",".next","dist","build","coverage","vendor",".venv","venv","__pycache__",".turbo",".cache"}
KEY={"AGENTS.md","README.md","package.json","pnpm-workspace.yaml","turbo.json","nx.json","pyproject.toml","Cargo.toml","go.mod","composer.json","docker-compose.yml","docker-compose.yaml","compose.yml","compose.yaml","Makefile","justfile","tsconfig.json"}

def sh(cmd,cwd,check=True,binary=False):
    p=subprocess.run(cmd,cwd=str(cwd),stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=False)
    if check and p.returncode:
        raise RuntimeError(p.stderr.decode("utf-8","replace").strip() or "command failed")
    return p.stdout if binary else p.stdout.decode("utf-8","replace").strip()

def root_of(explicit):
    base=Path(explicit or os.getcwd()).expanduser().resolve()
    p=subprocess.run(["git","-C",str(base),"rev-parse","--show-toplevel"],stdout=subprocess.PIPE,stderr=subprocess.DEVNULL)
    return (Path(p.stdout.decode().strip()).resolve(),True) if p.returncode==0 else (base,False)

def git(root,*args,check=True,binary=False): return sh(["git",*args],root,check,binary)

def paths(root,is_git):
    # ponytail: --git-common-dir so every worktree shares one snapshot; HEAD/branch fingerprint still marks it STALE per worktree
    cache=((root/git(root,"rev-parse","--git-common-dir")).resolve()/"ai-personas") if is_git else (root/".ai-personas")
    return {"cache":cache,"summary":cache/"PROJECT_CONTEXT.md","state":cache/"state.json","graph":cache/"graphify-out"}

def sha(path):
    h=hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda:f.read(1024*1024),b""): h.update(chunk)
    return h.hexdigest()

def git_tree_state(root):
    h=hashlib.sha256()
    h.update(git(root,"diff","--binary","HEAD","--",".",check=False,binary=True))
    raw=git(root,"ls-files","--others","--exclude-standard","-z",check=False,binary=True)
    untracked=[x.decode("utf-8","surrogateescape") for x in raw.split(b"\0") if x]
    for rel in sorted(untracked):
        p=root/rel; h.update(rel.encode("utf-8","surrogateescape"))
        try:
            if p.is_file():
                h.update(str(p.stat().st_size).encode())
                with p.open("rb") as f:
                    for chunk in iter(lambda:f.read(1024*1024),b""): h.update(chunk)
        except OSError: h.update(b"<unreadable>")
    status=git(root,"status","--short","--untracked-files=all",check=False)
    return h.hexdigest(),[x for x in status.splitlines() if x.strip()]

def plain_tree_state(root):
    h=hashlib.sha256(); seen=[]
    for p in sorted(root.rglob("*")):
        try: rel=p.relative_to(root)
        except ValueError: continue
        if any(part in EXCLUDED for part in rel.parts) or not p.is_file(): continue
        try: st=p.stat()
        except OSError: continue
        r=rel.as_posix(); h.update(r.encode()); h.update(str(st.st_size).encode()); h.update(str(st.st_mtime_ns).encode()); seen.append(r)
        if len(seen)>=5000: h.update(b"<truncated>"); break
    return h.hexdigest(),seen

def current(root,is_git):
    if is_git:
        fp,dirty=git_tree_state(root)
        return {"schema":1,"head":git(root,"rev-parse","HEAD",check=False) or "UNBORN","branch":git(root,"branch","--show-current",check=False) or "(detached)","worktree_fingerprint":fp,"dirty":dirty}
    fp,seen=plain_tree_state(root)
    return {"schema":1,"head":"NO_GIT","branch":"NO_GIT","worktree_fingerprint":fp,"dirty":[],"seen_files":len(seen)}

def facts(root,is_git):
    if not is_git:
        top=sorted(p.name for p in root.iterdir() if p.name not in EXCLUDED)[:40]
        return "Top-level entries: "+(", ".join(top) if top else "(empty)")
    files=git(root,"ls-files",check=False).splitlines()
    top=sorted({f.split("/",1)[0] for f in files})[:60]
    keys=[f for f in files if Path(f).name in KEY][:60]
    counts={}
    for f in files:
        ext=Path(f).suffix.lower() or "[no-ext]"; counts[ext]=counts.get(ext,0)+1
    exts=", ".join(f"{e}:{n}" for e,n in sorted(counts.items(),key=lambda x:(-x[1],x[0]))[:12])
    return f"Top-level: {', '.join(top) or '(empty)'}\nKey manifests/docs: {', '.join(keys) or '(none detected)'}\nFile-type counts: {exts or '(none)'}"

def template(root,is_git):
    s=current(root,is_git)
    return f"""# Project Context Snapshot

{PENDING}

This is a compact navigation accelerator, not repository truth. Keep it under {MAX_BYTES} bytes.

## Project purpose
- TODO: one concise paragraph.

## Architecture and domain map
- TODO: applications/packages/services and their relationships.

## Stable contracts and invariants
- TODO: auth/data/API/design/runtime invariants worth reusing.

## Key entry points
- TODO: high-value code/docs/config paths.

## Current durable risks / constraints
- TODO: only cross-session facts.

## Source pointers
- TODO: authoritative ADRs, AGENTS.md, schemas, trackers or runbooks.

## Deterministic repository facts
Branch: {s['branch']}
HEAD: {s['head']}

{facts(root,is_git)}
"""

def load(path):
    try:return json.loads(path.read_text())
    except (FileNotFoundError,json.JSONDecodeError):return None

def ensure(root,is_git,p):
    p["cache"].mkdir(parents=True,exist_ok=True)
    if p["summary"].exists(): return False
    p["summary"].write_text(template(root,is_git)); return True

def commit_delta(root,old,new):
    if old in {"","NO_GIT","UNBORN"} or new in {"","NO_GIT","UNBORN"}: return []
    probe=subprocess.run(["git","-C",str(root),"cat-file","-e",f"{old}^{{commit}}"],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
    if probe.returncode:return [f"? previous snapshot commit unavailable: {old}"]
    return [x for x in git(root,"diff","--name-status",old,new,"--",".",check=False).splitlines() if x.strip()]

def payload(root,is_git,p):
    ensure(root,is_git,p); saved=load(p["state"]); cur=current(root,is_git); summary=p["summary"].read_text()
    ready=bool(saved and saved.get("ready") and PENDING not in summary)
    fresh=bool(ready and saved.get("head")==cur["head"] and saved.get("worktree_fingerprint")==cur["worktree_fingerprint"] and saved.get("summary_sha256")==sha(p["summary"]))
    status="FRESH" if fresh else ("NEEDS_CONTEXT" if not ready else "STALE")
    return {"status":status,"project_root":str(root),"cache_dir":str(p["cache"]),"summary_path":str(p["summary"]),"graph_dir":str(p["graph"]),"saved":saved,"current":cur,"committed_delta":commit_delta(root,str((saved or {}).get("head","")),cur["head"]) if is_git else [],"working_delta":cur["dirty"] if is_git else [],"summary_bytes":len(summary.encode())}

def print_delta(title,lines):
    if not lines:return
    print(title)
    for x in lines[:MAX_DELTA]:print("  "+x)
    if len(lines)>MAX_DELTA:print(f"  ... +{len(lines)-MAX_DELTA} more")

def print_status(x,compact=False):
    c=x["current"]; print(f"{x['status']} branch={c['branch']} head={c['head']} summary_bytes={x['summary_bytes']}")
    if compact:return
    if x["status"]=="STALE":
        s=x.get("saved") or {}; print(f"snapshot_head={s.get('head','(none)')} snapshot_branch={s.get('branch','(none)')}")
        print_delta("committed_delta:",x["committed_delta"]); print_delta("working_delta:",x["working_delta"])
        if not x["committed_delta"] and not x["working_delta"]:print("  machine fingerprint changed; re-check task-relevant files before checkpointing")
    elif x["status"]=="NEEDS_CONTEXT":
        print("Run one proportional discovery, replace the pending marker/TODOs, then checkpoint.")

def resolve(args):
    r,g=root_of(args.root); return r,g,paths(r,g)

def bootstrap(args):
    r,g,p=resolve(args); made=ensure(r,g,p); print(("created " if made else "keep    ")+str(p["summary"])); print_status(payload(r,g,p)); return 0

def status(args):
    r,g,p=resolve(args); x=payload(r,g,p)
    print(json.dumps(x,indent=2,sort_keys=True)) if args.json else print_status(x,args.compact); return 0

def show(args):
    r,g,p=resolve(args); x=payload(r,g,p); print_status(x); print("\n--- PROJECT_CONTEXT.md ---"); print(p["summary"].read_text().rstrip()); return 0

def checkpoint(args):
    r,g,p=resolve(args); ensure(r,g,p); summary=p["summary"].read_text(); size=len(summary.encode())
    if PENDING in summary and not args.allow_pending: print("Refusing checkpoint: pending marker remains.",file=sys.stderr); return 2
    if size>MAX_BYTES: print(f"Refusing checkpoint: {size} bytes exceeds {MAX_BYTES}.",file=sys.stderr); return 2
    s=current(r,g); s.update({"schema":SCHEMA_VERSION,"ready":PENDING not in summary,"summary_sha256":sha(p["summary"]),"summary_bytes":size,"updated_at":datetime.now(timezone.utc).isoformat().replace("+00:00","Z")})
    p["state"].write_text(json.dumps(s,indent=2,sort_keys=True)+"\n")
    print(f"CHECKPOINTED branch={s['branch']} head={s['head']} summary_bytes={size}"); return 0

def path_cmd(args):
    r,g,p=resolve(args); ensure(r,g,p); print(p["summary"]); return 0

def graph_dir(args):
    r,g,p=resolve(args); p["graph"].mkdir(parents=True,exist_ok=True); print(p["graph"]); return 0

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--root")
    sp=ap.add_subparsers(dest="cmd",required=True)
    sp.add_parser("bootstrap")
    st=sp.add_parser("status"); st.add_argument("--json",action="store_true"); st.add_argument("--compact",action="store_true")
    sp.add_parser("show")
    cp=sp.add_parser("checkpoint"); cp.add_argument("--allow-pending",action="store_true",help=argparse.SUPPRESS)
    sp.add_parser("path"); sp.add_parser("graph-dir")
    a=ap.parse_args()
    return {"bootstrap":bootstrap,"status":status,"show":show,"checkpoint":checkpoint,"path":path_cmd,"graph-dir":graph_dir}[a.cmd](a)

if __name__=="__main__": raise SystemExit(main())
