---
date: 2026-11-25
section: AI
importance: High
kind: paper
source: "arXiv 2611.32946"
url: https://arxiv.org/abs/2611.32946
status: unread
id: 2026-11-25-shellbench-models-vs-harness
---
2026-11-25 07:16
Tags: #daily-knowledge #ai

---
# ShellBench across 53,100 runs, the model explains 95.7% of the variation in everyday-task

100 everyday assistant tasks drawn from more than 10 million user requests, each in a messy workspace (median 188 files) and graded for correctness and safety. GPT-6 Astra (62.5%), Claude Fable 5.2 (61.9%) and GPT-6.1 Sol (61.4%) are within 1.1 points, but a Sol run costs about $0.19 against $0.83 for Fable and $1.10 for Astra; harness averages span only 42.9 (Claude Code) to 45.2 (OpenClaw) pass@1. Tested on: 12 models from OpenAI, Anthropic, Google, DeepSeek, Moonshot, Meta and others, 5 harnesses, 3 effort levels, 3 attempts each.

## Details

**Caveats**
Several authors are OpenClaw maintainers, and OpenClaw scored highest. A single LLM judge from one vendor; many safety criteria partly measure completeness. Only 20 tasks are public.

**For your work**
For client assistants, spend evaluation effort on model choice and cost per run first; harness choice mostly shifts cost and tool behaviour. Report pass-all-3, not just pass@1.

**Method**
- 100 tasks (90 judged by GPT-6.1 Sol against 721 rubric criteria, 381 on safety), checked against 290 human-graded decisions
- Claude Code, Codex, Hermes, OpenClaw and Pi used as shipped with default tools
- Two-way ANOVA over configuration means; costs from OpenRouter list prices

**Problem**
Buyers choose both a model and a harness for general assistant work, with no clear evidence on which matters more for correctness, safety and cost.

**Results**
- Model 95.7% of variance, harness 0.36%; among the top five models only, model 65.6% and harness 16.5%
- Mean pass@1 44.4%, but only 28.2% pass all three attempts
- Run cost by harness: $0.29 Pi vs $0.51 Claude Code and $0.53 OpenClaw
- Claude Code shifts model scores the most (residual SD 4.7 points); 2,589 of 8,340 safety-failing runs passed every correctness criterion

**Concepts:** [[Evals and benchmarks]] · [[Agents]] · [[Coding agents]]
**From:** [[2026-11-25]]

# My notes


---
# References
[arXiv 2611.32946](https://arxiv.org/abs/2611.32946)
