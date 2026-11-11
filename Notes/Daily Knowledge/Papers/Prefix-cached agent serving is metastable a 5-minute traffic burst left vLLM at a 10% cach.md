---
date: 2026-11-11
section: AI
importance: Med
kind: paper
source: "arXiv 2611.13412"
url: https://arxiv.org/abs/2611.13412
status: unread
id: 2026-11-11-prefix-cache-metastable
---
2026-11-11 07:16
Tags: #daily-knowledge #ai

---
# Prefix-cached agent serving is metastable a 5-minute traffic burst left vLLM at a 10% cach

Microsoft researchers ran paired servers with identical base load: in 9 of 12 pairs only the run that got a short burst stayed degraded for the rest of the 90-minute run, because slower service keeps more agent sessions alive, their KV no longer fits, and every turn becomes a full recompute. Throttling new admissions recovered 1 of 7 collapsed runs, while suspending admitted sessions against a KV-pool limit recovered all of them, and a KV budgeter prevented the failure in every run tested. Tested on: Qwen3-8B and Qwen3-32B on single AMD MI300X GPUs, vLLM and SGLang, synthetic sessions and SWE-bench agent trace shapes.

## Details

**Caveats**
Single-GPU engines, synthetic token contents, fixed output lengths and greedy decoding; the budgeter idea is classic working-set load control, which the authors say is not new; a concurrent paper reports the same failure on disaggregated SGLang.

**For your work**
If clients self-host models for agents, load tests should include a burst followed by normal load, and the gateway should cap resident sessions by KV demand and pause sessions, not only rate-limit new ones. Pairs well with last week's retry-storm finding.

**Method**
- Paired runs share every base session arrival and differ only in an injected 5-minute burst; endpoints are token-weighted hit ratio, turn throughput and sessions in the system.
- Controls: cache disabled, a cache-flush trigger, Qwen3-32B replaying mini-SWE-agent trace shapes, SGLang, vLLM CPU KV offload (128 GiB).
- Recovery arms: admission throttling, latency-driven AIMD, suspending admitted sessions at turn boundaries against a pool-derived limit, and a KV-demand budgeter; a first-order workload-balance model predicts when the regime can drain.

**Problem**
Agent sessions are closed loops whose context grows every turn; serving them cheaply depends on prefix caching (a hit costs about a thousand tokens of prefill, a miss recomputes 10-40K tokens). What happens when the hit ratio is lost under a transient spike?

**Results**
- Burst runs settle near 0.1 hit ratio, about 0.4 turns/s and a backlog past 100 sessions, while twins stay at 0.94-0.95 hit ratio with about 10 sessions; the load is about 70% of cache-warm capacity.
- Without prefix caching the same burst drains away; SGLang shows the regime but tolerates larger triggers.
- Suspending admitted sessions restored throughput and a 0.93-0.95 hit ratio in every collapsed run within 6 minutes; CPU offload only delayed collapse (from minute 20-25 to 40-60).

**Concepts:** [[Inference efficiency]] · [[Agents]] · [[Open-weight models]]
**From:** [[2026-11-11]]

# My notes


---
# References
[arXiv 2611.13412](https://arxiv.org/abs/2611.13412)
