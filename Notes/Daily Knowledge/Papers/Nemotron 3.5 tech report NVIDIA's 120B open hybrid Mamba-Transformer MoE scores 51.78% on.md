---
date: 2026-11-01
section: AI
importance: Med
kind: paper
source: "arXiv 2610.38095"
url: https://arxiv.org/abs/2610.38095
status: unread
id: 2026-11-01-nemotron-3-5-super
---
2026-11-01 07:16
Tags: #daily-knowledge #ai

---
# Nemotron 3.5 tech report NVIDIA's 120B open hybrid Mamba-Transformer MoE scores 51.78% on

NVIDIA details Nemotron 3.5 Super (120B parameters, 12B active, multimodal) and Lightning (30B, 3B active, text), open hybrid Mamba-Transformer mixture-of-experts models for agentic work. Super reaches 51.78% on SWE-bench Pro, beating Nemotron 3 Ultra with about 4.6x fewer active parameters; parallel agents with self-verification lift Terminal-Bench 2.1 from 62.7% to 71.9%, and NVFP4 quantization keeps 99.62% median accuracy versus BF16. Tested on: NVIDIA's own benchmark suite for its two models (a technical report, not an independent comparison).

## Details

**Caveats**
All numbers come from NVIDIA's own runs and harnesses; independent leaderboard results will matter more. The throughput figures are for GB200 hardware. Check the licence and the actual weights release before proposing it to a client.

**For your work**
A candidate self-hosted coding or agent model for clients that cannot send code to a frontier API, especially with NVFP4 on NVIDIA hardware. The test-time-scaling recipe (parallel agents plus self-verification) is also worth copying for any agent where you can afford several tries.

**Method**
- Hybrid Mamba-Transformer MoE with large-scale distillation and native speculative decoding (multi-token prediction heads).
- Context extended to 1M tokens with 35B tokens of continued pretraining, then 65.4B tokens of agentic software-engineering mid-training at 256K context (issue-PR pairs, whole repos, commit diffs, CI logs, agent traces).
- Post-training with SFT, RLVR and RLHF, plus multi-teacher on-policy distillation for Super; Indic continued pretraining.

**Problem**
Open models for agentic coding need long context, strong tool use and cheap inference at the same time, which usually pulls in opposite directions.

**Results**
- Super: 51.78% on SWE-bench Pro, above Nemotron 3 Ultra with about 4.6x fewer active parameters.
- Parallel agent execution with self-verification: Terminal-Bench 2.1 62.7% to 71.9%, DeepSWE 24.6% to 34.5%.
- Speculative-decoding acceptance length up to 21.8% longer after MTP boosting; NVFP4 keeps 99.62% median accuracy; up to 4,856 output tokens/s/GPU on GB200 at 50+ tokens/s/user.
- Indic continued pretraining improves Indian-language benchmarks by up to 9.82 points.

**Concepts:** [[Open-weight models]] · [[Coding agents]] · [[Inference efficiency]]
**From:** [[2026-11-01]]

# My notes


---
# References
[arXiv 2610.38095](https://arxiv.org/abs/2610.38095)
