# Agent, tools and query gateway

## One agent, bounded control loop

Input is the current message, verified identity scope, sanitized history/state and versioned domain configuration. The agent can respond directly, ask a clarification, call an allowed tool, observe its result and continue. Authentication, budgets and final-output checks are ordinary backend code, not model discretion. Do not expose unrestricted ADK code execution, shell, web browsing or raw MCP toolsets.

Proposed configurable ceilings per run: 6 model turns, 4 tool calls, 2 submitted query jobs including corrections, 1 SQL correction, 60 seconds total wall time, 30 seconds per query, 8,000 input and 2,000 output model tokens per call, 500 result rows, 100 chart points, 256 KiB result payload and 1 GiB maximum bytes billed per job. These are demo design limits, not tested platform guarantees. Enforce cumulative token/query/byte budgets and per-user daily spend reservations across concurrent runs. Configure currency-denominated spend caps from current regional pricing before live work. A LIMIT on rows does not cap scanned bytes. Fail closed if mandatory limits cannot be enforced.

## Tool contracts

All inputs reject unknown keys; dates use ISO dates, timezone uses validated IANA identifiers, dimensions/metrics come from the scoped registry, filter values are bound parameters. Caller identity is injected server-side, never an argument from the agent.

| Tool | Input | Output / constraints |
| --- | --- | --- |
| discover_capabilities | optional permitted domain ID | Scoped metric/dimension IDs, definitions and sanitized verified schema; no global project listing |
| standard_report | report_id, metric_id, start, end, timezone, dimensions, typed filters, top_n | Gateway result envelope; template identifiers server-controlled |
| custom_analysis | analysis intent, metric_id, explicit period(s), dimensions, typed filters, min_orders | Inspect permitted metadata; generate candidate SQL internally; gateway validates before execution |
| reuse_result | opaque result_id, presentation enum metric/line/bar/table | Reauthorize ownership, lineage, freshness and completeness; return validated new presentation or needs_query |

The custom tool accepts a structured intent from the agent, not an end-user SQL endpoint. Internal generated SQL remains untrusted. No tool accepts credentials, arbitrary project IDs, URLs or user-controlled job IDs. Unknown metrics/dimensions cause clarification or unsupported, not speculative query construction. Permission denials and budget denials are not retryable SQL errors.

## Shared gateway algorithm

1. Load current policy; validate typed parameters against scoped metric and domain definitions.
2. Resolve a template or generated candidate. Bind all values as typed BigQuery parameters. Map identifiers from allowlists, never interpolate user strings.
3. Parse using a pinned GoogleSQL-capable parser. Require exactly one supported read-only query AST. Resolve every table, column, alias, subquery and CTE; reject ambiguity or unsupported syntax. Enforce approved joins and aggregate output semantics. Reject `SELECT *` except a deliberately supported safe aggregate such as COUNT(*).
4. Deny DDL/DML/scripts, EXECUTE IMMEDIATE, exports, arbitrary INFORMATION_SCHEMA, wildcard tables, decorators/time travel, remote/external functions, EXTERNAL_QUERY, routines/table functions, connections, AI/ML calls and any unapproved indirect access. A SELECT prefix or read-only transport alone is insufficient. Allow only explicit approved built-ins and fully resolved source tables.
5. Dry-run the exact validated SQL and parameters in the verified location. Reject errors, unsupported estimates or bytes above policy. Never use a different statement after validation; hash SQL, parameter types/values, policy and domain version into the execution record.
6. Submit with maximum_bytes_billed, deadline, deterministic job identity where supported and server billing project. Reserve cumulative budget first. Poll/page/cancel only the run-owned job. Reauthorize before delivery.
7. Aggregate in the database, bound results, validate output schema and attach lineage/provenance. Persist complete result status; do not send whole source tables to the model.

SQL syntax validation does not establish business correctness: metric/joins/grain checks and known-answer tests are required. If the parser cannot safely support a construct, reject it. Query failure allows one sanitized correction within remaining budgets, re-running all checks; no invented fallback values.

## MCP and client transport decision

Google's BigQuery MCP reference documents read-only execution, result polling/pagination and job cancellation. During integration capture the selected server's actual `tools/list` schemas and verify authentication, location, dry-run, maximum bytes, timeout, idempotency, result completeness and cancellation behavior. Do not assume required controls from a tool name.

Prefer existing MCP metadata/read tools where suitable behind the adapter. If execution does not expose every required job control, use the BigQuery client for dry-run **and execution**, polling and cancellation behind the same gateway. A client dry-run followed by uncontrolled MCP execution is not sufficient. Do not expose the API fallback as a model-callable bypass. If neither route enforces requirements, disable live query execution. Keep server credentials and MCP connections entirely off Android.
