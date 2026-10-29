# Product charter and value validation

## Purpose and evidence status

Primary purpose: learn and demonstrate how to build a trustworthy Android conversational analytics system, end to end. Secondary possibility: later validate a narrow commercial workflow. The owner chose learning/portfolio first; see [ADR 0001](../decisions/0001-learning-first-scope.md).

Current evidence is a reviewed specification, not a working app, customer study or paid pilot. TheLook is a fictitious dataset for teaching technical behavior. Neither a convincing demo nor a large-cloud reference proves demand, correctness on private data or willingness to pay.

## The user problem we will demonstrate

A business user has a follow-up question that a fixed dashboard does not immediately answer. They need an understandable answer using a consistent metric definition and their own permissions, without composing SQL or waiting for every small refinement to be handled manually.

Demonstration story: a sales analyst asks for completed-item sales by month for explicit dates, narrows to an available country, compares categories using a minimum-order threshold, switches to a table, and checks the calculation's definition and provenance. A catalog viewer can inspect products but cannot obtain sales figures, including through follow-ups or saved results. The app explains missing context and unsupported questions rather than pretending to know.

This is descriptive analytics and navigation through approved measures. It is not a finance system of record, a forecasting product, a causal inference engine, or an autonomous decision-maker. “Why did sales fall?” may lead to an approved breakdown of where the change occurred; it must not invent causes such as pricing, marketing or stockouts without relevant evidence. No automated business actions are in scope.

## Learning product success

A successful portfolio release demonstrates all of the following with reproducible evidence:

1. A clean-checkout sample works without a model or cloud account, with unmistakable sample labels.
2. Typed/voice input uses the same conversation and accessible structured answers.
3. A developer can explain each trust boundary, reproduce fixture totals and show why a deliberately wrong join fails.
4. Both roles work, and adversarial tests demonstrate denial outside the model itself.
5. Disconnect, duplicate Send, Stop and permission changes have inspectable outcomes.
6. Query/model costs and errors are visible without exposing credentials or sensitive logs.
7. Each lesson records the design choice, alternative, test evidence and limitation. A guided demo includes a failure/clarification, not only a happy path.

Measure completion by working checkpoints and understanding, not by number of services, lines of code, model calls or features. Existing [learning modules](13-learning-path.md) remain the implementation route.

## Commercial hypothesis — not validated or selected as a business

One candidate is mobile sales-performance follow-ups for a distributed commercial team already using BigQuery and approved sales definitions. Potential users are commercial managers and analysts; a possible sponsor is the head of sales operations or analytics. The data owner validates definitions; IT/security controls identity and data access; procurement evaluates the supplier. These are personas to test, not identified customers.

Why this might matter: repetitive follow-ups can consume analyst capacity and delay decisions. Why it might not: the team's BI tool may already answer them, data definitions may be the real bottleneck, or users may prefer a browser or Teams over an installed Android app. TheLook country/category examples are proxies; they do not prove coverage of stores, territories, inventory or the customer's business.

Do not claim a differentiator based on chat, charts, voice, MCP or text-to-SQL alone. A future advantage would need measured evidence such as better completion of a specific mobile workflow, faster governed onboarding, or a domain package that outperforms the customer's existing configuration. None is established today.

## Build versus buy before commercial expansion

