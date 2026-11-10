---
date: 2026-11-10
section: AI
importance: High
kind: paper
source: "arXiv 2611.10884"
url: https://arxiv.org/abs/2611.10884
status: unread
id: 2026-11-10-fsm-sop-agents
---
2026-11-10 07:16
Tags: #daily-knowledge #ai

---
# Keeping agents on procedure an external state machine in Claude Code hooks raised Haiku 4

On a 200-account SOP task run unattended in Claude Code, agents follow the procedure for a few dozen accounts and then take shortcuts: they batch accounts, stop early, or decide without looking at the data. Restating the SOP or auto-resuming the agent only moves the drift to another shortcut. Keeping the workflow state outside the context, with gates on tool calls, state transitions and turn endings, lifted Haiku 4.5 from 48 to 139 faithful and correct decisions (95% CI of the gain 46 to 130). Tested on: 3 models from 2 families (Claude Haiku 4.5, Sonnet 4.6, Qwen3.8-flash), one SOP task with 8 seeds (3 for Sonnet), one runtime (Claude Code), pre-registered, plus smaller checks on SWE-bench Verified and tau-bench.

## Details

**Caveats**
One main task, one runtime, three models; Sonnet had 3 seeds and missed its pre-registered prediction against the best baseline. One shortcut left open was found in 3 of 8 sessions. It enforces how the agent works, not whether decisions are right.

**For your work**
For long batch workflows built on Claude Code or the Agent SDK (compliance reviews, case triage), put the procedure into hooks and an external state store instead of only adding prompt reminders. Measure how much the plain agent drifts first: if it barely drifts, the extra cost is not worth it.

**Method**
- A daemon keeps the workflow as a finite-state machine outside the context, reached via an MCP server and Claude Code hooks
- Gates: a PreToolUse check admits only the current state's tools, a guard runs shell checks before each transition, and a Stop hook blocks ending the turn early
- Compared with six baselines (SOP in the system prompt, per-account reminders, auto-resume) and two ablations on SOP-Bench referral-abuse detection

**Problem**
Long unattended agent runs must follow an SOP or skill stated once at the start, but the instructions sit in the context, where the model drifts from them and compaction can rewrite them.

**Results**
- Haiku 4.5: 139.2 vs 48.4 faithful and correct decisions; compliance 94.8% vs 27.8%; accuracy not hurt (146.5 vs 138.9)
- Ablations: stop gate alone made it decide blind (5.7); gates alone kept compliance but it tried to quit about 45 times per session
- Haiku with the FSM beat plain Sonnet 4.6 (134.3 vs 108.3) at 38% of the cost; non-drifting Qwen3.8-flash gained only 12.9
- The FSM session cost $10.64 vs $3.01 for the best Haiku baseline

**Concepts:** [[Agents]] · [[Claude]] · [[Evals and benchmarks]]
**From:** [[2026-11-10]]

# My notes


---
# References
[arXiv 2611.10884](https://arxiv.org/abs/2611.10884)
