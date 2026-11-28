---
date: 2026-11-27
section: AI
importance: Med
kind: paper
source: "Hugging Face blog (NVIDIA)"
url: https://huggingface.co/blog/nvidia/building-on-nemotron-35-parse-open-data-fine-tunin
status: unread
id: 2026-11-27-nemotron-parse-open-data-recipe
---
2026-11-27 07:16
Tags: #daily-knowledge #ai

---
# NVIDIA opens the data and fine-tuning recipe behind Nemotron 3.5 Parse GRPO cuts looping p

NVIDIA released three synthetic datasets (9.98M charts, 1M tables, 7.9M multilingual OCR examples), an SFT-plus-GRPO fine-tuning recipe and a DFlash2 speculative-decoding draft model for its 0.6B document parser Nemotron 3.5 Parse. RL with verifiable rewards cut loop-flagged pages from 126 to 29 and raised the overall score from 66.24 to 71.38, and on one H200 the model parses 20.44 pages/s with speculation versus 2.98 for Parse 2.0. Tested on: one model family, NVIDIA's own evals on development checkpoints, one GPU type and one 2,078-page set.

## Details

**Caveats**
Self-reported by the vendor; RL comparison uses development checkpoints, not the released model; Parse 2.0 throughput from single trials; no absolute baseline ParseBench scores. The model itself shipped on 17 October under the OpenMDW licence (commercial use allowed); the new parts are the data, recipe and draft model.

**For your work**
A cheap, commercially usable parser plus a recipe to fine-tune it on a client's own forms (insurance, invoices) for document RAG pipelines.

**Method**
- SFT on text, layout, tables, charts and multilingual pages, then RLVR with GRPO whose rewards check extraction quality, chart values, usable structure, completion and no looping.
- Architecture changes from Parse 2.0: dynamic NaViT image inputs, visual tokens as a causal prefix instead of cross-attention, GQA-8.
- DFlash2 draft model for speculative decoding; optional double or triple pass that re-parses hard regions.

**Problem**
Document parsers for RAG and agent pipelines must turn page images into reading-order text, tables and charts reliably and cheaply; small models tend to loop or run to the token cap.

**Results**
- GRPO vs SFT: loop-flagged pages 126 to 29, outputs hitting the 9,000-token cap 185 to 35, score 66.24 to 71.38 (+5.18 tables, +4.15 charts).
- One H200, concurrency 512: 13.48 pages/s without speculation, 20.44 with DFlash2, vs 2.98 for Parse 2.0.
- Double and triple pass add 2.18 and 2.46 ParseBench points.
- Synthetic dental-form adaptation: pass@1 0.00% to 95.85% after SFT and 96.58% after RLVR.

**Concepts:** [[RAG]] · [[Post-training and RL]] · [[Open-weight models]]
**From:** [[2026-11-27]]

# My notes


---
# References
[Hugging Face blog (NVIDIA)](https://huggingface.co/blog/nvidia/building-on-nemotron-35-parse-open-data-fine-tunin)
