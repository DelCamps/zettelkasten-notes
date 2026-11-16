---
date: 2026-11-13
section: AI
importance: Med
kind: value
source: "Claude Platform docs and release notes"
url: https://platform.claude.com/docs/en/managed-agents/self-hosted
status: unread
id: 2026-11-13-self-hosted-claude-managed-agents
---
2026-11-13 07:16
Tags: #daily-knowledge #ai

---
# Anthropic lets clients run the whole Claude Managed Agents service on their own infrastruc

Self-hosted Claude Managed Agents moves the agent loop, API and storage of agents, sessions and history onto the customer's cloud account or data center, not just the sandboxes. Model calls can go to the Claude API, Amazon Bedrock, Claude Models on Google Cloud, Microsoft Foundry or the client's own gateway; access is through the Anthropic account team.

## Details

**Availability and price**
Launched 12 November 2026; request access via the Anthropic account team. Licensed under a separate server software licence. No price stated.

**Caveats**
Not everything is there: no cloud environments, Files API, prebuilt docx/pdf/pptx/xlsx skills, scheduled deployments, dreams or webhooks; multiagent only in coordinator mode with 1 to 20 listed agents. web_fetch works only with anthropic or foundry providers. The bash tool is a real shell, so isolation depends on the container or VM the worker runs in.

**Client use cases**
- Regulated clients (banking, public sector, health) that must keep agent session history and transcripts in their own tenancy
- Azure-first clients that want Claude agents with inference through Microsoft Foundry
- On-premise agent platforms with MCP servers inside the private network, without MCP tunnels

**How we could offer it**
- Reference deployment on AKS or EKS with Helm, PostgreSQL, egress gateway and MCP/Git allowlists
- Security hardening and operating model (release upgrades, isolation, monitoring), since the client takes on what Anthropic secures in the hosted service

**Pitch**
Claude's managed agent runtime, with your data, identity and model provider staying inside your perimeter.

**What it is**
A downloadable server (cma-server) that serves the same Managed Agents API as Anthropic's hosted service, runs the agent loop and stores data in PostgreSQL 16 or later. Workers (an ant beta:worker command or SDK worker) poll the server and run shell and file tools in the client's sandboxes; Docker Compose and a cma-sandboxes Helm chart start each session's worker in its own container or pod. It adds features the hosted service lacks: OIDC single sign-on with group-based roles, the client's own secret manager for vault credentials, and signed short-lived agent identity tokens for MCP servers. A console runs on the server.

**Concepts:** [[Claude]] · [[Agents]] · [[Agent security]]
**From:** [[2026-11-13]]

# My notes


---
# References
[Claude Platform docs and release notes](https://platform.claude.com/docs/en/managed-agents/self-hosted)
