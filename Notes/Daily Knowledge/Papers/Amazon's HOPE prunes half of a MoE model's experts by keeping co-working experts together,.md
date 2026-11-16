---
date: 2026-11-10
section: AI
importance: Med
kind: paper
source: "Hugging Face blog (Amazon)"
url: https://huggingface.co/blog/amazon/higher-order-pruning-experts
status: unread
id: 2026-11-10-hope-moe-expert-pruning
---
2026-11-10 07:16
Tags: #daily-knowledge #ai

---
# Amazon's HOPE prunes half of a MoE model's experts by keeping co-working experts together,

Amazon researchers prune Mixture-of-Experts models by scoring pairs of experts that tend to fire together, not each expert alone. At 50% pruning, HOPE gets the best average rank of five methods (1.58 vs 2.42 for REAP), and pruned Qwen3.5-35B-A3B scores 42.3 on SWE-Bench Pro against 41.8 unpruned, where REAP drops to 36.2. Tested on: Qwen3.5-122B, Qwen3.5-35B and GLM-4.5-Air (2 families), 2 calibration sets, Tulu3 suite and SWE-Bench Pro, 10-50% pruning, against 4 first-order baselines.

## Details

**Caveats**
At 10-20% pruning, first-order methods like REAP and MAN are sometimes as good. Each layer is pruned on its own, with no cross-layer effects. The method comes from Amazon's own paper (arXiv 2609.18916) and has not been reproduced by anyone else.

**For your work**
For clients who must run open MoE models on their own hardware, this could halve expert memory with no training, and it works alongside quantization. Calibrate on the client's own agent trajectories, then re-run your agentic evals before you ship.

**Method**
- Run one forward pass over calibration data (code prompts or SWE-Bench agent trajectories), recording gate weights, output norms and how often pairs of experts are picked together.
- Build a pairwise interaction matrix from an upper bound on the pruning error, then pick the prune set per layer by solving a binary quadratic program, which takes a few seconds per layer.
- The output is a normal, smaller Hugging Face checkpoint; vLLM and SGLang need no changes. Code is open (awslabs/HOPE).

**Problem**
In MoE models nearly all memory goes to expert weights (95% of Qwen3.5-122B's ~250 GB), but only 8 of 256 experts per layer are used per token. Existing pruning methods score each expert on its own and miss that experts work in stable groups, so aggressive pruning breaks those groups.

**Results**
- Best average rank across all conditions: 2.07 of 5 methods, top-1 in 39% of conditions and top-2 in 67%.
- At 50% pruning: average rank 1.58 vs 2.42 for REAP, the next best.
- Qwen3.5-35B-A3B at 50% pruning: 42.3 on SWE-Bench Pro vs 41.8 unpruned and 36.2 with REAP.
- Calibrating on code did not badly hurt non-coding Tulu3 benchmarks.

**Concepts:** [[Inference efficiency]] · [[Open-weight models]] · [[Coding agents]]
**From:** [[2026-11-10]]

# My notes


---
# References
[Hugging Face blog (Amazon)](https://huggingface.co/blog/amazon/higher-order-pruning-experts)
