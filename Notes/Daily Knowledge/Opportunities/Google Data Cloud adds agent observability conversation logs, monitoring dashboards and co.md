---
date: 2026-11-14
section: AI
importance: Med
kind: value
source: "Google Cloud blog"
url: https://cloud.google.com/blog/products/data-analytics/enterprise-ai-agent-observability-with-bigquery-and-looker
status: unread
id: 2026-11-14-google-agent-observability
---
2026-11-14 07:16
Tags: #daily-knowledge #ai

---
# Google Data Cloud adds agent observability conversation logs, monitoring dashboards and co

Google made conversation logging in BigQuery, the Conversational Analytics API, BigQuery Studio agent dashboards and Looker System Activity dashboards generally available, so data agents' traces, token use and latency land in customer-owned BigQuery tables. Daily token quotas per project, user or agent and native BigQuery agent evaluations are in preview.

## Details

**Availability and price**
GA: conversation logging in BigQuery, Conversational Analytics API (with CMEK, VPC Service Controls, regional and multi-regional data residency), A2A workflows for BigQuery data agents in Gemini Enterprise, BigQuery Studio and Looker dashboards. Preview: Looker ratings and query review, daily token quotas, native BigQuery evaluations. Promotional trial pricing for Conversational Analytics; no prices given.

**Caveats**
Mainly for agents on Google Data Cloud; logging adds storage costs; several pieces are preview.

**Client use cases**
- Production monitoring of 'talk to your data' agents: usage, latency, top knowledge sources, token use
- FinOps for agents: per-turn token counts, byte-scan caps that block oversized queries, daily token quotas (preview)
- Root-cause and drift analysis with BigQuery AI functions
- Pre-release regression tests with the open-source Prism evaluation tool

**How we could offer it**
- Agent observability and FinOps setup for Google Cloud clients, including dashboards and cost guardrails
- Governance review: decide which agents may log prompts and responses, and check CMEK, VPC Service Controls and data residency settings
- Evaluation harness with Prism wired into release pipelines

**Pitch**
Clients running data agents on Google Cloud can now see, cap and test them in their own BigQuery; we can stand that up as a short governance-and-FinOps engagement.

**What it is**
One telemetry framework for Google's own data agents (Conversational Analytics in BigQuery and Looker) and custom agents built with ADK or LangGraph. Telemetry lands in a customer-owned BigQuery table (agent_events); custom agents add it with single-line SDK instrumentation. Logging is opt-in per agent and is skipped automatically when a knowledge source uses row-level security, policy tags or data masking.

**Concepts:** [[Google Cloud]] · [[Agents]] · [[Evals and benchmarks]]
**From:** [[2026-11-14]]

# My notes


---
# References
[Google Cloud blog](https://cloud.google.com/blog/products/data-analytics/enterprise-ai-agent-observability-with-bigquery-and-looker)
