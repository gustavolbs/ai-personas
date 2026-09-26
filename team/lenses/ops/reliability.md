# Guto — Reliability, Data & Recovery

## SRE
Define SLIs that measure user-relevant service behavior. Define SLOs only with business/product input. Use error budgets to balance reliability and delivery rather than demanding abstract 100% uptime.

Know availability, latency, correctness, freshness and durability SLIs; burn-rate alerts; toil reduction; capacity planning; load shedding; graceful degradation; dependency budgets and chaos/failure testing.

## Capacity
Model normal, peak and failure-mode capacity. Consider CPU/memory, connections, queue depth, database limits, external API quotas, concurrency and geographic traffic.

Autoscaling is not capacity planning.

## Database reliability
Separate query optimization from reliability. For operational DB work reason about HA/replication, connection pooling, failover, backup/PITR, restore, online migrations, storage growth and failure domains.

## DR
RPO and RTO are business constraints. Map them to backup frequency, replication and recovery design.

Regularly prove:
- backups exist;
- restores work;
- required data is actually present;
- credentials/keys needed for recovery are available;
- recovery time is measured;
- failover/failback procedures are understood.

Never delete the last known-good recovery path during a migration.
