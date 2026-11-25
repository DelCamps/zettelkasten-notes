---
date: 2026-11-25
section: AI
importance: Med
kind: paper
source: "arXiv 2611.31839"
url: https://arxiv.org/abs/2611.31839
status: unread
id: 2026-11-25-spec-test-coverage-gap
---
2026-11-25 07:16
Tags: #daily-knowledge #ai

---
# Overspecified tests two LLM judges flag 23% of SWE-bench Verified and 35% of SWE-bench Pro

Tests copied from the original fix often demand details the issue never states, so correct alternative fixes fail. Claude Opus 5.5 and GPT-6.1 Sol, judging spec against test patch, caught 89% of human-confirmed overspecified tasks with a 4% false-flag rate; the top 30 Verified submissions solve 31% of flagged tasks against 88% of the rest, and counting relaxed-test passes would raise resolve rates by up to 12 points. Tested on: 2 judges from 2 families, 206 validation tasks, all 500 Verified and 731 public Pro tasks, 2,186 failed patches from 30 submissions.

## Details

**Caveats**
Gains are an upper bound, not corrected scores. The Pro false-flag rate is unknown and the executable check covers Verified only.

**For your work**
Do not pick a coding agent for a client on single-digit SWE-bench gaps. In your own repo-based evals, check whether the tests encode the reference implementation rather than the requirement.

**Method**
- Spec-Test Coverage Gap scale (1-4); a task is flagged when both judges score 3 or higher
- Validation on 206 tasks labelled by earlier human audits and agent results
- Executable check: Opus 5.5 loosens only the overspecified requirements, which must still pass the reference fix and earlier resolving patches, then failed patches are regraded

**Problem**
SWE-bench-style scores are read as coding ability, but some tests reject correct fixes; finding those so far needed expert review.

**Results**
- 89% recall and 4% false flags on validation
- Flagged: 23% of Verified, 35% of Pro
- 61% of 2,186 failed patches on flagged tasks pass relaxed tests; each top-30 submission would gain 33 to 60 tasks and 28 of 30 would change rank by up to 10 places
- A forced control (relaxing tasks that were not flagged) adds only 2 to 6 tasks

**Concepts:** [[Evals and benchmarks]] · [[Coding agents]]
**From:** [[2026-11-25]]

# My notes


---
# References
[arXiv 2611.31839](https://arxiv.org/abs/2611.31839)
