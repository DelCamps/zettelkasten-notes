---
date: 2026-10-25
section: AI
importance: High
kind: paper
source: "arXiv 2610.30612"
url: https://arxiv.org/abs/2610.30612
status: unread
id: 2026-10-25-fusion-tax
---
2026-10-25 07:16
Tags: #daily-knowledge #ai

---
# The Fusion Tax hybrid BM25+dense retrieval hurts 13-48% of individual queries

Across 7 BEIR corpora, 5 dense encoders (22M-596M, incl. Qwen3-Embedding) and SPLADE, even the best fusion (dense-weighted score interpolation) ranks relevant documents below the better single retriever on 13-48% of queries and below dense-only on 8-21%, while still winning on average. RRF, the default in most docs, pays more tax whenever the dense retriever is clearly stronger; the authors key the fuse/don't-fuse decision to the measured sparse-dense balance of your corpus.

## Details

**Caveats**
BEIR-only and English; no enterprise or multilingual corpora, no LLM-generated queries. Fusion failure is only weakly predictable within a corpus and transfers poorly across corpora, so you still need your own labelled queries.

**For your work**
Before shipping RRF by default in a client RAG system, measure BM25 vs dense on a small labelled set of the client's queries. If dense clearly dominates, use dense-only or dense-weighted interpolation (about 0.7 dense) rather than RRF, and track per-query regressions, not just mean nDCG.

**Method**
- Standard Anserini BM25, five dense encoders across three generations (MiniLM, BGE small/base/large, Qwen3-Embedding 596M), a SPLADE alternative and a cross-encoder reranker.
- Seven BEIR datasets and three fusion functions (RRF, score interpolation, dense-weighted interpolation), with 'do not fuse' treated as a valid outcome.
- Per-query 'fusion tax' = share of queries where fusion ranks relevant docs below the better (or the deployable dense-only) component, plus loss-averse risk-sensitive evaluation.

**Problem**
Hybrid retrieval (BM25 plus a dense encoder, usually merged with reciprocal rank fusion) is the default recommendation in vector-database and framework docs, justified by aggregate nDCG gains. Nobody checks what fusion costs on individual queries, which is what a user of a RAG app actually experiences.

**Results**
- Best fusion still hurts 13-48% of queries vs. the better component and 8-21% vs. dense-only, while beating dense-only on aggregate on every corpus.
- The downside is statistically significant under risk-sensitive evaluation on 6 of 7 corpora.
- With Qwen3-Embedding, interpolation hurts 14-43% of queries and loses to dense-only on ArguAna (0.638 vs 0.674).
- RRF carries a higher tax wherever dense is clearly stronger and only beats dense-only when the two retrievers are balanced; a cross-encoder recovers part of the tax only where it is itself reliable.

**Concepts:** [[RAG]] · [[Evals and benchmarks]]
**From:** [[2026-10-25]]

# My notes


---
# References
[arXiv 2610.30612](https://arxiv.org/abs/2610.30612)
