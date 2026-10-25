---
date: 2026-10-23
section: AI
importance: Med
kind: paper
source: "arXiv 2610.30066"
url: https://arxiv.org/abs/2610.30066
status: unread
id: 2026-10-23-looped-udlm
---
2026-10-23 07:16
Tags: #daily-knowledge #ai

---
# Looped uniform diffusion LMs

Looping a few early layers inside each denoising step reaches the same validation NLL with 2.8–3.3x fewer training FLOPs, and up to 9.8% lower generation perplexity at the same number of model calls. The objective and sampler stay unchanged.

## Details

**Problem**
Uniform diffusion language models (UDLMs) corrupt text with random real tokens, so the denoiser must work out which tokens are wrong from a context that may itself be corrupted. This gives better downstream reasoning than masked diffusion but costs more training FLOPs.

**Method**
- Take the Duo++ recipe (a 170M-parameter DiT) and loop transformer blocks 1-2 up to 12 times inside each denoising step. Looping adds depth but no parameters; the objective and sampler stay unchanged.
- Draw a random loop count each training step: uniform, FLOP-proportional (small counts more often) or noise-proportional.
- At inference, use a fixed loop count or adaptive looping that stops when the hidden state stops changing.

**Results**
- Reaches the validation NLL of a non-looped model trained on about 0.5T tokens with up to 2.8x fewer training FLOPs on OpenWebText and 3.3x fewer on FineWeb-Edu.
- Up to 9.8% lower generation perplexity at the same number of denoiser calls, and 11.5% lower zero-shot perplexity on average across seven out-of-domain datasets.
- Adaptive looping matches 12 fixed loops on ten multiple-choice tasks with 26-35% fewer iterations; FLOP-proportional training needs 12% fewer loops than uniform at no accuracy cost.
- 93-94% of the gain comes from better predictions at replaced tokens.

**Caveats**
Small-scale study (170M params, GPT-2 tokenizer). Comparisons at matched model calls are not compute-matched at inference: 12 loops cost 2.05x the FLOPs of one. FLOP-proportional training trades some sample quality.

**For your work**
Little direct use: this is pretraining research on diffusion LMs, relevant only if you later evaluate diffusion-based models for low-latency generation.

**Concepts:** Diffusion language models · Training efficiency
**From:** [[2026-10-23]]

# My notes


---
# References
[arXiv 2610.30066](https://arxiv.org/abs/2610.30066)
