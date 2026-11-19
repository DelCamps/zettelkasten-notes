---
date: 2026-11-19
section: AI
importance: Med
kind: value
source: "GitHub changelog"
url: https://github.blog/changelog/2026-11-17-monitor-github-copilot-activity-through-microsoft-agent-365
status: unread
id: 2026-11-19-github-copilot-agent-365-monitoring
---
2026-11-19 07:16
Tags: #daily-knowledge #ai

---
# GitHub Copilot agent activity now streams into Microsoft Agent 365 prompts, responses and

Enterprises on GitHub Enterprise Cloud with Enterprise Managed Users can stream GitHub Copilot agent activity into Microsoft Agent 365, covering cloud agents on GitHub.com, Copilot CLI, VS Code, Visual Studio and partner IDEs. Admins can review sessions including prompts, responses and tool calls, track usage trends, and pull extra risk information from Purview and Defender.

## Details

**Availability and price**
Available for GitHub Enterprise Cloud customers with Enterprise Managed Users. The changelog does not state GA or preview, and gives no price; Agent 365 licensing applies on the Microsoft side.

**Caveats**
Only for Enterprise Managed Users tenants; setup goes through enterprise audit-log streaming. Release status and data residency are not described.

**Client use cases**
- One audit trail for coding agents alongside Copilot and Copilot Studio agents
- Investigate a suspicious coding-agent session, including its tool calls
- Report Copilot adoption and usage trends to engineering leadership

**How we could offer it**
- Developer-AI governance setup: audit streaming, Agent 365 views, Purview and Defender investigation playbooks
- Bundle with the Defender local-agent protection rollout as one coding-agent oversight package (skills: GitHub Enterprise admin, Agent 365, Purview)

**Pitch**
Regulated clients can now show auditors exactly what GitHub Copilot agents did, prompt by prompt and tool call by tool call, in the same Microsoft console as their other agents.

**What it is**
An integration that sends GitHub Copilot audit data into Agent 365, Microsoft's agent control plane, via GitHub's enterprise audit-log streaming. Admins see activity across Copilot clients (cloud agents on GitHub.com, Copilot CLI, Visual Studio Code, Visual Studio, JetBrains, Eclipse), review user sessions with prompts, responses and tool calls, follow usage trends, and investigate risk using Microsoft Purview and Defender.

**Concepts:** [[GitHub Copilot]] · [[Agent security]] · [[Coding agents]]
**From:** [[2026-11-19]]

# My notes


---
# References
[GitHub changelog](https://github.blog/changelog/2026-11-17-monitor-github-copilot-activity-through-microsoft-agent-365)
