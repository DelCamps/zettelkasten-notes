---
date: 2026-11-08
section: AI
importance: Med
kind: paper
source: "arXiv 2611.04091"
url: https://arxiv.org/abs/2611.04091
status: unread
id: 2026-11-08-rubric-language-judges
---
2026-11-08 07:16
Tags: #daily-knowledge #ai

---
# LLM judges disagree more with non-English rubrics, especially on negated rules write rubri

Judges from different providers agreed less when the same rubric was written in Korean than in English (Cohen's kappa 0.687 vs 0.745, 95% CI of the difference -0.072 to -0.045), and items phrased as negations, conditions or exceptions had 5.6 times the odds of disagreement of affirmative ones. A single model flipped its verdict between two items with the same meaning in 11-15% of cases. Adding paired examples did not close the language gap. Tested on: 6 low-cost judges from 3 providers (Claude, GPT, Gemini) plus Claude Opus 5.5 as reference, 51,744 requests, analysis plan fixed before data collection, no human labels.

## Details

**Caveats**
Measures consistency, not accuracy (no human labels). One language pair, one domain, low-cost models only; all materials drafted by Claude (the language effect holds without the Claude judges).

**For your work**
For Spanish-language judge rubrics, state requirements affirmatively, run negated or conditional items through two judges before relying on them, and do not count on few-shot examples to fix wording sensitivity. Worth testing on Spanish.

**Method**
- 12 criteria for support dialogues, each written in four clause structures (affirmative, negated, conditional, exception), with pairs that mean the same thing, in Korean and English.
- Judges: Claude Sonnet 5.5 and Haiku 4.5, GPT-5.6 Luna and GPT-5.4 nano, Gemini 3.5 and 3.1 Flash-Lite, rating 60 translated ESConv dialogues and 144 built minimal-pair cases.
- Hypotheses and tests committed to a public repo before the first request; bootstrap CIs and Holm-corrected tests.

**Problem**
Teams outside English-speaking markets write evaluation rubrics in their own language and hand them to LLM judges, assuming the wording does not change the verdict.

**Results**
- Korean vs English cross-provider kappa: 0.687 vs 0.745. On negated items in the built cases: 0.51 vs 0.78.
- Structure flips on same-meaning items ranged from 3.8% (Claude Sonnet 5.5) to 24.3% (GPT-5.4 nano). Run-to-run self-consistency was 0.74-0.97.
- Asking for a rationale before the verdict raised agreement (Korean 0.55 to 0.64, English 0.71 to 0.78) but left the gap. Two models from the same provider agreed no more than models from different providers.
- In one case a judge described the evidence correctly, then applied a Korean negated rule with the wrong polarity, so reading the rationales would not catch it.

**Concepts:** [[Evals and benchmarks]]
**From:** [[2026-11-08]]

# My notes


---
# References
[arXiv 2611.04091](https://arxiv.org/abs/2611.04091)
