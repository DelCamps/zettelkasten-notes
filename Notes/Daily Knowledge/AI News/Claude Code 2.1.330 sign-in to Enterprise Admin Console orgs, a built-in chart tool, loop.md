---
date: 2026-11-21
section: AI
importance: High
kind: news
source: "Claude Code changelog"
url: https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
status: unread
id: 2026-11-21-claude-code-2-1-330
---
2026-11-21 07:16
Tags: #daily-knowledge #ai #update

---
# Claude Code 2.1.330 sign-in to Enterprise Admin Console orgs, a built-in chart tool, loop

Claude Code 2.1.330 (published 20 November) lets users sign in to organizations managed in Anthropic's Enterprise Admin Console, which then apply the org's settings and cloud provider or gateway, and adds easel, a built-in chart tool on Pro, Max and some Team and Enterprise plans. Recurring scheduled tasks and /loop now run up to 30 days instead of 7, more rm commands aimed at root, home or the working folder ask for approval, and a long list of fixes covers freezes after compaction, WebFetch hangs, worktree deletion and MCP schema failures.

## Details

**Caveats**
Changelog only, no dates or rollout details; easel is limited to macOS and Linux and to some plans. Tasks made before this release still end at 7 days. deniedMcpServers name entries now hide only the named connector, so block lists may need the exact URL.

**For your work**
If you manage Claude Code for a client team, the Admin Console sign-in is the cleaner way to enforce provider and settings centrally. Re-check any deniedMcpServers rules and long /loop jobs after upgrading.

**Method**
- New: sign-in to Enterprise Admin Console organizations; after claude auth login, Claude Code applies the org's settings and uses its cloud provider or gateway.
- New: easel, a built-in mod that draws charts on request and under MCP metrics results (turn off in /config).
- Changed: scheduled tasks and /loop run up to 30 days; more rm commands at sensitive locations ask for approval and are refused where nobody can answer.
- VS Code: /fork, /workflows and a setting so Escape does not stop Claude.

**Problem**
Enterprise teams need Claude Code to pick up central org settings, and long-running agent sessions kept hitting freezes, lost settings and unsafe file deletions.

**Results**
- Fixed freezes of up to several minutes after compacting a very long conversation.
- Fixed ExitWorktree deleting a worktree another running session was using.
- Fixed turns failing with 'JSON schema is invalid' when many MCP tools have schemas the API refuses.
- Reverted 2.1.329's removal of the automatic retry when max_tokens exceeds a model's or gateway's limit.

**Concepts:** [[Claude]] · [[Coding agents]]
**From:** [[2026-11-21]]

# My notes


---
# References
[Claude Code changelog](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)
