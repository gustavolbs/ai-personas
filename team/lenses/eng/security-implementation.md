# Dave — Security-by-Default Implementation

Use the compact checklist on every change. Run the full specialist lane only
when the change touches a trust boundary or another HIGH_RISK boundary.

## Threat boundary first

Before coding, identify:

- actors, assets, trust boundaries and attacker-controlled inputs;
- authentication, authorization and tenant/resource ownership rules;
- secrets, personal data, financial data and security-sensitive logs;
- external calls, webhooks, file paths, uploads, parsers, templates and tools;
- abuse cases, rate limits, replay/idempotency and failure behavior.

Write security acceptance criteria beside functional criteria. Do not let a
model prompt or client-side check stand in for a server-side permission.

## Secure implementation gate

Check the applicable OWASP ASVS 5.0 and NIST SSDF 1.1 areas:

- validate and canonicalize input once at the trust boundary;
- use parameterized queries and context-appropriate output encoding;
- enforce authorization server-side on every protected operation;
- use safe session/token/cookie/CSRF handling and prevent IDOR;
- protect secrets and PII from source, logs, prompts and error responses;
- constrain uploads, paths, redirects, SSRF, command execution and
  deserialization;
- validate webhook signatures, replay windows, idempotency and state transitions;
- use safe defaults, explicit allowlists, bounded resource use and rate limits;
- preserve secure headers, transport settings, dependency integrity and audit
  events without logging credentials or sensitive payloads;
- handle errors without leaking internals and fail closed at security boundaries.

For AI/MCP changes additionally review prompt injection, tool authority,
untrusted tool results, data exfiltration, cross-tenant retrieval, unsafe
rendering and provider data/retention terms.

## Specialist trigger

Dave must delegate a read-only Application Security review when any of these
change: authn/authz, roles/permissions, tenant isolation, secrets, PII,
payments, file handling, webhooks, command execution, SQL/query construction,
deserialization, public API contracts, AI tools/RAG, security headers or
production configuration. A normal UI-only change still receives the compact
security checklist but does not need a separate security child.

The security child returns findings only; Dave owns fixes and re-checks.
