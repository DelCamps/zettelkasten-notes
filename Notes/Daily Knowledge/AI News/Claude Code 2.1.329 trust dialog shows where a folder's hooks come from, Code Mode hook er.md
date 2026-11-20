---
date: 2026-11-20
section: AI
importance: High
kind: news
source: "Claude Code changelog"
url: https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
status: unread
id: 2026-11-20-claude-code-2-1-329
---
2026-11-20 07:16
Tags: #daily-knowledge #ai #update

---
# Claude Code 2.1.329 trust dialog shows where a folder's hooks come from, Code Mode hook er

Claude Code 2.1.329 adds a trust-dialog warning naming where a folder's hooks are declared and a warning when hooks in managed settings fail to load. In Code Mode, a PreToolUse hook that errors no longer refuses the script's tool call; hooks that must refuse now need "onFailure": "block". /code-review with no target now reviews the whole branch against the default branch, and 2.1.326's automatic retry after a max_tokens error is removed.

## Details

**Caveats**
The hook change loosens Code Mode's default: an erroring hook used to block the call. Check any hook you rely on as a hard gate.

**For your work**
If client setups use PreToolUse hooks as security gates, add "onFailure": "block" before Code Mode rolls out; re-check gateway max-token settings.

**Method**
- New: trust dialog warning saying where a folder's hooks are declared; in-conversation warning when managed-settings hooks fail to load
- Code Mode: a PreToolUse hook that errors no longer refuses the call (set "onFailure": "block" on hooks that must refuse); Code Mode now also runs with OpenTelemetry events and metrics, and refuses reads of a line range over 256 MiB
- /code-review with no target reviews the whole branch against the default branch; with a PR number it reads the PR via gh pr diff or stops
- Removed 2.1.326's automatic retry at the limit named in a max_tokens error; set CLAUDE_CODE_MAX_OUTPUT_TOKENS behind gateways with lower output limits

**Problem**
Hooks and permission checks are the main guardrails for coding agents; teams need to see where hooks come from and know when they silently fail.

**Results**
- Fixes ~/.claude.json sometimes being reset to defaults after a network stall or file lock
- Fixes Code Mode scripts losing tool access in sessions with more than 4,096 tools, and a runaway Code Mode loop filling memory
- Computer use on macOS moves to newer safety rules, so some actions are refused and some apps get less access

**Concepts:** [[Claude]] · [[Coding agents]] · [[Agent security]]
**From:** [[2026-11-20]]

# My notes


---
# References
[Claude Code changelog](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)
