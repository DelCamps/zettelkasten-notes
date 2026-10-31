---
date: 2026-10-31
section: AI
importance: Med
kind: news
source: "Claude Code changelog"
url: https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#21316
status: unread
id: 2026-10-31-claude-code-2-1-316
---
2026-10-31 07:16
Tags: #daily-knowledge #ai

---
# Claude Code 2.1.316 subagent effort setting, Opus 4.8 fast mode deprecated, gateway model

Claude Code 2.1.316 adds CLAUDE_CODE_SUBAGENT_EFFORT and a switch to turn off the ultrathink keyword. It deprecates fast mode on Opus 4.8 as of October 30, 2026, with removal on November 30, 2026. It also fixes the Claude apps gateway, which was not checking every model a request names against the allow and deny lists.

## Details

**Problem**
Teams running Claude Code at scale need control over subagent cost and model policy, and need to plan for the end of Opus 4.8 fast mode.

**Method**
- New environment variables: CLAUDE_CODE_SUBAGENT_EFFORT sets the effort level of subagents that are not given one, instead of inheriting the session's; CLAUDE_CODE_DISABLE_ULTRATHINK turns the keyword off.
- Gateway: a pooled_budget that a group's members share; managed.policy_mode: layered, which merges every matching policy; guardrail.input_tagging for Amazon Bedrock prompt-attack filters.
- Fast mode on Opus 4.8 is deprecated. After November 30, 2026 those requests return an error instead of falling back, and Anthropic says to migrate to Opus 5.5.

**Results**
- Security-relevant fixes: the gateway now checks every model a request names against availableModels, deniedModels and models, and returns a 400 for a blocked one. --restricted sessions no longer upload files from outside the working directories.
- Reliability fixes: shell commands left running after exit, bash scripts stopping when SHELLOPTS is exported, sub-agents switching models when woken, and Grep and Glob hanging at timeout on Windows.

**Caveats**
This is a changelog with no performance numbers. The gateway model-check gap means policies set before this version may not have been enforced.

**For your work**
Set CLAUDE_CODE_SUBAGENT_EFFORT lower than the main session to cut cost on multi-agent runs. Search any API code for claude-opus-4-8 with speed 'fast' before November 30.

**Concepts:** [[Claude]] · [[Coding agents]] · [[Multi-agent systems]]
**From:** [[2026-10-31]]

# My notes


---
# References
[Claude Code changelog](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#21316)
