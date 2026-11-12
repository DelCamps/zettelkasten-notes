---
date: 2026-11-12
section: AI
importance: Low
kind: value
source: "AWS What's New"
url: https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-elasticache-serverless-search-aggregations/
status: unread
id: 2026-11-12-elasticache-serverless-vector-search
---
2026-11-12 07:16
Tags: #daily-knowledge #ai

---
# ElastiCache Serverless for Valkey adds vector, full-text and hybrid search, pitched for RA

Amazon ElastiCache Serverless now supports vector, full-text and hybrid search plus server-side aggregations on Valkey 9, in all commercial AWS Regions, GovCloud and the European Sovereign Cloud. AWS cites up to 99% recall, latency as low as microseconds and datastores ready in seconds, billed only for use.

## Details

**Availability and price**
Available now (published 10 November 2026) in all commercial Regions, AWS GovCloud (US) and the European Sovereign Cloud; requires ElastiCache for Valkey 9. Pay per use; no rates in the announcement.

**Caveats**
The announcement does not label GA vs preview; performance figures are AWS claims. A cache is not a system of record, so durability needs checking for memory use.

**Client use cases**
- Low-latency agent memory and session context stores
- Hybrid search for RAG over fast-changing data (prices, inventory, tickets)
- Product discovery and recommendations

**How we could offer it**
- Reference architecture for agent memory on AWS: AgentCore plus a per-agent ElastiCache datastore
- Cost/latency comparison against OpenSearch or a dedicated vector DB for existing RAG clients

**Pitch**
Give each agent a fast, pay-per-use memory store in seconds, inside the AWS account you already run, including the EU Sovereign Cloud.

**What it is**
Search built into the serverless Valkey cache: combine vector, keyword and hybrid queries in one call, tune recall and run aggregations, with writes searchable as soon as they complete. AWS explicitly targets RAG and per-agent or per-session datastores for memory and context, reachable over a public endpoint with no network setup.

**Concepts:** [[AWS]] · [[RAG]] · [[Agent memory]]
**From:** [[2026-11-12]]

# My notes


---
# References
[AWS What's New](https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-elasticache-serverless-search-aggregations/)
