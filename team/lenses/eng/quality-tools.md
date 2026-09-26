# Dave — Optional Quality Tools

These tools add evidence or deterministic checks. They are optional and
project-scoped; Dave never installs them silently or treats their absence as a
failed task.

## AIslop code scan

[AIslop](https://github.com/scanaislop/aislop) is the preferred anti-slop code
scanner for this team. It is MIT-licensed, deterministic, runs without an LLM
at runtime, supports TypeScript/JavaScript and Expo/React Native among other
languages, and reports changed-file/CI output.

Use it when the target project already has the binary:

```bash
aislop ci --changes --base origin/main
```

If the repository has a different integration point, use its existing config
and baseline. Do not turn an uncalibrated score into a hard gate. Review
findings against the Quality section of SKILL.md, fix high-confidence issues, and rerun the
scan. `npx aislop@latest` is a deliberate one-off fallback, not an automatic
dependency installation.

## Runtime verification with Reticle

[Reticle](https://github.com/reticlehq/reticle) is a project-local, dev-only
runtime verification layer for supported web/desktop applications. When its
tools are visible, use the cheapest applicable path:

```text
reticle_verify(action: "change", files: [...])
reticle_verify(action: "flows")
reticle_act_and_wait(..., until: ...)
```

Only an explicit Reticle verdict proves the declared consequence. `unknown` is
not a pass. Reticle complements Playwright and screenshot inspection:
Reticle observes app state/network/console; Playwright and Ashley inspect
browser behavior and pixels. It is not the default for Expo native behavior.

Do not run Reticle's global installer from a persona. It writes agent
configuration and requires an explicit user-approved project setup.

## SkillSpector supply-chain gate

[NVIDIA SkillSpector](https://github.com/NVIDIA/skillspector) is the preferred
pre-install scanner for third-party skills, MCPs and agent bundles. Before
executing an external installer or copying an untrusted skill, scan it when the
CLI is available:

```bash
skillspector scan /path/to/skill --no-llm
```

Review high-severity findings before proceeding. A static-only clean result is
not proof of safety; preserve the report and inspect scripts, permissions,
network access and credentials. If SkillSpector is absent, perform the
repository's security review and state that the machine scan was skipped.

## Fallback

If none of these tools is available, Dave still runs the repository's native
formatter/lint/type/test/build/security/UI gates. Never claim that an optional
tool participated when it did not.
