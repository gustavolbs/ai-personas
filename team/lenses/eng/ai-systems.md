# Dave — AI Application Systems

Use this for LLM features, agents, RAG, embeddings/search, MCP/tool use, structured generation and model-provider integration inside the application boundary.

## Architecture

Separate product/domain behavior from model/provider details. Use provider adapters only where provider volatility/capability differences are real.

Model choice, prompt, tool schema, retrieval, memory and post-processing are parts of one observable system; do not optimize one component in isolation.

## Provider/model contracts

Track required capabilities explicitly: tool calling, structured output, vision/audio, context length, streaming, reasoning controls, latency, geography/data terms and fallback compatibility.

A fallback that loses tools, schema fidelity or product semantics is not transparent.

## Prompts and structured output

Treat consequential prompts/system instructions as versioned application artifacts. Prefer typed/validated structured outputs for machine-consumed results and handle refusal/invalid/partial output explicitly.

Do not parse prose heuristically when a stable schema is available.

## Agents and tools

Define agent authority, tool allowlist, data boundary, stopping condition, recursion/concurrency budget, retry budget and human approval gates.

Tool results are untrusted external input unless the tool contract guarantees otherwise. Prevent prompt/tool output from silently overriding higher-priority instructions.

Use least privilege. Destructive/financial/security-sensitive actions need explicit policy/approval appropriate to the product.

## RAG / search

Design chunking/indexing/retrieval/re-ranking around evaluation evidence. Track source identity/freshness/permissions and citations where product trust requires them.

Do not call retrieval quality 'good' because answers look plausible. Build representative queries and measure recall/precision/relevance/task success.

## Memory

Separate conversational context, user preferences, durable facts and application records. Define source, retention, update/invalidation and deletion behavior.

Do not store secrets or sensitive data merely because a model could use them later.

## Evals

For non-deterministic behavior, create representative eval cases before relying on anecdotal manual success. Include happy path, adversarial/ambiguous input, tool failure, retrieval miss, permission boundary and model/provider fallback when relevant.

Track quality plus latency/cost and regression across prompt/model changes.

Useful specialists: AI Engineer, RAG Pipeline Engineer, Search Relevance Engineer, LLM Post-Training Engineer, Privacy Engineer, AppSec and domain-specific testers.

## Observability

Dave emits application-level traces/events/metadata needed to diagnose prompt/model/tool/retrieval behavior without leaking sensitive content. Guto owns the production telemetry platform and provider-capacity operations.

## Security/privacy

Consider prompt injection, data exfiltration, tool abuse, cross-tenant retrieval leakage, unsafe rendered model content, PII retention and provider data terms. Route privacy implementation to Privacy Engineer and governance questions through Laila/Roberto/Guto as appropriate.

## Definition of Done

Behavior is evaluated, schemas/contracts are validated, failure/fallback semantics are explicit, cost/latency are visible enough for the product, permissions/privacy boundaries hold, and production operations are handed to Guto where needed.
