# Setup and deployment guidance

For numbered setup/build substeps organized by database, MCP, backend, Android and the remaining components, use the [component setup guide](17-component-setup-guide.md).

## Today: specifications only

Clone the public repository and run `python3 scripts/validate_specs.py`. There is no Gradle wrapper, backend executable, fixture server, Docker image or deployed URL yet. Do not substitute guessed application commands or represent this check as application testing.

## Implementation setup sequence

1. Complete P0 decisions. Pin a mutually compatible Python, ADK, FastAPI, BigQuery client, SQL parser and identity SDK set using a lockfile; pin Android Gradle Plugin/Gradle/JDK/Kotlin/Compose and Android SDK levels. Verify APIs against installed packages and current official docs; avoid floating model/library aliases for reproducibility.
2. Write contracts and fixtures, then implement the isolated sample flavor/provider. Document exact install/start/build/test commands and run them from a clean checkout. Keep sample CI network-independent where feasible.
3. Resolve the intended Google Cloud project's exact ID/number privately from its display name and confirm owner authorization. Verify billing, IAM, organization policies, region, source dataset location, Gemini tool-calling availability, identity configuration and required APIs. No API enablement or IAM grant was performed by this repository bootstrap.
4. Use local Application Default Credentials for authorized developer testing; deployed workloads use attached service identity/workload identity. Avoid downloaded long-lived service account keys. Put operational secrets in a managed secret store and local config outside tracked source.
5. Inspect source schema with bounded queries, freeze reviewed domain mappings and validate semantics. Inspect actual MCP schemas and choose the compliant adapter route. Pin model ID/location and evaluation settings after an actual compatibility check.
6. Configure Firebase Google sign-in, Android package/signing fingerprints and token audience. Bootstrap two separate test UIDs through the server-only operator process. Confirm an unassigned third UID is denied. Identity configuration and role storage are separate from chat input.
7. Run all fixture/security/contract tests before explicit paid live verification. Live tests record dynamic data evidence rather than pretending fixture expectations match live tables.

## Proposed live topology (not provisioned)

Cloud Run API/worker, server-only Firestore persistence, managed secrets, Cloud Logging/Monitoring and a dedicated query execution identity. Source tables stay in the public project; jobs bill to the verified execution project. BigQuery job location must match the source dataset. Model/Cloud Run regions and data residency are explicit decisions, not inferred from the user's timezone.

If Cloud Run accepts external Firebase-authenticated clients, the network ingress may need to reach application auth without Cloud Run IAM bearer auth. Document that boundary explicitly: application middleware verifies every API request; a network-reachable service is not an anonymous data API. Health responses contain no sensitive configuration. Restrict Firestore client rules; only backend identity accesses memberships, runs and results. Define minimum IAM from actual adapter/API requirements; never grant Owner/Editor to the runtime as a shortcut.

Worker execution must continue independently of a client SSE connection. Select a durable queue/worker mechanism and reconcile leases, or explicitly configure an execution model that guarantees accepted-run processing through restarts. Do not rely on an untracked background coroutine after a request ends. Queue selection and IAM belong in P3/P6 decisions.

## Deployment checklist and rollback

- Review generated infrastructure plan, service identity permissions, costs, retention, network exposure and database rules; no secrets in plan artifacts.
- Build immutable images with pinned dependencies; scan dependencies/images. Use workload identity for CI, protected environment approval for paid live deployment, and no public-cloud secrets in PR tests.
- Fail startup on missing limits, unknown environment/model/domain, mock auth in live mode, unsupported row policy or incomplete adapter controls.
- Stage traffic on a verified revision; test login, both roles, unauthenticated denial, query controls, reconnect, Stop, revocation and costs.
- Capture revision/image digest, sanitized configuration version and live test evidence. Roll back to the last verified revision or disable query execution on correctness/security failure. A rollback does not undo queries already billed or disclosures already made.
- Keep secret rotation, role revocation, budget exhaustion and schema drift runbooks. Budget alerts alone are not hard execution limits.

## Secret exclusion

Never commit `.env`, service account JSON, ADC files, tokens, Firebase account configuration, Android signing keys, local.properties, recordings, real user history, raw query outputs or cloud state files. Public examples use placeholders only. Review staged files and run secret detection before each publication. The initial `.gitignore` is defense in depth, not proof that arbitrary file content is safe.

## Local Android connection plan

Keep the sample server bound to the development host's loopback interface. During implementation document and verify an adb reverse tunnel for the chosen port so emulator or USB-connected device can reach it through its own localhost. Do not bind a mock-auth server to a public/LAN interface to make the sample work. If debug HTTP is needed, scope its network-security allowance to the sample/debug build and local address; live builds require TLS. Confirm the actual tunnel/build commands in the Android lesson rather than publishing an untested quickstart here.

## Release claims and enterprise boundary

A successful P6/P7 deployment is a verified public-data demo only. Before connecting private data, follow [enterprise gates E01–E08](16-enterprise-readiness.md), including a real identity-to-database access design and provider/region/retention review. SSO, isolation, audit evidence and an applicable support agreement must be evaluated for the specific customer; choosing managed cloud services does not provide these automatically to this application.

For the learning deployment, record and test the durable dispatch decision, per-instance versus distributed quota handling, bounded queue behavior, timeout reconciliation and worker authentication. A worker callback uses workload identity; it is not an extra unauthenticated public API. No queue/service is selected or provisioned by this documentation review.
