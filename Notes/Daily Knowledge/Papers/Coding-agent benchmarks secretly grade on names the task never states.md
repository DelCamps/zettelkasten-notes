---
date: 2026-10-25
section: AI
importance: Med
kind: paper
source: "arXiv 2610.30635"
url: https://arxiv.org/abs/2610.30635
status: unread
id: 2026-10-25-spec-oracle-gaps
---
2026-10-25 07:16
Tags: #daily-knowledge #ai

---
# Coding-agent benchmarks secretly grade on names the task never states

A static audit of test dependencies finds that a quarter of SWE-Milestone's graded milestones need an unstated, non-inferable name or path; units with such a hidden dependency fail in 80.6% of runs vs 48.4% for comparable ones. Benchmarks whose specs are release notes or LLM summaries are hit hardest (a third or more of tasks); the audit and corrected filters are released.

## Details

**Caveats**
Single author; the audit is lexical and name-level, so it misses behavioural gaps (which explain most persistent SWE-bench Verified failures they reviewed) and its counts are a lower bound. The realisation analysis is observational.

**For your work**
When you build internal evals for client coding or extraction agents, check that every test dependency is stated in the task prompt; LLM-written task descriptions are the risky case. Run a cheap dependency audit before trusting a score drop.

**Method**
- Formalises the 'specification-oracle gap', including inconsistencies introduced by chains of dependent tasks.
- Builds a static, model-free audit for five languages that classifies every name-, path- and literal-level dependency of each scored test (held-out precision 89.2%, recall 92.9%).
- Applies it to SWE-Milestone (98 milestones, 35 published runs) and four other benchmarks, plus a counterfactual that hides one name in the reference solution.

**Problem**
Coding-agent benchmarks describe a task in prose but grade it with the upstream project's own tests. Those tests can require details the description never mentions (a constant's name, a module path, an exact error message), so a score partly measures whether the agent happens to reproduce upstream implementation details.

**Results**
- 25 of 98 milestones contain a test depending on an unstated, non-inferable name or path.
- Build units with such a dependency fail in 80.6% of runs vs 48.4% for comparable units.
- Withholding a single hidden name stops the unit's tests compiling in 126 of 128 cases.
- Leaderboard ranking survives removing affected tests, but per-repository scores shift; a third or more of tasks are affected where specs are release notes or LLM summaries, almost none where tasks are written for their tests.

**Concepts:** [[Evals and benchmarks]] · [[Coding agents]]
**From:** [[2026-10-25]]

# My notes


---
# References
[arXiv 2610.30635](https://arxiv.org/abs/2610.30635)
