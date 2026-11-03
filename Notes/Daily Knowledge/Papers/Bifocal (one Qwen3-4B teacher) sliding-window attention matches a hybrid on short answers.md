---
date: 2026-11-03
section: AI
importance: Low
kind: paper
source: "Hugging Face blog"
url: https://huggingface.co/blog/sirluk/sliding-window-beats-linear-attention
status: unread
id: 2026-11-03-bifocal-sliding-window
---
2026-11-03 07:16
Tags: #daily-knowledge #ai

---
# Bifocal (one Qwen3-4B teacher) sliding-window attention matches a hybrid on short answers

A community author distilled Qwen3-4B-Instruct-2507 into students where every attention layer uses the same memory budget: a sliding window with a learned sink, or Bifocal, which adds an mLSTM state beside a smaller window. The sliding window led by 0.7 to 1.5 points on short tasks, while Bifocal averaged 15.5 vs 13.8 on math and produced 66 correct answers longer than 4,000 tokens versus 26. Tested on: one teacher, one 4.1B-token distillation budget, 120 math problems; the 95% interval on the math gain runs from 0.0 to 3.4 points.

## Details

**Caveats**
The math gain is small and uncertain (interval 0.0 to 3.4). Bifocal hit the generation limit on 24% of rollouts vs 12% for SWA. There is only one teacher and one budget, the speed tests use synthetic weights, and one student's short-task results were dropped because of a bug.

**For your work**
This is mostly of interest to people choosing efficient long-context open models. Pure sliding-window variants look fine for short enterprise tasks, but they may struggle on long reasoning traces.

**Method**
- Bifocal runs a linear mixer (mLSTM) beside a small sliding window with a learned per-head sink, blended by a per-head sigmoid gate.
- Four students replace all 36 attention layers of Qwen3-4B-Instruct-2507 under an equal per-layer budget of 576 cached-token equivalents, each trained on 4.1B tokens.
- Evaluated on GSM8K, IFEval, HumanEval, AIME 2024/2025 and HMMT, plus decode and prefill speed in vLLM on one H100.

**Problem**
Fixed-memory attention replacements make long-context decoding cheap. A recent paper argues that sliding-window attention (SWA) with sinks is enough. This post tests whether that still holds when the model must generate long reasoning answers.

**Results**
- Short tasks (SWA vs Bifocal): GSM8K 92.3 vs 90.8, IFEval 80.0 vs 79.3, HumanEval 87.2 vs 86.0.
- Math average 13.8 vs 15.5. On answers under about 4,000 tokens they tie (59.1% vs 59.6%), and on longer ones it is 2.5% vs 4.4%.
- Both decode near 195 tokens/s from 1K to 128K prompts, while full attention falls from 200 to 92.
- Shrinking Bifocal's window to 64 collapses math to 4.2.

**Concepts:** [[Inference efficiency]] · [[Open-weight models]]
**From:** [[2026-11-03]]

# My notes


---
# References
[Hugging Face blog](https://huggingface.co/blog/sirluk/sliding-window-beats-linear-attention)
