---
date: 2026-11-04
section: AI
importance: Med
kind: news
source: "Claude Code CHANGELOG"
url: https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#21318
status: unread
id: 2026-11-04-claude-code-2-1-318
---
2026-11-04 07:16
Tags: #daily-knowledge #ai

---
# Claude Code 2.1.318 per-job effort for mod side tasks, sign-in expiry warnings, cross-acco

Claude Code 2.1.318 lets a mod run a quick side job at low effort whatever the session uses, reports when a stored claude.ai sign-in expires and warns 10 days ahead in claude -p output, and adds assume_role for AWS upstreams of the Claude apps gateway. It also fixes --continue losing earlier conversation (a 2.1.314 regression), idle compaction swapping a conversation for a non-summary, and SDK sessions reporting success after an API error cut off a reply.

## Details

**Caveats**
Claude Code no longer installs or updates the IDE extension when started in an IDE terminal; subagent progress summaries on Bedrock, Vertex or Foundry may wait up to 5 minutes on a cold cache.

**For your work**
If you run Claude Code headless in CI or for clients, read credential_expires_at to alert before tokens lapse, and use assume_role to bill each developer's usage to the right AWS account.

**Method**
- New effort option on a mod's $.model.fork, so a side job can run at low effort; the result reports the effort sent.
- claude auth status shows loginExpiresAt and claude -p JSON shows credential_expires_at; a stderr warning starts 10 days before a stored sign-in ends.
- Gateway: assume_role on mantle upstreams, for a role in another AWS account and per-developer AWS cost attribution.
- Background subagents move a shell command to the background after 3 minutes on all providers so the prompt cache does not expire.

**Problem**
Unattended and gateway deployments of Claude Code hit silent failures: expired logins, lost conversations, success reported on cut-off replies, and cost that could not be split by AWS account.

**Results**
- Fixes --continue losing the earlier conversation after a malformed tool call's retries ran out (regression in 2.1.314).
- Fixes idle compaction replacing a conversation with a reply that was not a summary, and claude -p / Agent SDK runs reporting success when an API error cut off a reply.
- deniedMcpServers URL entries now also block Anthropic-provided servers and connectors whose upstream URL matches.

**Concepts:** [[Claude]] · [[Coding agents]]
**From:** [[2026-11-04]]

# My notes


---
# References
[Claude Code CHANGELOG](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#21318)
