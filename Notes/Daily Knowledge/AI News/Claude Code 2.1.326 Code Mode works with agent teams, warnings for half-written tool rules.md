---
date: 2026-11-17
section: AI
importance: Med
kind: news
source: "Claude Code changelog"
url: https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
status: unread
id: 2026-11-17-claude-code-2-1-326
---
2026-11-17 07:16
Tags: #daily-knowledge #ai #update

---
# Claude Code 2.1.326 Code Mode works with agent teams, warnings for half-written tool rules

Claude Code 2.1.326 (16 November) lets Code Mode run alongside agent teams and warns at startup when an --allowedTools, --disallowedTools or --tools entry is not a complete rule. Fixes include file-deleting Bash commands being shown as reads and permission rules that looked saved when the settings file could not be written.

## Details

**Caveats**
Mostly fixes; no new model or pricing change.

**For your work**
If clients audit Claude Code through OpenTelemetry, upgrade so hook denials are logged, and use the new startup warning to catch malformed tool allowlists in scripted runs.

**Method**
- Code Mode can now be turned on while agent teams are enabled
- Startup warning for incomplete tool rules; /status row when a provider or DISABLE_TELEMETRY turns features off
- OTEL_RESOURCE_INCLUDE_HOST adds host.name and host.id to OpenTelemetry attributes (off by default)

**Problem**
Silent failures in permissions, settings and auth make it hard to know what a coding agent is actually allowed to do.

**Results**
- Fixed: cp refused when only its source matched an Edit deny rule; find -delete, cat a > b and sort -o summed up as a search or read
- Fixed: managed PreToolUse hooks that refused a call left no OpenTelemetry tool_decision event
- Fixed: compaction on Bedrock, Vertex and Foundry sometimes replying instead of summarizing; Vertex sessions stuck on a 30 MB request-size 400 error
- Settings values nested past 64 levels are now dropped with a warning

**Concepts:** [[Claude]] · [[Coding agents]]
**From:** [[2026-11-17]]

# My notes


---
# References
[Claude Code changelog](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)
