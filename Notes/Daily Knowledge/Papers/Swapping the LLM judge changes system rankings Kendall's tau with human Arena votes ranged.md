---
date: 2026-11-04
section: AI
importance: Med
kind: paper
source: "arXiv 2611.04090"
url: https://arxiv.org/abs/2611.04090
status: unread
id: 2026-11-04-swapping-the-judge
---
2026-11-04 07:16
Tags: #daily-knowledge #ai

---
# Swapping the LLM judge changes system rankings Kendall's tau with human Arena votes ranged

In a preregistered study, five judges re-judged 4,000 Chatbot Arena battles in both response orders; agreement with the human vote was low (median Cohen's kappa 0.22) and rankings moved with the judge, so the 'rankings stay stable' hypothesis failed. Checking a conclusion with a second-provider judge helped only by filtering out one poorly aligned judge, and bigger judges were not better aligned with voters. Tested on: 5 judges from 3 providers (Anthropic, OpenAI, Google), 9 systems, 33 system pairs, up to 100 verdicts per pair.

## Details

**Caveats**
One crowd vote per battle from 2025 is a noisy reference that reflects preference, not correctness; judged systems are older than the judges; one judge was dropped after partial results (disclosed deviation); all judges proprietary.

**For your work**
Before trusting an LLM-judge comparison in a client eval, calibrate each judge against a small human-labelled set; do not count cross-provider agreement as validation, and watch for family preference when a Claude or GPT judge scores its own family.

**Method**
- Judges: Claude Opus 5.5, Claude Sonnet 5.5, Claude Haiku 4.5, GPT-6 Luna, Gemini 3.1 Flash-Lite; the three low-cost ones form the cross-provider set
- 4,000 Chatbot Arena battles with human votes, each judged in both orders; Bradley-Terry rankings compared with the human ranking
- Preregistered hypotheses on ranking stability, replication precision and verdicts needed to converge

**Problem**
Without human labels, practitioners often validate an LLM-judge comparison by repeating it with a judge from another provider. How far can that cross-provider check be trusted?

**Results**
- Median kappa 0.22; GPT-6 Luna kappa 0.052 and tau 0.167, Gemini 3.1 Flash-Lite kappa 0.302
- Two-judge replication: +0.10 precision over single judges, but pairs involving Luna left a conclusion for only 35% of comparisons
- Poorly aligned judges failed to converge on 26-70% of system pairs
- Opus and Sonnet judges rank Claude Opus 4 fourth of nine; human votes rank it seventh

**Concepts:** [[Evals and benchmarks]]
**From:** [[2026-11-04]]

# My notes


---
# References
[arXiv 2611.04090](https://arxiv.org/abs/2611.04090)
