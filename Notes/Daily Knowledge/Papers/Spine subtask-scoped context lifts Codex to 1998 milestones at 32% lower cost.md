---
date: 2026-10-29
section: AI
importance: Med
kind: paper
source: "arXiv 2610.37224"
url: https://arxiv.org/abs/2610.37224
status: unread
id: 2026-10-29-spine-subtask-context
---
2026-10-29 07:16
Tags: #daily-knowledge #ai

---
# Spine subtask-scoped context lifts Codex to 1998 milestones at 32% lower cost

Spine lets a coding agent mark subtask boundaries (work scopes). Before each model call, the runtime rebuilds the context: unfinished subtasks keep their full history, while finished ones collapse to their returned result. In Codex with GPT-5.6 Sol it resolves 19 of 98 SWE-Milestone milestones, against 14 for native Codex and 17 for recursive subagents, which cost 3.8x more. Tested on: 4 models from 4 providers, 2 harnesses (Codex, Pi), 3 long-horizon benchmarks.

## Details

**Caveats**
Milestone gains are a handful of tasks (14 to 19 of 98) and appear to come from single runs; ProgramBench uses a 50-task sample and FrontierSWE 10 tasks. The baseline comparison was run with one model only.

**For your work**
If you build long-running agents, scoping context by subtask and collapsing finished work into its result looks cheaper than both compaction and subagent-per-step designs. It is worth trying in your own harness.

**Method**
- The agent declares nested work scopes; a persistent SpineTree records subtask relations, local interactions, completion states and results
- The tree is compiled into context just in time, keeping the prompt-cache prefix intact
- Delegation is kept only for independent parallel work; tested against AgentDiet, context folding and recursive-subagent baselines

**Problem**
Long coding sessions bloat context. Generic compaction throws away state that unfinished subtasks still need, and delegating every subtask to a subagent adds a lot of coordination overhead.

**Results**
- SWE-Milestone (GPT-5.6 Sol): score 42.6% vs 38.1% for Codex, at $460.77 vs $681.22
- Recursive Subagent reaches a similar score (42.4%) but costs $1,749.73 and makes 32,650 model requests vs 8,792
- ProgramBench test-pass rate +17.3% (Sol) and +10.2% (Grok 4.6); cost falls in 5 of 6 benchmark-model settings
- In the Pi harness with Gemini 3.8 Flash and Qwen 3.8 27B: SWE-Milestone score +9.5-17.5%

**Concepts:** [[Coding agents]] · [[Agents]] · [[Inference efficiency]]
**From:** [[2026-10-29]]

# My notes


---
# References
[arXiv 2610.37224](https://arxiv.org/abs/2610.37224)
