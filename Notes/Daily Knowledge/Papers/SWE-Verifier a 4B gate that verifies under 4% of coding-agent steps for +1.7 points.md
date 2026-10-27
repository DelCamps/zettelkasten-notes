---
date: 2026-10-25
section: AI
importance: Med
kind: paper
source: "arXiv 2610.30284"
url: https://arxiv.org/abs/2610.30284
status: unread
id: 2026-10-25-swe-verifier
---
2026-10-25 07:16
Tags: #daily-knowledge #ai

---
# SWE-Verifier a 4B gate that verifies under 4% of coding-agent steps for +1.7 points

A small verifier fine-tuned from Qwen3.5-4B scores each proposed coding-agent action and only triggers candidate sampling and reranking when needed. On SWE-Bench Verified it lifts MiniMax-M2.7 from 75.47% to 77.20% at 1.09x cost and transfers to DeepSeek-V4-Flash (72.60% to 74.27%, 1.13x), verifying fewer than 4% of steps.

## Details

**Caveats**
Only one harness and SWE-Bench Verified; cost savings rely on prompt-cache discounts for repeated candidate prompts. Teacher-labelled preferences may carry teacher biases.

**For your work**
A cheap pattern for agent products: put a small learned or rubric-based gate in front of risky or expensive steps and only branch-and-rerank there, instead of best-of-n on every step. Make sure your provider's prompt caching covers the repeated prefix.

**Method**
- SWE-Verifier, a generative verifier trained from Qwen3.5-4B, scores the agent's proposed action and decides whether extra candidates are needed.
- When triggered, it samples alternatives and ranks them before execution.
- Training uses preference data pairing contrasting actions with their resulting environment observations and rubric-guided teacher scores.

**Problem**
Coding agents waste compute when a poor action steers them into low-value states. Sampling and verifying alternatives at every step helps but multiplies cost.

**Results**
- MiniMax-M2.7 in mini-swe-agent: 75.47% to 77.20% resolved at 1.09x cost, verifying 3.43% of steps.
- Transfers to DeepSeek-V4-Flash without training on its actions: 72.60% to 74.27% at 1.13x cost.
- Matches or beats trajectory-level and all-step verification baselines at substantially lower cost; uniform verification adds cost without consistent gains.

**Concepts:** [[Coding agents]] · [[Inference efficiency]]
**From:** [[2026-10-25]]

# My notes


---
# References
[arXiv 2610.30284](https://arxiv.org/abs/2610.30284)
