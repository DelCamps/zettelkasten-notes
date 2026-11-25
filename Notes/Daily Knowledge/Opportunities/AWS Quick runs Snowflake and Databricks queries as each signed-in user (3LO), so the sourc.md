---
date: 2026-11-25
section: AI
importance: Low
kind: value
source: "AWS What's New"
url: https://aws.amazon.com/about-aws/whats-new/2026/11/aws-quick-snowflake-databricks-3lo-end-user-permissions/
status: unread
id: 2026-11-25-aws-quick-3lo-ai-ready-datasets
---
2026-11-25 07:16
Tags: #daily-knowledge #ai

---
# AWS Quick runs Snowflake and Databricks queries as each signed-in user (3LO), so the sourc

AWS Quick now supports three-legged OAuth for Snowflake and Databricks, so Chat, dashboards and Apps query the source as the signed-in user and Unity Catalog or Snowflake row- and column-level rules are enforced by the source. It works only for DirectQuery datasets.

## Details

**Availability and price**
Both in the supported AWS Quick Regions. Neither page mentions pricing.

**Caveats**
End-user permissions through 3LO work only for DirectQuery datasets. Not a Microsoft-stack offer.

**Client use cases**
- Chat over governed Snowflake or Databricks data without copying permissions into Quick
- Upgrade old QuickSight-era datasets for natural-language Q&A

**How we could offer it**
- Quick rollout for AWS-centred clients with Snowflake or Databricks data estates
- Semantic-layer curation sprint, with accuracy measured by Dataset Evaluation

**Pitch**
AWS clients can put AI chat on top of their governed warehouse without rebuilding datasets or duplicating access rules.

**What it is**
Two AWS Quick data updates. 3LO with trusted identity propagation passes each user's identity to Snowflake or Databricks, which enforce existing row-level, column-level, table and view permissions. 'AI-ready' legacy datasets gain Dataset Semantics, topics, semantic models and Dataset Evaluation, which measures answer accuracy before and after adding descriptions and custom instructions.

**Concepts:** [[AWS]] · [[RAG]]
**From:** [[2026-11-25]]

# My notes


---
# References
[AWS What's New](https://aws.amazon.com/about-aws/whats-new/2026/11/aws-quick-snowflake-databricks-3lo-end-user-permissions/)
