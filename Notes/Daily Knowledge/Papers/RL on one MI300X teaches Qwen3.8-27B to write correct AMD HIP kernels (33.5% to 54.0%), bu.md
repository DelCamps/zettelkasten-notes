---
date: 2026-11-26
section: AI
importance: Low
kind: paper
source: "Hugging Face blog (community)"
url: https://huggingface.co/blog/ik6626/hip-kernel-rl-mi300x
status: unread
id: 2026-11-26-hip-kernel-rl-mi300x
---
2026-11-26 07:16
Tags: #daily-knowledge #ai

---
# RL on one MI300X teaches Qwen3.8-27B to write correct AMD HIP kernels (33.5% to 54.0%), bu

A community RL run trained a LoRA adapter for Qwen3.8-27B to turn PyTorch modules into HIP kernels. On 100 unseen tasks, the share of correct kernels rose from 0.335 to 0.540 (+20.5 points, 95% CI 14.3-27.0). Speed did not improve: 80% of the reward came from correctness, and a 0.5x kernel scored the same as a 1.05x one. Tested on: one model, one seed, 100 validation and 200 held-out tasks from the same public sources as training.

## Details

**Problem**
Most LLM kernel-writing work targets CUDA. How far does plain RL get on AMD's stack with a single GPU?

**Method**
- Single-turn task with no compiler feedback. The answer is one .hip file with its own __global__ kernels.
- The grader works as containment: a safety scan, compilation without network, a fresh locked-down container per answer, 3 random input seeds, and a profiler check that the model's own kernel actually ran.
- Reward: 1 + 0.5·clip(log2 speedup, 0, 3) if correct, 0.1 if it compiles but is wrong. Plain group-centred policy gradient with no KL term. The trainer and SGLang sampler take turns on one 192 GB GPU (about 41 minutes per step).

**Results**
- Held-out set: 0.289 to 0.515 (+22.6 points). Finishing more often explains only about 1 point; the share of finished answers that are correct went from 0.36 to 0.62.
- Correct kernels that are also 1.1x faster than PyTorch: 116 to 169 of 800. On tasks both models solve, speed is unchanged (1.05x, CI 0.92-1.23).
- Other benchmarks are unchanged except MMLU-Pro, -3.3 points at the edge of significance.
- SFT on reference kernels with empty reasoning taught the model to skip reasoning. RL undid it within 20 steps.

**Caveats**
In-distribution evaluation, one seed and one hyperparameter setting. Correctness is checked on 3 random inputs only.

**For your work**
A clean example of 'you get what the reward pays for' in RL post-training. Model-generated code also needs sandboxing as hostile input.

**Concepts:** [[Post-training and RL]] · [[Open-weight models]] · [[Coding agents]]
**From:** [[2026-11-26]]

# My notes


---
# References
[Hugging Face blog (community)](https://huggingface.co/blog/ik6626/hip-kernel-rl-mi300x)
