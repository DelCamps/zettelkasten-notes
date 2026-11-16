---
date: 2026-11-05
section: AI
importance: Med
kind: paper
source: "Epoch AI"
url: https://epoch.ai/publications/eci-bayesian-methodology
status: unread
id: 2026-11-05-epoch-eci-bayesian
---
2026-11-05 07:16
Tags: #daily-knowledge #ai

---
# Epoch's Capabilities Index goes Bayesian 72% chance GPT-6 Astra is ahead of Claude Opus 5

Epoch AI refits its Capabilities Index with a Bayesian item-response model, which gives calibrated intervals and head-to-head probabilities. At the frontier GPT-6 Astra (166.2-172.7) and Claude Opus 5.5 (165.8-172.0) overlap heavily; weaker models drop 13.7 points on average. Tested on: 2,810 scores from 252 models on 59 benchmarks.

## Details

**Caveats**
Neighbouring frontier models overlap a lot, so exact rankings near the top are uncertain. Weak models with few scores depend on the uniform priors, and coverage near 0% scores is worse than the old method (80.5% vs 92.5%). Snapshot of October 26 data.

**For your work**
When a client asks 'which model is best', this is a good citation for saying the top models are statistically tied on general capability, so pick on price, latency, data residency and your own task evals instead.

**Method**
- Item response theory as before: each model has a capability, each benchmark a difficulty and slope; the scale is anchored at Claude 3.5 Sonnet = 130 and GPT-5 = 150.
- Bayesian fit with MCMC (NUTS in PyMC); reported scores are posterior means with 5th-95th percentile intervals.
- Beta likelihood keeps predicted scores between 0% and 100%; each benchmark gets its own noise level; hierarchical log-normal priors on slopes and noise.

**Problem**
Capability indices combine many benchmarks into one score, but most models have only four to ten benchmark results, so bootstrapped confidence intervals are unreliable and the old least-squares fit could not say how likely one model is to beat another.

**Results**
- For the 176 models at or above 125, old and new scores agree closely (R squared 0.995), and intervals are about 13% narrower.
- The 76 models below 125 all move down, by 13.7 points on average.
- Out of sample: leave-one-out RMSE 0.092 vs 0.094, and 89.6% vs 84.2% coverage for 90% intervals.
- Head-to-head: 72% probability GPT-6 Astra beats Claude Opus 5.5, 54% against GPT-6.1 Sol.

**Concepts:** [[Evals and benchmarks]] · [[Frontier models]]
**From:** [[2026-11-05]]

# My notes


---
# References
[Epoch AI](https://epoch.ai/publications/eci-bayesian-methodology)
