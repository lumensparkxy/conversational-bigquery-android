# Implementation specification index

Status: proposed implementation contract, authored 2026-10-29. No application implementation or live dataset verification has occurred. MUST denotes an acceptance requirement; defaults are explicit proposed choices that may be changed through a recorded decision and updated tests.

Read in order, then work from the task plan:

1. [Product and Android experience](01-product-and-ux.md)
2. [Architecture, boundaries and source tree](02-architecture.md)
3. [Data contract and metric semantics](03-data-and-metrics.md)
4. [Authentication and authorization](04-auth-and-security.md)
5. [Agent, tools and query controls](05-agent-and-query-gateway.md)
6. [HTTP, streaming and result contracts](06-api-and-contracts.md)
7. [Session state, storage and cancellation](07-state-and-lifecycle.md)
8. [Tests, evaluations and observability](08-testing-and-operations.md)
9. [Phased implementation tasks](09-implementation-plan.md)
10. [Setup, dependency pinning and deployment](10-setup-and-deployment.md)
11. [Decisions and unresolved configuration](11-decisions-and-configuration.md)
12. [Authoritative references and verification boundaries](12-references.md)

13. [Step-by-step learning path](13-learning-path.md)
14. [Requirements and acceptance map](14-requirements-traceability.md)

See the [specification audit](../reviews/2026-10-29-specification-audit.md) for corrections and known limits.

Precedence: security and ownership constraints apply to every route. A convenience sample, diagram or default cannot override them. If a required platform capability is unavailable, fail closed, record a decision and revise the design; do not silently remove the control. Update contracts and acceptance cases together when behavior changes.
