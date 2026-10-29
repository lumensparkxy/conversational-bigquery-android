# Requirements and acceptance map

This map connects product intent to design ownership, implementation phase and evidence. All application acceptance cases are **planned/unexecuted**. The specification validator checks structure only; it cannot certify security or runtime behavior.

| Requirement | Owning specification | Phase | Acceptance cases/evidence |
| --- | --- | --- | --- |
| Typed chat, voice transcript and accessible blocks | [UX](01-product-and-ux.md) | P2 | T12, T19; physical voice demonstration |
| Sample mode before cloud; no silent fixture fallback | [setup](10-setup-and-deployment.md) | P2 | T16, T18; clean offline sample startup |
| One bounded conversational agent; small talk no query | [agent](05-agent-and-query-gateway.md) | P5.1 | T01, T02, T16 |
| Follow-up state, clarification and result reuse | [state](07-state-and-lifecycle.md) | P3/P5 | T03, T04, T28 |
| Verified data and business semantics | [metrics](03-data-and-metrics.md) | P4.1/P4.2 | T05, T20, T23, T24; source inspection |
| Analyst and catalog viewer, default deny | [security](04-auth-and-security.md) | P3.1 | T06, T09, T22 |
| Ownership, scoped history/cache/schema, revocation | [security](04-auth-and-security.md) | P3/P5 | T10, T11, T21, T25 |
| Shared template/generated SQL and adapter controls | [gateway](05-agent-and-query-gateway.md) | P4.3 | T07, T08, T16, T17 |
| Typed grounded output, provenance and completeness | [contracts](06-api-and-contracts.md) | P1/P5 | T12, T13, T26 |
| Idempotency, persistence, Stop, replay and failure | [state](07-state-and-lifecycle.md) | P3.2 | T14, T15, T27, T29 |
| Redacted audit, budgets and evaluations | [operations](08-testing-and-operations.md) | P6.1 | T16, T29; audit/redaction review |
| Reproducible setup, reviewed deployment and no secrets | [setup](10-setup-and-deployment.md) | P0/P6/P7 | Clean checkout, staged deployment/rollback evidence |
| Unverified inputs and licensing remain explicit | [decisions](11-decisions-and-configuration.md) | Before relevant live phase/P7 | Reviewed decision records; no guessed account values |
| Learning objectives, exercises and checkpoints | [learning path](13-learning-path.md) | Every phase | Per-lesson reproducible note and learner review |

## Definition of done for a module

Record the phase and requirement rows covered, tests actually executed, sanitized outputs, remaining risks and status (planned / local verified / live verified). Update this map if scope changes. Add links to implemented tests/evidence when they exist; do not fill the map with nonexistent paths. Security, semantic and lifecycle requirements cannot be waived merely because a demonstration looked correct.

## Intentionally unfinished design artifacts

P1 still owes machine-readable OpenAPI/JSON Schemas and complete examples; P0 owes pinned toolchain decisions; P4.1 owes verified live schema mappings. These were intentionally deferred implementation deliverables, not missing files caused by interrupted repository creation. The specifications are sufficient to start P0/P1, but they are not a claim that every live implementation decision is settled.

## Product/architecture review additions

| Requirement | Owning specification | Phase/gate | Evidence |
| --- | --- | --- | --- |
| Learning first; commercial claims remain hypotheses | [product charter](15-product-charter-and-value-validation.md) | P0/P7 | ADR 0001; reproducible lessons; no invented adoption/ROI claims |
| Finite semantic plan before optional generated SQL | [gateway](05-agent-and-query-gateway.md) | P4.3/P5.3 | T31, T32; disabled-route and semantic mismatch tests |
| Descriptive answers, inspectable definitions and correction loop | [UX](01-product-and-ux.md), [evals](08-testing-and-operations.md) | P5/P6 | T30, T35, T36; held-out review |
| Concurrent isolation and durable dispatch recovery | [state](07-state-and-lifecycle.md) | P3/P6 | T33, T34; workload/failure evidence |
| Private-data adoption requires identity/data/operating approval | [enterprise gates](16-enterprise-readiness.md) | Future E01–E09 | Customer-specific admission evidence; no gates passed today |

Enterprise gates are conditional future requirements and do not change the current repository into an enterprise implementation project.
