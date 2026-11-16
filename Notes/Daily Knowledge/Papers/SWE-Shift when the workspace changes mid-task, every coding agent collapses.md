---
date: 2026-10-26
section: AI
importance: High
kind: paper
source: "arXiv 2610.32196"
url: https://arxiv.org/abs/2610.32196
status: unread
id: 2026-10-26-swe-shift
---
2026-10-26 07:16
Tags: #daily-knowledge #ai

---
# SWE-Shift when the workspace changes mid-task, every coding agent collapses

From the same saved history, agents continue either untouched or after a realistic mid-task change (code edited by a colleague, dependency bump, new requirement, tool or auth change). All 17 systems drop: GPT-6 Astra goes from 67.35% to 24.79%, Claude Fable 5.1 from 62.01% to 18.33%, and tool/session changes and stale evidence give zero paired success for every system. Tested on: 17 coding-agent systems, closed (Codex and Claude Code apps) and open-weight, 120 scenarios at 9 intervention points.

## Details

**Caveats**
One update per run, designed scenarios (some share task roots), point estimates with uncontrolled model randomness; diagnostic controls cover only five systems.

**For your work**
When agents run long tasks in shared repos or against live APIs, tell them explicitly when something changed (new commits, rotated credentials, schema changes) and make them re-verify evidence before finishing; never assume a long-running agent noticed.

**Method**
- Matched continuations: from the same saved history and workspace, a Clean run continues untouched and a Shifted run receives one task-relevant update.
- 120 scenarios across 12 change families (code, dependencies, runtime state, requirements, tools and sessions, stale evidence), each injected at nine positions.
- Success requires finishing the task, preserving still-valid work and passing state and evidence checks; same tools and a 1,000,000-token budget per continuation.
- Provider systems run in their native apps (Codex for GPT models, Claude Code for Claude) at xhigh reasoning; open-weight systems served locally.

**Problem**
Coding benchmarks assume the repo, dependencies and requirements stay frozen while the agent works. In real teams they change mid-task, and a failure after a change could mean the agent never could solve it, or that the change derailed a run that was going fine.

**Results**
- Success drops in all 17 Clean-vs-Shifted comparisons: Clean 10.71-67.35% vs Shifted 1.16-24.79%.
- GPT-6 Astra 67.35% to 24.79% (20.34% paired); Claude Fable 5.1 62.01% to 18.33%; Claude Opus 5 53.76% to 16.09%.
- Tool/session changes and stale evidence yield zero paired success across all systems.
- Higher clean success does not mean better retention: DeepSeek V4-Pro retains more than the stronger Kimi-K3.

**Concepts:** [[Coding agents]] · [[Evals and benchmarks]]
**From:** [[2026-10-26]]

# My notes


---
# References
[arXiv 2610.32196](https://arxiv.org/abs/2610.32196)
