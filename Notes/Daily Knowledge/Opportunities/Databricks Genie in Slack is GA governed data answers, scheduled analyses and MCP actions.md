---
date: 2026-11-13
section: AI
importance: Low
kind: value
source: "Databricks blog"
url: https://www.databricks.com/blog/genie-slack-now-generally-available-governed-ai-cowork-right-where-work-happens
status: unread
id: 2026-11-13-databricks-genie-slack-ga
---
2026-11-13 07:16
Tags: #daily-knowledge #ai

---
# Databricks Genie in Slack is GA governed data answers, scheduled analyses and MCP actions

Users can DM or @mention Genie in Slack for answers, tables and charts grounded in Databricks data, schedule recurring analyses and let it act in other tools via MCP after approval. Every question runs under the asker's own Unity Catalog permissions.

## Details

**Availability and price**
Generally available as of 12 November 2026; install from the Slack Marketplace. Private Link workspaces supported via context-based ingress policies. No pricing given.

**Caveats**
Slack only; the post does not mention Microsoft Teams. Responses are visible to the whole channel by default unless admins change the default. No adoption or accuracy figures given.

**Client use cases**
- Sales or finance teams asking KPI questions in their team channel
- Weekly automated metric reports delivered to a manager's DM
- Ops teams triggering approved follow-up actions in Jira from a data answer

**How we could offer it**
- Add Slack delivery to existing Databricks Genie or data-agent implementations
- Governance setup: Unity Gateway MCP policies, approval rules and private-response defaults

**Pitch**
Put governed company data answers where the team already talks, without widening anyone's access.

**What it is**
A Slack Marketplace app connecting Slack channels and DMs to a Databricks workspace, using Genie One by default or a specific Genie Agent per channel. It can search connected sources such as Google Drive, Confluence and Jira, take actions through MCP connectors with approval, accept file uploads, return PDFs and deliver scheduled reports. Admins govern MCP policies, cost controls, monitoring and traces in Unity Gateway.

**Concepts:** [[Agents]]
**From:** [[2026-11-13]]

# My notes


---
# References
[Databricks blog](https://www.databricks.com/blog/genie-slack-now-generally-available-governed-ai-cowork-right-where-work-happens)
