---
date: 2026-11-27
section: AI
importance: Low
kind: paper
source: "arXiv 2611.34852"
url: https://arxiv.org/abs/2611.34852
status: unread
id: 2026-11-27-drbench-pro-deep-research
---
2026-11-27 07:16
Tags: #daily-knowledge #ai

---
# DRBench Pro scores deep research reports by how much of a knowledge tree they cover; the b

DRBench Pro builds knowledge trees from Wikipedia and turns each relation into a rubric, measuring breadth across research directions and depth along knowledge chains (144 cases, 24 domains, 44,102 rubrics). Claude Opus 5 leads at 57.04% overall coverage, ahead of Grok 4.5 at 50.98%, and agents with similar totals can follow opposite strategies. Tested on: 16 deep research agents, 144 cases, one judge (Gemini 2.5 Pro) checked against human labels.

## Details

**Problem**
Deep research benchmarks score report quality but not which research directions a report covers and how deeply it follows them.

**Method**
- Automated pipeline builds local knowledge trees from Wikipedia; sampled subgraphs generate queries and evidence-grounded rubrics, one per relation.
- Breadth and depth scores, combined by geometric mean into overall coverage.
- Gemini 2.5 Pro judges all 2,304 report-case evaluations; ten PhD-level annotators label 3,695 report-rubric pairs.

**Results**
- Best agent Claude Opus 5 at 57.04% overall coverage; Grok 4.5 second at 50.98%.
- Judge agrees with human labels at Macro-F1 0.893; rankings stable under metric perturbations.
- One case: breadth 27.33 and depth 55.19 for one agent vs 54.48 and 29.82 for Grok 4.5, giving similar totals.

**Caveats**
Tasks and rubrics were built with Claude Opus 4.8, which may favour Claude; the swap to Kimi K2.6 was checked on only 10 cases. Wikipedia-based knowledge only.

**For your work**
Little direct use; the breadth vs depth split is a useful way to grade client deep-research or report-writing agents.

**Concepts:** [[Evals and benchmarks]] · [[Agents]]
**From:** [[2026-11-27]]

# My notes


---
# References
[arXiv 2611.34852](https://arxiv.org/abs/2611.34852)
