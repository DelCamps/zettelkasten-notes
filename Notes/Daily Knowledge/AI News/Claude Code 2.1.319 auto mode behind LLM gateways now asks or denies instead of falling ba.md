---
date: 2026-11-07
section: AI
importance: High
kind: news
source: "Claude Code changelog"
url: https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#21319
status: unread
id: 2026-11-07-claude-code-2-1-319
---
2026-11-07 07:16
Tags: #daily-knowledge #ai

---
# Claude Code 2.1.319 auto mode behind LLM gateways now asks or denies instead of falling ba

Claude Code 2.1.319 changes auto mode when telemetry or feature flags are off, including behind LLM gateways: calls the server can't check are now asked about or denied, with no fallback to the built-in classifier (Bedrock, Vertex and Foundry unchanged). It also adds permissions.denyInsteadOfPrompting, background MCP tasks and /claude-api latency-optimize, and claude -p now exits 1 when auto mode refused actions.

## Details

**Caveats**
If your gateway strips the server-side review, expect more prompts or denials in auto mode after upgrading; decide explicitly between =0 and =1.

**For your work**
Check CI pipelines that rely on claude -p exit codes, and consider denyInsteadOfPrompting for headless agent jobs so they fail fast rather than hang.

**Method**
- Auto mode: unverifiable calls are asked or denied; CLAUDE_CODE_AUTO_MODE_SERVER=0 keeps the old classifier, =1 forces the server check even with CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS
- permissions.denyInsteadOfPrompting denies any call that would wait on a prompt and lets the turn continue (terminal, subagents, teammates)
- MCP tools run as tasks go to the background immediately; /claude-api latency-optimize tests faster settings against your eval
- Claude apps gateway: spend in /usage, pooled-budget priority rules, login notice, JSON logs

**Problem**
Teams running Claude Code through corporate gateways or with telemetry off were silently getting a weaker, local safety check in auto mode, and unattended runs could stall on permission prompts or report success after refused actions.

**Results**
- claude -p in auto mode now exits 1 (not 0) when actions were refused for lack of a safety check
- Fixes include Bash deny/ask rules missing commands with quoted words and a 401 retry loop breaking other sessions
- /status no longer claims the auto mode server is enabled when a gateway drops it

**Concepts:** [[Coding agents]] · [[Claude]] · [[Agent security]]
**From:** [[2026-11-07]]

# My notes


---
# References
[Claude Code changelog](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#21319)
