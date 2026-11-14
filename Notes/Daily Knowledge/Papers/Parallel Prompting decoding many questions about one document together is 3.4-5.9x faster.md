---
date: 2026-11-14
section: AI
importance: Low
kind: paper
source: "arXiv 2611.15130"
url: https://arxiv.org/abs/2611.15130
status: unread
id: 2026-11-14-parallel-prompting-shared-doc
---
2026-11-14 07:16
Tags: #daily-knowledge #ai

---
# Parallel Prompting decoding many questions about one document together is 3.4-5.9x faster

Prefix caching stores a shared document once, but every question's decode step still re-reads its KV cache. Parallel Prompting decodes many questions as streams of one request with a per-stream attention mask, added to SGLang in about 80 lines; with CodeLlama-7B it was 3.7x faster than stock SGLang on an A100 and faster in all 144 timed runs, with matching answer quality, but modern grouped-query-attention models gain far less. Tested on: 6 open models from 2 families (CodeLlama 7B/13B, Qwen2.5 1.5B-32B), SGLang, single GPU, offline batches.

## Details

**Caveats**
Batch and offline workloads only; one attention backend, a single GPU and greedy decoding; outputs are not bitwise identical to standard decoding.

**For your work**
Worth a test for large offline extraction or eval runs over the same contracts or reports on self-hosted models; check the model's attention type first, since GQA models gain much less.

**Method**
- Decode P questions as P independent streams of a single request, so each step reads the shared document's KV cache once for all streams.
- A stream-id attention mask, evaluated inside the attention kernel, keeps each answer conditioned only on the document and its own question.
- Implemented in SGLang with fixed-shape decode steps captured as CUDA graphs.

**Problem**
Document QA, data labelling and LLM-as-judge jobs often ask many independent questions about the same long document. Decoding is memory-bandwidth bound and scales with the number of questions.

**Results**
- CodeLlama-7B, 8k-16k-token documents, 64-256 questions: 3.7x faster than stock SGLang (FlashInfer) on an A100, 5.9-6.0x on an RTX A6000.
- Long answers shrink the gain: from 3.6x to 1.9x on the A100 going from 128 to 1024 output tokens.
- Qwen2.5-1.5B and 7B gain only 1.3-1.5x; Qwen2.5-1.5B was 5-7% slower with 64 questions.
- SQuAD exact match and F1 matched the stock backends.

**Concepts:** [[Inference efficiency]]
**From:** [[2026-11-14]]

# My notes


---
# References
[arXiv 2611.15130](https://arxiv.org/abs/2611.15130)
