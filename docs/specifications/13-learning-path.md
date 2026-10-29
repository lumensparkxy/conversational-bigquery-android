# Step-by-step learning path

For numbered setup/build substeps organized by database, MCP, backend, Android and the remaining components, use the [component setup guide](17-component-setup-guide.md).

This repository is both an implementation specification and a learning project. Learn one boundary at a time: understand the input, build a small piece, observe its output, deliberately break it, then explain why the protection works. These are planned lessons, not existing tutorials or completed application modules.

## How to work through a lesson

1. Read the linked design and explain the concept in your own words before coding.
2. Agree on that lesson's small scope. Use one branch/PR per coherent checkpoint; preserve a working sample as modules are added.
3. Implement only its prerequisites and deliverable. Start with fixtures/fakes before a live service.
4. Run the positive example and the failure experiment. Save sanitized expected/actual results and exact commands in a lesson note under `docs/learning/` when the lesson is implemented.
5. Answer the checkpoint question without relying on copied code. Review the diff, test evidence and remaining limitations before marking the module complete.

A lesson note must include: objective, prerequisite commit/tool versions, concepts, files changed and why, reproducible commands, expected and actual output, failure experiment, troubleshooting, cost/network requirements, and what remains unfinished. Never publish tokens, real account configuration or private logs. Add a validated checkpoint tag only after the module actually works; none exist yet.

## Modules and exercises

| Lesson | Learn / read | Build and demonstrate | Failure experiment / checkpoint | Phase |
| --- | --- | --- | --- | --- |
| L00 Repository and architecture | Git, modules and trust boundaries; [architecture](02-architecture.md) | Draw one request from Android to data and back; run spec validator | Explain why the LLM cannot authorize itself and why MCP is not the agent | P0 |
| L01 Contracts before code | JSON types, HTTP errors, closed schemas; [contracts](06-api-and-contracts.md) | Full valid sample result, request, each event and API schema | Reject an unknown field and a chart referencing a missing column | P1.1 |
| L02 Data and metric reasoning | Grain, joins, denominators, nulls; [metrics](03-data-and-metrics.md) | Materialize synthetic orders/items and independently calculate 190 January sales | Explain why category order counts sum to 3 while total orders is 2 | P1.2 |
| L03 A deterministic API | FastAPI boundaries, fixtures, dependency injection | Start loopback sample service; “Hi,” January sales, and unsupported input | Show zero cloud/model calls and explicit sample labeling | P2.1 first slice |
| L04 Android typed chat | Kotlin, Compose, ViewModel, network state; [UX](01-product-and-ux.md) | Send text over verified local tunnel, render response and loading/error states | Disconnect and rotate; show preserved input without duplicate submission | P2.2 first slice |
| L05 Structured visual answers | Decimal precision, typed blocks, accessibility | Render metric, line/bar chart and accessible table from identical fixtures | Inject bad chart keys and partial data; explain rejection | P2.2 completion |
| L06 Streams and run ownership | SSE, idempotency, retries; [lifecycle](07-state-and-lifecycle.md) | Persist run identity locally; stream status, reconnect and Stop | Duplicate Send/replay; prove one run and one final UI message | P2.1 completion |
| L07 Voice as input | Permission lifecycle and transcription | Record, review/edit transcript, send through the same message path | Deny microphone permission; typed flow still works | P2.3 |
| L08 Identity versus permission | Tokens, server membership, roles; [security](04-auth-and-security.md) | Test policy with synthetic identities, then verified Firebase login when configured | Viewer asks for sales; role string in body cannot grant access | P3.1 |
| L09 Durable conversations | State, leases, cache freshness and revocation | Persist session/run/results, pending clarification, ownership checks | Restart worker and downgrade role; no duplicate job or stale disclosure | P3.2 |
| L10 Discover real data | BigQuery metadata, location, profiling | With authorization, capture sanitized schema/status/currency evidence | Reject unverified mapping and unexpected join cardinality | P4.1 |
| L11 SQL and business meaning | Templates, aggregates, parameter binding | Implement approved reports and compare fixture expected values | Null amount, returned item, misleading order/item join | P4.2 |
| L12 Controlled tools and MCP | AST validation, dry-run, caps, adapter design | Same gateway for template/custom routes; inspect actual MCP schemas | Attempt remote function/unauthorized table/cost overflow; fail closed | P4.3 |
| L13 One conversational agent | Tool loop, observations, budgets, context | Connect scoped tools to one pinned ADK/Gemini agent | Greeting zero jobs; follow-up retains dates; formatting reuses result | P5.1 |
| L14 Integrated live experience | Authenticated Android/API/agent integration | Run authorized analyst and viewer journeys with provenance | Expire token during stream; refresh/replay without a new query | P5.2 |
| L15 Evaluation and operations | Golden tests, adversarial evals, redaction | Execute [test matrix](08-testing-and-operations.md); inspect latency/cost/denials | Inject query/model failure; demonstrate bounded correction | P6.1 |
| L16 Deployment and release | IAM, durable workers, secrets, immutable revisions | Only after authorization, deploy staging and capture real evidence | Roll back or disable querying; explain residual costs and data already seen | P6.2–P7 |

L00–L07 can be developed without paid cloud resources. Tool installation can require downloads; OS speech recognition may need network access. L08–L09 can first be exercised with emulators/fakes, but live-identity acceptance remains pending. L10 onward includes explicitly authorized cloud/model checks; offline fixture tests remain the default throughout. No live credentials are required merely to read or improve the specifications.

## First practical checkpoint

Start with L00/P0.1: inspect the development tools, choose compatible pinned versions, and write the local toolchain decision. Then L01 authors machine-readable contracts and full examples. Do not jump to generated SQL or cloud deployment before the contracts, deterministic sample and policy gates exist.

The phase plan governs dependencies, so a lesson may use a fake implementation until its live dependency is ready. “Lesson completed locally” and “live capability verified” are separate statuses; neither implies release readiness.

## Product and architecture reflection at checkpoints

At L00, read the [product charter](15-product-charter-and-value-validation.md) and explain the difference between a learning project, a valuable business workflow and a proven commercial product. At L11/L12, compare the finite semantic compiler with the generated-SQL extension: identify what each validator can and cannot guarantee. At L15, review an unsupported causal question and a plausible but wrong metric answer; chart validity alone is not a pass.

L13 can initially integrate only templates/semantic plans. Advanced generated SQL is the optional P5.3 extension after that working journey. After L16, discuss [enterprise gates](16-enterprise-readiness.md) as an architecture exercise; do not implement them or collect private data without a separately approved scope. Record one build-versus-buy tradeoff in the portfolio even if the selected demo deliberately builds a component to learn it.
