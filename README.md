# Conversational BigQuery Android

**Specification-only repository. No Android application, backend, runnable sample mode, or cloud deployment exists yet.**

Build an Android chat experience that answers ecommerce questions using one conversational agent and controlled access to `bigquery-public-data.thelook_ecommerce`. Typed messages and push-to-talk transcripts share the same conversation. Answers combine explanations, metric cards, charts, tables, and traceable business definitions.

TheLook is fictitious public ecommerce data. This demo's access controls demonstrate application authorization; they do not make that public dataset private. Dataset schema, coverage, currency, and location require inspection before live implementation.

## Start here

Read the [specification index](docs/specifications/README.md), then execute the [phased implementation plan](docs/specifications/09-implementation-plan.md). Each phase has dependencies and evidence required for completion. The documents are self-contained and distinguish design requirements from verified runtime behavior.

- Default design: Kotlin/Jetpack Compose, Python/FastAPI, Google ADK with one configurable Gemini tool-calling agent, eventual Cloud Run hosting.
- Sales analysts may use approved sales and product capabilities. Catalog viewers may use approved product capabilities only. Unassigned users have no data access.
- A deterministic, clearly labeled sample-response mode is the first implementation milestone, before paid cloud work.
- MCP is a server-side tool protocol. Backend policy and job controls remain mandatory regardless of adapter transport.

## Repository map

| Path | Purpose |
| --- | --- |
| [docs/specifications](docs/specifications/README.md) | Canonical requirements, contracts, security, tests, setup, tasks |
| [android](android/README.md) | Planned Android modules and rendering responsibilities |
| [backend](backend/README.md) | Planned API, agent, policy, query and persistence modules |
| [contracts](contracts/README.md) | Contract authoring and compatibility plan |
| [infra](infra/README.md) | Future environment/deployment definitions |
| [tests](tests/README.md) | Fixture, security, evaluation and live verification plan |
| [scripts](scripts/README.md) | Specification validation only |

## What works today

With Python 3 installed, run `python3 scripts/validate_specs.py` from this directory. It checks required documents, local file links, planned folder markers, and accidental credential-file names. It does **not** compile an app, run application tests, validate external links, or prove security or cloud readiness. There are no install/build/deploy commands for an application yet.

## Configuration and publication

No real project identifier, account configuration, token, service account key, or Android signing material belongs here. The intended Google Cloud project was identified only by a spoken display name; exact identity and permissions remain unverified. Resolve the [configuration checklist](docs/specifications/11-decisions-and-configuration.md) privately before live work. Do not enable APIs, change IAM, or deploy merely by following the documentation without the appropriate environment owner's authorization.

## Licensing

No license has been selected or granted by this repository. Public visibility is not an open-source license. Choose licensing before distributing an open-source release; also review third-party code, dataset terms, and attribution requirements.
