---
date: 2026-11-14
section: AI
importance: Med
kind: value
source: "Databricks blog"
url: https://www.databricks.com/blog/bring-your-business-context-chatgpt-claude-microsoft-copilot-cowork-and-grok-bot
status: unread
id: 2026-11-14-genie-plugins
---
2026-11-14 07:16
Tags: #daily-knowledge #ai

---
# Databricks Genie plugins bring governed business data into Microsoft Copilot Cowork, ChatG

Databricks released Genie plugins that let Copilot Cowork, ChatGPT, Claude and Grok Bot ask Genie business questions: Genie interprets terms with its Genie Ontology, runs SQL over data the user may see, and returns cited answers. Agents without a native plugin can use the Genie MCP server.

## Details

**Availability and price**
Described as working natively 'today' in the four clients; the post gives no GA or preview label, regions or prices.

**Caveats**
Answer quality depends on how well the client's Genie Ontology and metric definitions are built; status and pricing need confirming with Databricks.

**Client use cases**
- Copilot Cowork preparing client-meeting briefings, Excel overviews and decks from Azure Databricks metrics
- Analysts using Claude to explain a revenue miss with certified metric definitions
- Always-on agents (ChatGPT dots, Grok Bot) checking adoption or campaign metrics on a schedule

**How we could offer it**
- Semantic-layer project: define certified metrics in Genie Ontology once, then expose them to every agent the client uses
- Pilot in Microsoft 365 for Azure Databricks clients via the Cowork plugin, with permission and approval checks
- Governance review of which agents may query which data through the MCP server

**Pitch**
Databricks clients can now give Copilot Cowork and other agents the same certified numbers finance reports; we can build the definitions and roll out the plugins.

**What it is**
Plugins that give third-party agents a governed interface to Databricks. An agent can hand a business question to Genie, which resolves business terms using Genie Ontology (governed definitions plus learned organisational knowledge), finds data across tables and documents, writes and runs SQL and returns an answer with citations. Or the agent keeps the task and asks Genie only for missing context. Genie can route questions to domain Genie Agents (for example finance or marketing), and clients that support MCP Apps get interactive charts in the chat.

**Concepts:** [[Microsoft 365 Copilot]] · [[Agents]] · [[RAG]]
**From:** [[2026-11-14]]

# My notes


---
# References
[Databricks blog](https://www.databricks.com/blog/bring-your-business-context-chatgpt-claude-microsoft-copilot-cowork-and-grok-bot)
