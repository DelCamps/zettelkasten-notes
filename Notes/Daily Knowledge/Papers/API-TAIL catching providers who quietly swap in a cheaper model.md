---
date: 2026-10-28
section: AI
importance: Med
kind: paper
source: "arXiv 2610.36801"
url: https://arxiv.org/abs/2610.36801
status: unread
id: 2026-10-28-api-tail
---
2026-10-28 07:16
Tags: #daily-knowledge #ai

---
# API-TAIL catching providers who quietly swap in a cheaper model

A statistical audit detects when an API provider routes a fraction of requests to a cheaper substitute while billing for the advertised model. It aligns one effective temperature to absorb honest decoding differences, then counts responses that stay in the surprise tail; published rank- and MMD-based audits had zero power against 10% substitution with 200 requests under the same calibration. Tested on: 26 honest OpenRouter endpoints for 2 model families, 6 substitutes on 7 endpoints, 143,955 responses.

## Details

**Caveats**
Requires local access to the claimed model's weights to score likelihoods, so it works for open-weight models, not closed APIs like Claude or GPT. Only two model families tested.

**For your work**
When a client buys an open-weight model through a third-party host (OpenRouter, a cloud marketplace), this gives a cheap, defensible way to verify they get the model they pay for. Worth keeping in mind for vendor due-diligence and model-procurement advice.

**Method**
- Score each returned response by its standardized excess surprisal under the claimed model, computed exactly over the full vocabulary.
- Pick one effective temperature that centres those scores for the batch, which absorbs batch-wide shifts from honest serving choices.
- Count responses whose score stays above 3 and compare with a threshold calibrated on locally generated responses across a pool of legitimate configurations.

**Problem**
Commercial APIs return only text, so a provider can answer some requests with a cheaper model and nobody notices in any single response. Detection is hard because honest providers also change outputs through undocumented temperature, truncation, penalties and default system prompts, so an audit must tolerate many legitimate configurations at once.

**Results**
- Accepts every plain honest endpoint among 26 serving Qwen3.8-27B or Gemma-4-31B-it via OpenRouter.
- Detects 10% substitution with a few hundred requests, at an API cost of cents plus a few GPU-minutes of scoring.
- Existing rank-based and MMD-based audits, calibrated the same way, had zero power against 10% substitution with 200 requests.

**Concepts:** [[Evals and benchmarks]] · [[Open-weight models]] · [[Model releases and pricing]]
**From:** [[2026-10-28]]

# My notes


---
# References
[arXiv 2610.36801](https://arxiv.org/abs/2610.36801)
