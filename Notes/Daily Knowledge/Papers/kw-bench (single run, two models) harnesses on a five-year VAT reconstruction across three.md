---
date: 2026-10-28
section: AI
importance: Low
kind: paper
source: "arXiv 2610.36405"
url: https://arxiv.org/abs/2610.36405
status: unread
id: 2026-10-28-kw-bench
---
2026-10-28 07:16
Tags: #daily-knowledge #ai

---
# kw-bench (single run, two models) harnesses on a five-year VAT reconstruction across three

A new benchmark asks a coding-agent harness to do an audit-style investigation: rebuild five years of VAT from raw extracts of three generations of SAP and defend every number to the cent. On Claude Opus 5.5, micro-cc and Claude Code scored 0.9986 and 1.000 in 22 and 25 minutes for about $5.80-5.89; on DeepSeek v4.1 Flash, Claude Code and Codex scored 0.00 while OpenCode and micro-cc scored 0.542 and 0.528. Tested on: 4 harnesses, 2 models, one run each, synthetic data.

## Details

**Caveats**
One run per harness and only two models, so harness rankings are not established. Lab harnesses needed configuration changes to run off their home model. The author built micro-cc. Data is synthetic and the tax rules are simplified.

**For your work**
Directly relevant to PwC: a concrete, deterministic template for evaluating agents on audit and tax investigation work, and a data point that a frontier model in Claude Code can do a weeks-long reconciliation in minutes. Treat the harness comparison as anecdotal.

**Method**
- First task family: five-year VAT reconstruction across legacy SAP ECC, a partial S/4HANA migration and a consultant redesign, delivered as raw extracts with no documentation.
- The harness must reverse-engineer the systems, parse, join and reconcile them, avoid traps that invent exposure, and deliver the package on company templates plus a reusable tool.
- Deterministic grading with no LLM judge; runs on Harbor, headless, for two hours.

**Problem**
Most knowledge-work benchmarks are generative (build a memo, a model or a spreadsheet, judged by an LLM). The expensive part of audit, tax and due diligence is investigative: recovering an answer hidden in messy, inconsistent evidence across systems.

**Results**
- On DeepSeek v4.1 Flash: OpenCode 0.542, micro-cc 0.528, Claude Code and Codex 0.00 each.
- On Claude Opus 5.5: micro-cc 0.9986 and Claude Code 1.000, in 22 and 25 minutes, for $5.80 and $5.89.
- What sank the weaker runs was keeping many weak signals alive over a long session, not any single step.

**Concepts:** [[Coding agents]] · [[Evals and benchmarks]] · [[Claude]]
**From:** [[2026-10-28]]

# My notes


---
# References
[arXiv 2610.36405](https://arxiv.org/abs/2610.36405)
