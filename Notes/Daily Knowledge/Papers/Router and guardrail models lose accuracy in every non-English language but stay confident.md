---
date: 2026-11-27
section: AI
importance: Med
kind: paper
source: "arXiv 2611.33307"
url: https://arxiv.org/abs/2611.33307
status: unread
id: 2026-11-27-multilingual-decision-models
---
2026-11-27 07:16
Tags: #daily-knowledge #ai

---
# Router and guardrail models lose accuracy in every non-English language but stay confident

Across 25 open-weight decision models (fine-tuned LMs that output a probability per option, used by routers and guardrails), every model loses accuracy in every language on parallel items, about 3.5 points on average and 1.8 in Spanish, while confidence falls only about half as much. Losses depend on the language and base model more than leaderboard rank, and LLM-translated test sets understate the gap. Tested on: 25 models built on Qwen and Gemma bases, 17 tasks, 14 languages, 81 fine-tuning runs.

## Details

**Caveats**
At most 100 items per benchmark-language cell; translation provenance is confounded with language and task in aggregate splits. Only open-weight decision models, not general chat models used as judges.

**For your work**
For Spanish-language routers or guardrails, recalibrate thresholds on Spanish data rather than reusing English ones, and test on human-translated or native Spanish sets.

**Method**
- 25 top-ranked open-weight decision models on 17 sub-tasks (knowledge, reasoning, intent and retrieval, tool use, content safety and more) in 14 languages, 75 benchmarks.
- Paired comparison with English on parallel items, with bootstrap confidence intervals.
- 81 controlled fine-tuning runs, plus a human vs LLM translation comparison.

**Problem**
Decision models are thresholded directly by routers and guardrails, yet they are ranked almost entirely in English. Do their accuracy and calibration hold in other languages?

**Results**
- Mean accuracy change vs English: -3.5 points (95% CI -4.0 to -3.0); confidence drops 1.8 points.
- Spanish, French and German lose 1.7-1.8 points; Swahili and Tamil 7.3 and 7.8.
- In Tamil the eight Qwen3.8 models lose 15.4 points on average against 4.0 for Gemma 4 models.
- Items are answered more accurately in all 23 benchmark-language pairs when an LLM, not a person, translated them.

**Concepts:** [[Evals and benchmarks]] · [[AI safety]] · [[Open-weight models]]
**From:** [[2026-11-27]]

# My notes


---
# References
[arXiv 2611.33307](https://arxiv.org/abs/2611.33307)
