---
date: 2026-11-20
section: AI
importance: Low
kind: value
source: "AWS What's New"
url: https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-opensearch-memory-generally-available/
status: unread
id: 2026-11-20-amazon-opensearch-memory-ga
---
2026-11-20 07:16
Tags: #daily-knowledge #ai

---
# Amazon OpenSearch Memory is GA serverless long-term memory for agents, available in Frankf

AWS made OpenSearch Memory generally available: a serverless capability that stores agent interactions as searchable events, derives structured memories and retrieves relevant context across sessions, so agents need not replay full histories. It runs in five regions including Europe (Frankfurt).

## Details

**Availability and price**
GA, announced 18 November 2026, in US East (N. Virginia, Ohio), US West (Oregon), Europe (Frankfurt) and Asia Pacific (Tokyo). Pricing is on the OpenSearch Service pricing page, not in the announcement.

**Caveats**
Access is per memory store via IAM with actor and session scoping; retention needs explicit expiry settings for GDPR. Price not stated.

**Client use cases**
- Customer-service agents that remember past decisions and preferences
- Internal assistants that keep context across long-running projects
- Cutting token costs by retrieving memories instead of replaying conversations

**How we could offer it**
- Design memory scopes, retention and access per client use case
- Add memory to existing AWS agent builds (AgentCore or custom) as part of implementation
- Governance: set expiry and IAM scoping for personal data

**Pitch**
A managed, EU-available memory layer lets us add persistent context to client agents on AWS without running our own vector clusters.

**What it is**
A managed agent memory store in Amazon OpenSearch Service that handles extraction, embedding, indexing, consolidation and retrieval with keyword, semantic and hybrid search. There are no clusters, instance types or indexes to provision.

**Concepts:** [[Agent memory]] · [[AWS]]
**From:** [[2026-11-20]]

# My notes


---
# References
[AWS What's New](https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-opensearch-memory-generally-available/)
