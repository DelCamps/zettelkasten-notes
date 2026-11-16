---
date: 2026-11-11
section: AI
importance: Med
kind: paper
source: "arXiv 2611.13246"
url: https://arxiv.org/abs/2611.13246
status: unread
id: 2026-11-11-expertcrowd-swe
---
2026-11-11 07:16
Tags: #daily-knowledge #ai

---
# ExpertCrowd-SWE on 100 unpublished, expert-written coding tickets, Claude Opus 5.5 (67.3%)

Toptal engineers wrote 100 multi-file change requests across 87 open-source projects and 11 languages, graded with partial credit plus maintainer-style blockers and gates. Opus 5.5 and GPT-6 Astra lead with no significant gap, ahead of Claude Fable 5.1 (46.5%) and Gemini 3.8 Flash (40.0%); only 26.6% of Opus runs earn full credit, and GPT-6 Astra takes a median 33 steps against 160 for Opus. Tested on: 7 frontier models from six providers, 3,495 scored runs (5 per task), one platform harness (HUD) exposing each provider's native tools.

## Details

**Caveats**
Tasks were selected for difficulty against current frontier models; one harness only, not a test of Claude Code, Codex CLI or other products; Claude Fable 5.2 was not evaluated (runs collected 1-10 October 2026); the authors run a commercial expert network.

**For your work**
A good template for client eval suites: author tasks against the client's own repos, grade with weighted criteria plus hard gates, and report task-sampling intervals, not just reruns. If a single attempt must be right, consistency (Astra) can matter more than peak score (Opus).

**Method**
- 17 practising engineers authored tickets against pinned recent commits in codebases they know; changes are unpublished and 76 of 100 tasks are held out; screened against 93 public benchmark datasets.
- Each task has weighted, mostly executable criteria; blockers cap the score and gates (e.g. 'repo tests untouched') zero it; build fails unless the reference scores 1.0 and an inert change scores 0; nearly half ship alternative, lazy and adversarial control patches.
- Seven models, five runs each, 1,000-step limit, in the HUD harness with provider-native tool schemas; paired permutation tests and task-sampling intervals.

**Problem**
SWE-bench-style benchmarks are contaminated, their inherited tests misgrade alternative solutions, and frontier agents now sit within a point of each other on newer authored benchmarks, so leaderboards no longer separate models.

**Results**
- Scores: Opus 5.5 67.3%, GPT-6 Astra 63.7%, Fable 5.1 46.5%, Gemini 3.8 Flash 40.0%; Qwen 3.8 Max, DeepSeek V4.1 Flash and Grok 4.6 indistinguishable at 32.2-33.5%.
- Full-credit runs: 26.6% Opus, 23.4% Astra, at most 8.6% for others; on 80 tasks no model is fully right on all five runs. Pass/fail grading would squash four models into 1-4%.
- Astra is more consistent (full credit 5 of 5 on 15 tasks vs 9) while Opus is broader (47 vs 36 tasks with at least one full-credit run); Astra reaches 95% of Opus's score with about a fifth of the steps.
- Task-sampling intervals (3.3-5.5 points) are two to ten times wider than run-to-run intervals; gates zeroed 2.3% of runs, e.g. an Asynq task where Opus and Grok scored zero every run.

**Concepts:** [[Coding agents]] · [[Evals and benchmarks]] · [[Frontier models]]
**From:** [[2026-11-11]]

# My notes


---
# References
[arXiv 2611.13246](https://arxiv.org/abs/2611.13246)
