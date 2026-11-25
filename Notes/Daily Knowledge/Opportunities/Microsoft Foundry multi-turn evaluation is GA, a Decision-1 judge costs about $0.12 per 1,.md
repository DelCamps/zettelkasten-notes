---
date: 2026-11-25
section: AI
importance: Med
kind: value
source: "Microsoft Foundry blog"
url: https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-ignite-2026/
status: unread
id: 2026-11-25-foundry-evals-cost-controls
---
2026-11-25 07:16
Tags: #daily-knowledge #ai

---
# Microsoft Foundry multi-turn evaluation is GA, a Decision-1 judge costs about $0.12 per 1,

Microsoft's Ignite round-up for Foundry, published 24 November, makes multi-turn evaluation generally available and previews rubric evaluators, human annotation and Microsoft-Decision-1 as a low-cost judge (0.59 s median latency). It also previews cost views and cost controls: dollar or token budgets that alert at a threshold and return HTTP 429 once the budget is spent.

## Details

**Availability and price**
Multi-turn evaluation and Insights: GA. Microsoft-Decision-1 judge: public preview, about $0.12 per 1,000 evaluator calls, needs azure-ai-evaluation 1.18.12+. Cost views and cost controls: public preview. Priced cost data typically arrives 8-24 hours later.

**Caveats**
Budgets exclude tool charges, hosted-agent compute and provisioned throughput, and are not a guaranteed invoice cap. About 2% of Decision-1 verdicts change on reruns, and it gives no written rationale.

**Client use cases**
- Regression tests for whole agent conversations before each release
- Cheap LLM-as-judge scoring at scale for customer-service agents
- Per-project AI spend caps for business units running agents

**How we could offer it**
- Agent evaluation and quality-gate setup as part of every Foundry build
- AI FinOps package: cost views, budgets and alerts across a client's Foundry projects

**Pitch**
Clients ask 'is the agent good enough?' and 'what will it cost?'. Foundry now answers both in the same place, and we can wire it in from day one.

**What it is**
Evaluation and FinOps features for agents built on Microsoft Foundry. Insights and multi-turn evaluation are GA. Rubric evaluators, safety rubric evaluators, task-level rubrics and human annotation are in preview; in HelpSteer3 testing, alignment with human judgment rose from 65% to 81%. Cost controls set dollar or token budgets, for example alerting at 80% and blocking at 100%.

**Concepts:** [[Evals and benchmarks]] · [[Agents]]
**From:** [[2026-11-25]]

# My notes


---
# References
[Microsoft Foundry blog](https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-ignite-2026/)
