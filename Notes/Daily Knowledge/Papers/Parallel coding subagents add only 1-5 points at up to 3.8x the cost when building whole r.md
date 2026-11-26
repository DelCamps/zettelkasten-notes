---
date: 2026-11-26
section: AI
importance: Med
kind: paper
source: "arXiv 2611.33893"
url: https://arxiv.org/abs/2611.33893
status: unread
id: 2026-11-26-parallel-subagents-coding
---
2026-11-26 07:16
Tags: #daily-knowledge #ai

---
# Parallel coding subagents add only 1-5 points at up to 3.8x the cost when building whole r

On repository-construction tasks from NL2Repo and ProgramBench, letting Codex's main agent delegate to parallel subagents raised hidden-test pass rates by about 1-5 points at 2.6-3.8x the cost. At equal cost, a single agent matched or beat the delegating setup. The bigger gains on hard tasks trace to three things a single agent can also get: more self-checking, fresh context, and more modular code. Tested on: GPT-5.6 Sol, GPT-6 Sol and GPT-6.1 Sol in Codex, plus smaller replications on Claude Code (Opus 5.5, Grok 4.6, MiniMax-M3) and DeepSeek's dsh harness; 30 random tasks per benchmark and 16 hard ones; mostly 1-3 runs per setup.

## Details

**Problem**
Codex and Claude Code can spawn parallel subagents, which multiplies cost. Does delegating actually produce a better program, and when?

**Method**
- Single agent vs a main agent allowed to delegate, compared at equal time and equal cost.
- Interventions: a one-sentence prompt telling the single agent to probe the reference program first; chains of fresh sessions in runs up to 20 hours.
- Code structure is analysed (files, function length) to test the modularity explanation.

**Results**
- Random tasks: Multi beats Single by 1.2-4.7 points across three GPT generations, at 2.6-3.2x the cost (3.8x on NL2Repo).
- Hard task 'atlas': a single GPT-5.6 Sol agent stops at 47% of hidden tests, while the delegating setup reaches 77%.
- With GPT-5.6 Sol, the probe sentence adds 6.7 points vs 8.8 for Multi. With GPT-6.1 Sol, single agents already check their own work and the gain shrinks.
- Opus 5.5 on Claude Code: Multi is 4.7 points above Single on ProgramBench (95.5 vs 90.7) at 3.1x the cost.

**Caveats**
Most comparisons rest on 1-3 runs. The probe sentence did not transfer to dsh or NL2Repo, and the extended-run advantage is clear on only one task.

**For your work**
Default to a single agent. Add 'verify against a reference before stopping' and fresh-session restarts, and save subagents for hard, modular builds where the extra 3x spend is justified.

**Concepts:** [[Coding agents]] · [[Multi-agent systems]] · [[Evals and benchmarks]]
**From:** [[2026-11-26]]

# My notes


---
# References
[arXiv 2611.33893](https://arxiv.org/abs/2611.33893)
