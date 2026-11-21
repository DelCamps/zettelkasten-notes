---
date: 2026-11-21
section: AI
importance: High
kind: paper
source: "arXiv 2611.25673"
url: https://arxiv.org/abs/2611.25673
status: unread
id: 2026-11-21-compact-bench-compaction-lossy
---
2026-11-21 07:16
Tags: #daily-knowledge #ai

---
# CompAct-Bench after context compaction, agents finish only 56.7% of tasks they had solved

Fudan and Tencent took 200 agent tasks (BrowseComp, SWE-bench and an internal workspace suite) that a fixed executor solved in all three screening runs, compacted the history partway through with 12 different models, and let the executor carry on. Average success fell to 56.7%; Claude Opus 5 led at 68.5% and Doubao Seed 2.1 Pro trailed at 46.0%, and summaries often turned open questions into settled 'facts'. Tested on: 12 compactor models from 9 providers, 200 tasks in 3 domains, one fixed executor per domain, 3 continuations each, 10% retention target.

## Details

**Caveats**
The 10% retention target is aggressive. There is one executor per domain, CompanyBench is internal with only 25 tasks, and each compaction was generated once.

**For your work**
Don't treat compaction as a generic summary. Choose the compaction model on purpose, keep task state outside the context (files, repository, a todo list), and tell the summary to mark unverified findings as tentative. For research and search agents, raise the retention budget.

**Method**
- Keep only tasks the executor solved in all three screening runs (79 BrowseComp, 96 SWE-bench, 25 CompanyBench), then cut each run at 25%, 50% or 75% of its progress.
- The model under test compacts the history to a calibrated 10% of its characters; the same executor (Claude Opus 4.8, or GPT-5.5 Codex for CompanyBench) resumes from the saved environment state with a matched action budget.
- Score Avg@3 continuations with bootstrap intervals, and hand-annotate failures into six error types.

**Problem**
Every long-running agent harness now compacts its history when the context fills up, but nobody had measured how much that compaction breaks the rest of the task, or which model writes the best compaction.

**Results**
- Overall success ranged from 46.0% to 68.5% across the 12 compactors (average 56.7%); the top and bottom confidence intervals do not overlap ([62.0,74.5] versus [40.0,52.5]).
- Search got worse the later the cut (52.9%, then 42.6%, then 34.6%), while Coding got better (64.0% to 86.1%), because code progress is saved in the repository.
- Restarting coding from the saved repository state with no history at all already scored 71.9% at the 75% cut, against 15.6% from the initial state.
- 'Premature commitment' showed up in 56.7% of early failures, and critical omissions came with an 18.2-point rise in repeated work.

**Concepts:** [[Agent memory]] · [[Evals and benchmarks]]
**From:** [[2026-11-21]]

# My notes


---
# References
[arXiv 2611.25673](https://arxiv.org/abs/2611.25673)
