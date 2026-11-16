---
date: 2026-11-06
section: AI
importance: High
kind: news
source: "METR"
url: https://metr.org/blog/2026-11-05-anthropic-ai-rd-acceleration-assessment/
status: unread
id: 2026-11-06-metr-anthropic-rd-acceleration
---
2026-11-06 07:16
Tags: #daily-knowledge #ai

---
# METR's inside look at Anthropic capability growth about 1.9x faster than before, perhaps 8

METR spent about 11 weeks with internal data at Anthropic and estimates that its capability index (AECI) is now rising at 1.9x [95% CI 1.5-2.8x] the March 2024-October 2025 pace, from +15 to +29 points a year. It attributes perhaps about 80% of the current acceleration to AI use, found no convincing bottlenecks for the next 12 months (low confidence), and notes Anthropic redacted much of the most informative evidence.

## Details

**Caveats**
Anthropic had redaction rights and redacted most of the evidence METR found most informative, and cancelled a planned compute-allocation check midway. Claude helped with much of the analysis. Gains may be limited to well-specified, automatically graded tasks, and benchmarks are near saturation.

**For your work**
Expect model releases (and the tooling around Claude) to keep arriving faster; plan client architectures so models can be swapped quickly, and treat 'roughly two years of progress in one year' as the working assumption for roadmap and evaluation refresh cycles.

**Method**
- Engagement August 12 to October 29, 2026, 2.5 full-time-equivalent staff over about 11 weeks, on Anthropic devices; no query access to unreleased models
- Data: internal benchmark scores and AECI (Anthropic's version of the Epoch Capabilities Index) for internal models, algorithmic-efficiency history, compute, headcount, PRs, agent inference spend, internal uplift surveys and about 15 staff interviews
- Acceleration = ratio of growth rates, from piecewise linear fits with a breakpoint fixed at October 7, 2025, with bootstrap 95% confidence intervals

**Problem**
If AI speeds up AI R&D, capabilities could arrive suddenly. METR asked whether Anthropic's internal capability growth has accelerated, how much of that is due to AI, and whether bottlenecks will slow it in the near term.

**Results**
- AECI acceleration 1.9x [95% CI: 1.5-2.8x]; robustness variants range 1.1x-2.9x; including all labs' public models gives 1.4x
- METR is confident training-compute growth did not drive it; share due to AI perhaps about 80%
- Self-reported uplift for the most capable internal model reached about 12x in October 2026 polls, which METR treats as loose evidence
- A permanent slope change fits better than a one-off jump at Mythos Preview (RMSE 1.9 vs 3.9 AECI points)

**Concepts:** [[AI safety]] · [[Evals and benchmarks]] · [[Frontier models]]
**From:** [[2026-11-06]]

# My notes


---
# References
[METR](https://metr.org/blog/2026-11-05-anthropic-ai-rd-acceleration-assessment/)
