---
date: 2026-11-13
section: AI
importance: High
kind: paper
source: "arXiv 2611.15102"
url: https://arxiv.org/abs/2611.15102
status: unread
id: 2026-11-13-one-fabrication-forecasters
---
2026-11-13 07:16
Tags: #daily-knowledge #ai

---
# One fake news article is enough retrieval-based LLM forecasters follow it, and the stronge

Northwestern researchers published one invented news article per question into the archive a forecasting agent searches. Once retrieved, it reversed 74-82% of the forecasts that disagreed with it on every model tested, and the multi-agent designs of two leading deployed forecasters retrieved it in about 90% of runs. Average accuracy barely moved, so you cannot spot the attack from the outputs. Tested on: 5 models from 5 providers (Gemini 3.7 Flash, GPT-5.6, GLM-5.3 Flash, Grok 4.20, Claude Sonnet 5), 183 stock and 308 prediction-market questions, a single-retrieval forecaster and re-implementations of two deployed systems.

## Details

**Caveats**
No live-web test. The deployed systems are re-implementations over the authors' archives, without the vendors' own search. The scale experiments rest on 42 questions.

**For your work**
Any client RAG or deep-research agent reading the open web is exposed: one planted source steers decisions while quality metrics stay flat. Monitor which passage decided the answer and flag single-source claims.

**Method**
- Frozen 2026 news archives. An outside model wrote one fake article per question, checked for style, falsity and by a human.
- Measured reversal with the article forced into context, and how often the systems' own search retrieved it.
- Tested two retrieval-time defences, passage filtering and partitioned retrieval, alone and combined.

**Problem**
Forecasting agents that search the news are only as reliable as every article they retrieve, and anyone can publish through paid press-release wires. How far does the weakest attacker get: one who knows only the question, has no access to the model or retriever, and publishes one plausible article?

**Results**
- A genuine article in the same position changed forecasts about one third as often as the fabricated one. Asked directly, models flagged the fabrication but also nearly half of the genuine news.
- Two opposing fake articles did not make the model hedge. It returned a confident forecast in whichever direction it weighed more.
- Each defence stopped a single article but was bypassed by a one-prompt change. Combined, they held at four articles, fell to sixteen distorted copies, changed 29% of clean decisions, discarded 39% of genuine news and needed 48 LLM calls per forecast.

**Concepts:** [[Agent security]] · [[RAG]]
**From:** [[2026-11-13]]

# My notes


---
# References
[arXiv 2611.15102](https://arxiv.org/abs/2611.15102)
