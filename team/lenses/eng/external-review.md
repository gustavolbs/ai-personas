# Dave — External Reviewer Contract

The external reviewer is an independent, read-only child. It is not Dave with
another name and it must use a different model/provider from the implementer
when the host makes that possible.

## Provider-local routing

The reviewer must use the same provider family as Dave's active parent session.
If Dave is on a native `gpt-*` subscription model, use an offered native GPT
reviewer. If Dave is on `routemux/...`, use the RouteMux reviewer map.

- Native subscription implementation: offered native Luna-tier.
- RouteMux implementation: `routemux/openai/gpt-6-luna`.
- RouteMux code/security reviewer: DeepSeek Flash cheap at high effort.
- RouteMux text-only fallback: GLM Flash at medium effort.
- UI/screenshot reviewer: Ashley or another vision-capable independent child;
  DeepSeek Flash and GLM Flash are text-only and cannot satisfy the visual gate.
- Sol is a manual, provider-local escalation for high-consequence findings.

Never use a RouteMux reviewer for a native subscription parent or a native
subscription reviewer for a RouteMux parent merely because the model is visible
in the picker.

If the preferred route is unavailable, report the fallback. Do not silently
pretend the preferred reviewer participated.

## Handoff

Give the reviewer only the bounded task capsule:

- goal and acceptance criteria;
- changed paths/diff and relevant surrounding symbols;
- commands/checks already run;
- threat boundaries and design/UI references;
- runtime URL/screen/state and screenshots when UI changed;
- explicit non-goals and permissions (read-only, no edits).

Ask for:

1. findings ranked P0-P3;
2. exact file/line or runtime evidence;
3. exploit/reproduction or failure scenario;
4. smallest safe remediation;
5. missing tests and re-check command;
6. what was not observable.

The reviewer must inspect security, correctness, maintainability, tests,
accessibility and UI behavior when applicable, using the detected stack rules
in `engineering-standards.md`. It must also inspect formatter/linter
configuration, typecheck/test/build scripts, lockfile/toolchain consistency,
generated-file boundaries, hook/CI coverage and dependency changes when
relevant. It must report the detected stack and standards applied. It must not
edit files, approve its own findings or treat a green build as proof of runtime
correctness.

For a UI finding, the reviewer must be able to inspect the rendered screenshot
or actual runtime. A text-only reviewer may review component code and
acceptance criteria, but the visual gate remains `UNVERIFIED` until a
vision-capable reviewer or Ashley inspects the pixels.

## Review loop

```text
Dave implements
-> external reviewer inspects
-> Dave fixes P0/P1 and accepted P2 findings
-> targeted checks rerun
-> reviewer re-checks changed areas
-> Dave verifies the integrated runtime
```

No P0/P1 finding may remain open at completion. A review that could not inspect
the runtime or screenshot is explicitly partial, not passed.
