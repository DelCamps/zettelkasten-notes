---
date: 2026-11-09
section: AI
importance: Med
kind: paper
source: "arXiv 2611.09028"
url: https://arxiv.org/abs/2611.09028
status: unread
id: 2026-11-09-scout-cost-router
---
2026-11-09 07:16
Tags: #daily-knowledge #ai

---
# Price each query, not each model a small 'scout' model predicts reasoning-model output len

Routers usually price a model at its average output length, but reasoning models' output length varies 11-121x across problems. A linear probe on a small frozen LLM's prompt activations predicts each candidate's length and success, and saves 9.4-33.0% against median-length pricing on 8 of 9 datasets, up to 69% of what perfect cost knowledge would save. Tested on: 5 reasoning candidates in the main pool (gpt-oss-20b/120b at several effort levels, deepseek-v4-flash) plus an appendix pool of 8 candidates from three further families, 9 benchmarks, 10 training splits with 95% intervals, against reimplemented ZeroRouter, MixLLM-style and other estimators.

## Details

**Caveats**
Each candidate needs output-length labels. The probe does not raise the best achievable accuracy, and it barely separates two strong candidates with similar prices (at most 7.0%). Models are called via OpenRouter, where length varies by provider.

**For your work**
If you route between reasoning tiers or effort levels for clients, a cheap length probe on a small model can cut spend noticeably. Measure per-query length variance first, since that is where the saving comes from.

**Method**
- A frozen 'scout' LLM (Qwen3, 0.6B-14B) reads only the prompt; one linear probe per candidate predicts success and output length
- Compared with median pricing, perfect per-query cost knowledge, and external estimators given the same success predictions
- Tests on how many labels are needed, transfer to new benchmarks, and mixed traffic

**Problem**
Model routers trade accuracy against cost but treat cost as a constant per model. With reasoning models, cost per query mostly depends on how long the answer is.

**Results**
- Perfect cost knowledge would save 29-61% on 8 of 9 datasets with reasoning candidates, much less with non-reasoning ones
- Ahead of external estimators in 69 of 72 comparisons, significantly in 50
- 20 labelled problems keep most of the saving; 22.4% saving on mixed traffic beyond pricing per benchmark
- Savings stop growing around a 2B scout; above 4B, a bigger scout costs more than it saves

**Concepts:** [[Inference efficiency]] · [[Model releases and pricing]]
**From:** [[2026-11-09]]

# My notes


---
# References
[arXiv 2611.09028](https://arxiv.org/abs/2611.09028)
