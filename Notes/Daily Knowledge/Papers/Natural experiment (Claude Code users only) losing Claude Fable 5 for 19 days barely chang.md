---
date: 2026-11-21
section: AI
importance: Low
kind: paper
source: "arXiv 2611.23216"
url: https://arxiv.org/abs/2611.23216
status: unread
id: 2026-11-21-fable5-suspension-merge-rate
---
2026-11-21 07:16
Tags: #daily-knowledge #ai

---
# Natural experiment (Claude Code users only) losing Claude Fable 5 for 19 days barely chang

A Harvard study used the 19-day US suspension of Claude Fable 5 as a natural experiment, comparing 297 Fable 5 users with 8,908 developers who stayed on Opus 4.8. Having Fable 5, 11 points higher on SWE-Bench Pro, changed the 7-day merge rate by +1.4 points [-1.4; +4.3]. Across five other Claude upgrades it changed by -0.9 points, but 95% of sampled PRs were merged by their own authors, so merges were already near the ceiling. Tested on: Claude models only (Fable 5 vs Opus 4.8, plus five Opus and Sonnet upgrades), public GitHub PRs from Claude Code, 1,208 developers in the upgrade analysis.

## Details

**Caveats**
There is one vendor only, and merge rate is a weak proxy: 90% of sampled PRs had no approval from anyone else, so quality differences may not show. The study is observational for the upgrade analysis.

**For your work**
This is useful evidence when clients ask whether to pay for the top model. Measure outcomes on your own tasks rather than relying on vendor benchmark gaps, especially for routine tickets.

**Method**
- Identify each PR's model from the Claude Code co-author line, checked against the commits in 96% to 99% of 200 sampled PRs.
- Difference-in-differences with developer and calendar-day fixed effects across before, available, suspended and restored phases.
- A second analysis of the same developers in the week before and after five model upgrades (15,442 PRs), pooled by inverse-variance weighting.

**Problem**
Vendors sell new coding models on benchmark gains, but no study had tested whether a higher-scoring model gets more real work done for the same people on the same projects.

**Results**
- The suspension contrast was +1.4 points [-1.4; +4.3], and the placebo was -2.6 points.
- After upgrades the merge rate changed by -0.9 points [-1.9; +0.2]; all five estimates were negative, despite SWE-Bench Pro gains of 5 to 18 points.
- Weekly merged PRs changed by +2.4% [-4.9%; +10.2%] and failed checks by +0.3 points, neither significant.

**Concepts:** [[Coding agents]] · [[Evals and benchmarks]] · [[Claude]]
**From:** [[2026-11-21]]

# My notes


---
# References
[arXiv 2611.23216](https://arxiv.org/abs/2611.23216)
