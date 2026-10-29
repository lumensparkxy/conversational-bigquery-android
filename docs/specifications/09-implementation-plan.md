# Phased implementation plan

No task below is marked implemented. Work in dependency order; each phase should be a reviewable commit/PR with requirements, tests and recorded limitations. Do not treat this plan as permission to create paid resources.

| Phase/task | Dependencies | Implementation deliverable | Acceptance evidence |
| --- | --- | --- | --- |
| P0.1 Compatibility decisions | none | Record Android SDK/JDK/Kotlin/Compose, Python/ADK/FastAPI, model interface and libraries; dependency lock strategy | Clean documented toolchain install; compatible minimal experiments kept separate from claimed app |
| P0.2 Environment decisions | none | Record defaults privately; distinguish local choices from deferred live configuration | Sample work unblocked; live project/IAM/model values may remain explicitly unresolved until needed |
| P1.1 Contracts | P0.1 | OpenAPI, JSON Schemas for events/results/tools/domain; complete synthetic examples | Positive/negative contract tests; no open-ended model UI |
| P1.2 Fixtures | P1.1 | Logical source fixtures, expected aggregates, scripted model/tool observations | Exact expected values from testing spec |
| P2.1 Sample backend | P1 | Deterministic scripted response provider, mock identity, session/run/SSE lifecycle | Runs on loopback with no cloud/model credentials; conspicuous sample mode; cancellation/reconnect tests |
| P2.2 Sample Android | P2.1 | Compose chat, cards/charts/tables, sample flavor, accessibility | Installable sample APK; typed input and deterministic follow-ups; instructions tested from clean checkout |
| P2.3 Voice | P2.2 | Push-to-talk transcript/review/send using same chat path | Permission/offline tests and physical-device evidence |
| P3.1 Live identity/policy | P1, P0.2 | Verified Firebase identity, server membership/bootstrap, deny-by-default policy | Both-role, forged claim, ownership and revocation tests; no live mock switch |
| P3.2 Durable lifecycle | P2.1, P3.1 | Persistent runs/results/events, leases/reconciler, retention | Restart/idempotency/cancel-race tests; no duplicate jobs in fake adapter |
| P4.1 Data inspection | P0.2, authorized cloud access | Bounded metadata/profile report; verified mappings, location, currencies/statuses | Reviewed sanitized snapshot and quality results; unverified metrics disabled |
| P4.2 Domain metrics | P4.1, P1.2 | Versioned semantic registry/templates and lineage | Independent SQL review and fixture known-answer checks |
| P4.3 Query gateway | P3, P4.2 | AST policy, dry-run, job caps, shared adapter and scoped metadata | Security matrix passes for template/generated/MCP/API routes |
| P5.1 Agent | P4.3 | One bounded ADK agent, scoped tools/context, model configuration | Small talk zero jobs, clarifications, multi-turn/reuse, failure budgets and grounded output evaluations |
| P5.2 Live Android integration | P5.1, P2.3 | Live login, authenticated stream, history and revocation handling | End-to-end two-role evidence, malformed/partial data rejection, logout cleanup |
| P6.1 Operations | P5 | Redacted metrics/audit, budget alerts, runbooks, secret scan | No credentials in source/log fixtures; retention/cancellation and incident drill |
| P6.2 Opt-in cloud validation | P6.1, environment authorization | Least-privilege staged deployment and explicit paid live tests | Actual revision/config, live correctness, spend and access evidence |
| P7 Release readiness | P6.2 | Updated README/setup, supported versions, license decision, demo recording | Reproducible sample and live setup; security gates pass; no unsupported claims |

For P2, publish exact local commands only after the implementation exists and they are tested. Expected future workflow: install pinned backend dependencies, start sample server on loopback, build/install sample Android flavor, select one of two synthetic roles, run documented fixture conversations. Sample mode must work without Google Cloud, Firebase, Gemini or MCP accounts and must not claim arbitrary questions are live analytics. Unknown scripted inputs return a sample-mode limitation.

Before P5, keep custom SQL behind a disabled feature flag until P4 gateway and bypass tests pass. Before P6, review infrastructure changes and estimated costs with the environment owner. Completion means acceptance evidence exists, not that a folder or TODO was added.

## Learning-sized checkpoints

Use the [learning path](13-learning-path.md) to divide these phases into individual lessons. P0.2 does not require paid setup before sample work. Implement policy logic with synthetic verified principals before connecting Firebase; add the live verifier only when identity configuration is authorized. Synthetic metric fixtures likewise precede live data discovery; P4.1 validates their mapping to actual source data. Each module should end with a small working demonstration, a failure case and a learner explanation before moving on.
