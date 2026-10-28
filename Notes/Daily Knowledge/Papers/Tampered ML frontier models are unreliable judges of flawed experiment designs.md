---
date: 2026-10-26
section: AI
importance: Med
kind: paper
source: "arXiv 2610.32114"
url: https://arxiv.org/abs/2610.32114
status: unread
id: 2026-10-26-tampered-ml
---
2026-10-26 07:16
Tags: #daily-knowledge #ai

---
# Tampered ML frontier models are unreliable judges of flawed experiment designs

Anthropic Fellows built 1,858 pairs of experiment proposals from published ML papers, each with a minimally edited twin containing a methodological flaw. The best model, Opus 5, picks the sound one in both orders only 77.9% of the time; models flip with presentation order and prefer flawed designs that look more specific or conventional. Tested on: frontier models from Anthropic, OpenAI, Google and Moonshot, 1,858 pairs, with a human-validated sample (86% valid).

## Details

**Caveats**
Costly construction and the generation pipeline is not released; pairwise choice is easier than open-ended critique; 14% of items may be invalid.

**For your work**
Do not use an LLM as the sole reviewer of eval designs or experiment plans; when you use LLM judges in pairwise mode, always score both orders and treat order-inconsistent verdicts as unknown.

**Method**
- Reconstruct experiment proposals from published ML papers.
- Generate a minimally edited counterfactual that introduces one validity-relevant flaw (e.g. circular metric, unfair baseline, leakage), filtered by automated checks.
- Models must pick the sounder proposal in both presentation orders; a stratified human study validates the items.

**Problem**
Automating research, including alignment research, needs models that can tell whether an experiment actually supports its claim, a hard-to-supervise skill that standard benchmarks don't measure.

**Results**
- 1,858 item pairs; human validation estimates 86% of items valid (95% CI 81-91%).
- Best both-orders accuracy: Opus 5 at 77.9%; all models above chance but far from reliable.
- Strong order sensitivity, and a bias toward flawed designs that look more specific, transparent or conventional.
- Some failures involve hallucinated recall of the source paper.

**Concepts:** [[Evals and benchmarks]] · [[AI for science and math]]
**From:** [[2026-10-26]]

# My notes


---
# References
[arXiv 2610.32114](https://arxiv.org/abs/2610.32114)
