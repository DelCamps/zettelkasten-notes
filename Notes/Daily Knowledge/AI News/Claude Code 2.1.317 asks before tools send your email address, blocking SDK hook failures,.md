---
date: 2026-11-03
section: AI
importance: Med
kind: news
source: "Claude Code changelog"
url: https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#21317
status: unread
id: 2026-11-03-claude-code-21317
---
2026-11-03 07:16
Tags: #daily-knowledge #ai

---
# Claude Code 2.1.317 asks before tools send your email address, blocking SDK hook failures,

Claude Code 2.1.317 asks before a web or shell tool call sends your account email address to the network. It adds onFailure: "block" for Agent SDK hook callbacks, a cost-report admin API on Claude apps gateways, and a warning when a cloud scheduled task gets connectors you did not ask for. Subagents on a different model now use that model's own effort level.

## Details

**Caveats**
These are changelog statements only. The email check is a single heuristic, not general DLP.

**For your work**
If you run guard hooks through the Agent SDK, set onFailure: "block" so they fail closed. Note that subagent effort changed. The gateway cost endpoint helps with chargeback for client teams.

**Method**
- A new check asks before a web or shell tool call sends the account email address to the network.
- Agent SDK hook callbacks get onFailure: "block", so a crashing guard hook blocks the action instead of letting it run.
- /schedule warns when a new cloud task gets connectors you did not request. The gateway admin API adds GET /v1/organizations/analytics/cost, with spend per developer, per day or per IdP group.
- OTel now carries plan, seat type, provider and custom base URL attributes.

**Problem**
This release closes small agent-safety and admin gaps: identity data leaking through tool calls, hooks that fail open, unrequested connectors on scheduled tasks, and no easy way to read past spend per developer.

**Results**
- Subagents and teammates on a different model use that model's saved or default effort level, not the session's.
- Fixes include partial Grep/Glob results being treated as complete when a search timed out, auto mode failing every turn behind gateways that answer 403/422 to its safety check, and MCP servers disconnecting after the first turn in the desktop app.

**Concepts:** [[Claude]] · [[Coding agents]] · [[Agent security]]
**From:** [[2026-11-03]]

# My notes


---
# References
[Claude Code changelog](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#21317)
