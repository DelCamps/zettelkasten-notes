---
date: 2026-11-15
section: AI
importance: Med
kind: paper
source: "arXiv 2611.14925"
url: https://arxiv.org/abs/2611.14925
status: unread
id: 2026-11-15-toolturns-multiturn-benchmark
---
2026-11-15 07:16
Tags: #daily-knowledge #ai

---
# ToolTurns the best tool agent resolves 69.6% of single requests but only 39.8% of three-re

A new benchmark of 2,620 underspecified tool-use dialogues over 11,004 API endpoints finds every model scores lower on follow-up requests than on the first one, and Claude Opus 4.8 leads at 39.8% full-dialogue completion. Dialogue-quality rubric scores and task success barely agree (Spearman 0.23): GPT-5.4-mini tops the rubric but is second-worst on task success. Tested on: 9 models from 5 providers (OpenAI, Anthropic, Qwen, Google, Z.ai), 2,620 dialogues each, one fixed simulator and judge.

## Details

**Caveats**
Simulated users and tools, generated queries, and LLM judges throughout; the judge ignores evidence from earlier subtasks, which may inflate follow-up drops. Proprietary models are mostly small tiers.

**For your work**
- When evaluating a client's tool agent, score full conversations with follow-ups, not single requests, and report task success separately from rubric quality scores
- The released simulator and checker-fixer can seed multi-turn test sets for client APIs

**Method**
- 2,620 problems across 1,827 RapidAPI tools; each starts underspecified and continues with two context-dependent follow-ups
- Simulated user (Qwen3-32B) reveals withheld context and writes follow-ups; a checker-fixer pipeline rewrites flawed user turns
- Tools served from the StableToolBench cache or an LLM simulator; gpt-oss judges task success (human agreement kappa 0.68) and a five-part rubric

**Problem**
Most large tool-use benchmarks score isolated requests, but real assistants must clarify vague asks and handle follow-ups that depend on earlier turns.

**Results**
- Subtask success 55.2-69.6%; all-three-pass 24.9-39.8% (Opus 4.8 best, GLM-5.2 37.7%, Gemma 4-31B 36.4%)
- All nine models drop from the initial request to the follow-ups, by 2.1 to 16.2 points
- Open-weight GLM-5.2 and Gemma 4 beat every OpenAI mini model; size predicted little
- Checker-fixer cut detected user-turn defects by 41.2%; humans preferred revised turns 63.3% of the time

**Concepts:** [[Evals and benchmarks]] · [[Agents]]
**From:** [[2026-11-15]]

# My notes


---
# References
[arXiv 2611.14925](https://arxiv.org/abs/2611.14925)
