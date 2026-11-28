---
date: 2026-11-27
section: AI
importance: Med
kind: paper
source: "Hugging Face blog (community)"
url: https://huggingface.co/blog/Avifenesh/layby-kv-cache-placement
status: unread
id: 2026-11-27-layby-kv-cache-placement
---
2026-11-27 07:16
Tags: #daily-knowledge #ai

---
# Layby predicting when an idle agent session returns halves time-to-first-token on a 320B M

A community study replaces recency-based KV-cache tiering with a 33.8M-parameter survival model that predicts when an idle agent session will come back, plus a cost rule that picks RAM, disk, both or drop. On GLM-5.3-Flash it cut mean time-to-first-token to 21.51 s from 42.23 s (LMCache ARC) and 91.57 s (no disk tier), and avoided the write-queue pile-up that made stock write-through worse than no disk at all. Tested on: 4 models on 5 hardware setups, vLLM and SGLang, plus a 33-cell trace simulator; Layby averaged over 2-3 repeats, several baselines run once; one author's own benchmarks.

## Details

**Caveats**
Single author, own hardware; baselines in several cells ran once; on fast quiet disks plain recency is near-optimal; mis-sized sliding-window KV on Inkling 2 Mini.

**For your work**
If you self-host agents with long idle gaps (vLLM or SGLang with a CPU/disk KV tier), the idea of predicting session return instead of LRU is worth testing before buying more GPU memory.

**Method**
- Layby-Dwell: a 33.8M-parameter survival model (32M Ettin text encoder plus telemetry tower) reads tool calls, recent messages, token counts and timing and estimates return probability over 15 horizons from 0.5 s to 30 min; runs on CPU in about 11-19 ms.
- A cost rule multiplies that probability by runtime-measured costs (link speed, queue wait, prefill speed, eviction rate) to choose one of four actions per finished turn, with no per-workload threshold.
- About 412 lines of Python inside vLLM 0.34 and SGLang 0.5.23; GPU eviction stays with the engine's LRU.

**Problem**
Agent sessions sit idle during tool calls, tests or human pauses, and their large KV caches are either dropped (forcing a full prefill) or written to disk by recency, which on slow or shared disks clogs the write queue with sessions that won't return soon.

**Results**
- GLM-5.3-Flash (320B MoE, 4x RTX PRO 6000): mean TTFT 21.51 s vs 42.23 s LMCache ARC, 91.57 s no disk tier, 167.91 s Continuum; 148.9 GB written vs 222.3 GB.
- Slow 141 MB/s disk, Qwen3-8B: 2.06 s mean and 13.57 s p99 with 0 GB written, vs 10.53 s mean and 274.3 s p99 for write-through.
- DGX Spark, Inkling 2 Mini: 8.17 s vs 23.10 s without a disk tier, but plain write-through won there (6.18 s).
- Simulator: worst cell about 4% worse than no disk tier.

**Concepts:** [[Inference efficiency]] · [[Agents]]
**From:** [[2026-11-27]]

# My notes


---
# References
[Hugging Face blog (community)](https://huggingface.co/blog/Avifenesh/layby-kv-cache-placement)
