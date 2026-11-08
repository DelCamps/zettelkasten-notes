---
date: 2026-11-08
section: AI
importance: Low
kind: news
source: "GitHub changelog"
url: https://github.blog/changelog/2026-11-06-github-copilot-weekly-releases-november-2
status: unread
id: 2026-11-08-copilot-app-weekly-nov-2
---
2026-11-08 07:16
Tags: #daily-knowledge #ai

---
# GitHub Copilot weekly Agent Merge, assisted tool approvals in the Copilot app, and VS Code

GitHub's weekly Copilot roundup adds Agent Merge (Copilot merges a PR once checks and rules pass) and 'assisted approval', where you tell Copilot which tool requests it may approve without asking. VS Code 1.145 adds cron-scheduled local automations and remote previews in the Agents window; no models were added or removed.

## Details

**Caveats**
The post does not say which plans get each feature. Several VS Code items are experimental or preview.

**For your work**
Assisted approval and Agent Merge move more trust decisions to the agent; decide where you would allow them in client repos before developers switch them on.

**Method**
- Copilot app: Agent Merge set from a PR stays enabled while required checks or rules are pending
- Assisted approval: personal instructions on which tool requests to auto-approve; opt-in, local sessions only
- Context-limit errors now offer to compact the chat or show what is using space
- Copilot CLI /settings becomes one searchable dashboard for plugins and MCP servers; VS Code 1.145 local automations accept cron expressions and workspace custom agents

**Problem**
Long-running agent sessions stall on merges, approvals and context limits that need a human.

**Results**
- No model changes this week
- Also lists the already-covered JetBrains Air and Xcode integrations

**Concepts:** [[GitHub Copilot]] · [[Coding agents]]
**From:** [[2026-11-08]]

# My notes


---
# References
[GitHub changelog](https://github.blog/changelog/2026-11-06-github-copilot-weekly-releases-november-2)
