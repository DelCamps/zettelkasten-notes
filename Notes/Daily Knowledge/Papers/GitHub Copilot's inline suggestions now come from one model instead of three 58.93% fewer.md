---
date: 2026-11-26
section: AI
importance: Med
kind: paper
source: "arXiv 2611.33314"
url: https://arxiv.org/abs/2611.33314
status: unread
id: 2026-11-26-copilot-unified-inline-edits
---
2026-11-26 07:16
Tags: #daily-knowledge #ai

---
# GitHub Copilot's inline suggestions now come from one model instead of three 58.93% fewer

Microsoft's CodeAI and VS Code teams describe merging Copilot's separate completion, next-edit and long-distance-edit models into one model. It outputs anchored diff patches and can predict several edits per response. The client caches those later edits, so they need no further model calls. The model was trained with SFT and then RL using a binary LLM-graded reward. Tested on: randomised online A/B experiments with VS Code stable users in GitHub Copilot, plus offline benchmarks; a single in-house model.

## Details

**Problem**
The old system called three models in a fixed order. It could not express one intent spanning distant locations, sometimes needed several sequential calls per suggestion, and favoured completion even when a correction was better.

**Method**
- One output space: a sequence of anchored diff patches (location, deleted lines, added lines), allowing multiple edits per response.
- Multi-edit training data synthesised from single-edit data by model pseudolabelling and edit-history playback.
- RL with a binary LLM-graded reward, a shared patch-validity taxonomy, and 'grader boosting' for targeted failure modes. Phase 2 adds code completion and client changes.

**Results**
- Phase 1 (2-in-1) vs the three-model system: time to display -6.77%, output tokens -58.93%, with no significant regression in accepted or retained characters.
- Phase 2 (3-in-1 with client changes): dismissed suggestions per user -10.06%, not significant after Bonferroni correction.
- In Phase 2, output tokens rise 20.98%, and accepted and retained characters have negative (non-significant) point estimates.

**Caveats**
Industry report on one proprietary model. The phase comparisons use different controls and cannot be multiplied into a total effect. The base model is not named.

**For your work**
Useful as a real-world playbook: offline evals did not fully predict online results, so they tuned model and client together and gated on A/B guardrail metrics. That is relevant when clients ask how Copilot suggestions are evaluated.

**Concepts:** [[GitHub Copilot]] · [[Post-training and RL]] · [[Coding agents]]
**From:** [[2026-11-26]]

# My notes


---
# References
[arXiv 2611.33314](https://arxiv.org/abs/2611.33314)
