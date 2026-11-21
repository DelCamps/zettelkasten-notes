---
date: 2026-11-21
section: AI
importance: Med
kind: news
source: "Thinking Machines Lab"
url: https://thinkingmachines.ai/news/inkling-2-mini/
status: unread
id: 2026-11-21-inkling-2-mini
---
2026-11-21 07:16
Tags: #daily-knowledge #ai

---
# Thinking Machines releases Inkling 2 Mini a 26.4B looped open-weight model for laptops tha

Thinking Machines' Inkling 2 Mini is a mixture-of-experts looped transformer with 26.4B total and 3.4B active parameters, whose middle blocks run three times per token; it needs about 20GB and runs on Macs with at least 32GB via Ollama. The lab reports 79.2% on SWE-bench Verified (bash only) and 48.2% on DeepSWE v1.1 versus 77.8% and 42.2% for Qwen3.8-27B, and a tied 20.1 on the AA Index v5.0.

## Details

**Caveats**
Benchmarks are mostly the lab's own; the lab says it is not the strongest small model for multi-turn chat or many-constraint instructions (50.0% on MultiChallenge) and its non-hallucination rate is 63.4% vs 71.4% for Qwen3.8-27B. The lab's page does not name a license.

**For your work**
A credible candidate for on-device or air-gapped coding and agent pilots where data cannot leave the client. Test hallucination and instruction-following on your own tasks before relying on it.

**Method**
- 24 stored layers in four blocks of six; the two middle blocks loop three times, giving 48 layer applications per token.
- Derived from a larger model by pruning two-thirds of the experts (from 384 to 128 per layer); weights mostly NVFP4, last four layers MXFP8.
- Open weights on Hugging Face; also on Tinker for inference and fine-tuning, with GGUF builds via Unsloth and llama.cpp.
- A variable-loop research model (one to five passes) is released for monitorability research.

**Problem**
Small open models that can run locally usually trail on agentic coding; Thinking Machines bets on looping layers instead of more parameters.

**Results**
- SWE-bench Pro v2 (Hard): 77.9% vs 73.8% for Qwen3.8-27B; MCP Atlas 82.7% vs 77.3%.
- Terminal Bench v2.1: 71.6% vs 73.0% for Qwen3.8-27B.
- BrowseComp: 79.0% vs 78.9% for Nemotron 3.5 Super VL; AA Index (v5.0) 20.1, tied with Qwen3.8-27B.
- Vals Index v2.2: 46.5% vs 29.8% for Nemotron 3.5 Super VL.

**Concepts:** [[Open-weight models]] · [[Model releases and pricing]] · [[Coding agents]]
**From:** [[2026-11-21]]

# My notes


---
# References
[Thinking Machines Lab](https://thinkingmachines.ai/news/inkling-2-mini/)
