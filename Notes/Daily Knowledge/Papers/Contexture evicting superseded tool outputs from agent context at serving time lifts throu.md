---
date: 2026-11-24
section: AI
importance: Low
kind: paper
source: "arXiv 2611.26980"
url: https://arxiv.org/abs/2611.26980
status: unread
id: 2026-11-24-contexture-kv-eviction
---
2026-11-24 07:16
Tags: #daily-knowledge #ai

---
# Contexture evicting superseded tool outputs from agent context at serving time lifts throu

Agents resend growing histories, and shared KV cache in GPU memory becomes the throughput bottleneck. Tracing tokens to the tool operations that produced them showed 64% of final-history tokens were superseded by later operations; Contexture evicts them at the serving layer, using global KV-cache pressure to decide when, without changing the harness or model. Tested on: two models (including Qwen3.8-27B), two harnesses (including Hermes), two benchmarks, vLLM on H100 and H200.

## Details

**Caveats**
- Only two models and two harnesses
- Observation masking wins on throughput in three configurations (all Qwen MoE)
- Matters mainly to teams self-hosting agent serving, not API users

**For your work**
If a client self-hosts open models for agents with vLLM, context eviction at the serving layer is a real capacity lever. For API-based agents, the takeaway is to drop superseded tool outputs in your own harness.

**Method**
- Trace each token to the tool operation that created it; later operations (re-reading or rewriting a file) supersede earlier outputs
- Keep the harness's full history but give the model a reduced execution context, without modifying harness logic or model execution
- Decide eviction using global KV pressure and prefix residency, so removal only happens when it is worth losing cached computation

**Problem**
Coding and terminal agents resend their whole execution history on every call, so shared KV-cache capacity in GPU memory, not compute, limits how many agent sessions a server can run. Harness-side compaction cannot see cache state, and KV managers cannot see which tool outputs are stale.

**Results**
- Throughput under SLO up 20-73% over the best of no eviction, harness compaction, AgentDiet and Continuum
- 7-63% over observation masking in five of eight configurations; masking loses 3-28 accuracy points
- GPU energy per completed session down 8-11% at high load; mean accuracy +1.4 points, worst case -3.7

**Concepts:** [[Inference efficiency]] · [[Agent memory]]
**From:** [[2026-11-24]]

# My notes


---
# References
[arXiv 2611.26980](https://arxiv.org/abs/2611.26980)
