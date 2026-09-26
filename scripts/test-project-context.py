#!/usr/bin/env python3
from pathlib import Path
import subprocess,tempfile
ROOT=Path(__file__).resolve().parents[1]; SCRIPT=ROOT/"team/scripts/project-context.py"
def run(a,c,ok=True):
 p=subprocess.run(a,cwd=c,text=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
 if ok and p.returncode: raise AssertionError(f"{a}\n{p.stdout}\n{p.stderr}")
 return p
with tempfile.TemporaryDirectory() as td:
 r=Path(td)/"repo"; r.mkdir(); run(["git","init","-q"],r); run(["git","config","user.email","eval@example.com"],r); run(["git","config","user.name","Eval"],r)
 (r/"src").mkdir(); (r/"README.md").write_text("# Demo\n"); (r/"package.json").write_text('{"name":"demo"}\n'); (r/"src/app.ts").write_text("export const value=1;\n")
 run(["git","add","."],r); run(["git","commit","-qm","init"],r)
 assert "NEEDS_CONTEXT" in run(["python3",str(SCRIPT),"bootstrap"],r).stdout
 p=Path(run(["python3",str(SCRIPT),"path"],r).stdout.strip()); assert p.exists() and ".git" in str(p); assert not run(["git","status","--porcelain"],r).stdout.strip()
 s=p.read_text().replace("<!-- AI_PERSONAS_CONTEXT_PENDING -->\n\n","")
 s=s.replace("- TODO: one concise paragraph.","- Demo project.").replace("- TODO: applications/packages/services and their relationships.","- src/ is the app.")
 s=s.replace("- TODO: auth/data/API/design/runtime invariants worth reusing.","- package.json owns package metadata.").replace("- TODO: high-value code/docs/config paths.","- src/app.ts")
 s=s.replace("- TODO: only cross-session facts.","- None.").replace("- TODO: authoritative ADRs, AGENTS.md, schemas, trackers or runbooks.","- README.md"); p.write_text(s)
 run(["python3",str(SCRIPT),"checkpoint"],r); assert run(["python3",str(SCRIPT),"status","--compact"],r).stdout.startswith("FRESH")
 (r/"src/app.ts").write_text("export const value=2;\n"); stale=run(["python3",str(SCRIPT),"status"],r).stdout; assert stale.startswith("STALE") and "src/app.ts" in stale
 run(["python3",str(SCRIPT),"checkpoint"],r); assert run(["python3",str(SCRIPT),"status","--compact"],r).stdout.startswith("FRESH")
 (r/"src/new.ts").write_text("export const created=true;\n"); run(["git","add","-A"],r); run(["git","commit","-qm","add"],r)
 stale=run(["python3",str(SCRIPT),"status"],r).stdout; assert stale.startswith("STALE") and "src/new.ts" in stale
 gd=Path(run(["python3",str(SCRIPT),"graph-dir"],r).stdout.strip()); assert gd.parent==p.parent
 run(["python3",str(SCRIPT),"checkpoint"],r); wt=Path(td)/"wt"; run(["git","worktree","add","-q","-b","wt",str(wt)],r)
 assert run(["python3",str(SCRIPT),"path"],wt).stdout.strip()==str(p), "worktree must share the repository cache"
 out=run(["python3",str(SCRIPT),"status"],wt).stdout; assert out.startswith("FRESH"), out
 status=run(["git","status","--porcelain"],r).stdout
 assert "ai-personas" not in status and "graphify-out" not in status, status
print("Project context cache tests passed.")
