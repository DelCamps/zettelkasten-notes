---
date: 2026-11-04
section: AI
importance: Med
kind: paper
source: "arXiv 2611.04399"
url: https://arxiv.org/abs/2611.04399
status: unread
id: 2026-11-04-silent-instrument-errors
---
2026-11-04 07:16
Tags: #daily-knowledge #ai

---
# Agent leaderboard audit grader bugs in HAL and tau2-bench turned a 13-point scaffold gap i

On HAL's TAU-bench Airline results, a general-purpose agent trailed a benchmark-specific scaffold by 13 points only because about half its episodes never triggered the grader and were stored as failures; grading them under the benchmark's own rule makes it a tie. Other silent errors: a cost column that counts nested calls twice (one row lists $149.98 for a $74.99 run), grader actions logged as agent actions, and a re-grade bug that cut four scores by 59 to 82 points. Tested on: 2 public leaderboards (HAL, tau2-bench), audited from published artifacts only; HAL maintainers confirmed three errors within five weeks.

## Details

**Caveats**
Case studies on two leaderboards rather than a systematic error rate; single author; some corrections (e.g. tasks whose gold only reads the database) pass trivially under the benchmark's rule.

**For your work**
When citing leaderboards to clients, or running in-house agent evals, report the graded fraction, sum cost from root spans only, tag who produced each logged action, and pin evaluator versions with a re-grade diff.

**Method**
- Re-derived scores and costs from the published trajectories and traces of HAL and tau2-bench, without rerunning any agent
- Graded the ungraded episodes offline under TAU-bench's own reward rule
- Compared span-level cost aggregation with root-span costs; re-graded saved trajectories under a newer evaluator

**Problem**
Teams pick models and scaffolds from public agent leaderboards, but the code that grades, logs, prices and replays runs is rarely checked, and its errors produce plausible numbers rather than crashes.

**Results**
- Generalist vs Tool-Calling: published 13-point gap over nine models becomes a tie once ungraded episodes are scored
- Cost column double-counts nested model calls unevenly across rows, which reshapes the cost-accuracy frontier
- A mode check that misreads four files collapses their scores by 59 to 82 points with no error printed
- HAL maintainers added disclosures; archives remain unchanged

**Concepts:** [[Evals and benchmarks]] · [[Agents]]
**From:** [[2026-11-04]]

# My notes


---
# References
[arXiv 2611.04399](https://arxiv.org/abs/2611.04399)
