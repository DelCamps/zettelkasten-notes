---
date: 2026-10-27
section: AI
importance: Low
kind: paper
source: "arXiv 2610.35767"
url: https://arxiv.org/abs/2610.35767
status: unread
id: 2026-10-27-simple-rca-harnesses
---
2026-10-27 07:16
Tags: #daily-knowledge #ai

---
# Simple harnesses beat hand-crafted root-cause-analysis agents 65-77% vs 16-53%

On 90 validated microservice-failure cases, three harnesses that let the model investigate freely (one call over an evidence package, a SQL agent, Codex) reach PR@1 of 65-77% on mid-tier models versus 16-53% for five published RCA agents, whose scripted steps skip decisive evidence. More reasoning effort moves accuracy by a few points while taking up to seven times longer. Tested on: 6 models from 4 providers, 3 effort levels, 8 public datasets; Codex is the only coding harness tested.

## Details

**Caveats**
Only Codex as general harness; all models from 2026; RCA domain only.

**For your work**
Before building a multi-stage agent with fixed steps, try giving a capable model the data and a SQL or code tool; it may win outright.

**Method**
- RCAtlas: 90 validated cases from eight public datasets.
- Compares three free harnesses, five published LLM RCA agents and statistical/causal methods with one scorer.
- Models: GPT-6 Luna, DeepSeek V4.1 Flash, Claude Haiku 5.5, plus GPT-6.1 Sol, GPT-6 Astra and MiMo-V2.6-Pro.

**Problem**
RCA papers keep building agents with fixed procedures and role agents, each evaluated on its own data.

**Results**
- Simple harnesses 65-77% PR@1; published agents 16-53%; non-LLM methods 6-39%.
- Flash with Codex reaches 85.6% for about five cents per case; the best run (Sol at xhigh with Codex) 88.9% at about 26 cents.
- Every Pareto-optimal run in cost or time uses a simple harness.

**Concepts:** [[Agents]] · [[Coding agents]] · [[Evals and benchmarks]]
**From:** [[2026-10-27]]

# My notes


---
# References
[arXiv 2610.35767](https://arxiv.org/abs/2610.35767)
