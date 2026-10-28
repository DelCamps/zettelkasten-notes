---
date: 2026-10-28
section: AI
importance: Med
kind: news
source: "Claude Code changelog"
url: https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
status: unread
id: 2026-10-28-claude-code-2-1-311-312
---
2026-10-28 07:16
Tags: #daily-knowledge #ai

---
# Claude Code 2.1.311-312 ultrathink means xhigh, a hook concurrency cap, subagent MCP fixes

Claude Code shipped 2.1.311 (26 Oct) and 2.1.312 (27 Oct). 'ultrathink' now runs a turn at xhigh effort on Opus/Sonnet/Haiku 5.5 and Fable 5.1. Prompt and agent hooks are capped at 24 concurrent per session. Several MCP, subagent and compaction bugs are fixed.

## Details

**Caveats**
These are changelog claims, not measured improvements. The silent switch to a shorter system prompt on custom Foundry/Bedrock deployment names can change behaviour.

**For your work**
If you run Claude Code on Azure Foundry behind custom deployment names, check the system-prompt change. Hook-heavy setups should expect the new concurrency cap.

**Method**
- ultrathink in the terminal now sets xhigh effort, and typed mid-turn it raises effort for the rest of that turn
- Hooks run at most 24 at a time per session (subagents included); a timeout under 1s counts as 1s
- On Bedrock, Vertex, Foundry and Mantle, unrecognized deployment names now get the shorter system prompt (set CLAUDE_CODE_SIMPLE_SYSTEM_PROMPT=0 to opt out); model settings load from a signed catalog file (CLAUDE_CODE_MODEL_CATALOG=off)
- New oidc.user_id_claim for the Claude apps gateway (for example Entra ID's oid)

**Problem**
Long agent sessions were hitting harness bugs: subagents could not use MCP servers that connected late, Claude saw stale CLAUDE.md content after compaction, and sessions over 200K tokens stopped with '1M context credits required'.

**Results**
- Over-200K standard-context sessions now compact and continue instead of failing
- Write no longer overwrites a very large CLAUDE.md after reading only its start
- Retries the API marked not-retryable no longer hang turns

**Concepts:** [[Claude]] · [[Coding agents]]
**From:** [[2026-10-28]]

# My notes


---
# References
[Claude Code changelog](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)
