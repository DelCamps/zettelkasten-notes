---
date: 2026-11-16
section: AI
importance: Med
kind: paper
source: "arXiv 2611.17808"
url: https://arxiv.org/abs/2611.17808
status: unread
id: 2026-11-16-carryon-context-manager
---
2026-11-16 07:16
Tags: #daily-knowledge #ai

---
# CarryOn keeping a compact task state plus linked raw evidence lifts long-horizon agent suc

CarryOn pairs a compact execution state with source-linked snippets of original tool output, chosen by a small learned selector with no extra LLM calls; it reaches 75.7% average task success, 6.7 points above the best baseline (SWE-Pruner) and 13.3 above keeping full history, at the lowest cost per success. Evidence often comes back into context after being dropped (40.2% of trajectories). Tested on: 3 models from 3 families (Claude Sonnet 5, Qwen3.8-27B, Gemma-4-31B), AppWorld, OfficeBench and Tau2 Telecom.

## Details

**Caveats**
Single run per setting; a separate selector is trained per benchmark; text-only environments.

**For your work**
For long tool-using agents, try keeping a structured state block plus re-selectable raw tool outputs instead of LLM summaries; exact IDs and values survive and you save the summarization calls.

**Method**
- Separate a persistent progress state from fine-grained evidence units linked to the original observations
- A learned selector (reranker-based) and adaptive retention policy choose which evidence to show each step, within a fixed character budget
- Compare with Full History, FIFO-5, retrieval, LLMLingua-2, ACON, SWE-Pruner and AGORA

**Problem**
Summaries lose exact details later actions need, while full histories drown the agent in irrelevant tokens.

**Results**
- 75.7% macro task success vs SWE-Pruner by 6.7 points and Full History by 13.3 points
- Lowest mean normalized cost per success, 0.792
- Tau2 Telecom with Gemma: 77.5% vs 65.0% for SWE-Pruner

**Concepts:** [[Agent memory]] · [[Agents]] · [[Inference efficiency]]
**From:** [[2026-11-16]]

# My notes


---
# References
[arXiv 2611.17808](https://arxiv.org/abs/2611.17808)
