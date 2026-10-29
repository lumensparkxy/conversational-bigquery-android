# Decisions and unresolved configuration

## Settled design direction

Standalone Android demo; public repository; specifications first; one conversational agent; query TheLook in place; typed and push-to-talk share state; capability/table roles enforced server-side; deterministic sample mode before cloud setup; no ingestion or multi-agent services in v1. Kotlin/Compose, Python/FastAPI, Google ADK/Gemini and eventual Cloud Run are recommended defaults, subject to compatibility verification.

## Required inputs before live work

| Decision/configuration | Current state | Owner/action |
| --- | --- | --- |
| Cloud project ID/number | Unknown; only spoken display name supplied privately | Environment owner resolves exact project; do not put private account config in source |
| Billing, APIs, IAM, org constraints | Unverified | Owner authorizes scoped setup and budget |
| Dataset schema/location/coverage/status/currency | Unverified | Implementer captures sanitized contract evidence |
| Model ID/region/version/quotas | Unverified | Verify tool calling, pin and evaluate |
| Android package ID/min SDK/target SDK/signing | Unselected | Choose independently of existing apps |
| Firebase project/provider/audience | Proposed, not configured | Confirm identity project and Google sign-in setup |
| Analyst/viewer test UIDs and operator | Unassigned | Out-of-band trusted bootstrap, no public UIDs needed |
| Store, queue and lease implementation | Firestore proposed; queue unresolved | Validate durable run processing and delivery barriers |
| MCP vs controlled client execution | Pending actual tool schemas | Require all gateway controls; no silent downgrade |
| Budgets/quotas/spend alerts | Proposed ceilings in gateway spec | Set affordable daily/monthly limits and current pricing |
| Timezone/date and currency semantics | Proposed UTC; monetary unit unknown | Verify source semantics and label defaults |
| Retention/privacy/audio provider | Proposed TTLs; OS recognizer default | Confirm policy and user disclosure |
| Licensing | No license selected | Owner decides before open-source licensing |

Nonsecret configuration names to implement: APP_MODE (sample/live), AUTH_MODE (mock/firebase), GOOGLE_CLOUD_PROJECT, BIGQUERY_LOCATION, GEMINI_MODEL_ID, GEMINI_LOCATION, DOMAIN_CONTRACT_VERSION, IDENTITY_PROJECT_ID, QUERY_ADAPTER, MAX_BYTES_BILLED, RUN_DEADLINE_SECONDS, DAILY_SPEND_LIMIT, RESULT_TTL_SECONDS. Store actual environment values outside public source. Secrets use managed references, not example token strings.

Keep decision records with date, choice, alternatives, verification evidence and consequences under a future docs/decisions directory. Any change to metric semantics, permission scope, protocol schema or sample/live separation requires matching test updates. No unresolved configuration authorizes guessing a project or deploying resources.

## Product and enterprise decision status

- Accepted: learning and portfolio first; commercial direction later ([ADR 0001](../decisions/0001-learning-first-scope.md)).
- Proposed default: templates plus a finite semantic compiler; generated SQL remains a gated advanced extension.
- Unvalidated: buyer, recurring workflow, Android/voice preference, willingness to pay, savings, pricing and competitive advantage. See [product validation](15-product-charter-and-value-validation.md).
- Deferred until an approved private pilot: enterprise federation/provisioning, identity-to-warehouse row/column scope, deployment isolation, provider data-processing review, load/SLO/RTO/RPO targets, customer support and procurement requirements.

These deferred commercial decisions do not block local learning. They do block claims that the demo is ready for private enterprise data. Keep actual customer/account details outside public configuration.
