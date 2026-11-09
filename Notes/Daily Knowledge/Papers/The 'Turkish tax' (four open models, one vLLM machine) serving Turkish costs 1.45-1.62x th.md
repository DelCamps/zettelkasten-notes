---
date: 2026-11-09
section: AI
importance: Low
kind: paper
source: "Hugging Face blog (community)"
url: https://huggingface.co/blog/serkanpeker/turkish-tax
status: unread
id: 2026-11-09-turkish-serving-tax
---
2026-11-09 07:16
Tags: #daily-knowledge #ai

---
# The 'Turkish tax' (four open models, one vLLM machine) serving Turkish costs 1.45-1.62x th

A Hugging Face community study served the same FLORES+ content in Turkish and English with vLLM and found Turkish cost 1.45 to 1.62 times as much GPU time at 256 concurrent requests, with token count explaining 76-82% of the gap. Six of seven tokenizers needed 1.36-1.62x as many tokens for Turkish, and 4-bit GGUF quantization without an importance matrix hurt Turkish more than English. Tested on: Turkish-Gemma-9b-T1, Gemma 4 12B, Ministral 3 14B and Qwen3.8-27B on one 6xH200 vLLM machine, FLORES+ translated text, fixed 256-token outputs; serving cost only, not answer quality.

## Details

**Caveats**
Single author, community blog. Cost per word assumes generated text tokenizes like FLORES+, which is translated from English; outputs were fixed at 256 tokens with short prompts and prefix caching off, so no quality benchmark was run. Tensor-parallel results cover only Qwen3.8-27B, and most runs shared the machine with other models.

**For your work**
When sizing self-hosted LLMs for Spanish or other non-English clients, budget from token counts in the client's language, not English benchmarks, and check the tokenizer and quantization calibration before quoting GPU costs.

**Method**
- Served 562 FLORES+ documents in Turkish and English with vLLM 0.33.0 on a 6xH200 machine, 256 generated tokens per request, at 1 to 256 concurrent requests.
- Counted tokens on 2,009 parallel FLORES+ sentences across seven tokenizers.
- Measured quality loss from dynamic FP8 (perplexity in vLLM) and GGUF Q4_K_M (KL divergence in llama.cpp).

**Problem**
Non-English text usually costs more to serve on open LLMs than the same content in English. The author measures how big this 'Turkish tax' is and where it comes from.

**Results**
- At 256 concurrent requests Turkish cost 1.45x (Gemma 4 12B) to 1.62x (Ministral 3 14B) the GPU time of English; token count explains 76-82% of the gap, and Turkish output speed was 6.2-8.4% lower.
- Six of seven tokenizers needed 1.36-1.62x as many tokens for Turkish; Turkish-native Kumru-2B was the exception at 0.64x.
- For Qwen3.8-27B, one GPU was cheapest at maximum throughput (0.157 GPU-hours per million Turkish words vs 0.218 on four), but four GPUs won under a ~22 ms per-token latency target.
- Q4_K_M without an importance matrix gave 1.68x (Turkish-Gemma) and 1.58x (Trendyol-LLM) the per-token KL divergence on Turkish; using any importance matrix mattered more than its calibration language.

**Concepts:** [[Inference efficiency]] · [[Open-weight models]]
**From:** [[2026-11-09]]

# My notes


---
# References
[Hugging Face blog (community)](https://huggingface.co/blog/serkanpeker/turkish-tax)
