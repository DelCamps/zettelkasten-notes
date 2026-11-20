---
date: 2026-11-20
section: AI
importance: Low
kind: paper
source: "Hugging Face blog"
url: https://huggingface.co/blog/NeuML/introducing-atto
status: unread
id: 2026-11-20-atto-compact-embeddings
---
2026-11-20 07:16
Tags: #daily-knowledge #ai

---
# Atto embeddings a 28M-parameter model reaches 0.5138 nDCG@10 on three BEIR sets, above Min

NeuML released Atto, a family of tiny embedding models built from convolution-plus-gated-attention mixers and router-free convolutional experts, with dense, sparse and ColBERT variants distilled from LightOn models. atto-17m-8192d scores 0.5109 and atto-28m-8192d 0.5138 average nDCG@10, against 0.4802 for all-MiniLM-L6-v2 and 0.5638 for the 110M DenseOn teacher. Tested on: 3 BEIR datasets (ArguAna, NFCorpus, SciFact), one author's models against 6 baselines.

## Details

**Caveats**
Only three small BEIR datasets. Parameter count hides storage cost: a 2,048-dimension float32 vector is about 8 KiB per document before index overhead. Results are the author's own.

**For your work**
Little direct use for cloud RAG; worth a look for on-device or very cheap retrieval prototypes.

**Method**
- Each layer: a GatedConvAttentionMixer (depthwise convolution plus gated attention) and a PhaseGatedMoE of local and dilated convolutional experts with no learned router
- Compute in a compact hidden space, then a linear projection to large outputs (up to 8,192 dimensions)
- Masked language modelling on English Wikipedia, then distillation from DenseOn on MS MARCO 500K triplets (dense and sparse) and from LightOn data for ColBERT

**Problem**
Small embedding models for local or edge retrieval usually trade a lot of quality for size.

**Results**
- atto-28m-8192d: 0.5138 average nDCG@10 vs all-MiniLM-L6-v2 0.4802 and DenseOn 0.5638
- atto-90k-2048d: 0.4257 with about 256x fewer parameters than MiniLM-L6-v2
- Sparse atto-17m-8192d-sparse: 0.4596, about 90% of its dense counterpart (SlideOn 0.5349)
- colbert-atto-950k-128d: 0.4816, close to LateOn's 0.5463 at a fraction of the size

**Concepts:** [[RAG]] · [[Inference efficiency]]
**From:** [[2026-11-20]]

# My notes


---
# References
[Hugging Face blog](https://huggingface.co/blog/NeuML/introducing-atto)
