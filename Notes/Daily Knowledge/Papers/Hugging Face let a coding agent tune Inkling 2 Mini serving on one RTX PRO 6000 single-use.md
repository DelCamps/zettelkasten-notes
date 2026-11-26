---
date: 2026-11-26
section: AI
importance: Low
kind: paper
source: "Hugging Face blog"
url: https://huggingface.co/blog/inkling-2-mini-inference-hillclimb
status: unread
id: 2026-11-26-hf-inkling-hillclimb
---
2026-11-26 07:16
Tags: #daily-knowledge #ai

---
# Hugging Face let a coding agent tune Inkling 2 Mini serving on one RTX PRO 6000 single-use

Hugging Face gave a coding agent an inference-optimisation skill (change one variable at a time, bracket every candidate between two control runs, keep a full log), the hf CLI and HF Jobs. Over an afternoon and 46 valid benchmark runs, it found that vLLM nightly with DSpark speculative decoding (7 drafts, probabilistic draft sampling) beats SGLang. Greedy outputs stayed byte-identical. Tested on: one model (Inkling 2 Mini) on one GPU type, vLLM vs SGLang, a fixed panel of six prompts.

## Details

**Problem**
The published serving recipes for Inkling 2 Mini target B200 and GB300 GPUs. How fast can it run on a single RTX PRO 6000 96 GB ($2.75/h endpoint)?

**Method**
- The agent measured hardware ceilings first (1,469 GB/s copy bandwidth) and computed a theoretical decode limit.
- Changes were kept only if they beat both surrounding control runs without regressing other metrics.
- Before deploying, the config had to pass long-context retrieval, a concurrency soak and greedy-equivalence checks.

**Results**
- Single-user decode: SGLang baseline 134-139 tok/s, vLLM 157.0, vLLM + DSpark 190.6. 8-user aggregate went from about 570 to 716 tok/s (+26%).
- Speculative verification touches about 40% of each layer's experts instead of 6%, so the ceiling drops to about 201 tok/s. 190.6 is about 95% of that.
- Needle retrieval passed 3/3 at 249,970 tokens. Greedy decoding with DSpark was byte-identical in 6/6 prompts.
- Some apparent wins were noise: an SGLang flag showed +4% once and did not reproduce. SGLang varied ±4.5% between runs vs 0.4% for vLLM.

**Caveats**
One model, one GPU and nightly engine builds. Speedups are specific to this looped MoE and its drafter.

**For your work**
A reusable pattern: give an agent a strict benchmarking protocol (bracketing controls, a ledger, acceptance gates) to tune client inference endpoints instead of hand-tuning flags.

**Concepts:** [[Inference efficiency]] · [[Open-weight models]] · [[Coding agents]]
**From:** [[2026-11-26]]

# My notes


---
# References
[Hugging Face blog](https://huggingface.co/blog/inkling-2-mini-inference-hillclimb)
