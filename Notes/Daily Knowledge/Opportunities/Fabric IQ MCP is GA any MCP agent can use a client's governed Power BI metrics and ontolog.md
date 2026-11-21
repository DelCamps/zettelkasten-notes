---
date: 2026-11-21
section: AI
importance: High
kind: value
source: "Microsoft Fabric blog"
url: https://community.fabric.microsoft.com/t5/Fabric-Updates-Blog/Bringing-trusted-Fabric-IQ-context-to-wherever-people-and-agents/ba-p/5423049
status: unread
id: 2026-11-21-fabric-iq-mcp-ga
---
2026-11-21 07:16
Tags: #daily-knowledge #ai

---
# Fabric IQ MCP is GA any MCP agent can use a client's governed Power BI metrics and ontolog

Microsoft made Fabric IQ MCP generally available. It is a remote MCP server that connects any compatible agent or app to Fabric IQ (semantic models, ontologies, OneLake) and keeps users' existing Fabric permissions. Microsoft also announced Fabric IQ plugins for ChatGPT and Claude (preview, coming soon), Fabric IQ in Excel (Insiders Beta), and GA of faster Fabric data agents.

## Details

**Availability and price**
Fabric IQ MCP: generally available. Fabric IQ plugins for ChatGPT and Claude: preview, coming soon. Excel: Insiders Beta. Data agents in Microsoft Copilot: GA coming soon. Faster data agent answers: GA. No pricing given in the post.

**Caveats**
The ChatGPT/Claude plugins and the Copilot data agent GA are not yet available. Value depends on the quality of the client's semantic models and ontologies.

**Client use cases**
- Let a client's Claude, ChatGPT or custom agent answer revenue or margin questions from the same Power BI measures used in the quarterly review
- Ground Foundry agents in governed metrics plus documents, with OneLake row and column security applied per user
- Give finance teams Copilot in Excel answers backed by live, Fabric-connected PivotTables
- Expose Fabric data agents in Copilot Chat and Cowork (GA coming soon)

**How we could offer it**
- Semantic-layer readiness assessment: clean up Power BI models and build Fabric IQ ontologies so agents give consistent numbers
- Multi-assistant rollout: connect Fabric IQ MCP to the client's existing agents with permission testing
- Governance package: register data agents in Agent 365 and trace them with Foundry observability

**Pitch**
Define revenue once and every agent, Microsoft or not, gives the same answer under the user's own permissions. Microsoft says more than 22 million Power BI semantic models are in use every day, so most clients already have the starting point.

**What it is**
A remote Model Context Protocol server for Fabric IQ, the part of Microsoft IQ that holds business definitions: Power BI semantic models, ontologies and OneLake data. It ships with Skills for Fabric, an open-source collection that teaches agents how to work with Fabric.

**Concepts:** [[Power BI and Fabric]] · [[Agents]] · [[Microsoft 365 Copilot]]
**From:** [[2026-11-21]]

# My notes


---
# References
[Microsoft Fabric blog](https://community.fabric.microsoft.com/t5/Fabric-Updates-Blog/Bringing-trusted-Fabric-IQ-context-to-wherever-people-and-agents/ba-p/5423049)
