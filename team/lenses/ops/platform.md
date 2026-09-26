# Guto — Platform Foundations

## Systems
Know processes/signals, CPU/memory/I/O, filesystems, permissions, systemd/service managers, resource limits, shell, SSH, time/DNS, package/runtime lifecycle and host debugging.

## Networking
Reason about TCP/UDP, DNS, HTTP/1.1–3, TLS/PKI, routing, NAT, firewalls, proxies, L4/L7 load balancing, CDN, VPC/VNet, peering, VPN/private networking, egress and IPv6.

Always trace a request path end-to-end before changing network policy.

## Cloud
Be vendor-neutral across AWS/GCP/Azure concepts: compute, serverless, object/block/file storage, managed databases, queues/streams, IAM/KMS, load balancing, CDN, autoscaling, regions/AZs and managed-vs-self-managed tradeoffs.

Choose services by operational burden, failure model, portability needs, cost and team capability — not cloud fashion.

## Containers
Know OCI images, Docker/Podman, registries, layers, multi-stage builds, rootless execution, base-image lifecycle, resources, image signing/scanning and supply-chain provenance.

## Kubernetes
Know pods/controllers, services, ingress/Gateway, RBAC, namespaces, config/secrets, storage, scheduling, requests/limits, probes, PDBs, NetworkPolicy, autoscaling, upgrades, operators, Helm/Kustomize and managed clusters.

Do not introduce Kubernetes when a simpler managed runtime satisfies the actual reliability/scale requirements.

## Infrastructure as Code
Use Terraform/OpenTofu, Pulumi, CDK/CloudFormation or repository-native IaC consistently. Understand state, locking, remote state, imports, drift, modules, lifecycle, immutable infrastructure and policy-as-code.

Plan before apply. Do not manually mutate managed resources and then pretend IaC is source of truth.
