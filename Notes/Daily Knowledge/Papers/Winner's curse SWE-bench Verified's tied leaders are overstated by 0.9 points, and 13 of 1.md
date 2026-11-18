---
date: 2026-11-18
section: AI
importance: Med
kind: paper
source: "arXiv 2611.22227"
url: https://arxiv.org/abs/2611.22227
status: unread
id: 2026-11-18-winners-curse-leaderboards
---
2026-11-18 07:16
Tags: #daily-knowledge #ai

---
# Winner's curse SWE-bench Verified's tied leaders are overstated by 0.9 points, and 13 of 1

Ranking noisy benchmark scores rewards luck. The authors' m-out-of-N bootstrap estimates that the two SWE-bench Verified leaders at 79.2% are inflated by 0.90 percentage points and have only 30.5% and 29.0% chances of really being first. That inflation is larger than the 0.8-point median by which the top score rose each of the 13 times it rose in 2025. Across 14 benchmarks, the correction for the top model ranges from about 0.09 to 3.86 points. Tested on: 14 benchmarks from 5 benchmark families, including 173 models on SWE-bench Verified, plus simulations and sample-splitting checks.

## Details

**Caveats**
It assumes i.i.d. bounded tasks and a fixed model pool. It covers task sampling only, not rerun noise, contamination or selective reporting, and it can overcorrect when gaps are comparable to noise.

**For your work**
When a client asks which model to use, treat leaderboard gaps of about 1 point as ties. For internal evals, report rank intervals and tiers, not just the top score.

**Method**
- An m-out-of-N bootstrap that resamples tasks and re-ranks all models together, allowing arbitrary correlation between models within a task.
- Produces RULER: bias-adjusted scores, a rank probability matrix, 80% rank intervals and tiers of indistinguishable models.
- Proves the bias drops from order N^-1/2 to o(N^-1/2) when tiers are separated.

**Problem**
Leaderboards drive model choice and procurement, but picking the highest of many noisy averages overestimates the winner. The same selection effect inflates scores near the top and deflates them near the bottom.

**Results**
- SWE-bench Verified (500 tasks, 173 models): the tied leaders at 79.2% adjust to 78.3%; both 80% rank intervals span ranks 1-6.
- 13 of 173 models fall in the leading tier.
- In 2025 the top score rose 13 times with a median gain of 0.8 points; 7 of those gains were smaller than the estimated inflation.
- In simulations it removes about 85% of mean winner bias, against 68% for the standard bootstrap and 22% for empirical Bayes.

**Concepts:** [[Evals and benchmarks]]
**From:** [[2026-11-18]]

# My notes


---
# References
[arXiv 2611.22227](https://arxiv.org/abs/2611.22227)
