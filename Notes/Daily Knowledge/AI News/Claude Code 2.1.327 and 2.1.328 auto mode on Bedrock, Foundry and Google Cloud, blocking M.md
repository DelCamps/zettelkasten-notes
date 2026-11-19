---
date: 2026-11-19
section: AI
importance: Med
kind: news
source: "Claude Code changelog"
url: https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
status: unread
id: 2026-11-19-claude-code-2-1-328
---
2026-11-19 07:16
Tags: #daily-knowledge #ai #update

---
# Claude Code 2.1.327 and 2.1.328 auto mode on Bedrock, Foundry and Google Cloud, blocking M

Two releases since the last brief. 2.1.328 brings auto mode to Opus 4.6 and Sonnet 4.6 on Amazon Bedrock, Google Cloud's Agent Platform, Microsoft Foundry and the Claude apps gateway, and adds "onFailure": "block" for mcp_tool hooks. 2.1.327 adds claude mcp add-json from stdin, so tokens stay off the command line, and a /status list of broken agent, skill and hook files.

## Details

**Caveats**
Changelog entries only; auto mode on third-party providers covers Opus 4.6 and Sonnet 4.6.

**For your work**
For clients on Foundry or Bedrock, auto mode is now an option. Set onFailure: block on any security-relevant MCP hooks, and move MCP setup scripts to add-json from stdin so tokens stay out of shell history.

**Method**
- mcp_tool hooks can now block the action when the hook call itself fails, as command and HTTP hooks already could
- Automatic compaction now rebuilds the system prompt the way /compact does, instead of reusing the old one
- MCP tools whose schemas start with anyOf, oneOf or allOf no longer go missing; a tool with an invalid schema is left out and Claude is told why
- Self-hosted runner: new labels, metadata and orchestrator metrics for spawn-runner hooks

**Problem**
Enterprise users on cloud providers lacked auto mode, and hook or MCP failures could silently let actions through.

**Results**
- 2.1.327: only the first 100 @-mentions are looked up as files; WebFetch refuses URLs over 2,000 characters before any permission prompt; claude -p moves on after 10 seconds if fetching model settings stalls
- 2.1.327: remote MCP servers that dropped (for example, after a VPN outage) are retried in the background for about a day
- Many Code Mode fixes in 2.1.328 around resuming, permissions and background scripts

**Concepts:** [[Claude]] · [[Coding agents]] · [[Agent security]]
**From:** [[2026-11-19]]

# My notes


---
# References
[Claude Code changelog](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)
