---
date: 2026-10-26
section: AI
importance: Med
kind: paper
source: "arXiv 2610.32110"
url: https://arxiv.org/abs/2610.32110
status: unread
id: 2026-10-26-warped-formatters
---
2026-10-26 07:16
Tags: #daily-knowledge #ai

---
# Tool output that hides result caps makes RAG agents overclaim, and verifiers miss it

In a production RAG system, tools printed true but incomplete text (for example 'Found 20 documents' out of 4,772), and agents overclaimed on 62-100% of answers. Stating the missing details cut overclaiming to 0-20% for three of four failure types, and in one test verifiers went from accepting wrong answers 90 of 90 times to rejecting them 90 of 90 times.

## Details

**Caveats**
One production system, adversarially chosen cases, single-shot answers with no tool loop; rates are stress-test numbers, not frequencies.

**For your work**
Audit every tool formatter in your RAG and agent apps: print totals, caps, filters and ID namespaces ('first 20 of 4,772'). Their audit prompt is quick to run on a client codebase.

**Method**
- Studied four failure families from a production RAG research system at the Pilsudski Institute in New York.
- Fed agents and verifiers tool results from two formatter versions: one with the omissions, one with every missing detail stated.
- Released an audit prompt for Codex and Claude Code to find warped formatters in a codebase.

**Problem**
Agents and verifiers only see the text a tool prints. A tool can compute correctly while its formatter omits search limits, result caps or identifier namespaces, misleading everything downstream.

**Results**
- Warped wording: agents overclaimed on 62-100% of answers; clear wording cut scope, completeness and uncertainty failures to 8%, 0% and 20%; identifier provenance barely changed (94%).
- Verifiers flipped from accepting incorrect answers 90/90 times to rejecting them 90/90.
- The audit prompt rediscovered live defects plus twelve new ones, and found warped formatters in OpenClaw and Hermes (OpenClaw fix merged).

**Concepts:** [[RAG]] · [[Hallucination]] · [[Agents]]
**From:** [[2026-10-26]]

# My notes


---
# References
[arXiv 2610.32110](https://arxiv.org/abs/2610.32110)
