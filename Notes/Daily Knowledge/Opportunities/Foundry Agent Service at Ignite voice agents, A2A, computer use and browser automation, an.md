---
date: 2026-11-20
section: AI
importance: High
kind: value
source: "Microsoft Foundry blog"
url: https://devblogs.microsoft.com/foundry/whats-new-in-foundry-agent-service-at-ignite-2026/
status: unread
id: 2026-11-20-foundry-agent-service-ignite-ga
---
2026-11-20 07:16
Tags: #daily-knowledge #ai

---
# Foundry Agent Service at Ignite voice agents, A2A, computer use and browser automation, an

Microsoft made a batch of Foundry Agent Service features generally available: voice agents with native telephony, an A2A tool, computer use and browser automation with Live View and session recordings, network egress controls and long-running resiliency for hosted agents, and Insights that also covers LangGraph, LangChain and CrewAI agents. The Microsoft Copilot harness, memory snapshots, skill and cost optimization are in public preview.

## Details

**Availability and price**
Features listed above are GA as of 18 November 2026; Microsoft Copilot harness, memory snapshots, private CA trust, Azure Policy governance, annotations, evaluation datasets, skill and cost optimization are preview; customer-owned AKS deployment targeted for public preview in early December. The post gives no prices or EU region details.

**Caveats**
Long-running recovery reruns the handler, so developers must avoid duplicate side effects. State needed across idle periods must be stored externally. Pricing and regional availability need checking in Microsoft docs.

**Client use cases**
- Voice agents for contact centres and service desks on existing agents
- Browser automation for back-office work in web apps without APIs, with recordings for audit
- Agent-to-agent hand-offs between Foundry agents and partner agents via A2A
- One production monitoring view for clients running mixed LangGraph, CrewAI and Foundry agents

**How we could offer it**
- Pilot: move an existing chat agent to voice or browser automation
- Implementation of hosted agents with egress controls and private networking for regulated clients
- Managed service: run Insights and evaluations across a client's agent estate, mixed frameworks included

**Pitch**
Foundry now covers voice, browser and agent-to-agent work in production, with network controls and monitoring that also reads LangGraph and CrewAI agents. We can take clients' stalled pilots to governed production on the Microsoft stack they already buy.

**What it is**
Production features for building, hosting and operating agents in Microsoft Foundry. GA: voice agents (interruptions, phone and contact-centre connection), Web Search via Web IQ for prompt agents, A2A tool, computer use and browser automation, shared subnet IPs (default 1,000-2,000 concurrent sessions per subscription and region), network egress controls, long-running resiliency (idle timeout 2 minutes to 4 hours), and Insights for Foundry, LangGraph, LangChain and CrewAI agents.

**Concepts:** [[Agents]] · [[Computer-use agents]]
**From:** [[2026-11-20]]

# My notes


---
# References
[Microsoft Foundry blog](https://devblogs.microsoft.com/foundry/whats-new-in-foundry-agent-service-at-ignite-2026/)
