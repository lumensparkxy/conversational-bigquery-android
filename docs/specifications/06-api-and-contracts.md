# API, streaming and result contracts

This is the normative contract design. P1 must translate it into OpenAPI 3.1 and JSON Schema with closed objects, discriminated unions, fixtures and compatibility tests before app code. All endpoints except health require Bearer ID token in live mode. Unknown fields fail validation. Opaque UUID identifiers are never authorization.

## HTTP surface

| Method/path | Request | Response |
| --- | --- | --- |
| POST /v1/sessions | title optional, max 120 chars | 201 session_id, created_at |
| GET /v1/sessions | bounded cursor/limit | Owned session summaries only |
| GET /v1/sessions/{sid} | none | Current authorized history/state |
| DELETE /v1/sessions/{sid} | none | 202 deletion queued; revoke access immediately |
| POST /v1/sessions/{sid}/runs | Idempotency-Key header; message, input_kind | 202 run_id, status, events_url |
| GET /v1/sessions/{sid}/runs/{rid} | none | Current status and authorized final response if present |
| GET /v1/sessions/{sid}/runs/{rid}/events | Last-Event-ID optional | Authenticated SSE |
| POST /v1/sessions/{sid}/runs/{rid}/cancel | empty object | 202 cancelling or 200 existing terminal status |
| GET /v1/results/{result_id} | scoped opaque pagination cursor optional | Authorized typed data and provenance |

`message` is nonempty UTF-8 text, maximum 8,000 characters and 32 KiB request body. `input_kind` is typed or voice_transcript and changes no policy. No role, tenant override, raw SQL or client history is accepted. Server derives tenant and history. One active run per session: conflicting new request returns 409. Rate limit returns 429 with Retry-After; invalid token 401, invalid input 422, invisible resource 404, policy denial on a known action 403. A model-level denied outcome may be a successful completed run with no query. Errors use `{code, message, retryable, request_id}` without internal details.

## SSE envelope and lifecycle

Each persisted event has SSE `id: <run_id>:<monotonic_sequence>`, `event: <type>`, and a JSON `data` object `{schema_version: "1", run_id, sequence, emitted_at, payload}`. Event types: accepted, status, text_delta, response, error, cancelled, done. Status payload uses thinking/checking/querying/formatting; never hidden reasoning. Heartbeat comments every 15 seconds carry no data. Persist before delivery.

Only validated final response text may be chunked as text_delta in v1; buffer analytical narration until grounding checks pass. There is exactly one terminal outcome and one done event with terminal status. Application failures after headers may use error events while the connection is writable. A broken transport cannot guarantee delivery of any event; the client recovers through the run endpoint and replay. Last-Event-ID replays subsequent authorized persisted events; invalid cross-run cursors are rejected. Expired replay retention returns 410 and the client retrieves current run state. Reconnect never reruns the agent.

## Result data and block types

A result envelope contains `schema_version`, `result_id`, `mode` (sample/live), `status` (complete/partial/empty), `columns`, `rows`, `row_count_returned`, `total_row_count` (nullable), `next_cursor` (nullable), `provenance`, `created_at`, `expires_at`. Columns have unique `key`, label, type (string/date/timestamp/decimal/integer/boolean), nullable and optional unit. Decimal and 64-bit integer values use canonical strings in JSON to avoid precision loss; UI converts chart coordinates only after safe range checks. Rows are objects with exactly those keys. Null is distinct from zero.

Final response contains `schema_version`, `run_id`, `outcome`, `text`, `blocks`, `result_refs`, `clarification` (nullable), and `warnings`. Outcomes: answered, clarification_needed, no_data, denied, query_failed, unsupported, cancelled. Non-answered outcomes must not carry fabricated analytical blocks.

