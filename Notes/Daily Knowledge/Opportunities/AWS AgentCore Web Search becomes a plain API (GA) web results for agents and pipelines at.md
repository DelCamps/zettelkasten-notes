---
date: 2026-11-11
section: AI
importance: Med
kind: value
source: "AWS What's New"
url: https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-bedrock-agentcore-web-search-api/
status: unread
id: 2026-11-11-agentcore-web-search-api
---
2026-11-11 07:16
Tags: #daily-knowledge #ai

---
# AWS AgentCore Web Search becomes a plain API (GA) web results for agents and pipelines at

Amazon Bedrock AgentCore's Web Search, previously only an MCP tool behind AgentCore Gateway, is now generally available as a single-call InvokeWebSearch API returning ranked results from an Amazon-operated web index. It costs $7 per 1,000 queries with no gateway charges, in six regions including Europe (Ireland).

## Details

**Availability and price**
GA. $7 per 1,000 queries, same as Web Search through AgentCore Gateway, with no gateway charges. Regions: US East (N. Virginia), US East (Ohio), US West (Oregon), Asia Pacific (Sydney), Asia Pacific (Tokyo), Europe (Ireland). Callable via AWS SDKs or CLI.

**Caveats**
Returns raw ranked results, not answers; web content is untrusted input and needs prompt-injection handling in the agent. Only one EU region.

**Client use cases**
- Grounding a custom agent loop (not built on AgentCore Gateway) in current web content
- Market and competitor monitoring pipelines restricted to approved domains and recent dates
- Research agents for regulated clients that must keep traffic on AWS via PrivateLink and log every query in CloudTrail

**How we could offer it**
- Drop-in web grounding for AWS-hosted client agents, with domain allowlists as a guardrail
- Include in AgentCore-based agent builds alongside the Web Answer tool covered last week

**Pitch**
Web search for your agents that stays inside your AWS account controls: IAM, PrivateLink and CloudTrail, priced per query.

**What it is**
A GA web search API (InvokeWebSearch) in Amazon Bedrock AgentCore. Applications, custom agent loops and data pipelines can search the web without creating resources. Results come from an Amazon-operated index, each with a text extract and, when available, title, URL and publication time; requests can filter by domain and publication time.

**Concepts:** [[AWS]] · [[Agents]] · [[RAG]]
**From:** [[2026-11-11]]

# My notes


---
# References
[AWS What's New](https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-bedrock-agentcore-web-search-api/)
