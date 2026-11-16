---
date: 2026-10-27
section: AI
importance: Med
kind: paper
source: "arXiv 2610.35328"
url: https://arxiv.org/abs/2610.35328
status: unread
id: 2026-10-27-constrained-decoding
---
2026-10-27 07:16
Tags: #daily-knowledge #ai

---
# Constrained decoding does not hurt reasoning; the prompt change does

Across 11 open models, the accuracy drop usually blamed on JSON-constrained decoding comes from changing the prompt and output format, not from token masking; under the same prompt and format, constrained decoding matches or beats free decoding, and 'validity constraints' that mask invalid answers give gains of up to 17.4%. Tested on: 11 models (1.7B-32B) from 4 families (Qwen, Gemma, Llama, SmolLM), several benchmarks.

## Details

**Caveats**
Open models up to 32B only; no hosted structured-output APIs (OpenAI, Anthropic) tested; code not yet public.

**For your work**
Keep strict JSON schemas, but compare against the same prompt; use enums and types as validity constraints for classification fields rather than free text.

**Method**
- Taxonomy: format constraints (enforce structure), validity constraints (mask invalid answers, e.g. wrong types or labels), reasoning constraints (restrict the reasoning path).
- Theory: with the same prompt and expected output format, masking cannot hurt, since it only removes invalid paths.
- Causal ablations that separate prompt and format changes from decoder masking, using state-of-the-art grammar-constrained decoders.

**Problem**
Many teams avoid strict structured outputs because earlier papers reported that forcing JSON degrades reasoning.

**Results**
- Apparent degradation is mostly explained by non-equivalent prompts and output formats.
- Validity constraints give the most consistent gains, up to 17.4%, and improve extractability.
- Reasoning constraints help only when the enforced trajectory is itself a good one.

**Concepts:** [[Structured outputs]] · [[Evals and benchmarks]]
**From:** [[2026-10-27]]

# My notes


---
# References
[arXiv 2610.35328](https://arxiv.org/abs/2610.35328)
