---
date: 2026-10-29
section: AI
importance: Low
kind: paper
source: "arXiv 2610.36114"
url: https://arxiv.org/abs/2610.36114
status: unread
id: 2026-10-29-context-pipeline-attrition
---
2026-10-29 07:16
Tags: #daily-knowledge #ai

---
# Harness truncation (one agent) a third of tool results cut to broken JSON while the window

In a kernel-trace root-cause agent, a fixed-length cut on tool output truncated 3,827 of 11,189 results, and every one became broken JSON, even though the largest prompt used only 5.75% of the window. Because JSON keys come in a fixed order, the cut wipes out whole later fields. In a controlled rerun, accuracy held only when the agent could reach the answer another way, and the cut cost 43% more tool calls. Tested on: one harness, one model, one domain (145 controlled runs plus 720 field runs).

## Details

**Caveats**
One agent, one domain, five recordings per fault class. The authors say outright that whether the cut causes the drop in accuracy is not settled.

**For your work**
Audit how your harness truncates tool output: cut at record or row boundaries and say that you cut, rather than slicing JSON text. Log what the model actually received, not only what the tool produced.

**Method**
- Models the agent's context as a five-stage pipeline (deliver, act, retain, transfer, persist) and counts losses at each stage
- Replayed 864 real tool results under a prefix cut vs a row-aware cut
- Pre-registered experiment putting each defect back one at a time; survey of 7 agent frameworks' truncation code

**Problem**
Agent evals report window size and accuracy but not how much tool output the harness throws away before the model sees it.

**Results**
- One field reached the model in 4.7% of 742 calls; a field next to it in the same results arrived in 99.3%
- Under the cut: tool calls 53 to 68 to 76, computations 18 to 36, and the share of computations that led to a finding fell from 0.61 to 0.31, while accuracy stayed 14-15/15
- Production replay: the shipped cut delivered 0 of 128 records of the fault's evidence
- langchain-core keeps only the first 500 characters of tool output; smolagents deletes the middle of anything over 20k characters

**Concepts:** [[Agents]] · [[Evals and benchmarks]]
**From:** [[2026-10-29]]

# My notes


---
# References
[arXiv 2610.36114](https://arxiv.org/abs/2610.36114)
