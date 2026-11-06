---
date: 2026-11-06
section: AI
importance: Med
kind: value
source: "AWS What's New"
url: https://aws.amazon.com/about-aws/whats-new/2026/11/web-answer-amazon-bedrock/
status: unread
id: 2026-11-06-agentcore-web-answer
---
2026-11-06 07:16
Tags: #daily-knowledge #ai

---
# AWS AgentCore Web Answer is GA one MCP call returns a cited answer from current web source

Amazon Bedrock AgentCore adds Web Answer, a managed tool that takes a natural-language question, plans its own parallel web searches and returns a synthesized, cited answer in one call. It attaches to an AgentCore Gateway, is called over MCP with IAM auth, supports domain allow/deny lists and publish-date filters, and is GA in US East (N. Virginia) with per-call pricing.

## Details

**Availability and price**
Generally available, US East (N. Virginia) only. Priced per tool call (no rate given in the announcement).

**Caveats**
Single US region, so EU data-residency clients may not be able to use it yet. Answer quality and citation accuracy still need evaluation per use case; per-call price not stated in the announcement.

**Client use cases**
- Market and competitor monitoring agents that need cited, current answers
- Regulatory-watch assistants limited to official domains (regulators, official journals) via allow lists
- Adding fresh web grounding to an existing AgentCore or Amazon Connect agent without building a search-and-summarise pipeline

**How we could offer it**
- Pilot a cited research agent for a client's analysts on AgentCore Gateway
- Governance: define domain allow/deny lists and date filters as part of a source policy

**Pitch**
AWS now sells cited web research as a single agent tool call; for AWS clients we can add governed, source-restricted web grounding to their agents in days rather than building our own search pipeline.

**What it is**
A managed research tool for agents on Amazon Bedrock AgentCore that extends the existing Web Search tool. Instead of returning links, it decides how many parallel searches to run, stops when it judges it has enough evidence, and returns one synthesized answer with citations grounded in current web sources. Builders can restrict sources with domain include and deny lists and filter by publish date. It is added as a target on an AgentCore Gateway, so any MCP-capable agent can call it, with IAM authentication.

**Concepts:** [[AWS]] · [[Agents]]
**From:** [[2026-11-06]]

# My notes


---
# References
[AWS What's New](https://aws.amazon.com/about-aws/whats-new/2026/11/web-answer-amazon-bedrock/)
