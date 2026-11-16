---
date: 2026-11-10
section: AI
importance: High
kind: value
source: "Microsoft Copilot Blog (Tech Community)"
url: https://techcommunity.microsoft.com/blog/microsoft-copilot-blog/turn-copilot-insights-into-action-with-connector-write-capabilities/4571160
status: unread
id: 2026-11-10-copilot-connector-write-actions-ga
---
2026-11-10 07:16
Tags: #daily-knowledge #ai

---
# Copilot connector write actions are GA Copilot Chat and Cowork can now create, update and

Microsoft has made write actions for Copilot connectors generally available in Copilot Chat and Cowork. Users ask in plain language, review a confirmation card and approve, and Copilot changes the record in the connected app using the user's own permissions. Write actions in the Office apps are 'coming soon'.

## Details

**Availability and price**
Generally available in Copilot Chat and Cowork (announced 9 Nov 2026). Federated connectors need a Microsoft 365 Copilot license. Write actions only work where the connector publisher provides write tools. No price change mentioned.

**Caveats**
Researcher stays read-only. Not yet in Word, Excel, PowerPoint or Outlook. 'Always allow' removes the confirmation step for that tool, so clients need a policy on its use. Actions send customer data to the third-party service, so review each connector's privacy and third-party terms first.

**Client use cases**
- Turn a Teams meeting transcript into Jira work items with acceptance criteria (Atlassian Rovo connector)
- Draft a Statement of Work under an existing MSA and save it to the right iManage matter
- Turn approved Excel rows into records in a connected accounting system, or log a CRM activity and follow-up task after a call
- Update Notion project pages from weekly status emails

**How we could offer it**
- Connector-to-action pilots: pick 2-3 systems of record a client already owns, enable their federated connectors and write scenario playbooks
- Governance package: tenant settings for publisher types, staged rollout, tool-level blocking, default approval policy and user/help-desk guidance
- Custom MCP connectors with write tools for client line-of-business systems, published to the client's tenant

**Pitch**
Copilot can now close the loop: the summary becomes the ticket, the CRM entry or the draft contract, with a human approving each change. We set up the connectors and the guardrails so this is safe at scale.

**What it is**
MCP-based federated Copilot connectors can now run the write, update and delete tools their publishers expose, not just read data. Write tools start at 'Needs approval'. Per tool, users can choose Allow once, Allow for conversation or Always allow. Admins can review each connector's tools in the Microsoft 365 admin center and audit activity in Purview.

**Concepts:** [[Microsoft 365 Copilot]] · [[Agents]]
**From:** [[2026-11-10]]

# My notes


---
# References
[Microsoft Copilot Blog (Tech Community)](https://techcommunity.microsoft.com/blog/microsoft-copilot-blog/turn-copilot-insights-into-action-with-connector-write-capabilities/4571160)
