---
date: 2026-11-04
section: AI
importance: Med
kind: value
source: "Microsoft Fabric blog"
url: https://community.fabric.microsoft.com/t5/Fabric-Updates-Blog/OneLake-The-file-system-for-agent-first-data-engineering/ba-p/5383035
status: unread
id: 2026-11-04-onelake-hosted-mcp-discovery
---
2026-11-04 07:16
Tags: #daily-knowledge #ai

---
# Fabric OneLake gets a hosted MCP server and an endpoint discovery API so agents can find a

Microsoft says OneLake now has a remotely hosted MCP server (preview), so agents can explore and manage Fabric data without installing a local server. A new endpoint discovery API (preview) tells an agent which Fabric engines, MCP servers and skills can query each item. In Microsoft's demo, GitHub Copilot in VS Code answered data questions and ran a Spark analysis from plain prompts.

## Details

**Availability and price**
The hosted OneLake MCP server and the endpoint discovery API are both in preview. The post gives no pricing or regional details.

**Caveats**
Both are previews, and the post says they rolled out 'over the last few weeks'. The MCP tools include write operations, so scope permissions carefully.

**Client use cases**
- Let analysts ask a coding agent questions about mirrored databases and get engine-specific queries
- Auto-document a client's lakehouse, including its OneLake security roles
- Combine SharePoint/OneDrive files with mirrored data through shortcuts, from one prompt

**How we could offer it**
- Pilot: connect GitHub Copilot or a Foundry agent to a client's OneLake through the hosted MCP server and discovery API
- Governance: review OneLake security and MCP allowlists before agents get write tools
- Skills needed: Fabric/OneLake, MCP, agent skills authoring

**Pitch**
Fabric clients can now point agents at OneLake with nothing to install, and the agent works out how to query each dataset. That makes a quick 'talk to your lakehouse' pilot.

**What it is**
This is a set of OneLake features for agent-first data engineering. The first is a remotely hosted OneLake MCP server (preview); the local MCP option remains. New tools in the Fabric Core MCP server manage shortcuts and OneLake security. The second is an endpoint discovery API (preview). For each item it returns the available Fabric engines (for example SQL analytics or Spark), their MCP servers, the matching skill from Microsoft's skills-for-fabric repo, and the OneLake Table and File APIs. With these, an agent can connect directly or through tools like DuckDB. Agents work within the user's existing permissions.

**Concepts:** [[Power BI and Fabric]] · [[Agents]]
**From:** [[2026-11-04]]

# My notes


---
# References
[Microsoft Fabric blog](https://community.fabric.microsoft.com/t5/Fabric-Updates-Blog/OneLake-The-file-system-for-agent-first-data-engineering/ba-p/5383035)
