---
date: 2026-11-02
section: AI
importance: Med
kind: paper
source: "arXiv 2610.41073"
url: https://arxiv.org/abs/2610.41073
status: unread
id: 2026-11-02-bf16-fair-cast
---
2026-11-02 07:16
Tags: #daily-knowledge #ai

---
# bf16 rounding silently throws away most RL policy updates; a one-line stochastic-rounding

RL stacks keep fp32 master weights and serve rollouts from a bf16 copy made by round-to-nearest. On Qwen3-1.7B only 0.4-0.5% of served weights change per step, so the sampler lags the optimizer by 50-150 steps, and existing mismatch checks cannot see it. Fair Cast (unbiased rounding at export, with the loss computed on the served copy) is ahead on 18 of 25 matched seed-pairs, tied on 6 and behind on 1, with a mean gain of 6.1 points. Tested on: one model family (Qwen3-0.6B to 4B), AdamW and Muon, 25 matched seed-pairs, one training implementation.

## Details

**Caveats**
Models of at most 4B, one training implementation, and several configurations run with one seed. Removing the implicit lag hurt in two configurations unless an explicit lag was added back.

**For your work**
If you run RL fine-tuning with verl or TRL, check how weights are exported to the sampler, and always evaluate the served bf16 model, not the fp32 checkpoint.

**Method**
- The authors measure the hidden master-vs-served ratio, which frameworks never compute, against the visible trainer-vs-sampler ratio.
- Fair Cast exports with stochastic rounding or error feedback and computes the training loss on the exact served copy: one line, no hyperparameters.
- GRPO-style training on maths, puzzles and games with a vLLM bf16 sampler.

**Problem**
Near a weight w, the bf16 spacing is about |w|/128, so any update smaller than about |w|/256 is rounded away when the trainer exports weights to vLLM/SGLang. Every open-source framework examined (verl, TRL, OpenRLHF, slime, prime-rl, AReaL) rounds this way.

**Results**
- The visible ratio stays near 0.01 per token while the hidden one grows to 0.10-0.45.
- On zebra puzzles Fair Cast reaches 0.57 ± 0.16 over four runs, where round-to-nearest collapses to 0.33 ± 0.10.
- Under round-to-nearest, the saved fp32 checkpoint can score 12-50 points below its own served export; under Fair Cast the two agree.
- Cost: 22-38 ms per export of 1.7B parameters.

**Concepts:** [[Post-training and RL]] · [[Inference efficiency]]
**From:** [[2026-11-02]]

# My notes


---
# References
[arXiv 2610.41073](https://arxiv.org/abs/2610.41073)
