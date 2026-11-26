---
date: 2026-11-26
section: AI
importance: Low
kind: news
source: "Codex changelog"
url: https://learn.chatgpt.com/docs/changelog
status: unread
id: 2026-11-26-codex-cli-0-172
---
2026-11-26 07:16
Tags: #daily-knowledge #ai #update

---
# Codex CLI 0.172.0 lets app-server clients choose Amazon Bedrock Runtime, sets per-tool app

OpenAI's Codex CLI 0.172.0 lets app-server clients pick Amazon Bedrock Runtime during setup or sign-in, and lets admins set an approval reviewer for individual connected-app tools in config.toml. Optional stdio MCP servers with cached tool lists now start only on their first tool call, and `codex exec resume` restores saved sandbox permissions and workspace roots.

## Details

**Problem**
Enterprise Codex deployments need non-OpenAI hosting options, finer approval control and faster startup with many MCP servers.

**Method**
- Amazon Bedrock Runtime selectable for app-server clients
- Per-tool approval reviewer for connected app tools in config.toml
- Lazy start for optional stdio MCP servers with cached tool lists
- Spend-limit errors now say which limit was hit; interrupting a parent turn keeps queued child-agent replies

**Results**
- Released 24 November 2026; also bundles an openai-docs skill covering migration to GPT-6.2 Astra and Sol
- Code Mode now uses gRPC for all host connections; the code_mode_host_grpc setting is deprecated

**Caveats**
Incremental release; the changelog gives no performance numbers.

**For your work**
Clients that must keep traffic on AWS can now run Codex through Bedrock, and per-tool approvers help meet four-eyes controls.

**Concepts:** [[Coding agents]] · [[OpenAI enterprise]] · [[AWS]]
**From:** [[2026-11-26]]

# My notes


---
# References
[Codex changelog](https://learn.chatgpt.com/docs/changelog)
