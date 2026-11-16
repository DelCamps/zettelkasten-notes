---
date: 2026-11-14
section: AI
importance: Med
kind: paper
source: "arXiv 2611.17161"
url: https://arxiv.org/abs/2611.17161
status: unread
id: 2026-11-14-rag-parametric-provenance
---
2026-11-14 07:16
Tags: #daily-knowledge #ai

---
# Cited but unused 1.2% to 15.7% of cited RAG claims came from model memory, and NLI citatio

Swapping a fact in the retrieved passages for a false value and re-asking shows whether a cited claim really came from the context. Between 1.2% and 15.7% of citable claims came from the model's own memory, rising with model size; standard NLI citation verification could not tell these apart, because a model answering from memory picks a citation that agrees with it. Tested on: 6 open models from 2 families (Qwen2.5 0.5B-14B, Llama-3.1-8B), mainly ASQA, plus ELI5 and QAMPARI on one model.

## Details

**Caveats**
Small open models only, no frontier or API models; rates depend on how far the substituted value is from the original; the detector is not yet usable.

**For your work**
Don't sell 'every claim is cited' as proof of grounding. In client RAG audits, add counterfactual tests: change a fact in the source and check that the answer changes.

**Method**
- Counterfactual value substitution: replace a fact in the retrieved passages with a false variant, re-query, and see whether the answer follows the passage.
- Five Qwen2.5-Instruct sizes and Llama-3.1-8B, greedy decoding, ASQA with GTR retrieval; ELI5 and QAMPARI on Qwen2.5-7B.
- Compared ten attribution methods on identical claims.

**Problem**
RAG systems attach citations, and teams verify them with entailment (NLI) checks. A claim can be supported by the cited passage yet actually come from the model's parametric memory.

**Results**
- Within Qwen the rate rose from 1.2% at 0.5B to 13.3% at 14B; Llama-3.1-8B reached 15.7% vs 8.2% for Qwen2.5-7B.
- ELI5 4.5% and QAMPARI 2.4% on Qwen2.5-7B.
- A DeBERTa NLI verifier was at chance on every model (all intervals contained 0.5); three more entailment models gave the same result.
- Contrasting the model's output with and without context separated provenance best, but not well enough to act on.

**Concepts:** [[RAG]] · [[Hallucination]] · [[Evals and benchmarks]]
**From:** [[2026-11-14]]

# My notes


---
# References
[arXiv 2611.17161](https://arxiv.org/abs/2611.17161)
