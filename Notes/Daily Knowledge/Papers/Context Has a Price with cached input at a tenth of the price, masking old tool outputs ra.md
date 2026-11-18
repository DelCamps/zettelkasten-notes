---
date: 2026-11-18
section: AI
importance: High
kind: paper
source: "arXiv 2611.22238"
url: https://arxiv.org/abs/2611.22238
status: unread
id: 2026-11-18-context-has-a-price
---
2026-11-18 07:16
Tags: #daily-knowledge #ai

---
# Context Has a Price with cached input at a tenth of the price, masking old tool outputs ra

A Huawei-led study priced uncached input, cached input and output separately across more than 20,000 coding-agent runs on SWE-bench Verified, SWE-bench and Loc-Bench. Adding retrieved code cut read and search commands by 18-34% but raised cost by 33-42% with a tenth-price cache and no measurable gain in resolution; removing old observations saved 19-36% without a cache discount but cost 38-116% more with one, because each edit breaks the cached prefix and agents then take more steps. Tested on: seven open models from three families (five Qwen), two scaffolds (a minimal bash agent and mini-SWE-agent), three benchmarks, thinking off.

## Details

**Caveats**
Only locally served open models (five of seven Qwen), thinking off, some 50-step caps. Prices are applied to token logs, not invoices, and provider cache expiry and write charges are not modelled.

**For your work**
Before adding compaction or tool-output masking to a Claude or Azure OpenAI agent, measure cost with the real cached-input price and the step count per run.

**Method**
- Cost = uncached + c x cached + p x output tokens, with c (cached price ratio) varied from 0.1 to 1 and p = 4.
- Preregistered paired tests: an evidence package of retrieved code versus none, and rolling or break-even masking of old observations versus none.
- Counts only cache hits a run could produce itself, since conditions run side by side on one server share prefixes.

**Problem**
Context-management tricks (adding retrieved code, masking or summarising old tool outputs) are usually judged by token counts. But with prefix caching, a token added early is paid every turn and an edit invalidates the cache from that point, so fewer tokens need not mean a smaller bill.

**Results**
- Evidence package: read and search down 18-34%, cost up 33-42% at c = 0.1, no measurable resolution gain.
- Rolling masking: 19-36% cheaper without a cache discount, 38-116% dearer at c = 0.1; with GLM-4.7-Flash, +38% at c = 0.1 and -36% at c = 1 (crossover at 0.21).
- Shared server caches turned a measured +8% premium into +36% once removed.
- Masking makes Qwen3.6-27B re-fetch masked content 2.0 times per run.

**Concepts:** [[Coding agents]] · [[Inference efficiency]] · [[Evals and benchmarks]]
**From:** [[2026-11-18]]

# My notes


---
# References
[arXiv 2611.22238](https://arxiv.org/abs/2611.22238)
