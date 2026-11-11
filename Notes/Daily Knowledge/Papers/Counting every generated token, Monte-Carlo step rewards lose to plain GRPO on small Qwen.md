---
date: 2026-11-11
section: AI
importance: Low
kind: paper
source: "arXiv 2611.13560"
url: https://arxiv.org/abs/2611.13560
status: unread
id: 2026-11-11-dense-rewards-grpo
---
2026-11-11 07:16
Tags: #daily-knowledge #ai

---
# Counting every generated token, Monte-Carlo step rewards lose to plain GRPO on small Qwen

At matched generated tokens, the Monte-Carlo step reward that beats GRPO per update ends 14.3 points lower on Qwen2.5-1.5B (7.8 lower at equal training time), because its continuations take 91% of all tokens, and none of four dense-reward variants beats GRPO. Training on prompts whose predicted success is nearest 1/2 adds 1.7 points on Qwen3-0.6B and 0.8 on Qwen2.5-1.5B. Tested on: 1,668 preregistered runs on six models up to 4B (dense rewards on Qwen only; two Llama-3.2 models for prompt selection only), MATH problems.

## Details

**Caveats**
Models of at most 4B, numeric MATH answers only; four of six models are Qwen and no prompt-selection gain was shown outside Qwen; gains are small, around seed-to-seed variation.

**For your work**
When evaluating any RL or fine-tuning trick for a client, compare at equal tokens and GPU-hours, not equal steps, and fix the verifier first; cheap prompt filtering beats expensive per-step rewards here.

**Method**
- A matched-compute protocol: every intervention gets the same budget of generated tokens (including continuations and discarded samples) and training GPU-hours.
- Preregistered hypotheses and equivalence margins; paired seeds; controls for random prompt choice, a retuned learning rate and a strict verifier.
- Compared a Monte-Carlo step reward, learned critics (TD and baseline forms) and critic-based prompt selection against outcome-only GRPO.

**Problem**
Dense (process) rewards are proposed to fix GRPO's equal credit on every token, and they are usually vetted per training update or with a gradient test on one batch, which ignores what they cost to compute.

**Results**
- Monte-Carlo reward leads per update but trails at equal tokens by 14.3 points and at equal training time by 7.8 points, in every seed.
- Learned critics match GRPO within about a point; the per-token gradient test ranks rewards correctly but overestimates each by one to two points.
- Prompt selection gains replicate on fresh seeds and unseen problems; GRPO with twice the learning rate comes within half a point of it.
- A lenient verifier made runs stop boxing answers; a strict verifier removed that drift without losing accuracy.

**Concepts:** [[Post-training and RL]]
**From:** [[2026-11-11]]

# My notes


---
# References
[arXiv 2611.13560](https://arxiv.org/abs/2611.13560)
