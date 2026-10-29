# ADR 0001: Learning and portfolio first

Status: accepted scope direction. Date: 2026-10-29.

The owner selected a learning and portfolio project first, with commercial direction later. This decision governs the product/architecture review and implementation sequencing.

## Decision

Continue the independent Android conversational analytics demo with synthetic fixtures and TheLook public data. Teach the request-to-answer path, semantic correctness, tool boundaries, authentication, authorization, streaming, evaluation and operations through reviewable modules. Do not turn the first build into a multi-cloud enterprise platform.

Enterprise requirements are documented as conditional future admission gates, not implemented features or extra prerequisites for local lessons. A future private-data pilot requires a new scoped decision and evidence; the demo's release gate does not authorize it. Android is the selected learning surface, not proof that an Android-only commercial product fits buyers.

## Consequences

- Keep one backend and one conversational agent; avoid microservice and multi-agent expansion for its own sake.
- Deliver a small complete journey before advanced generated SQL. Retain generated SQL as a later, explicitly gated learning module.
- Record architecture tradeoffs, failures, tests and reproducibility as portfolio evidence. Do not claim revenue, customers, enterprise readiness or compliance without evidence.
- Prefer existing governed analytics capabilities in a future customer evaluation if they already solve the problem. Building the demo remains valuable as education even when buying is the better commercial choice.
- Customer interviews, pricing and private-data integration remain optional future work. No outreach, deployment or cloud/account changes are authorized by this decision.

See the [product charter](../specifications/15-product-charter-and-value-validation.md) and [enterprise gates](../specifications/16-enterprise-readiness.md).
