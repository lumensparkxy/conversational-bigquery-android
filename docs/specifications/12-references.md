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
