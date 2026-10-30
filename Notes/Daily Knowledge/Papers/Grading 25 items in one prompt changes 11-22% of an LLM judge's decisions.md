---
date: 2026-10-30
section: AI
importance: High
kind: paper
source: "arXiv 2610.40241"
url: https://arxiv.org/abs/2610.40241
status: unread
id: 2026-10-30-batched-llm-judging-flips
---
2026-10-30 07:16
Tags: #daily-knowledge #ai

---
# Grading 25 items in one prompt changes 11-22% of an LLM judge's decisions

Putting the same 2,000 items into different random batches of 25 changed 11-22% of harm and grading decisions, 6.5-13.3 points more than rewording the instruction, while AUROC against human labels moved only -0.033 to +0.010, so accuracy checks miss it. Voting over nine permutations still leaves 52-60% of the flips; the authors recommend one item per prompt with a cached prefix. Tested on: nine open-weight models from four families (4-32B), three English tasks, 2,000 items each, pre-registered gates and bootstrap CIs; no proprietary model in the main runs.

## Details

**Caveats**
Small and mid-size open models only; one prompt template plus one rewording; other output formats may behave differently.

**For your work**
If a client pipeline batches classification or LLM-as-judge calls, measure agreement with one-at-a-time grading before trusting it; with prompt caching, isolating items is often about as cheap.

**Method**
- Grade the same 2,000 items per task alone and in three random partitions of 25, with JSON output and greedy decoding
- Separate the effect of neighbour order, slot and which items share the prompt, against baselines such as renamed keys and a reworded instruction
- Edit single generations to test whether earlier verdicts or neighbour texts carry the effect

**Problem**
Teams batch many items into one judge prompt to save cost, assuming each verdict depends only on its own item. Nothing in a decoder-only model guarantees that.

**Results**
- Harm and short-answer grading: 11-22% of decisions change for five 4-9B models; 6-15% for four 14-32B models
- The majority of fifteen random batches still disagrees with single-item grading on 8.4-17.8% of decisions
- Both channels act: swapping in another batch's verdicts changes 7-23% of decisions, its texts 9-26%
- On easy star ratings only 2.9-3.9% of decisions change

**Concepts:** [[Evals and benchmarks]] · [[Structured outputs]]
**From:** [[2026-10-30]]

# My notes


---
# References
[arXiv 2610.40241](https://arxiv.org/abs/2610.40241)
