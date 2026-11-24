---
date: 2026-11-24
section: AI
importance: Med
kind: paper
source: "arXiv 2611.27622"
url: https://arxiv.org/abs/2611.27622
status: unread
id: 2026-11-24-benchmarks-last-exam
---
2026-11-24 07:16
Tags: #daily-knowledge #ai

---
# Benchmarks' Last Exam only 29.3% of tasks in six multi-step agent and rubric suites pass a

A synthesis of task-level quality reviews covering 749 tasks across eight 2026 frontier benchmarks and 767 public model evaluations. Closed-form suites revised after error reports reach 92.5% verified validity, but six multi-step suites (rubric and agentic) reach just 29.3%; most confirmed defects (71.7%) withhold credit from valid work, so leaderboard ceilings understate capability. Grading patches in a fresh container cut runtime bypasses from 14.7% to 2.7%. Tested on: 8 benchmarks (HLE-Diamond, AA-Omniscience, GDP.pdf, Harvey LAB, Terminal-Bench 4.0, Terminal-Bench-Science, DeepSWE, AutomationBench).

## Details

**Caveats**
- A synthesis of reviews from one initiative, not an independent re-audit
- Some large suites were sampled rather than fully reviewed
- Validity rates depend on the reviewers' framework and may not transfer to other benchmarks

**For your work**
When a client compares models on an agentic benchmark, treat the raw score as noisy and check failed tasks by hand. For your own evals, grade in a fresh container and validate each task with an oracle and a shortcut before trusting it.

**Method**
- Synthesise eight published review reports from the Benchmarks' Last Exam initiative, each task judged Accepted, Doubtful or Refused under one shared framework
- Map every flagged task to a failure class (C1 to C5): prompt-reference mismatches, incomplete state assertions, shared-channel leaks, grading-time collisions and others
- Relate defects to 767 public model evaluations to see whether they inflate or deflate scores

**Problem**
Leaderboards assume a pass means the task was done and a fail means it was not. For long rubric-graded and agentic tasks, the prompt, environment and grader often disagree on what success is, and nobody had measured how often, across grading designs, or in which direction defects move scores.

**Results**
- Closed-form suites after public error reporting: 92.5% verified validity; six multi-step suites: 29.3%, still yielding 161 verified complex tasks
- 71.7% of confirmed defects withhold credit from compliant solutions; 28.3% allow shortcut passes
- Grading committed patches in a fresh container cuts confirmed runtime bypasses from 14.7% to 2.7% (0% in read-only or static suites)

**Concepts:** [[Evals and benchmarks]] · [[Agents]]
**From:** [[2026-11-24]]

# My notes


---
# References
[arXiv 2611.27622](https://arxiv.org/abs/2611.27622)
