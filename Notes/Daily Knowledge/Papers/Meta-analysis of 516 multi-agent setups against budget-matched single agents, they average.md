---
date: 2026-11-16
section: AI
importance: High
kind: paper
source: "arXiv 2611.17610"
url: https://arxiv.org/abs/2611.17610
status: unread
id: 2026-11-16-multi-agent-vs-compute-meta
---
2026-11-16 07:16
Tags: #daily-knowledge #ai

---
# Meta-analysis of 516 multi-agent setups against budget-matched single agents, they average

Pooling nine studies, the authors find multi-agent systems match or trail a baseline given the same samples or compute in 74% of comparable contrasts, averaging -0.042 accuracy; gains against a single greedy pass mostly vanish when one large study is dropped. They argue communication only pays off with partitioned evidence, external verification or genuinely diverse models. Tested on: 516 multi-agent configurations from nine published studies.

## Details

**Caveats**
One paper contributes 180 of the 516 configurations; the first five studies were picked without a search protocol; descriptive means are unweighted and some contrasts use tiny test sets.

**For your work**
Before selling or building a debate or multi-agent design, benchmark it against self-consistency or more thinking tokens at the same cost. Justify multiple agents by task structure (oversized context, parallel tools, sandboxes), and add external verification.

**Method**
- Extract 516 configurations from nine primary studies and code each on a six-dimension resource vector
- Re-score against a four-level baseline ladder: single pass, sample-matched, budget-matched
- Random-effects models on log odds plus sensitivity checks

**Problem**
Multi-agent papers usually compare against one greedy pass, mixing up coordination with extra samples and extra inference compute.

**Results**
- Against sample- or budget-matched baselines: mean -0.042 across 474 contrasts in eight studies
- Multi-agent equals or trails the baseline in 74% of comparable contrasts
- With matched thinking tokens, single agents match or beat debate from 500 tokens upward
- Majority voting without communication beat two-round debate, 0.747 vs 0.715

**Concepts:** [[Multi-agent systems]] · [[Evals and benchmarks]] · [[Inference efficiency]]
**From:** [[2026-11-16]]

# My notes


---
# References
[arXiv 2611.17610](https://arxiv.org/abs/2611.17610)
