# Agent, tools and query gateway

## One agent, bounded control loop

Input is the current message, verified identity scope, sanitized history/state and versioned domain configuration. The agent can respond directly, ask a clarification, call an allowed tool, observe its result and continue. Authentication, budgets and final-output checks are ordinary backend code, not model discretion. Do not expose unrestricted ADK code execution, shell, web browsing or raw MCP toolsets.

Proposed configurable ceilings per run: 6 model turns, 4 tool calls, 2 submitted query jobs including corrections, 1 SQL correction, 60 seconds total wall time, 30 seconds per query, 8,000 input and 2,000 output model tokens per call, 500 result rows, 100 chart points, 256 KiB result payload and 1 GiB maximum bytes billed per job. These are demo design limits, not tested platform guarantees. Enforce cumulative token/query/byte budgets and per-user daily spend reservations across concurrent runs. Configure currency-denominated spend caps from current regional pricing before live work. A LIMIT on rows does not cap scanned bytes. Fail closed if mandatory limits cannot be enforced.

## Tool contracts

All inputs reject unknown keys; dates use ISO dates, timezone uses validated IANA identifiers, dimensions/metrics come from the scoped registry, filter values are bound parameters. Caller identity is injected server-side, never an argument from the agent.

| Tool | Input | Output / constraints |
| --- | --- | --- |
| discover_capabilities | optional permitted domain ID | Scoped metric/dimension IDs, definitions and sanitized verified schema; no global project listing |
| standard_report | report_id plus its closed report-specific input schema (sales periods or catalog filters/paging) | Gateway result envelope; template identifiers server-controlled |
| custom_analysis | closed union: semantic_plan with typed plan, or gated generated_sql with the same plan plus candidate_sql | Canonical compiler by default; generated SQL from the same agent only within the advanced supported subset |
| reuse_result | opaque result_id, presentation enum metric/line/bar/table | Reauthorize ownership, lineage, freshness and completeness; return validated new presentation or needs_query |

The custom tool accepts a typed analysis plan from the single conversational agent, not an end-user SQL endpoint. The default semantic_plan mode compiles that plan deterministically. In the gated generated_sql mode the same agent first uses scoped discovery and then proposes candidate SQL; there is no nested agent/model call inside a tool. Generated SQL remains untrusted. The SQL must match the declared metric/filters as well as the access policy; if the supported validator cannot establish this, reject and offer a supported report. No tool accepts credentials, arbitrary project IDs, URLs or user-controlled job IDs. Unknown metrics/dimensions cause clarification or unsupported, not speculative query construction. Permission denials and budget denials are not retryable SQL errors.

## Shared gateway algorithm

1. Load current policy; validate typed parameters against scoped metric and domain definitions.
2. Resolve a template, compiled semantic plan or gated generated candidate. Bind all values as typed BigQuery parameters. Map identifiers from allowlists, never interpolate user strings.
3. Parse using a pinned GoogleSQL-capable parser. Require exactly one supported read-only query AST. Resolve every table, column, alias, subquery and CTE; reject ambiguity or unsupported syntax. Enforce approved joins and aggregate output semantics. Reject `SELECT *` except a deliberately supported safe aggregate such as COUNT(*).
4. Deny DDL/DML/scripts, EXECUTE IMMEDIATE, exports, arbitrary INFORMATION_SCHEMA, wildcard tables, decorators/time travel, remote/external functions, EXTERNAL_QUERY, routines/table functions, connections, AI/ML calls and any unapproved indirect access. A SELECT prefix or read-only transport alone is insufficient. Allow only explicit approved built-ins and fully resolved source tables.
5. Dry-run the exact validated SQL and parameters in the verified location. Reject errors, unsupported estimates or bytes above policy. Never use a different statement after validation; hash SQL, parameter types/values, policy and domain version into the execution record.
6. Submit with maximum_bytes_billed, deadline, deterministic job identity where supported and server billing project. Reserve cumulative budget first. Poll/page/cancel only the run-owned job. Reauthorize before delivery.
7. Aggregate in the database, bound results, validate output schema and attach lineage/provenance. Persist complete result status; do not send whole source tables to the model.

SQL syntax validation does not establish business correctness: metric/joins/grain checks and known-answer tests are required. If the parser cannot safely support a construct, reject it. Query failure allows one sanitized correction within remaining budgets, re-running all checks; no invented fallback values.

## MCP and client transport decision

Google's BigQuery MCP reference documents read-only execution, result polling/pagination and job cancellation. During integration capture the selected server's actual `tools/list` schemas and verify authentication, location, dry-run, maximum bytes, timeout, idempotency, result completeness and cancellation behavior. Do not assume required controls from a tool name.

Prefer existing MCP metadata/read tools where suitable behind the adapter. If execution does not expose every required job control, use the BigQuery client for dry-run **and execution**, polling and cancellation behind the same gateway. A client dry-run followed by uncontrolled MCP execution is not sufficient. Do not expose the API fallback as a model-callable bypass. If neither route enforces requirements, disable live query execution. Keep server credentials and MCP connections entirely off Android.

## Budget and deadline interpretation

The 60-second run deadline starts at acceptance, includes queue time and stops new analytical work/output when reached; safe terminal status/error delivery and cleanup continue. The 30-second query deadline is an application watchdog plus requested server timeout; BigQuery cancellation is best effort, not a guaranteed wall-clock billing cutoff. Retain reservations for uncertain/running jobs until reconciliation. Do not claim the SDK forcibly stops a remote job at the deadline. See the [BigQuery job configuration reference](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/Job).

Reserve the configured maximum billable bytes (not merely a possibly stale dry-run estimate) and bounded model-token cost before submission, using an atomic tenant/user ledger. A two-job run reserves up to two per-job caps as calls are admitted; rejected/cancelled work cannot release uncertain spend prematurely. Include all model calls, including SQL correction, within the six-turn limit. Four tool calls count agent-visible invocations; backend bounded poll/page operations use the same deadline but are not new agent turns. Configure polling backoff and page ceilings explicitly in P1. Infrastructure and identity/storage costs are outside the per-query cap and require separate budgets; do not promise a hard total cloud bill ceiling.

## A finite semantic compiler before generated SQL

The first complete learning journey uses standard templates and a closed semantic plan supporting approved metrics, dimensions, filters, sort/top-N and two-period category growth with min_orders. Plan fields are version, metric_id, dimension_ids, period(s), timezone, typed filters, comparison_basis, min_orders and approved ordering/limit fields as applicable to the operation. Unknown fields/operations fail. The registry owns joins, status rules, grain and formulas; the model cannot redefine them. The minimum-order threshold is an aggregation constraint, not a raw-row filter.

This provides genuinely custom parameter combinations without requiring a general SQL-verification engine. The plan and resulting SQL pass the same authorization, lineage, dry-run, cost, result and provenance checks. Domain constants are compiled by trusted code; only filter values are bound parameters.

Generated SQL is an advanced learning extension, disabled by default through a server-owned feature policy. Support only an enumerated grammar/operation subset for which the implementation can verify conformance to the declared semantic plan. Reject a candidate that removes status filters, changes the denominator/grain or uses an unauthorized field even if it parses and returns plausible results. Do not claim to prove arbitrary SQL equivalence; if conformance cannot be established, use the canonical compiled plan or return unsupported. This extension cannot bypass the gateway, and is unnecessary for the initial portfolio release. The retained custom SQL lesson teaches its limitations as well as its mechanics.
