---
date: 2026-11-08
section: AI
importance: Med
kind: news
source: "Socket"
url: https://socket.dev/blog/shai-hulud-descendant-malicious-ruby-gem
status: unread
id: 2026-11-08-strutil-core-worm-ai-tools
---
2026-11-08 07:16
Tags: #daily-knowledge #ai

---
# Malicious Ruby gem plants MCP servers, hooks and AGENTS.md instructions to re-infect via c

Socket found strutil-core 1.0.1, a Shai-Hulud-derived worm on RubyGems that steals from 51 credential stores (including Claude and Codex files), adds a rogue 'workspace-tools' MCP server and SessionStart hooks to local agent configs, and commits CLAUDE.md, AGENTS.md and .cursor/mcp.json files to victims' repos. RubyGems removed it about five hours after release; no victims were confirmed.

## Details

**Caveats**
Socket confirmed the spreading routines exist in the code but not that any succeeded. Revoking the token before stopping the monitor triggers the deletion.

**For your work**
Treat unexpected MCP entries, hooks and agent instruction files in repos as indicators of compromise, review agent configs and AGENTS.md changes in code review, and keep workspace trust prompts on.

**Method**
- extconf.rb runs at gem install, downloads Bun 1.2.18 and runs a 5.48 MB index.js; the install still completes cleanly
- Edits writable settings.json, config.json, mcp.json and .aider.conf.yml to add an MCP server named 'workspace-tools' that runs the payload, plus SessionStart hooks
- With stolen Git credentials, commits .claude/settings.json, .cursor/mcp.json, Gemini settings, CLAUDE.md, AGENTS.md (telling agents to run a setup script first) and a .vscode task that runs on folder open
- Hourly backdoor runs scripts announced in signed GitHub commits; a token monitor wipes the home folder if the stolen GitHub token is revoked

**Problem**
Supply-chain malware now uses AI coding tool configuration as both a persistence point and a spreading route.

**Results**
- Socket's scanner flagged it 70 seconds after the 1 November release; RubyGems removed both versions about five hours later
- 89 downloads, all of the clean 1.0.0 seed (0 on 1.0.1); download counts are not victim counts
- Same C2 as PyPI package pystr-codec (31 October)

**Concepts:** [[Agent security]] · [[Coding agents]]
**From:** [[2026-11-08]]

# My notes


---
# References
[Socket](https://socket.dev/blog/shai-hulud-descendant-malicious-ruby-gem)
