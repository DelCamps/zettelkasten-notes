---
date: 2026-11-21
section: AI
importance: Med
kind: value
source: "Microsoft Fabric blog"
url: https://community.fabric.microsoft.com/t5/Fabric-Updates-Blog/Fabric-Data-Warehouse-at-Ignite-Built-for-AI-era-analytics/ba-p/5414274
status: unread
id: 2026-11-21-fabric-warehouse-agentic-ignite
---
2026-11-21 07:16
Tags: #daily-knowledge #ai

---
# Fabric Data Warehouse tunes for agent workloads a remote MCP server, Agent Skills, GA cust

Microsoft's Fabric Data Warehouse Ignite update targets 'machine-paced' agent queries. It adds a remote Data Warehouse MCP server and Agent Skills so coding agents can explore schemas, write SQL and troubleshoot. Metadata sync for the SQL analytics endpoint and custom SQL pools are GA, on-demand billing with budget ceilings is in preview, and Microsoft says performance improved 70% on an industry-standard benchmark over the past year.

## Details

**Availability and price**
GA: SQL analytics endpoint metadata sync, custom SQL pools. Preview: on-demand billing. Limited preview: GPU query acceleration, Live Query Troubleshooting. Limited private preview: Warehouse Clones. Cache cooldown arrives in January 2027. The post does not state the release stage of the MCP server.

**Caveats**
Many pieces are preview or coming soon. The 70% figure is Microsoft's own benchmark claim.

**Client use cases**
- Let coding agents (GitHub Copilot, Claude Code) build and debug warehouse SQL against real schemas
- Data agents in Teams or Copilot that answer from governed warehouse data
- Cap agent-driven query spend with workspace-level ceilings
- Agent-assisted Synapse dedicated SQL pool and Teradata migrations to Fabric

**How we could offer it**
- Agent-ready warehouse assessment: workload isolation with custom SQL pools and budget controls
- Migration factory that uses the Synapse migration skill and Migration Assistant
- Data agent build-out grounded in Fabric IQ ontologies

**Pitch**
Agents query far more often than people do. We can make the client's warehouse fast, safe and affordable for them.

**What it is**
A set of Fabric Data Warehouse updates for agentic analytics. Agents get direct access through a remote MCP server and Agent Skills. Fabric IQ ontologies ground data agents, which can be published to Teams, Microsoft 365 Copilot or Copilot Studio. New cost and workload controls and migration tooling (Teradata, Synapse) round it out.

**Concepts:** [[Power BI and Fabric]] · [[Agents]] · [[Coding agents]]
**From:** [[2026-11-21]]

# My notes


---
# References
[Microsoft Fabric blog](https://community.fabric.microsoft.com/t5/Fabric-Updates-Blog/Fabric-Data-Warehouse-at-Ignite-Built-for-AI-era-analytics/ba-p/5414274)
