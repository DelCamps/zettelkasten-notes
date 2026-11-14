---
date: 2026-11-14
section: AI
importance: High
kind: value
source: "AWS What's New"
url: https://aws.amazon.com/about-aws/whats-new/2026/11/new-agentcore-runtime-default/
status: unread
id: 2026-11-14-agentcore-runtime-default
---
2026-11-14 07:16
Tags: #daily-knowledge #ai

---
# AWS makes its next-generation AgentCore runtime the default agent sessions start in under

New Amazon Bedrock AgentCore runtimes now restore each agent session from a snapshot, start in under 2 seconds at P75 on a 2 GB image (down from 29.7 seconds), and scale idle agents to zero. AWS says multi-turn agents can see up to 68% less billed memory per session; sessions scale to 8 vCPU and 32 GB.

## Details

**Availability and price**
Default now for new runtimes in listed Regions including Europe (Spain), Europe (Frankfurt), Europe (Ireland) and US East (N. Virginia). Existing runtimes stay on V1 until moved. Pricing: see AgentCore pricing (no new prices in the post).

**Caveats**
The 68% figure is an 'up to' for multi-turn agents; startup figures are for a 2 GB image at P75. Existing runtimes must be migrated deliberately.

**Client use cases**
- Long-running coding or document-processing agents that need up to 8 vCPU and 32 GB per session
- Chat-style multi-turn agents where idle time currently drives the memory bill
- Browser-driving agents that need fast cold starts and per-session isolation
- Agents that load a small local model inside the session (images up to 10 GB)

**How we could offer it**
- Migration assessment: move existing AgentCore runtimes by setting platformVersion to V2, with regression and cost tests before and after
- Cost review for agent estates: measure billed memory per session before and after the switch
- Reference architecture for isolated agent hosting in EU Regions

**Pitch**
AWS just cut agent cold starts from 29.7 seconds to under 2 and scales idle agents to zero; we can move clients' AgentCore agents over and prove the savings.

**What it is**
The second-generation AgentCore runtime, now the default for new runtimes. Each session still runs in its own Firecracker microVM, but is restored from a snapshot of the initialized agent, scales compute and memory with the work, and releases memory within minutes when idle. Sessions can do heavy work such as compiling a large codebase, driving a browser or loading a local model.

**Concepts:** [[AWS]] · [[Agents]]
**From:** [[2026-11-14]]

# My notes


---
# References
[AWS What's New](https://aws.amazon.com/about-aws/whats-new/2026/11/new-agentcore-runtime-default/)
