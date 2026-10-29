# Specification audit — 2026-10-29

## Scope and baseline

Reviewed the root README, all 12 original specification chapters, folder placeholders and validator at commit `9df1e4b`. Local HEAD matched origin/main, repository visibility was public, and the working tree was clean. No interrupted commit or partial push was found. Reviewed documentation only; no application or cloud resource was created or tested.

## Findings corrected

| Finding | Correction |
| --- | --- |
| Implementation phases did not provide a learning curriculum | Added lesson objectives, exercises, failure experiments, checkpoints and traceability |
| Catalog questions had no clear report route and blanket date requirement | Added catalog report IDs, report-specific schemas, date-free catalog semantics and T22 |
| Equal-length growth periods conflicted with January/February fixtures | Distinguished calendar-period totals from equal-day custom comparisons and added T23 |
| Ignoring null sale amounts could understate sales and average | Null affected monetary aggregates, preserve valid order counts; concrete T24 expectation |
| Custom SQL generation could imply a hidden second agent | Same conversational agent supplies internal candidate SQL through the controlled tool |
| Timeout wording could imply guaranteed remote cancellation | Explicit application deadline, best-effort remote stop and retained spend reservations |
| SSE transport/terminal behavior was incomplete | Disconnect recovery, deduplication, atomic finalization and accepted-to-failed transition |
| Pagination bounds could be interpreted per page | Whole-result limits, cursor binding, immutable page order and T26 |
| Pending clarification/freshness/revocation races were underspecified | Separate pending intent, historical retention and reuse freshness; emission authorization boundary |
| Default token verification could miss revocation | Explicit revocation option and token-expiry/reconnect behavior |
| Loopback sample server lacked a device connection plan | Require a verified local adb tunnel; no publicly exposed mock-auth service |
| Validator hard-coded chapter count without index/number checks | Validate sequential chapter IDs, index coverage and fenced JSON examples |

The BigQuery job configuration reference explicitly describes timeout cancellation as best effort, and Firebase notes ordinary ID-token verification does not check revocation. Sources are linked in the affected specifications. These are design corrections; their runtime enforcement still needs implementation tests.

## Boundaries and residual work

No application tests have run because the application does not exist. Dataset schema/location/statuses/currency, Google project IAM/billing, model availability, exact package versions, durable queue choice and live Firebase configuration remain intentionally unresolved. OpenAPI and JSON Schemas are P1 deliverables. Licensing remains an owner decision. The next safe learning step is L00/P0.1 followed by L01/P1.1; no paid setup is required for those steps.

Validation evidence is the commit's successful specification validator, diff whitespace check and anonymous comparison of tracked files against the published commit. This is a review of internal consistency and coverage, not a proof of production safety.
