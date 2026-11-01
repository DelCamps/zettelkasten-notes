---
date: 2026-11-01
section: AI
importance: Low
kind: paper
source: "arXiv 2610.40488"
url: https://arxiv.org/abs/2610.40488
status: unread
id: 2026-11-01-rtaste-research-agents
---
2026-11-01 07:16
Tags: #daily-knowledge #ai

---
# rTaste frontier research agents propose many good experiments but cannot yet tell which to

Six frontier models, alone or in teams, proposed 415 minimum viable experiments on seven recent NLP papers, forecast their outcomes and ranked them; an executor then ran every one. 194 were judged sound, valuable and new, but only 73 also went beyond the seed paper in a non-obvious way. First choices beat a random pick but not simply taking the first experiment written, and forecasts were no better than a fresh copy of the same model. Tested on: 6 frontier models, 7 papers, 415 experiments, model-only auditors.

## Details

**Caveats**
All labels come from models, with no human baseline; two of the three auditors are also evaluated models. Every experiment ran regardless of rank, so ranking never decided what ran.

**For your work**
Little direct use. For 'AI analyst' agents, do not rely on the agent's own prioritisation or confidence; keep a human choosing which analyses to run.

**Method**
- Give each model a recent NLP paper; it proposes minimum viable experiments, sets a pass threshold, forecasts the result and ranks them.
- A separate executor attempts every experiment, including the lowest-ranked.
- Three model auditors judge soundness, value and novelty after seeing the results.

**Problem**
Research agents can now generate and run experiments, but the scarce skill is taste: choosing which experiment is worth running before knowing the outcome.

**Results**
- 194 of 415 experiments judged sound, valuable and new; 73 also beyond the seed paper and non-obvious.
- Agents' top picks match the auditors' most valued experiment more often than random, but are not shown to beat choosing the experiment written first.
- Forecasts beat the base rate but are not measurably better than a fresh instance given only the paper. Teams cost more without a clear quality gain.

**Concepts:** [[AI for science and math]] · [[Evals and benchmarks]] · [[Multi-agent systems]]
**From:** [[2026-11-01]]

# My notes


---
# References
[arXiv 2610.40488](https://arxiv.org/abs/2610.40488)
