---
date: 2026-11-12
section: AI
importance: Med
kind: paper
source: "arXiv 2611.13396"
url: https://arxiv.org/abs/2611.13396
status: unread
id: 2026-11-12-token-spend-productivity
---
2026-11-12 07:16
Tags: #daily-knowledge #ai

---
# Token spend is the new lines-of-code at JetBrains, doubling an engineer's agent tokens wen

Linking five weeks of coding-agent token logs to the commits of 404 JetBrains engineers, researchers found spend is mostly a stable personal trait: among weeks with similar commit counts, the 90th percentile of spend was 39 to 240 times the 10th, and work metrics explained only 38% of the between-engineer variation. They advise using token spend only for resource accounting, not to judge productivity. Tested on: 404 engineers at one company (JetBrains), 5 weeks of gateway logs from two coding agents, plus a survey of 412 employees; observational, associations only.

## Details

**Caveats**
One company, five weeks, associations not causal; engineers choose how much to use agents. Commits are an imperfect output measure and the engineers' own time, the larger cost, is not in the data.

**For your work**
If PwC or a client is tempted to measure developer productivity by AI token spend, this is direct evidence against it. Use spend for cost accounting and budgeting only, and evaluate agent-assisted work by task outcomes, not by tokens or cost-per-PR ratios.

**Method**
- Pseudonymized internal gateway logs of every agent call (two agents, 69% and 31% of tokens) linked to commits on JetBrains' main IDE products over 29 June-2 August 2026.
- Compared spend between and within engineers against commit counts, sizes and issue types; credits reproduced the token ranking (Spearman rho 0.97).
- Analyzed an anonymous internal survey of 412 employees on how agents are used.

**Problem**
Companies increasingly use token spend to track AI adoption, set budgets and even rank engineers (Meta leaderboard dashboards, Salesforce spending targets, vendor 'cost per merged PR' ROI). Whether spend tracks engineering output had not been measured.

**Results**
- The engineer at the 90th percentile of spend used 71x the tokens of the 10th over five weeks; across similar-commit weeks the 90th was 39-240x the 10th.
- Within an engineer, doubling spend went with about 10% more commits; available work metrics explained 38% of between-engineer and 13% of week-to-week variation.
- Nearly nine in ten technical-role evaluations reported using agents for non-coding work (analysis, research, planning).
- Most tokens are re-sent context: the median call sends about 400x as many tokens as it receives.

**Concepts:** [[Coding agents]] · [[Evals and benchmarks]]
**From:** [[2026-11-12]]

# My notes


---
# References
[arXiv 2611.13396](https://arxiv.org/abs/2611.13396)
