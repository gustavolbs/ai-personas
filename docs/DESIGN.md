# Design rationale

Why the skill is shaped the way it is. The rules themselves live in `team/SKILL.md`; this file only explains them.

## Where the money goes

A prompt-only persona suite spends tokens in four places: instructions loaded per session, repository reads, child agents, and the expensive model. Version 4 controlled the last two well and the first two badly: every persona session read five shared contracts and its own SKILL.md (7 to 13k tokens and 7 to 12 tool calls before any work), and every persona handoff spawned a child that booted again and reread the repository.

Version 5 inverts that. One SKILL.md under 8 KiB carries every rule. A persona is a file read in the same thread (a "hat"). Children exist for three reasons only, and two of them are exactly the places where independent judgment is worth paying for.

## Hats

Intelligence comes from three things: the right domain knowledge loaded at the right time (lenses), rules of authority and evidence (SKILL.md), and independent judgment. A hat provides the first two for ~800 tokens. It cannot provide the third, because the same context reviewing itself shares its blind spots. That is why review and Sol decisions are the only children that are always allowed, and why the reviewer must run on a different model.

The mutation table survives unchanged: code is written only under Dave's hat, ops config only under Guto's, Ashley never writes production code. In a single thread this is observable as "the persona file was read before the edit", which is what the `hat-before-write` eval asserts.

## Luna runs, Sol decides

The resident session runs on the cheap tier. Sol is a read-only child that returns a decision packet and leaves. It is triggered by a decision gate, never by task size. FAST and STANDARD have a Sol budget of zero. Prompt text cannot change the model of an already-open session, so the user opens the session on Luna; `agents/openai.yaml` says so.

Never cross provider families for a child: provider choice controls quota, billing, credentials and tool compatibility. If the intended lane is unavailable, use the strongest same-provider route and say so.

Any model in the resident lane must be reliable at tool calling, long instruction following and, for Ashley's canvas work, vision. Smoke test after changing models: inspect a design without writing, create a small disposable frame, re-read it, produce two genuinely different variants. A model that narrates tool calls instead of executing them or loses the active context is unsuitable regardless of price.

## Parallelism

Parallel children pay 2 to 3× tokens for wall-clock savings and add integration work for one reviewer: the user. They are allowed only when write paths are disjoint, the shared contract is frozen and the clock matters. Contracts come first (Clara/Roberto/Ana semantics, Ashley flow, Dave types), then at most two writers in separate worktrees, then sequential integration and one review over the integrated diff.

## Project context

A new chat must not imply a new repository discovery. `project-context.py` keeps a ≤4 KiB snapshot under `--git-common-dir`, so every worktree shares it; HEAD, tree fingerprint and summary hash decide freshness. Current code always outranks the snapshot. Graphify remains optional for multi-hop dependency questions and is never auto-installed.

## Evidence and anti-slop

Evidence states (PROPOSED, CHANGED, BUILT, RUN, VERIFIED, UNVERIFIED) stop a diff from becoming "done" and a child's claim from becoming proof. Anti-slop is a quality check on generic or unsupported output; it never overrides security, accessibility, user voice or repository truth, and never infers authorship from style.

## Evals

The old suite had 47 narrative scenarios and a CI that grepped for phrases in docs. That verified the spec existed, not that a model obeyed it. The new suite has six cases whose failure would cost money or trust, each with a mechanical assertion over the Codex trace. They run before releases, not in CI, because they spend quota. The assertions self-test in CI.

## Third-party knowledge

Agency Agents, UI/UX Pro Max, Taste, Impeccable and similar projects are absorbed as principles in the lenses or referenced as optional external tools. Installing dozens of specialist agents adds their descriptions to every session's context; a 30-line lens loaded on demand delivers the same perspective for free.
