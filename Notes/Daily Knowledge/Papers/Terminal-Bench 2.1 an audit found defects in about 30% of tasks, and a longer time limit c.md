---
date: 2026-11-06
section: AI
importance: High
kind: paper
source: "arXiv 2611.08417"
url: https://arxiv.org/abs/2611.08417
status: unread
id: 2026-11-06-terminal-bench-21
---
2026-11-06 07:16
Tags: #daily-knowledge #ai

---
# Terminal-Bench 2.1 an audit found defects in about 30% of tasks, and a longer time limit c

Stanford researchers audited Terminal-Bench 2.0 with an agent-assisted workflow and repaired 28 tasks; re-running 19 agents raised accuracy by over 10 percentage points and moved some up to three ranks, though the ranking stayed highly correlated (Spearman 0.958). Extending the time limit closed a 20 pp harness gap on GPT 5.4 and shrank a 30 pp gap on GPT 5.4 mini to 5 pp, so time budgets are part of what a benchmark measures. Tested on: 19 agents from multiple providers on 89 tasks; extra-time condition on a subset.

## Details

**Caveats**
Precision and recall are measured against a release the workflow helped build, so they are not independent. The longer-time condition covers only some agents because of cost.

**For your work**
When you compare harnesses or models for a client, fix and report the time and token budgets, and pin dependencies. A harness gap at default settings may just mean one agent is slower. Use TB2.1 rather than 2.0.

**Method**
- Evidence agent gathers task files, prior agent traces and community reports; an auditor agent labels each task (instruction-verification mismatch, task drift, environment issue) and drafts a cited repair; a verifier reruns the oracle; maintainers approve
- Resource repairs give the oracle and verifier at least 1.5x slack on time, memory or CPU
- Re-evaluate 19 agents on TB2.0 vs TB2.1, then add a longer-time-limit condition

**Problem**
Agentic benchmarks go stale: models find valid solutions that verifiers reject, and packages, APIs and infrastructure drift after release. Terminal-Bench 2.0 was carefully reviewed, yet within months it had over 50 open defect reports.

**Results**
- Issues in 28 tasks, roughly a third: instruction-verification mismatch in 57%, task drift in 43%, environment issues in 29%
- Claude Code (Opus 4.6) and Codex (GPT-5.4) auditors agree at kappa 0.80; against the final release the workflow reaches 57.1% precision and 71.4% recall
- Claude Code + Claude Opus 4.6 lifts over 7 pp above the fit and climbs three places; Codex + GPT 5.4 sits below it
- More than 50% of failed trials are timeouts, up to about 68% for some harnesses

**Concepts:** [[Evals and benchmarks]] · [[Coding agents]]
**From:** [[2026-11-06]]

# My notes


---
# References
[arXiv 2611.08417](https://arxiv.org/abs/2611.08417)
