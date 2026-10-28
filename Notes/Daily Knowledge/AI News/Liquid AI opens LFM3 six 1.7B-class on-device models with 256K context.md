---
date: 2026-10-28
section: AI
importance: Low
kind: news
source: "Liquid AI blog"
url: https://www.liquid.ai/blog/lfm3
status: unread
id: 2026-10-28-liquid-lfm3
---
2026-10-28 07:16
Tags: #daily-knowledge #ai

---
# Liquid AI opens LFM3 six 1.7B-class on-device models with 256K context

Liquid AI released LFM3, six open-weight models (text, vision, audio, omni and two decision variants) that share an LFM3-1.7B-Base backbone. The text model was trained on 22T tokens, has 256K context, and runs in about 1 GB at 4-bit. Liquid says it decodes 1.8-2.8x faster than the next model on devices it tested.

## Details

**Caveats**
All numbers are self-reported. The license isn't stated in the post, and long-context retrieval is clearly weaker than larger models.

**For your work**
A candidate for cheap edge or local tool-calling and routing (strong BFCL and IFEval), but not for long-document RAG.

**Method**
- Hybrid architecture with 24 layers: 13 gated short convolutions, 5 sliding-window attention (256 tokens), 6 global attention
- 22T-token pretraining and a 128K vocabulary
- Weights on Hugging Face; tested targets include Galaxy S26 Ultra, Raspberry Pi 5, M4 Max and the Qualcomm Hexagon NPU

**Problem**
Small on-device models usually trade away context length, tool calling and instruction following for speed and memory.

**Results**
- Average 49.37 versus 47.24 for Qwen3.5-9B (vendor table)
- IFEval 96.66; BFCL V4 71.39
- Weaker on GPQA Diamond (63.37 vs 80.40) and RULER 128K (65.56 vs 87.11) than Qwen3.5-9B
- 3.6B tokens/day on one B300 at 1,024 concurrent requests

**Concepts:** [[Open-weight models]] · [[Model releases and pricing]] · [[Inference efficiency]]
**From:** [[2026-10-28]]

# My notes


---
# References
[Liquid AI blog](https://www.liquid.ai/blog/lfm3)
