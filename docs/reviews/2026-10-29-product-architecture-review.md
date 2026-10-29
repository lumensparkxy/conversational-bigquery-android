# Product, architecture and engineering review — 2026-10-29

Baseline reviewed: commit `5858c3d`, with local and remote main matching. Scope: all 14 baseline specifications and the learning sequence; compared against the official sources linked below and in [references](../specifications/12-references.md). No customer interviews, cloud account inspection, private datasets, application tests or competitive product trials were performed.

## Verdict

**Fits the learning/portfolio purpose, with changes incorporated. Commercial value remains unvalidated. Not ready for enterprise private-data use.**

The use case is a useful teaching vehicle because it connects Android UI/voice, APIs, agent orchestration, tool execution, SQL, data semantics, security, state, evaluation and cloud operations. The original design already includes important controls: one bounded agent, a shared query gateway, scoped history/results, two roles, explicit metrics and deterministic fixtures.

The specification is not evidence of a million-dollar opportunity. Conversational analytics is an established product category, so the commercial question is which particular workflow this implementation improves enough to justify adopting another product. Enterprise software purchases require both a business sponsor and operational/security acceptance. Neither has been established here. The owner explicitly selected learning/portfolio first; keep enterprise work conditional.

## Prioritized review comments

Priority is relative to the indicated gate, not an assertion that an unimplemented app has a demonstrated exploit. P1 means a blocker before that gate; P2 means an important improvement within the learning release or future validation.

| ID / priority | Review concern and consequence | Incorporated response / owner / gate |
| --- | --- | --- |
| R01 / P1 before commercial claims | No identified buyer, observed recurring task, baseline, willingness to pay or cost-to-serve evidence. A working chatbot does not validate a business. | Product charter defines hypotheses, discovery/pilot method and value arithmetic; product owner, future commercial decision. |
| R02 / P1 before commercial investment | Google, Microsoft and AWS already offer overlapping analytics capabilities. Generic chat-to-chart is weak differentiation. | Build-versus-buy comparison and workflow-specific advantage test; product/architecture owners, before expanding scope. |
| R03 / P2 | Android/voice may be excellent for learning but unsuitable for the buyer's daily tools or managed devices. | Keep Android as learning choice; validate device/workflow preference later, without adding web/iOS/Teams now. |
| R04 / P1 before live analytical claims | Correct SQL syntax and authorized tables do not prove the chosen metric, denominator or join is correct. A general SQL verifier is a large hidden engineering project. | Finite typed semantic compiler first; generated SQL a gated optional extension; data/engineering owners, P4/P5. |
| R05 / P1 before trusting answers | No formal owner/review lifecycle for definitions; chart schemas do not prevent misleading interpretation or causal claims. | Definition ownership/versioning, descriptive-answer limits, answer-details UI and feedback review; P4–P6, T30/T31/T35/T36. |
| R06 / P1 before private data | Firebase login plus two application roles does not demonstrate enterprise SSO or user-scoped database permissions. A broad service account may bypass intended row scope. | Enterprise identity-to-source matrix, federation/lifecycle checks and direct database negative tests; security/data owners, E02/E03. |
| R07 / P1 before private data | Prompts, transcripts, speech providers, model caches, backups and support traces create data paths beyond BigQuery. | Explicit handling inventory, provider/region/retention approval and private-voice gate; security/privacy owner, E05. |
| R08 / P1 before durable live operation | Queue selection was unresolved, concurrency envelope absent and expiry could leave an accepted run occupied. | Outbox/reconciliation requirements, concurrent isolation/load scenario and terminal timeout rule; engineering owner, P3/P6, T33/T34. |
| R09 / P1 before pilot quality claims | Synthetic SQL fixtures alone cannot estimate real-question answer quality; model-only judging can miss semantic errors. | Held-out scenarios, dimension-specific scoring, human/domain review and versioned regressions; data/QA owner, P6/E04. |
| R10 / P1 before production | No customer-specific SLO, recovery proof, operating owner, supplier/support commitments or offboarding evidence. | Conditional enterprise gates E06–E09; operations/authorized business owners. No false compliance claim. |
| R11 / P2 | Enterprise aspirations could overwhelm a step-by-step course and delay any complete demonstration. | Accepted learning-first ADR, thin vertical slice, optional advanced SQL and explicit demo versus enterprise release boundaries. |

## What the cloud references establish

- Google Looker describes using LookML semantics and composing queries from selected fields/filters. This supports the choice to make business definitions and a bounded query plan central to our design; it is not proof that our compiler works. [Looker overview](https://docs.cloud.google.com/looker/docs/conversational-analytics-overview)
- Microsoft Fabric documents source access using the requesting user's permissions. Azure architecture guidance emphasizes deterministic tenant isolation. Our service-account design must explicitly account for the user's data scope rather than assuming login propagates to the warehouse. [Fabric data agents](https://learn.microsoft.com/en-us/fabric/data-science/concept-data-agent), [Azure tenant controls](https://learn.microsoft.com/en-us/azure/architecture/guide/multitenant/considerations/agentic-systems)
- AWS offers reviewed Q-topic answers and dataset row security. Its AI guidance treats business scoping and continuing evaluation as lifecycle work. We therefore need both a business-outcome baseline and an answer-correction process, not just an impressive interface. [Reviewed answers](https://docs.aws.amazon.com/cli/latest/reference/quicksight/list-topic-reviewed-answers.html), [Generative AI lifecycle](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/generative-ai-lifecycle.html)
- Google Well-Architected covers security, reliability, operations, performance and cost as distinct concerns. A managed deployment is not evidence that the application has satisfied them. [Framework](https://docs.cloud.google.com/architecture/framework)

These sources inform the review; they do not certify this repository, establish customer demand or prove that one platform is best. Current product names, feature availability, licensing and regional constraints must be rechecked for an actual customer evaluation.

## What changed and what did not

Added a learning-first decision, [product charter and value validation](../specifications/15-product-charter-and-value-validation.md) and [conditional enterprise gates](../specifications/16-enterprise-readiness.md). Updated the existing architecture, metric ownership, tool contracts, feedback API, state lifecycle, test plan, implementation sequence, learning path and traceability. Added T30–T36 for the engineering gaps.

No application was implemented. No cloud resources, identity configuration or customer integrations were created. No claims of achieved savings, verified security, enterprise customers or passing runtime tests were introduced. The next practical work remains L00/P0.1 and L01/P1.1; enterprise discovery is not required to learn those modules.
