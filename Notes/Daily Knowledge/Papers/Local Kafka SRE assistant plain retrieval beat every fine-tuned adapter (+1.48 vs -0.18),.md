---
date: 2026-11-19
section: AI
importance: Med
kind: paper
source: "Hugging Face blog"
url: https://huggingface.co/blog/aywengo/building-a-local-kafka-sre-assistant-part-3-retrie
status: unread
id: 2026-11-19-kafka-sre-retrieval-beat-finetuning
---
2026-11-19 07:16
Tags: #daily-knowledge #ai

---
# Local Kafka SRE assistant plain retrieval beat every fine-tuned adapter (+1.48 vs -0.18),

After two fine-tuning attempts made a local Qwen3.8-27B assistant worse, the author found that the unmodified base model plus a 6,444-chunk documentation index scored +1.48 over the base model on 40 real questions (33 wins, 5 ties, 2 losses). A pre-registered ceiling check stopped a third adapter before any training. Tested on: one base model, 40 real plus 42 held-out questions, one local LLM judge (two passes), one Mac Studio.

## Details

**Caveats**
Single author, small question set, and an LLM judge; the item-by-item readings were also done by a model. Part of the +1.48 is fitted to six questions whose excerpts changed (an earlier index scored +1.19). Strict mode sometimes dropped an essential step.

**For your work**
This is a clean argument for clients asking for a fine-tuned model: measure base plus retrieval first, set the stop rule before the run, and check the teacher's ceiling before paying for data. The proxy leak also belongs on the checklist for any 'nothing leaves the machine' deployment.

**Method**
- Runtime: the model writes search terms, BM25 keeps 40 candidates, the BAAI/bge-reranker-v2-m3 cross-encoder reranks them, and up to 6 chunks (within 14,000 characters) go into the prompt
- Index over ten sources (Apache Kafka, Strimzi, Kubernetes, Argo CD, Prometheus Operator runbooks, own runbooks and more)
- Scoring: 40 real questions, two judge passes with answer order flipped, judged by a local GLM-5.3-Flash; a +0.3 gate fixed in advance
- Ceiling check: the teacher (DeepSeek-V4.1-Flash) answered with the same excerpts before any data generation

**Problem**
Can a fully local assistant answer Kafka, Strimzi and Kubernetes operations questions well enough to trust at 3 a.m., and is fine-tuning or retrieval the better route?

**Results**
- Base plus retrieval: +1.48 (standard error 0.21); the v1 adapter scored +0.08 and v2 −0.18
- Teacher with the same excerpts beat base plus retrieval by only +0.24, under the +0.3 line, so v3 was never trained
- Reading ten default answers found 17 invented or wrong items; a one-sentence strict mode brought that to 1, with judged score unchanged within noise (−0.11)
- A test from the published files found 14 problems, including a privacy defect: prompts to a loopback model server were routed through the corporate proxy

**Concepts:** [[RAG]] · [[Hallucination]] · [[Evals and benchmarks]]
**From:** [[2026-11-19]]

# My notes


---
# References
[Hugging Face blog](https://huggingface.co/blog/aywengo/building-a-local-kafka-sre-assistant-part-3-retrie)
