---
date: 2026-11-28
section: AI
importance: Med
kind: paper
source: "arXiv 2611.33098"
url: https://arxiv.org/abs/2611.33098
status: unread
id: 2026-11-28-delegent-slm-subagents
---
2026-11-28 07:16
Tags: #daily-knowledge #ai

---
# Delegent handing Claude Code subagent work to a local 27B model cuts frontier cost by 67%

Waterloo researchers keep the frontier model in charge of a Claude Code loop but route subagent calls (code investigation, running tests, search) to a small local model, with no router or training. With a 27B FP8 model the frontier cost of long-horizon coding falls by 67% and of agentic search by 59%, and even a 2B laptop model cuts coding cost by 66%, at roughly twice the median latency on short tasks. Tested on: 2 frontier models (GPT-6.1-Sol; Claude Opus 5.5 on DeepSWE only) and 2 small models from 2 families, 50 SWE-bench Verified, 75 SWE-bench Pro and 50 DeepSWE tasks plus 694 search questions; one harness (Claude Code).

## Details

**Caveats**
Only one harness and coding/search tasks; Opus tested on DeepSWE only; tasks are about twice as slow at the median; savings depend on how much legwork the frontier model does.

**For your work**
- A cheap pattern to pilot for clients worried about Claude Code or agent token bills: keep the frontier model as lead, put a local or cheap model behind subagents.
- Measure the frontier-cost share per task before and after, as the paper does.

**Method**
- Starts from stock Claude Code and routes calls by role: main loop to the frontier model, subagents to a local SLM (Qwen3.8-27B-FP8 or MiniCPM5-2B) served with vLLM.
- For search adds a Delegate tool and an evidence check; SLM reports cite a source for every claim.
- A short instruction tells the frontier model to delegate tool-heavy work and keep the main coding to itself.

**Problem**
Frontier agents re-read their whole context at every step and do all the legwork themselves, including in subagents, so long-horizon tasks are billed at frontier prices.

**Results**
- GPT-6.1-Sol on DeepSWE: frontier cost falls to 34% with no loss in resolved tasks; with the SLM paid at API prices total cost is still only 38%.
- On 694 search questions frontier cost falls to 41% with the same number of correct answers.
- Claude Opus 5.5 plans first and delegates less: about 21 turns move to the SLM and its cost falls to 69%.

**Concepts:** [[Coding agents]] · [[Multi-agent systems]] · [[Claude]]
**From:** [[2026-11-28]]

# My notes


---
# References
[arXiv 2611.33098](https://arxiv.org/abs/2611.33098)
