---
date: 2026-11-14
section: AI
importance: Low
kind: news
source: "Codex changelog"
url: https://learn.chatgpt.com/docs/changelog
status: unread
id: 2026-11-14-codex-cli-0-169
---
2026-11-14 07:16
Tags: #daily-knowledge #ai #update

---
# Codex CLI 0.169.0 side-chat tabs, custom model providers from the terminal, and untrusted

OpenAI's Codex CLI 0.169.0 adds multiple side-chat tabs, search in the agent command center, and adding or editing custom model providers (including gateway sign-in by device code) from the terminal. A fix keeps project configuration and MCP servers disabled in untrusted directories for codex exec, even with --sandbox workspace-write.

## Details

**Caveats**
Mostly workflow polish; several features are opt-in.

**For your work**
If you run Codex in CI against client repos, check that untrusted checkouts no longer load project MCP servers and add --trust only where intended.

**Method**
- Opt-in terminal workspace with multiple side-chat tabs that reopen after a restart
- Search older tasks by name, prompt preview or working directory; optional 'Collapse turn details' view
- Custom model providers can be created or edited in the terminal; supported gateways can sign in by device code over SSH
- Opt-in Cloud connection on macOS and Linux to send images, pick model and reasoning effort, and archive Cloud conversations

**Problem**
Codex users juggling several conversations, custom gateways and untrusted repositories needed better terminal workflows and safer defaults.

**Results**
- codex exec keeps project config and MCP servers off in untrusted directories; use --trust to save project trust
- 'Yes, clear context and implement' now hands the full approved plan to a fresh session
- Windows sandbox fixes for quoted cmd.exe paths and PowerShell sessions; bundled SQLite updated to 3.54

**Concepts:** [[Coding agents]] · [[OpenAI enterprise]]
**From:** [[2026-11-14]]

# My notes


---
# References
[Codex changelog](https://learn.chatgpt.com/docs/changelog)
