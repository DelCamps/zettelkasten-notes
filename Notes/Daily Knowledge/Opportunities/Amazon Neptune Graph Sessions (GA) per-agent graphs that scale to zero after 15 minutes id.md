---
date: 2026-11-28
section: AI
importance: Low
kind: value
source: "AWS What's New"
url: https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-neptune-graph-sessions-generally-available
status: unread
id: 2026-11-28-neptune-graph-sessions
---
2026-11-28 07:16
Tags: #daily-knowledge #ai

---
# Amazon Neptune Graph Sessions (GA) per-agent graphs that scale to zero after 15 minutes id

Neptune Graph Sessions is a new compute mode for per-agent, per-user or per-task graphs: pick a 4 s-NCU or 8 s-NCU starting size, let memory grow to twice that, and the graph scales to zero after 15 minutes idle and resumes in seconds on the next query. Billing follows the memory the graph uses.

## Details

**Availability and price**
Generally available. Billed for memory used; the page links to Neptune pricing but gives no rates. Regions not stated.

**Caveats**
Niche; graph memory only helps when relationships matter. Check regional availability and actual rates before proposing.

**Client use cases**
- Graph-based agent memory per user or case
- Per-investigation knowledge graphs (fraud, audit, claims) that sit idle most of the time
- GraphRAG prototypes without a provisioned graph's minimum cost

**How we could offer it**
- Pilot: graph memory for an AgentCore or Bedrock agent
- Architecture assessment: compare against vector-only memory on cost and answer quality

**Pitch**
A cheap way to give each agent or case its own graph memory on AWS, paying little while idle.

**What it is**
Serverless-style knowledge graphs for agents, queried with openCypher and created from the console, CLI or SDKs; data is kept between sessions so it doesn't need reloading.

**Concepts:** [[AWS]] · [[Agent memory]]
**From:** [[2026-11-28]]

# My notes


---
# References
[AWS What's New](https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-neptune-graph-sessions-generally-available)
