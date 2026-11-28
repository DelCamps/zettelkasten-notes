---
date: 2026-11-27
section: AI
importance: Low
kind: paper
source: "arXiv 2611.34363"
url: https://arxiv.org/abs/2611.34363
status: unread
id: 2026-11-27-text-to-sql-reward-hacking
---
2026-11-27 07:16
Tags: #daily-knowledge #ai

---
# Text-to-SQL RL rewards checked on one database pay for hacks; hidden database copies cut p

A wrong SQL query can match the reference by luck when the data lack rows that expose the bug; running the final query also on two or three hidden, code-generated copies of the database cut fully paid buggy queries from 29.5% to 16.8% and hacks from 54.1% to 1.9%, rejecting none of 2,847 correct queries. Training with this reward did not beat the plain reward in domain (8.4% vs 11.7%), and one seed reversed both results. Tested on: audit of 1,302 synthetic questions; RL on one 3.35B model, three seeds per arm.

## Details

**Caveats**
Synthetic questions; one small model; the two rewards disagreed on only 5-7% of rollouts, so the training test had little power.

**For your work**
When evaluating client text-to-SQL agents, score queries on several perturbed copies of the database, not one snapshot, to catch answers that are right by luck.

**Method**
- Counterfactual reward: also run the final query on hidden database copies, each edited by code for one bug family; pay only if all match (strict) or by share matched (mean).
- Audit on 2,847 correct queries, 1,814 realistic buggy variants and 2,839 constructed hacks (literal answers, empty results, hard-coded IDs).
- GRPO comparison with Tiny Aya Global 3.35B, LoRA, one run_sql tool, three seeds per arm.

**Problem**
RL for text-to-SQL agents pays a query when its result matches the reference on one database, so plausible but wrong queries and hacks can earn full reward.

**Results**
- Buggy queries paid in full: 29.5% to 16.8%; hacks: 54.1% to 1.9%; 0 of 2,847 correct queries rejected.
- Found an exploit in AgentTune's SQL reward (fixed upstream) and the same gap in SkyRL-SQL and eight published Spider systems.
- Training: no in-domain gain (8.4% vs 11.7%); +1.6 points on Spider, within seed noise. The copies add about 1 ms of CPU per rollout.

**Concepts:** [[Post-training and RL]] · [[Evals and benchmarks]] · [[Structured outputs]]
**From:** [[2026-11-27]]

# My notes


---
# References
[arXiv 2611.34363](https://arxiv.org/abs/2611.34363)
