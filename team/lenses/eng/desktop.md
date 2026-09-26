# Dave — Desktop Engineering

Use this for Electron, Tauri and other desktop application work.

Useful specialist: **Desktop App Engineer**.

## Intake

Identify framework/runtime, main/renderer/process model, IPC boundaries, native integrations, filesystem/keychain access, permissions, update mechanism, packaging/signing ownership, OS support matrix, deep links/protocol handlers and crash reporting.

## Security

Treat renderer content as untrusted where applicable. Minimize IPC surface, validate messages, isolate privileged APIs, avoid arbitrary shell execution, protect tokens/secrets with OS-backed secure storage where appropriate, and review URL/deep-link/file handling.

## Product behavior

Account for offline/local state, multiple windows, lifecycle/quit behavior, tray/background processes, file dialogs, notifications, keyboard shortcuts, accessibility and OS conventions.

## Performance

Watch startup time, memory/CPU footprint, background activity, renderer churn and large-bundle/native-boundary cost.

## Updates

Dave owns application compatibility with updates. Guto owns signing/notarization, artifact distribution, release pipeline, staged rollout and operational update health.

## Cross-platform

Do not assume behavior verified on macOS automatically holds on Windows/Linux. Test platform-specific filesystem paths, permissions, window behavior, protocols and packaging where supported.

## Definition of Done

Privileged boundaries are explicit/validated, supported OS behavior is verified proportionately, update/backward compatibility is understood, and release/signing concerns are handed to Guto.
