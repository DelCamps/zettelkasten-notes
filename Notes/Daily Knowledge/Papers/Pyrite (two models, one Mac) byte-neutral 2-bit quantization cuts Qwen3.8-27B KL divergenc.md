---
date: 2026-10-30
section: AI
importance: Low
kind: paper
source: "Hugging Face blog (community)"
url: https://huggingface.co/blog/masahiroid/qwen38-27b-on-a-16gb-mac-cutting-2-bit-kl-divergen
status: unread
id: 2026-10-30-pyrite-2bit-qwen38
---
2026-10-30 07:16
Tags: #daily-knowledge #ai

---
# Pyrite (two models, one Mac) byte-neutral 2-bit quantization cuts Qwen3.8-27B KL divergenc

A community post shows that, at exactly the same 10.11 GiB size, shifting bits from early MLP layers to the most sensitive late-layer projections cuts Qwen3.8-27B's KL divergence from the BF16 model by 22.29% in English and 22.42% in Japanese versus uniform 2-bit, running at 12.2 tokens/sec on a 16GB M2 Pro with stock mlx-lm. Tested on: Qwen3.8-27B and LLM-jp-4-32B-A3B, English, Japanese and multilingual held-out text, KL and perplexity only, one Mac.

## Details

**Caveats**
Single-author community post; only KL and perplexity, no task benchmarks; held-out set sizes not stated; still far from BF16 (English perplexity 9.60 vs 6.15).

**For your work**
If you run open-weight models locally on laptops, sensitivity-aware mixed-bit allocation is a free gain over uniform 2-bit, but check task quality before trusting it.

**Method**
- Streamed the 51.75 GiB BF16 checkpoint one layer at a time to measure activation-weighted output error per MLP projection; late-layer down_proj error spikes 10x to 40x.
- Widened gate_proj/up_proj group size from 64 to 128 to free 356,515,840 bytes, then spent them on 3-bit upgrades for the most sensitive projections, keeping total bytes identical.
- Uses only standard mlx-lm per-layer quantization settings, no custom kernels.

**Problem**
27B-32B models only fit on a 16GB Apple Silicon Mac at about 2 bits, and uniform 2-bit quantization raises Qwen3.8-27B's English perplexity from 6.1480 to 10.9244.

**Results**
- Winning recipe (22 down_proj + 8 gate/up_proj at 3-bit): English KL 0.622954 to 0.484077, perplexity 10.9244 to 9.6029, top-1 67.21% to 70.81%.
- Japanese KL 0.585637 to 0.454348 (-22.42%); multilingual validation KL -27.08%.
- On the LLM-jp-4-32B-A3B MoE: English KL -12.94% / -21.89% for two variants, at 34-49 tokens/sec.

**Concepts:** [[Inference efficiency]] · [[Open-weight models]]
**From:** [[2026-10-30]]

# My notes


---
# References
[Hugging Face blog (community)](https://huggingface.co/blog/masahiroid/qwen38-27b-on-a-16gb-mac-cutting-2-bit-kl-divergen)
