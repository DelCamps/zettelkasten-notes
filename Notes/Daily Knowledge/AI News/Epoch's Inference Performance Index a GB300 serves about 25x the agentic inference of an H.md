---
date: 2026-11-10
section: AI
importance: Med
kind: news
source: "Epoch AI"
url: https://epoch.ai/publications/inference-performance-index
status: unread
id: 2026-11-10-epoch-inference-performance-index
---
2026-11-10 07:16
Tags: #daily-knowledge #ai

---
# Epoch's Inference Performance Index a GB300 serves about 25x the agentic inference of an H

Epoch AI's new index rates AI chips by how many agentic inference requests each chip can serve, not by raw FLOP/s. Scaled so a GB300 NVL72 scores 1, the H200 scores about 0.12, the B300 HGX and MI355X about 0.55, and Vera Rubin VR200 about 2.18. The scores are simulated and validated against InferenceX benchmarks.

## Details

**Caveats**
The scores show what the hardware could do, not what today's software achieves. The precision choices differ by chip, the three-token speculative decoding figure is assumed, and the index covers only agentic workloads and four models. A geometric mean would lower Hopper's scores further.

**For your work**
When sizing or costing self-hosted open-model deployments for clients, older Hopper GPUs may serve far fewer long-context agent sessions per chip than FLOP/s suggests.

**Method**
- Epoch simulates prefill and decode with Nvidia's AISimulate for an agentic workload: a 262,144-token cached context, 1,024 new prefill tokens and speculative decoding with three accepted tokens.
- For each chip and model it takes the highest number of concurrent requests per chip at output speeds of 50-400 tokens/s per request.
- Four open models get equal weight: Kimi K3, GLM-5.2, Qwen3-Coder-480B and a stand-in for MAI-Base-2.

**Problem**
Comparing chips by FLOP/s understates inference differences, because memory and links between chips often matter more for serving long-context agent workloads.

**Results**
- The GB300 NVL72 scores about 1.9x the B300 HGX, which Epoch puts down to its 72-GPU high-bandwidth domain.
- On Kimi K3 alone, the GB300 is about 46x the H200, against about 8x across all four models.
- Measured GB300 throughput matched predictions that assume 50% of the modeled maximum, within about 12% on average across five points.

**Concepts:** [[Inference efficiency]] · [[Open-weight models]] · [[Evals and benchmarks]]
**From:** [[2026-11-10]]

# My notes


---
# References
[Epoch AI](https://epoch.ai/publications/inference-performance-index)
