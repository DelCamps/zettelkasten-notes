---
date: 2026-11-23
section: AI
importance: Med
kind: paper
source: "arXiv 2611.27860"
url: https://arxiv.org/abs/2611.27860
status: unread
id: 2026-11-23-splitbench-privilege-separation
---
2026-11-23 07:16
Tags: #daily-knowledge #ai

---
# SplitBench a trusted grader keeps the expected answers away from the agent, and 180 of 202

Coding agents can tamper with the tests that grade them. SplitBench runs the tests in an environment the agent's code may control, but a trusted Oracle outside it holds the expected answers and makes the pass or fail decision. Converted tasks matched the native graders on 98.7% of 1,374 comparisons. A full-knowledge Claude Opus 5.5 attacker got no pass through a flaw in SplitBench itself; most of its passes exploited weak upstream tests. Tested on: 180 tasks from 2 benchmarks, 2 agents from 2 vendors (Claude Sonnet 5.5 in Claude Code, GPT 6.1 Sol in Codex) run twice each, 360 attack attempts by one attacker model.

## Details

**Caveats**
Container and VM isolation is assumed to hold. Model safeguards stopped 53 of the 360 attack attempts. At least 34 tasks keep weak tests that SplitBench inherits.

**For your work**
For internal agent evals or client acceptance tests, never let the agent's code run in the same place as the expected answers or the scoring logic. Score outside the sandbox.

**Method**
- Split verification: an Evaluation environment that the candidate code can control runs the tests and collects evidence. A separate Oracle compares that evidence with hidden data and decides the verdict.
- The agent reaches the outside only through a relay to the model provider and an egress proxy limited to the domains each task allows. It gets no feedback from evaluation.
- Conversion pairs a converter agent with a reviewer agent and keeps each task's original tests and assertions. The median cost was about $10 per task at API prices.

**Problem**
Benchmark scores guide model choice, but agents can read answers, edit tests or game scorers. BenchJack reached near-perfect scores on nine of ten popular agent benchmarks without solving the tasks.

**Results**
- 180 of 202 tasks converted. Most of the rest need running services or set speed targets.
- 98.7% verdict agreement: 99.4% for Sonnet and 97.9% for GPT. Pass counts were similar, for example Sonnet passed 121 and 120 tasks natively and 118 and 125 under SplitBench.
- With full knowledge of the grading code, SplitBench rejected 126 of 168 completed attacks (75%), and 84% with limited knowledge. Of the 64 passes, 47 exploited weak upstream tests across 34 tasks, 2 came from conversion errors and 3 were faked implementations.

**Concepts:** [[Evals and benchmarks]] · [[Coding agents]] · [[Agent security]]
**From:** [[2026-11-23]]

# My notes


---
# References
[arXiv 2611.27860](https://arxiv.org/abs/2611.27860)
