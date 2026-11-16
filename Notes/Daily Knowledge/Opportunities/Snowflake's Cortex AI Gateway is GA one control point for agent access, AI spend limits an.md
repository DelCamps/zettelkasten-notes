---
date: 2026-11-04
section: AI
importance: High
kind: value
source: "Snowflake press release"
url: https://www.snowflake.com/en/news/press-releases/expedition-2026-business-ontology-ai-gateway/
status: unread
id: 2026-11-04-snowflake-cortex-ai-gateway
---
2026-11-04 07:16
Tags: #daily-knowledge #ai

---
# Snowflake's Cortex AI Gateway is GA one control point for agent access, AI spend limits an

At Expedition 2026 Snowflake made Cortex AI Gateway generally available. It is a single entry point where agents inherit the access policies already set for human users, with GA observability, cost governance with hard spending limits, and Cortex Inference. MCP tool-call governance is in public preview, and sandboxes, abuse detection and model routing are in private preview.

## Details

**Availability and price**
Generally available: the gateway, Observability, Cost Governance and Cortex Inference. Public preview: MCP tool governance. Preview soon: Guardrails and Business Ontology. Private preview: sandboxes, abuse detection, trace intelligence and model routing. No pricing or regions are given.

**Caveats**
Prompt-injection guardrails, sandboxes and abuse detection are not GA yet. It only governs agents that route through Snowflake.

**Client use cases**
- Banks or insurers on Snowflake that need an auditable record of what every agent read and did
- Charging AI spend back to business units, with hard caps per team or agent
- Validating MCP tool calls against authorization policies before they run (public preview)

**How we could offer it**
- Agent governance assessment: map the client's agents and tools onto gateway policies, cost limits and tracing
- Pilot: route one CoCo/CoWork or custom agent through the gateway and report traced spend and tool use
- Managed service: run cost governance and trace reviews; skills needed are Snowflake Horizon, IAM and agent observability

**Pitch**
Snowflake clients can now put every agent behind one gateway that reuses their existing data permissions and enforces hard AI spend limits. That is a ready-made governance engagement for our Snowflake accounts.

**What it is**
Cortex AI Gateway is part of Snowflake Horizon Catalog. It gives agents one entry point that applies the same access policies, authentication and permissions across clouds, frameworks and AI providers, and agents inherit the controls already set for human users. The GA pieces are Observability (model calls, tool use and decisions recorded in the client's own Snowflake account), Cost Governance (spend attributed to users, teams, agents or apps, with hard limits) and Cortex Inference.

**Concepts:** [[Agent security]] · [[Agents]]
**From:** [[2026-11-04]]

# My notes


---
# References
[Snowflake press release](https://www.snowflake.com/en/news/press-releases/expedition-2026-business-ontology-ai-gateway/)
