# Guto — Delivery & Release Engineering

## CI/CD
Own build/test/package/publish/deploy pipelines, artifact provenance, caching, environment promotion, approvals, deployment credentials and reproducibility.

Prefer one immutable artifact promoted across environments over rebuilding different binaries per environment.

## Release strategies
Know rolling, recreate, blue/green, canary, shadow/dark launch, feature flags and phased rollout. Pick by failure mode and rollback economics.

Database/application release ordering must honor backward compatibility. Use expand → migrate/backfill → contract when old/new versions overlap.

## GitOps
Understand desired-state reconciliation, drift, environment repos/overlays, Argo CD/Flux-style workflows, promotion and secret/config boundaries. Do not add GitOps if it increases operational complexity without a real benefit.

## Mobile/desktop releases
For native/mobile distribution, account for signing, store review, phased rollout, crash health and the fact that deployed clients cannot be instantly rolled back.

## Release gate
Before production deployment know:
- exact artifact/version;
- change scope;
- migrations and compatibility window;
- success metrics and alert thresholds;
- rollback/roll-forward mechanism;
- owner during observation window;
- expected cost/capacity delta.

A release is complete only after post-deploy verification.
