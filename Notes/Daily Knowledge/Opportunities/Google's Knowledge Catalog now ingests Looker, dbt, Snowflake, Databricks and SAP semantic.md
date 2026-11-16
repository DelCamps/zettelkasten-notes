---
date: 2026-11-01
section: AI
importance: Med
kind: value
source: "Google Cloud blog"
url: https://cloud.google.com/blog/products/data-analytics/expanded-semantic-model-support-in-knowledge-catalog/
status: unread
id: 2026-11-01-knowledge-catalog-semantic-models
---
2026-11-01 07:16
Tags: #daily-knowledge #ai

---
# Google's Knowledge Catalog now ingests Looker, dbt, Snowflake, Databricks and SAP semantic

Google Cloud's Knowledge Catalog now natively ingests semantic models and metric definitions from Looker LookML, BigQuery Graph, dbt MetricFlow, Snowflake Semantic Views, Databricks Metric Views and SAP CSN (all GA) into one 'context graph' for Gemini Enterprise, BigQuery Conversational Analytics and custom agents. Google's internal benchmarks claim nearly 4x more accurate agents, up to 33% lower latency and up to 75% fewer tokens. Power BI is not on the list.

## Details

**Availability and price**
Ingestion from the six listed sources is GA; Knowledge Studio is in preview. The post gives no pricing. Announced 29 Oct 2026.

**Caveats**
The accuracy, latency and token figures are Google's internal benchmarks with no published method. No Power BI support, so it matters less for Microsoft-stack clients. Competes with Fabric's semantic-model grounding for Copilot.

**Client use cases**
- Text-to-SQL and conversational analytics agents that reuse the metrics finance already certified, instead of re-deriving them.
- Multi-platform data estates (Snowflake plus Databricks plus SAP) that need one governed metric layer for agents.
- Finding and reconciling conflicting KPI definitions across BI tools.

**How we could offer it**
- Semantic-layer readiness assessment for clients on Google Cloud or multi-cloud data stacks.
- Implementation of context sets and trust signals (quality, freshness, lineage) for a first agent use case.
- Data governance service for metric reconciliation. Skills: dbt or LookML, Snowflake or Databricks semantics, Gemini Enterprise.

**Pitch**
Google now grounds its data agents in the semantic models clients already maintain in Looker, dbt, Snowflake, Databricks and SAP. For non-Microsoft data estates, this is the same 'semantic model first' offer we pitch for Power BI and Fabric.

**What it is**
Knowledge Catalog places semantic definitions next to schema, lineage, data profiles and glossary terms. When two tools define the same metric differently, both are kept and labelled by source so data stewards can reconcile them. Gemini-powered enrichment extracts context from playbooks, meeting notes, chat threads and code. Validated assets can be packaged as reusable 'context sets'. Knowledge Studio, the tool to explore the graph, is in preview.

**Concepts:** [[Google Cloud]] · [[RAG]] · [[Agents]]
**From:** [[2026-11-01]]

# My notes


---
# References
[Google Cloud blog](https://cloud.google.com/blog/products/data-analytics/expanded-semantic-model-support-in-knowledge-catalog/)
