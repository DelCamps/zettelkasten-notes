---
date: 2026-10-26
section: AI
importance: Low
kind: paper
source: "arXiv 2610.31820"
url: https://arxiv.org/abs/2610.31820
status: unread
id: 2026-10-26-rl-critic-confidence
---
2026-10-26 07:16
Tags: #daily-knowledge #ai

---
# The RL critic already is a confidence estimator for the policy

The authors prove that, with a correctness reward, confidence estimation and critic training predict the same thing. So a model trained with value-based RL can reuse its critic as a confidence score at no extra cost; it was the best estimator on every in-distribution split and best-calibrated on 14 of 16.

## Details

**Caveats**
Only applies to models trained with value-based RL (PPO-style critics); most API models give you no access to a critic.

**For your work**
Little direct use with closed APIs; the external-estimator result supports training a small correctness predictor on your own logs to route or flag low-confidence answers.

**Method**
- Compare self-estimators with external estimators of similar size trained on the same (question, response, correctness) triples.
- Prove that under a correctness-based outcome, confidence estimation equals critic (value function) training.
- Reuse the critic from value-based RL as an off-the-shelf confidence estimator, including at intermediate reasoning steps.

**Problem**
Reliable confidence scores for LLM answers usually need a separate training stage with extra data and compute.

**Results**
- An external estimator that sees only text matches the policy's own confidence: within 0.05 AUROC on four of five benchmarks.
- Across math, code, tool calling and general reasoning, the reused critic is the best confidence estimator on every in-distribution split and best-calibrated on 14 of 16.
- Task performance is unchanged since the policy is untouched.

**Concepts:** [[Post-training and RL]] · [[Hallucination]]
**From:** [[2026-10-26]]

# My notes


---
# References
[arXiv 2610.31820](https://arxiv.org/abs/2610.31820)
