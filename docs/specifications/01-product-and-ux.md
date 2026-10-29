# Product and Android experience

Primary purpose is learning and portfolio development; commercial fit remains a hypothesis. The [product charter](15-product-charter-and-value-validation.md) defines success and the [enterprise gates](16-enterprise-readiness.md) apply only to a separately approved private-data expansion.

## Goal and scope

A developer demo lets a signed-in user converse about permitted ecommerce data, understand each metric, inspect evidence, and refine a question without restating everything. V1 includes typed chat, push-to-talk transcription, clarification, bounded analysis, metric cards, line/bar charts, tables, cancellation, history, two roles, and local deterministic samples. No ingestion pipeline is needed: query the public dataset in place.

Continuous live voice, speech synthesis, uploads/document retrieval, scheduled reports, exports, arbitrary visualizations, and production private datasets are later work. Documents will need explicit retrieval and citations; text-to-SQL does not search documents.

## User journey

1. Launch into a persistent **Sample data — not live** banner in sample flavor, or verified login in live flavor. Show a concise data/permission explanation.
2. Present an empty chat with role-permitted examples. Analyst: monthly completed-order sales, category ranking, country comparison. Catalog viewer: product category listing and product count. Do not advertise restricted reports.
3. User types or presses the microphone. Request microphone permission only at use; show recording state, Stop, editable transcript and explicit Send. Denial, unavailable recognizer and offline failure preserve typed chat.
4. Submit a single message and show status: thinking, checking data, querying, formatting. Do not expose chain-of-thought, internal SQL errors or hidden schema. Stop remains accessible.
5. Render a validated final answer with source, date range, timezone, filters, metric definition and freshness details. Charts include units, axes and an accessible table alternative. Show sample/live mode on every result detail view.
6. Follow-ups preserve compatible state. “Now only Germany” changes country while retaining metric and dates; it still checks policy and coverage. “Show that as a table” reuses complete authorized data when sufficient. Do not imply Germany or any other country is available before verification.
7. A new session clears analytical context. Logout clears in-memory and on-device private state. Process recreation restores run ID and reconnects instead of resubmitting.

## Clarifications and outcomes

“Hi” gets a greeting and zero database calls. “What is a growth rate?” can be explained without data. “Sales by region” requires a definition of region if not in the configured dimensions. New time-based sales requests without dates ask for dates; no silent all-time scan. Current catalog counts and listings do not require a date range and must not inherit sales-only filters. Relative dates use server-resolved timezone and calendar boundaries shown to the user. No Zurich/Switzerland or currency assumptions based on device locale.

Keep distinct UI states for clarification needed, no data, denied, unsupported, query failed, cancelled, and successful response. A denial can say: “Your account doesn’t have access to sales figures. I can help with the product information available to you.” Offer only permitted alternatives. Never replace failed/no-data results with invented numbers or fixture data in live mode.

## Android implementation requirements

Use Compose, ViewModels, immutable UI state, a repository/network layer and lifecycle-aware event collection. Proposed packages appear in the architecture document. Choose minimum/target SDK, chart library and speech recognizer support during compatibility setup. Use the OS speech service behind an interface; disclose that recognition may use a remote provider, verify availability, and do not retain raw audio by default. Speech recognition is not a second analytics agent.

Support TalkBack labels, dynamic text, sufficient contrast, non-color-only series distinction, keyboard actions, screen rotation, narrow screens and dark theme. Tables scroll with labeled headers. Cards format decimal values without losing precision. Display incomplete-result warnings prominently; partial charts are disallowed. Test microphone interruption, expired auth, network loss, duplicate Send, Stop races, session switching and denied-history retrieval.

## Completion evidence

Record emulator screenshots and interaction tests for both roles and sample mode; verify at least one physical-device speech flow before claiming voice readiness. Sample APKs must not point to a live backend or carry live identities. No live build may expose a role selector or mock-auth toggle.

## Answer inspection and limits

The final learning release includes an answer-details view: metric definition/version, effective filters and dates, source/query timestamps, completeness, sample/live mode and warnings. “Definition reviewed” describes the definition's review status, not a guarantee that every answer is correct. No model-generated confidence percentage or unexplained “trusted” badge.

Keep explanations descriptive. For “why did sales fall?”, offer a supported breakdown that shows which groups changed, distinguish that from a causal explanation, and state when the available data cannot establish cause. Never infer stockouts, campaigns, profit or refunds from fields that do not support them. Do not present a top-N subset as the whole population.

At P6 add a small helpful/not-helpful control with reason codes, linked to the owned run. It submits no message to external services. A reported wrong answer enters an authorized review process; it does not automatically train the model or change definitions. The first sample UI can omit feedback until that lesson. See the feedback contract in specification 06.
