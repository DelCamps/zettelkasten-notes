---
date: 2026-11-09
section: AI
importance: Low
kind: paper
source: "arXiv 2611.08684"
url: https://arxiv.org/abs/2611.08684
status: unread
id: 2026-11-09-retries-overloaded-vllm
---
2026-11-09 07:16
Tags: #daily-knowledge #ai

---
# Client retries can keep a vLLM server down after a load spike (one GPU, 3 small open model

After a short overload pulse, clients that time out and retry, as the OpenAI Python SDK does twice by default, kept vLLM from recovering even once traffic fell to 0.6x capacity. Passing cancellations through to the engine still delivered only 12-38% of later calls. Aborted executions used 79-85% of the prompt computation, and vLLM's prompt-token counter missed a third to half of it. Tested on: vLLM 0.30.0 on one H100, Qwen2.5-7B, Qwen3-14B and Llama-3.1-8B, synthetic single-turn traffic, 2-3 runs per condition.

## Details

**Caveats**
One engine version, one GPU type, synthetic prompts, one retry policy and few runs. Larger models, multiple replicas and other engines were not tested.

**For your work**
For self-hosted endpoints behind agents, add request coalescing or retry budgets at the gateway and align client deadlines with the server queue. Do not trust vLLM's prompt-token counter to show the real load.

**Method**
- Load generator sends 0.6x capacity with a 107-second pulse at 2.7x, then a 720-second hold; 120-second client deadline with up to 4 attempts
- A proxy passes on or withholds cancellation and can apply a retry budget or attach retries to a running request (coalescing)
- vLLM scheduler traces link each client attempt to the engine work it created

**Problem**
Agents spend most of their time waiting on LLM calls. When an endpoint is overloaded, timeouts trigger retries that repeat the same work.

**Results**
- With retries on and cancellation off, no calls during the hold were delivered; with retries off, all three models recovered
- Retries that vLLM ran usually started prefill less than 0.5 seconds before their own deadline
- A retry budget restored service but left many calls from the overload undelivered
- Coalescing delivered every call from the overload onward (some late)

**Concepts:** [[Inference efficiency]] · [[Agents]]
**From:** [[2026-11-09]]

# My notes


---
# References
[arXiv 2611.08684](https://arxiv.org/abs/2611.08684)
