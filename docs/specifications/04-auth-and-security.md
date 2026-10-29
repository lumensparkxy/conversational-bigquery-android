# Authentication and authorization

## Concrete live identity design

Use Firebase Authentication with Google sign-in on Android as the proposed live identity provider. Backend verifies ID tokens with the Firebase Admin SDK for the configured project, including issuer, audience, expiry, signature and revocation/disabled-user checks. Verify platform details against pinned SDK docs during implementation. A valid login authenticates identity, not data access.

Use a server-owned membership store keyed by verified UID and tenant. It contains role, enabled flag and monotonically increasing policy version. Default deny for absent/unassigned memberships. A privileged operator bootstrap command, run out of band with operator credentials, assigns initial analyst and viewer UIDs; log actor, target, old/new role, reason and time. No self-service role claim, email-domain inference or client role switch. The public API has no role-management endpoint in v1. Client/body/token custom role claims cannot override the current server policy.

Local sample mode uses synthetic identities only, isolated flavor/storage, and a loopback-only fixture server. Live process refuses startup if mock auth, emulator auth host or sample provider is configured. Never fall back to mock auth on verification failure.

## Policy matrix

| Principal | Capabilities | Tables via gateway | Output restrictions |
| --- | --- | --- | --- |
| sales_analyst | catalog.read, sales.aggregate | approved products; orders/order_items/users for aggregate sales | No raw customers or transactional detail; approved columns only |
| catalog_viewer | catalog.read | approved products only | Product metadata/count/list price only; no sales-derived ranking or proxy |
| unassigned/disabled | none | none | Login/help only |

Policy structure supports tenant, capabilities, table IDs, column IDs, optional row-scope reference and policy version. V1 implements and tests capabilities, table scope and static column allowlists. It does **not** claim arbitrary per-user row security. Any nonempty row-scope configuration fails startup/query validation until database-backed row enforcement is implemented and tested. Never append a user filter string to unrestricted SQL. Future private data requires least-privilege database identities, authorized views/row policies and column controls in addition to application enforcement.

## Enforcement sequence for every action

1. Verify token and ownership on every session/run/result/event path; return a generic not-found for another user's resource.
2. Load current enabled membership and policy version before reading history. Rebuild context from permitted messages, summaries and results; never feed denied data or restricted schema into the model.
3. Scope tool names, descriptions, schema and discovery results; a hidden tool is still denied by backend if invoked directly.
4. Recheck capability, table/column lineage, tenant and budgets for every tool call, including formatting/reuse, pagination, metadata and both SQL routes.
5. Recheck before storing or delivering result blocks, and before each persisted-event replay batch. Revocation cancels running work and invalidates caches. Use a policy read/barrier at delivery: do not emit queued results under a stale version. Already displayed data cannot be retracted; clear client caches and stop future disclosure.

History and summaries carry lineage and policy dependencies. Mixed turns with restricted content are omitted entirely on downgrade unless a safe, separately stored permitted fragment exists. User text that repeats earlier restricted results is not a source of authoritative data. Do not hydrate expired result references. Cache keys include tenant, UID, policy version, domain version, normalized parameters and source freshness; no cross-user result caching in v1.

## Attack surfaces

Test prompt injection, role claims in chat/JSON, alternate table spellings, aliases/CTEs, nested queries, direct endpoints, result-ID guessing, pagination cursors, stale streams, generated SQL and API fallback. SQL identifiers are resolved canonically before policy checks. Denial messages do not enumerate hidden tables, columns, account membership or internal SQL. Database text is never trusted as an instruction.

Use TLS, token redaction, encrypted managed storage, server-side credentials and bounded retention. Android stores auth through the identity SDK and excludes sensitive caches from backups. No tokens in URLs, logs, analytics, crash reports or SSE event IDs. App Check/rate limiting may complement authentication but cannot replace it. Verify quotas per UID and tenant to limit abuse.
