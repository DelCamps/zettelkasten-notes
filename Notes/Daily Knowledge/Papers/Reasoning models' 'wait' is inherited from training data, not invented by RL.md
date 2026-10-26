---
date: 2026-10-25
section: AI
importance: Low
kind: paper
source: "arXiv 2610.30882"
url: https://arxiv.org/abs/2610.30882
status: unread
id: 2026-10-25-wait-provenance
---
2026-10-25 07:16
Tags: #daily-knowledge #ai

---
# Reasoning models' 'wait' is inherited from training data, not invented by RL

Tracing the reflection marker through open models' training histories, zero-RL almost never coins 'wait': on bases without it, RL raises MATH-500 accuracy while the word stays below 0.05 per 1k tokens. It arrives with mid-training or fine-tuning on traces; released RL-Zero recipes then multiply it while KL-free GRPO does not, and LLM judges can reverse human-labelled trends.

## Details

**Caveats**
Observational; models 0.5B-32B with outcome rewards on English maths only. Measures the word, not reflective behaviour itself.

**For your work**
Little direct use. Do not treat 'wait' counts or judge-scored 'self-correction' as proof that a fine-tune improved reasoning; measure task accuracy instead.

**Method**
- Follows 'wait' through checkpoint histories of open models (OLMo-3, MiMo, Qwen2.5, Mistral, Qwen3).
- Label-free indices of frequency, position, form and usage, plus an injected-error test, computed from sampled outputs.
- 18 zero-RL runs plus comparisons of released RL-Zero recipes and KL-free GRPO from the same base.

**Problem**
RL is widely credited with teaching reasoning models to self-correct, with the word 'wait' cited as evidence of an 'aha moment'. But accuracy gains do not require the word, so the claim may confuse what RL discovers with what was already in the data.

**Results**
- From bases lacking the marker, zero-RL raises accuracy while 'wait' stays below 0.05 per 1k tokens in most runs.
- It enters through mid-training (OLMo-3) or supervised fine-tuning on reasoning traces.
- OLMo-3 and MiMo RL-Zero recipes multiply an existing marker; KL-free GRPO does not, and a GRPO recipe erases a marker seeded by light fine-tuning.
- LLM-as-judge revision metrics can reverse human-labelled trends.

**Concepts:** [[Post-training and RL]] · [[Interpretability]]
**From:** [[2026-10-25]]

# My notes


---
# References
[arXiv 2610.30882](https://arxiv.org/abs/2610.30882)