| Existing option | Official evidence | Decision implication for this project |
| --- | --- | --- |
| Google Looker Conversational Analytics | Uses LookML definitions and query composition for conversational questions. [Overview](https://docs.cloud.google.com/looker/docs/conversational-analytics-overview) | Reuse the customer's governed definitions rather than inventing a conflicting metric layer; compare a configured Looker workflow against our journey. |
| Google Conversational Analytics API | Documents direct, ADK and MCP integration patterns. [Integration options](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/integration-patterns) | Custom UI does not imply a need to build every analytics component; evaluate a managed adapter before production investment. |
| Microsoft Fabric data agents | Documents conversational queries and source access under the requesting user's permissions. [Concepts](https://learn.microsoft.com/en-us/fabric/data-science/concept-data-agent) | For a Fabric/Power BI customer, benchmark the native option with the same questions and entitlement tests. |
| AWS Amazon Quick Sight / Q topic tooling | Provides reviewed-answer operations and dataset RLS. [Reviewed answers](https://docs.aws.amazon.com/cli/latest/reference/quicksight/list-topic-reviewed-answers.html), [RLS](https://docs.aws.amazon.com/quick/latest/userguide/row-level-security.html) | Curated answers and permissions are a competitive baseline, not a unique selling point. |
| Existing dashboard and analyst process | Requires observation at a future customer; no baseline captured | Use as the control. Some recurring questions are better solved by improving a dashboard or metric definition. |

These are documentation comparisons, not tested benchmarks, procurement recommendations or claims about feature parity. Verify region, licensing, availability, limits and total cost for the actual customer. Keep cloud-provider implementations behind interfaces only where useful; do not add Azure/AWS deployments to the learning scope.

## Future discovery and pilot protocol

Only if commercial exploration is requested:

1. Observe real recent questions from 5–8 prospective users plus a data owner and sponsor. Ask what decision followed, how they obtained the answer, active work time versus queue time, frequency, error consequences, permissions and preferred device. Avoid leading “would you use AI?” questions.
2. Obtain permission to collect a de-identified question set, with owner-reviewed definitions and expected answers. Do not copy customer questions/data into this public repository without explicit approval.
3. Compare the same supported tasks using the current workflow, a configured native BI option and this product. Include permissions, ambiguity, unsupported questions and correction time. Alternate task order to reduce learning effects.
4. For a small scoped pilot, agree up front on users, duration, accepted risk, support, data scope, cost ceiling and [enterprise admission gates](16-enterprise-readiness.md). Initial proposal: 10–20 participants over four weeks, after mandatory security gates. This is a study design, not an approved pilot.
5. Report successful and failed tasks, abandonment, repeated usage, costs and confidence intervals where meaningful. A successful demo with its author is not independent validation. Proceed, narrow, use an existing platform, or stop based on results.

Proposed criteria to negotiate before such a pilot: at least 30% reduction in median active time to a correctly reviewed answer versus baseline; at least 80% supported-task completion; repeated weekly use by at least half the enrolled users who have recurring tasks; and sponsor-confirmed willingness to fund continued use. These are hypotheses, not industry benchmarks. Security/correctness gates cannot be traded away for usage. Define supported tasks before testing so unsupported failures are not relabeled after the fact.

## What would make it a “million-dollar problem”?

Separate three claims: value created for a customer, revenue earned by a vendor, and business valuation. None follows automatically from the others.

An illustrative capacity-value model is:

`annual hours saved = eligible users × tasks/user/week × active minutes saved/task ÷ 60 × working weeks × adoption × correct-completion fraction`

`gross capacity value = annual hours saved × fully loaded hourly cost`

For illustration only: 1,000 users × 4 tasks/week × 15 minutes ÷ 60 × 46 weeks × 60% adoption × 90% correct completion = 24,840 hours; at an assumed $60/hour, that is $1,490,400 annual capacity value. These are invented inputs, not a forecast. Capacity freed is not automatically payroll savings. Use net measured time savings including review/rework; deduct integration, licenses, data stewardship, support, model/query/infrastructure costs and ongoing maintenance. Do not also count the same hours as analyst savings twice. Queue-time reduction is a separate benefit unless a causal financial outcome is established.

Vendor arithmetic is separate: 20 customers paying an illustrative $50,000/year would equal $1 million ARR, before costs. No evidence supports that price, customer count, sales cycle or retention here. Measure onboarding/support effort and gross margin before assuming SaaS economics. No valuation claim is made.

## Decision now

Proceed with the learning project. Keep the enterprise extension documented, not built preemptively. Reassess commercial investment only after workflow evidence, a named sponsor, reviewed data semantics, a build-versus-buy comparison and an affordable adoption path exist.
