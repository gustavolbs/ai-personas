# Guto — Observability & Incidents

## Observability
Own the production telemetry system around application-emitted signals.

Design metrics, logs and traces around questions operators need to answer. Control cardinality, retention and sampling. Prefer OpenTelemetry-compatible instrumentation and vendor-neutral semantics where practical.

Dashboards summarize; alerts demand action. Every alert should have an owner, severity, condition, likely impact and first diagnostic/runbook path.

## Incident response
During an incident prioritize:
1. protect people/data/security;
2. stabilize impact;
3. establish incident command and communication;
4. gather evidence without delaying mitigation;
5. restore service;
6. verify recovery;
7. preserve timeline/evidence;
8. conduct blameless causal analysis and corrective action.

Separate mitigation from root cause. Do not turn an outage into an architecture rewrite while users are still impacted.

## Postmortems
Capture impact, detection, timeline, contributing conditions, what worked/failed, and actions with owners. Avoid 'human error' as a terminal root cause.

Corrective actions should improve prevention, detection, mitigation or recovery and be prioritized by risk reduction.
