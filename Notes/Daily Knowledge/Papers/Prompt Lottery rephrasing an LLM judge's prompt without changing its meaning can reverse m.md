---
date: 2026-11-01
section: AI
importance: Med
kind: paper
source: "arXiv 2610.38076"
url: https://arxiv.org/abs/2610.38076
status: unread
id: 2026-11-01-prompt-lottery-judges
---
2026-11-01 07:16
Tags: #daily-knowledge #ai

---
# Prompt Lottery rephrasing an LLM judge's prompt without changing its meaning can reverse m

Paraphrased judge prompts that humans agree mean the same thing produce different LLM-as-a-judge verdicts; judges lose 6-9x more agreement under rephrasing than human annotators do, and on objective QA tasks the relative ranking of evaluated models can flip. Aggregating over several prompt variants restores robustness, and a selective version reaches 86% of full robustness at about 60% lower cost than naive aggregation. Tested on: several judge families and backbones, four evaluated models (GPT-4o, gpt-oss-120B, Kimi-K2.5, Qwen3.6-Plus) under five prompt variants, 100 samples per task, 10 human annotators.

## Details

**Caveats**
Only paraphrases are tested, not deliberate changes to criteria. Semantic equivalence rests on embedding similarity and human ratings, not formal entailment. The ranking test uses one fixed backbone and four evaluated models, so how often rankings flip in a typical client eval is not established.

**For your work**
For any client eval with an LLM judge, run 3-5 paraphrased judge prompts on a sample and report the spread; only trust model or prompt comparisons whose difference exceeds it. Use selective aggregation for the full run to keep cost down.

**Method**
- Create paraphrastic variants of judge prompts that preserve semantics, validated by sBERT similarity (0.93) and human task-equivalence judgments (kappa 0.78).
- Run them across several evaluation tasks, judge families and backbone models, and compare agreement and rankings.
- Run a user study with 10 human annotators on the same rephrasings as a baseline.
- Propose multi-prompt aggregation, plus a selective variant that only spends extra calls where judgments disagree.

**Problem**
Most eval pipelines treat a single judge prompt as a fixed measuring instrument. If wording alone, with the same criteria, changes the verdicts, then both absolute scores and model comparisons rest partly on luck in prompt phrasing.

**Results**
- LLM judges show 6-9x larger agreement degradation under rephrasing than humans, dropping below the usual usability threshold.
- Rephrasing can reverse the relative ranking of the four evaluated models, especially on objective QA tasks.
- Selective aggregation achieves 86% of full robustness while cutting inference cost by about 60% versus naive aggregation.

**Concepts:** [[Evals and benchmarks]]
**From:** [[2026-11-01]]

# My notes


---
# References
[arXiv 2610.38076](https://arxiv.org/abs/2610.38076)
