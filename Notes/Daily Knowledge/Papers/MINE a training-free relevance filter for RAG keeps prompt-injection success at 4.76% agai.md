---
date: 2026-11-28
section: AI
importance: Med
kind: paper
source: "arXiv 2611.34188"
url: https://arxiv.org/abs/2611.34188
status: unread
id: 2026-11-28-mine-rag-injection-filter
---
2026-11-28 07:16
Tags: #daily-knowledge #ai

---
# MINE a training-free relevance filter for RAG keeps prompt-injection success at 4.76% agai

Instead of detecting injections, MINE keeps only the retrieved spans that maximise mutual information with the user's query while penalising semantic spread, so off-topic injected instructions drop out before the LLM sees them. Against an attacker who knows the algorithm it keeps 85.45% accuracy with 4.76% attack success on Inj-SQuAD (23.20% on long contexts), and it is the fastest defence on long contexts. Tested on: 3 open models from 2 families (Llama, Qwen), 4 datasets including InjecAgent, 6 attack types.

## Details

**Caveats**
Span splitter assumes well-formed prose, so code, JSON or tables may yield spans too coarse to isolate an injection; open models only; long-context adaptive ASR still 23.20%.

**For your work**
- Cheap pre-LLM filter worth testing in client RAG pipelines over untrusted documents, alongside action-level controls.

**Method**
- Splits retrieved context into spans and embeds them.
- Treats defence as subset selection: maximise query-span mutual information, penalise embedding variance; solved by projected gradient ascent on simplex weights, then top-k selection.
- New LC-Inj-SQuAD long-context benchmark averaging 4,032 words per context.

**Problem**
Prompt-engineering defences for RAG get overridden by injected instructions, and supervised detectors need retraining for each new attack style.

**Results**
- Adaptive attack on Llama-3.1-70B: MINE 85.45% accuracy / 4.76% ASR on Inj-SQuAD vs Sandwich 79.97% / 16.28%; MELON and indirect-pia reach low ASR only by collapsing accuracy.
- InjecAgent with Qwen3-30B-A3B: 0.12% ASR at 99.60% valid rate.
- Latency on long contexts: 0.75 s per sample under attack vs 3.66 s for Sandwich.

**Concepts:** [[RAG]] · [[Agent security]]
**From:** [[2026-11-28]]

# My notes


---
# References
[arXiv 2611.34188](https://arxiv.org/abs/2611.34188)
