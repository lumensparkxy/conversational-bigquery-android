# References and verification boundaries

Official pages reviewed during specification authoring on 2026-10-29:

- [BigQuery public datasets](https://docs.cloud.google.com/bigquery/public-data): public datasets can be queried in place; query charges and access constraints still apply. No pricing allowance is relied upon by this design.
- [BigQuery MCP reference](https://docs.cloud.google.com/bigquery/docs/reference/mcp): documents read-only execution, polling/pagination and job cancellation. Actual selected tool schemas and required cost controls still need integration verification.
- [Running BigQuery queries](https://docs.cloud.google.com/bigquery/docs/running-queries): query-job setup reference; check the pinned client API during implementation.
- [ADK simple LLM agents](https://adk.dev/agents/llm-agents/): agent configuration/tool-calling reference. This specification chooses one agent; it does not claim a tested package/model version.
- [Firebase ID-token verification](https://firebase.google.com/docs/auth/admin/verify-id-tokens): server verification reference. Verify revocation handling and Android integration in the selected SDKs.

Additional implementation reading (not claims of deployed compatibility):

- [Use BigQuery MCP](https://docs.cloud.google.com/bigquery/docs/use-bigquery-mcp)
- [MCP Toolbox pre-built tools](https://docs.cloud.google.com/bigquery/docs/pre-built-tools-with-mcp-toolbox)
- [BigQuery pricing](https://cloud.google.com/bigquery/pricing)
- [ADK MCP integration](https://google.github.io/adk-docs/tools-custom/mcp-tools/)
- [ADK state documentation source](https://github.com/google/adk-docs/blob/main/docs/sessions/state.md)

No authenticated Google Cloud or BigQuery calls were made for this specification. Project identity, permissions, billing, dataset contents/location, model availability, Android builds, runtime tests and deployment remain unverified. Proposed security, budget, metric and lifecycle rules are requirements designed for this application, not guarantees supplied by the referenced frameworks.

## Product and enterprise architecture review sources

Reviewed 2026-10-29. These references support design comparisons, not implementation certification or commercial demand:

| Reference | Relevant evidence / use in this repository |
| --- | --- |
| [Looker Conversational Analytics overview](https://docs.cloud.google.com/looker/docs/conversational-analytics-overview) | Semantic-model-based query composition; compare governed metric handling. |
| [Google Conversational Analytics integration patterns](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/integration-patterns) | Managed/direct/ADK/MCP options; future build-versus-buy evaluation. |
| [Fabric data agent concepts](https://learn.microsoft.com/en-us/fabric/data-science/concept-data-agent) | User-permission-scoped analytical access and documented limitations. |
| [Azure multitenant agent considerations](https://learn.microsoft.com/en-us/azure/architecture/guide/multitenant/considerations/agentic-systems) | Deterministic identity/tenant boundaries across tools and state. |
| [AWS Q topic reviewed answers](https://docs.aws.amazon.com/cli/latest/reference/quicksight/list-topic-reviewed-answers.html) | Existing reviewed-answer capability; quality governance baseline. |
| [AWS Quick row-level security](https://docs.aws.amazon.com/quick/latest/userguide/row-level-security.html) | Dataset permission controls and role-specific behavior; do not confuse sharing with unrestricted access. |
| [AWS generative AI lifecycle](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/generative-ai-lifecycle.html) | Business scoping, success metrics and cost/feasibility assessment. |
| [AWS ongoing agent evaluation](https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentops06-bp02.html) | Continuing quality measurement and human review after deployment. |
| [Google Well-Architected](https://docs.cloud.google.com/architecture/framework) | Security, reliability, performance, operations and cost concerns. |
| [BigQuery row-level security](https://docs.cloud.google.com/bigquery/docs/row-level-security-intro) | Tradeoffs among policies, views and separate data scopes. |
| [Google model data governance](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/zero-data-retention) | Retention/caching conditions; actual model/endpoint settings require verification. |
| [Cloud Tasks limitations](https://docs.cloud.google.com/tasks/docs/common-pitfalls) | Duplicate/delayed delivery; application idempotency remains necessary. |

Study design numbers, value-model inputs, learning load envelopes and proposed product targets in chapters 15–16 are this project's illustrative assumptions, not statistics from these vendors. Private-data requirements require an authorized customer-specific review.
