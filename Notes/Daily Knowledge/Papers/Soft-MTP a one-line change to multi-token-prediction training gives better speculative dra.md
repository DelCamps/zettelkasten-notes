---
date: 2026-11-01
section: AI
importance: Low
kind: paper
source: "arXiv 2610.38331"
url: https://arxiv.org/abs/2610.38331
status: unread
id: 2026-11-01-soft-mtp
---
2026-11-01 07:16
Tags: #daily-knowledge #ai

---
# Soft-MTP a one-line change to multi-token-prediction training gives better speculative dra

Standard multi-token prediction (MTP) gradients contain a noisy residual that interferes with learning; the authors show the useful part is a KL self-distillation term toward the model's own next-token prediction and recover it exactly from existing cross-entropy gradients. The resulting Soft-MTP adds no parameters or measurable overhead, works with DeepSeek- and Meta-style MTP, and improves perplexity, zero-shot accuracy and speculative-decoding acceptance length at every scale tested. Tested on: models from 167M to 1.2B parameters trained by the authors.

## Details

**Caveats**
Only up to 1.2B parameters, far below production scale, where the authors argue the effect should grow but do not show it. Gains in acceptance length are small.

**For your work**
Little direct use unless a client pre-trains or continues pre-training its own models; worth knowing as background on why newer open models ship with stronger MTP drafts.

**Method**
- Decompose the MTP cross-entropy gradient into a KL self-distillation term plus a low signal-to-noise residual.
- A 'KL gradient-recovery trick': when two distributions share a linear output head, combine their cross-entropy gradients through straight-through routing to recover the KL gradient exactly, without vocabulary-sized logit matrices.
- Backpropagate only that KL signal, compatible with fused cross-entropy kernels.

**Problem**
MTP heads are now common in pre-training because they help quality and enable speculative decoding, but their training signal gets noisier with scale.

**Results**
- Lower next-token perplexity, faster speculative decoding and higher zero-shot accuracy than standard MTP at every scale from 167M to 1.2B.
- Averaged over five domains, acceptance length improves by 1.8-2.2% over standard MTP.
- Matches or beats direct KL minimisation on most metrics; stronger math and code after fine-tuning at 1.2B.

**Concepts:** [[Inference efficiency]] · [[Post-training and RL]]
**From:** [[2026-11-01]]

# My notes


---
# References
[arXiv 2610.38331](https://arxiv.org/abs/2610.38331)
