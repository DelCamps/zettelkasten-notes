---
date: 2026-11-03
section: AI
importance: High
kind: paper
source: "arXiv 2611.00442"
url: https://arxiv.org/abs/2611.00442
status: unread
id: 2026-11-03-table-size-fidelity
---
2026-11-03 07:16
Tags: #daily-knowledge #ai

---
# Don't make the model re-emit tool tables a production agent scores 92.3% vs 45.7% correct

In a deployed award-travel agent, feeding full tool record sets into the planner's context and answering follow-ups in-head (SYNTHESIS) got 45.7% of turns fully correct, versus 92.3% for keeping records in session state, filtering them with a deterministic tool and sending rows over a typed side channel (BYPASS). SYNTHESIS collapses as tables grow, to 8% or less beyond about 74 rows, and a bigger model only raises the threshold. Tested on: 4 models from 3 families (Gemini 2.5 Flash and Pro, GPT-4o-mini, Claude Haiku 4.5), 24 dialogues with 339 scored turns per condition, one production agent.

## Details

**Caveats**
One domain and one agent stack; sampling parity is imperfect for Claude (top_p cleared); no random seeds were set; one stated hypothesis (H2) was not measured.

**For your work**
For any agent that lists invoices, transactions or records, keep rows in state, let a deterministic filter answer follow-ups and send the table to the UI directly rather than through the model. Test fidelity at realistic table sizes, not 10-row demos.

**Method**
- A/B on the same production multi-agent flight system (a Google ADK fork) over frozen vendor payloads, with matched prompts and sampling; only the delivery path differs.
- SYNTHESIS: full row lists in the planner's context, follow-ups answered from memory. BYPASS: records kept in session state, follow-ups turned into arguments for a deterministic filter, rows sent on a typed side channel.
- Table size varied by capture date and by a content-controlled ladder of K-row prefixes of one 198-row payload; strict per-turn field fidelity scored against computed ground truth.

**Problem**
Most agent frameworks return a tool's structured result into the model's context for the model to re-emit every turn. Each re-emission can corrupt data the tool computed correctly, invisibly to schema validators.

**Results**
- Paired gap +46.6pp [+35.7, +57.1] on Gemini 2.5 Flash; +49.6pp on GPT-4o-mini and +55.8pp on Claude Haiku 4.5.
- Collapse threshold follows capability: under 10 rows for GPT-4o-mini, 10-25 for Haiku, 50-100 for Flash; Gemini Pro falls to 50% at 198 rows. BYPASS stays flat (140/144 ladder runs).
- Moving to Gemini 2.5 Pro only halves the gap (92.6% vs 72.0%) at 5 times Flash's per-turn cost; beyond 100 rows a correct SYNTHESIS answer costs $2.53 against BYPASS's flat $0.012.

**Concepts:** [[Agents]] · [[Structured outputs]] · [[Hallucination]]
**From:** [[2026-11-03]]

# My notes


---
# References
[arXiv 2611.00442](https://arxiv.org/abs/2611.00442)
