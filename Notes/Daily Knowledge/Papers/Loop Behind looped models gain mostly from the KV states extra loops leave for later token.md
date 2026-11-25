---
date: 2026-11-25
section: AI
importance: Low
kind: paper
source: "Hugging Face blog"
url: https://huggingface.co/blog/XijieGong/loop-behind-rethinking-where-extra-loops-pay-off-i
status: unread
id: 2026-11-25-loop-behind-decoding
---
2026-11-25 07:16
Tags: #daily-knowledge #ai

---
# Loop Behind looped models gain mostly from the KV states extra loops leave for later token

Tsinghua researchers split a looped language model's extra loops into two effects and found that on Dory-4B reading deeper KV states recovers 6.8 of the 7.2-point gain from a second loop, while extra compute for the current token recovers only 0.8. Their Loop-Behind decoding reads each token out after one loop and runs the rest in parallel with later tokens, reaching 47.2% vs 47.7% for full two-loop decoding at 1.36-1.53x the speed in memory-bound settings. Tested on: 3 looped models (Dory-4B, Huginn-0125, Ouro-1.4B), 12 benchmarks on Dory; the asymmetry fails on Ouro.

## Details

**Caveats**
Main results on one 4B model; the effect does not hold on Ouro-1.4B, where Loop-Behind breaks. Speedup shrinks in compute-bound regimes because FLOPs are unchanged. One sample per problem at temperature 1.0.

**For your work**
Mostly relevant if looped open-weight models (such as Inkling 2 Mini) reach client deployments: serving tricks may cut their latency without retraining.

**Method**
- Decoupled variants: one loop reading deeper KV (L1[KV2]) versus two loops reading shallow KV (L2[KV1])
- Loop-Behind decoding: emit each token after its first loop and finish its remaining loops in the same forward pass as later tokens; no retraining, one-loop KV cache, implemented in vLLM

**Problem**
Looped LMs reuse layers several times per token. Is the gain from more compute before each token is emitted, or from the KV cache those loops write for later tokens?

**Results**
- Dory-4B average accuracy: L1 40.5%, L2 47.7%, L1[KV2] 47.3%, L2[KV1] 41.3%
- Loop-Behind 47.2% at 2 loops and 48.3% at 4 loops, keeping 89% of native 4-loop gain
- Speed on one H100: 1.36-1.53x faster than L2 in 81 of 92 bandwidth-bound settings, up to 2.56x vs L4
- Huginn-0125: L8[KV16] 56.7% vs L16 57.4%; Loop-Behind matches 57.4% at 1.75x

**Concepts:** [[Inference efficiency]] · [[Open-weight models]]
**From:** [[2026-11-25]]

# My notes


---
# References
[Hugging Face blog](https://huggingface.co/blog/XijieGong/loop-behind-rethinking-where-extra-loops-pay-off-i)
