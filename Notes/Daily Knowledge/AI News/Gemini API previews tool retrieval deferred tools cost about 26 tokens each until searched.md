---
date: 2026-11-20
section: AI
importance: Med
kind: news
source: "Gemini API changelog"
url: https://aistudio.google.com/docs/tool-retrieval
status: unread
id: 2026-11-20-gemini-api-tool-retrieval
---
2026-11-20 07:16
Tags: #daily-knowledge #ai

---
# Gemini API previews tool retrieval deferred tools cost about 26 tokens each until searched

Google's Interactions API can now search a tool library and load function schemas only when needed: tools marked defer_loading show the model just a name and short description, and a tool_search tool (server or client side) fetches full schemas. Google's illustrative 200-tool example drops from about 164,000 to about 23,650 input tokens. Separately, the Gemini API now accepts Word, PowerPoint and Excel files and can process only chosen pages, sheets, cell ranges or time intervals.

## Details

**Caveats**
Retrieved schemas cannot be unloaded, server and client retrieval cannot be mixed, and a query matching no tool returns text rather than a structured error. The docs say static loading suits fewer than about 20 stable tools.

**For your work**
A ready pattern for agents with many MCP servers; compare with Anthropic's tool search when choosing a platform for tool-heavy agents.

**Method**
- Mark function or mcp_server tools with defer_loading: true; the model sees only name and description (about 26 tokens per deferred tool in early testing)
- Exactly one tool_search tool per request, with execution "server" (default, single API call) or "client" (your app returns declarations, one extra round trip)
- Deferring an mcp_server defers every tool it exposes
- Preview, v1beta, Interactions API only; supported on gemini-4-hydrogen, gemini-4-argon, gemini-3.8-flash and gemini-3.6-flash

**Problem**
Agents with large tool libraries or several MCP servers pay to send every tool schema on every request, and long tool lists hurt tool choice.

**Results**
- Illustrative example (round numbers, not measurements): 200 tools at 400 tokens each, about 164,000 input tokens static vs about 23,650 with retrieval across two requests
- No separate charge; each server-side search runs another model pass billed at normal rates
- Also new (18 November): direct Word, PowerPoint and Excel input, and slicing by page range, worksheet, cell range, time interval or content layer

**Concepts:** [[Agents]] · [[Google Cloud]] · [[Inference efficiency]]
**From:** [[2026-11-20]]

# My notes


---
# References
[Gemini API changelog](https://aistudio.google.com/docs/tool-retrieval)
