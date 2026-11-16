---
date: 2026-11-04
section: AI
importance: Med
kind: value
source: "GitHub changelog"
url: https://github.blog/changelog/2026-10-28-connect-your-tools-to-copilot-without-all-the-setup
status: unread
id: 2026-11-04-github-copilot-verified-connectors
---
2026-11-04 07:16
Tags: #daily-knowledge #ai

---
# GitHub Copilot connectors (preview) 26 GitHub-verified MCP servers, incl. Slack, Figma, At

GitHub launched 'connectors', GitHub-verified MCP servers that Copilot can use with a single sign-in and no local install or credential handling. There are 26 services at launch, including Slack, Figma, Notion, Sentry, Linear, Atlassian Rovo and Work IQ. They work across the Copilot app, CLI, VS Code, Copilot in the cloud and GitHub Mobile. It is a public preview on all Copilot plans.

## Details

**Availability and price**
Public preview, rolling out to all Copilot plans. Copilot Business and Enterprise need an admin to enable the 'Editor preview features' policy. Enterprises with an MCP allowlist must add the GitHub-verified servers. No pricing is stated.

**Caveats**
This is a preview with no GA date. External tools widen prompt-injection exposure (e.g. untrusted Slack text), so use least-privilege scopes. It was announced on 2026-10-28, at the edge of the 7-day window.

**Client use cases**
- Coding agents that read the Jira/Confluence ticket (Atlassian Rovo) and Sentry error before fixing a bug
- Pulling Figma designs into front-end work without hand-built MCP setups
- Bringing Microsoft 365 work context into developer workflows through Work IQ

**How we could offer it**
- Developer-platform assessment: decide which connectors to allow, and add them to the enterprise MCP allowlist
- Pilot with one team, measuring time saved on ticket-to-PR work
- Governance: set the 'Editor preview features' policy, and handle service-side approvals (e.g. Slack MCP access)

**Pitch**
GitHub now ships 26 verified MCP connectors that plug Copilot into Slack, Atlassian, Figma and Microsoft 365 with one sign-in. We can run the rollout and the allowlist governance.

**What it is**
Connectors are GitHub-verified MCP servers. A developer signs in to a service once, and Copilot can then use its context (Slack threads, Figma designs, Sentry errors) on every Copilot surface. Copilot calls a connected service's tools when they are relevant. In the Copilot app, automations can also run a connected service on a schedule. Work IQ is in the list, so Microsoft 365 context can reach coding agents.

**Concepts:** [[GitHub Copilot]] · [[Agents]]
**From:** [[2026-11-04]]

# My notes


---
# References
[GitHub changelog](https://github.blog/changelog/2026-10-28-connect-your-tools-to-copilot-without-all-the-setup)