| Block discriminant | Required fields | Validation |
| --- | --- | --- |
| metric | id, result_id, label, value_field, row_index, unit | Exactly one existing row/field; value read from result |
| line / bar | id, result_id, title, x_field, y_fields, unit | Existing typed fields; dates ordered for line; finite safe values; at most 100 points; complete result only |
| table | id, result_id, title, fields | Existing fields only; stable sort/cursor, explicit partial/page label |

No arbitrary HTML, formulas, URLs or executable chart specs. The server resolves numeric values from result references, not model guesses. Check any numeric claims in narrative against result cells/approved derived calculations; if grounding fails, use deterministic result-based text or return a formatting error. Do not let narrative bypass the structured-block validator.

Provenance includes domain and metric versions, public source table identifiers only if permitted, date basis, start/end/timezone, effective filters, status rules, currency or unverified-unit flag, data queried_at, available source modification time (nullable), completeness, cache/reuse status and query fingerprint. Server audit stores billing job IDs, bytes and validated SQL references; do not expose privileged job details by default. Never equate queried_at with source freshness.

## Synthetic example (contract shape, not live evidence)

```json
{
  "schema_version": "1",
  "run_id": "synthetic-run",
  "outcome": "answered",
  "text": "Sample completed-item sales total 150 demo units.",
  "blocks": [{"type":"metric","id":"m1","result_id":"synthetic-result","label":"Completed-item sales","value_field":"sales","row_index":0,"unit":"demo_unit"}],
  "result_refs": ["synthetic-result"],
  "clarification": null,
  "warnings": ["Synthetic sample; not a live query."]
}
```

Synthetic result row is `{"sales":"150.00"}` with a decimal column and mode sample. IDs here are illustrative; production ID schema requires UUIDs. P1 must produce full schema-valid examples including provenance rather than treating this abbreviated example as a golden payload.

Pagination does not imply analytical completeness. Full aggregate series must fit the bounded result or be reaggregated; fetching only page one must never render a complete-looking chart. Reuse requires a complete sufficient result with current authorization and unexpired freshness policy. A different grouping/filter needing missing rows returns needs_query.

## Protocol decisions required for consistent clients

A completed run has outcome answered, clarification_needed, no_data, denied or unsupported. Execution/validation exhaustion uses failed with query_failed and a safe error code (including MODEL_FAILED or FORMAT_FAILED); cancellation uses cancelled. The broad query_failed outcome covers execution failures in v1, not just SQL errors. Acceptance can fail asynchronously before a worker starts, so accepted may transition directly to failed.

Persist terminal response/error/cancelled plus done atomically with terminal run state. Replay is at-least-once delivery: clients deduplicate by run_id/sequence. Replayed terminal events are not additional terminal transitions. A response contains canonical full text; if text_delta was displayed, replace that draft with response.text rather than appending it. A deleted or newly unauthorized run may no longer replay historical success events.

At most 500 rows and 256 KiB are materialized per result across all pages, not per page. Proposed table page size is 50 rows, maximum 100. `status` describes the whole stored bounded result; paging a complete stored result does not make it partial. Include page start offset and returned count; `total_row_count` is null if unknown. Opaque authenticated cursors bind result ID, owner, tenant, policy version, sort order, offset and expiry; do not accept caller-controlled offsets. Immutable stored rows provide stable pagination. Exceeding the total bound produces partial with a warning or requests narrower scope, never an unbounded paging loophole. Metric blocks cannot reference partial aggregates.

Clarification payload is `{question, missing_fields, choices}` with choices an optional bounded array of text labels. Keep the pending intent server-side; the next normal message resolves it. Result provenance fields not applicable to catalog requests (dates, timezone, status rules) are explicitly null, not fabricated. Tables and scalar count results can therefore represent catalog-only questions.

P1 must define payload schemas for every event, timestamps as RFC 3339 UTC, UUID resource IDs, sequence as positive integer, stable error-code enum, default/max page limits, cursor expiry and all report-specific input variants. No implementation phase may mark P1 complete with this prose alone: schema-valid full examples and rejection tests are mandatory.
