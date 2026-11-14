---
date: 2026-11-14
section: AI
importance: Low
kind: paper
source: "Hugging Face blog"
url: https://huggingface.co/blog/token-pooling
status: unread
id: 2026-11-14-hf-token-pooling-training
---
2026-11-14 07:16
Tags: #daily-knowledge #ai

---
# Hugging Face (one encoder, one benchmark) training multi-vector retrievers for pooling kee

Token pooling merges similar token vectors to shrink ColBERT-style indexes. Training with an extra loss on pooled documents, now a loss wrapper in Sentence Transformers, raised retained nDCG@10 at pool factor 4 from 94.6% to 97.8% while storing 74.8% fewer document vectors than unpooled retrieval, with bigger gains at tighter budgets. Tested on: one ModernBERT-base encoder trained twice (one seed, 120,000 MS MARCO triplets), NanoBEIR.

## Details

**Caveats**
One run with no hyperparameter search on a small benchmark; the method builds on earlier pooling work by Stefan Josef and LightOn.

**For your work**
If a client RAG system uses ColBERT-style retrieval and index size or cost matters, combine quantization, token pooling and pooling-aware fine-tuning, and test on the client's own corpus.

**Method**
- Loss = half the normal retrieval loss on full document embeddings plus half on documents pooled to about a quarter of their vectors (Ward clustering, straight-through gradients).
- Two ModernBERT-base models trained identically except for the loss: one epoch over 120,000 MS MARCO triplets, seed 42.
- Evaluated on NanoBEIR with pool factors 2 to 6, fixed vector caps and calibrated adaptive thresholds.

**Problem**
Multi-vector (late-interaction) retrievers keep one vector per token, so large corpora need hundreds of millions of vectors; pooling them after training loses retrieval quality.

**Results**
- Pool factor 4: nDCG@10 from 49.03 to 51.23; retention from 94.6% to 97.8%.
- Unpooled retrieval also improved, from 51.84 to 52.39.
- At a cap of 4 vectors per document the gain was 5.78 points (37.22 to 43.00).
- Adaptive pooling at 29.58 vectors per document kept 97.3% of the unpooled score with 84.7% fewer vectors.

**Concepts:** [[RAG]] · [[Inference efficiency]]
**From:** [[2026-11-14]]

# My notes


---
# References
[Hugging Face blog](https://huggingface.co/blog/token-pooling)
