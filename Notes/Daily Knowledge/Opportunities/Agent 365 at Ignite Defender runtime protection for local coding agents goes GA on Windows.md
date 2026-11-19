---
date: 2026-11-19
section: AI
importance: High
kind: value
source: "Microsoft Agent 365 blog"
url: https://techcommunity.microsoft.com/blog/agent-365-blog/whats-new-in-microsoft-agent-365-ignite-2026/4571753
status: unread
id: 2026-11-19-agent365-local-agent-security-ga
---
2026-11-19 07:16
Tags: #daily-knowledge #ai

---
# Agent 365 at Ignite Defender runtime protection for local coding agents goes GA on Windows

Microsoft's Agent 365 Ignite update makes Defender runtime protection for local agents (Claude Code, GitHub Copilot CLI, OpenClaw, ChatGPT Desktop) generally available on Windows in Audit or Block mode, and Defender plus Global Secure Access now discover more than 60 local AI agents. Plugins and skills governance and the Tools Registry are also GA, while Purview DLP for local agents and Entra Agent ID for Salesforce, AgentCore, Vertex AI, Databricks, Snowflake and others are in preview.

## Details

**Availability and price**
Runtime protection: GA on Windows. Local agent discovery: GA on managed Windows and macOS. Plugins and skills governance and Tools Registry: GA. Many other items in preview; Action center preview in December. Expanded usage insights need qualifying Microsoft 365 subscriptions, premium capabilities an Agent 365 or ME7 licence. No prices given. More than 50 million agents registered since the May 2026 launch.

**Caveats**
Microsoft Learn's runtime protection page is still labelled preview and lists a known issue where Claude Code may keep processing a tool response after a post-tool-response block; network inspection does not cover certificate pinning or HTTP/3. Prompt evidence snippets in alerts are not redacted. Licence requirements for runtime protection are not stated in the blog.

**Client use cases**
- Let developers use Claude Code or GitHub Copilot CLI on corporate laptops with prompt-injection blocking and SOC alerts
- Inventory shadow coding agents and their MCP servers across the estate
- Control which Copilot plugins and skills each business unit can use
- Bring non-Microsoft agents (Salesforce, AgentCore, Vertex AI, Snowflake) under one identity and registry

**How we could offer it**
- Local-agent security assessment: discovery run, then Audit-mode pilot before switching to Block
- Agent governance implementation: plugin/skill assignment, Tools Registry, Entra Agent ID across platforms
- Managed service for agent security operations alongside Defender and Purview (skills: Defender for Endpoint, Intune, Entra, Agent 365)

**Pitch**
Clients want coding agents on developer machines but fear prompt injection and data loss; Microsoft now ships GA blocking and discovery for them, and we can roll it out as a governed 'safe AI developer workstation' package.

**What it is**
A set of Agent 365 control-plane updates announced at Ignite. GA: Defender runtime protection for local agents on Windows (inspects the agent loop for prompt injection and harmful actions; Audit or Block mode set in the Defender portal or Intune), local agent discovery on managed Windows and macOS devices tied to device and user, plugins and skills governance (assign plugins and skills to users and groups in Microsoft 365 Copilot and Copilot Cowork), and the Tools Registry (one view of the tools agents use). Preview: Purview DLP for Microsoft and local agents, Entra Agent ID for local agents and for agents on connected platforms, shadow AI discovery, MCP server governance via Azure AI Gateway and LiteLLM, and multi-tenant agent management.

**Concepts:** [[Agent security]] · [[Coding agents]] · [[Microsoft 365 Copilot]]
**From:** [[2026-11-19]]

# My notes


---
# References
[Microsoft Agent 365 blog](https://techcommunity.microsoft.com/blog/agent-365-blog/whats-new-in-microsoft-agent-365-ignite-2026/4571753)
