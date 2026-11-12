---
date: 2026-11-12
section: AI
importance: Med
kind: paper
source: "arXiv 2611.13541"
url: https://arxiv.org/abs/2611.13541
status: unread
id: 2026-11-12-agent-benchmarks-stop-ranking
---
2026-11-12 07:16
Tags: #daily-knowledge #ai

---
# Agent leaderboards stopped ranking SWE-bench Verified's top ten are statistically tied, an

Re-scoring released runs of eight agent benchmarks, the authors show saturation is often in the pass/fail scoring rather than the tasks: on SWE-bench Verified the gaps between neighbouring top agents are smaller than the tests' own errors, and on Terminal-Bench tasks where models tie on pass/fail, one model's median speedup was 10.9x against 1.3x for the others. They propose a clipped log-ratio score with cost as a separate axis. Tested on: released runs from 8 benchmarks (SWE-bench Verified, Terminal-Bench 2.0, OSWorld-Verified, ALE-Bench, MLE-bench, SWE-fficiency, AlgoTune, METR) plus a re-run of 13 Terminal-Bench tasks with 4 models from 3 families, 3 trials each, one harness (Terminus-2).

## Details

**Caveats**
Only 20% of Terminal-Bench tasks measure a quantity, and none in the SWE-bench, OSWorld or tau2 samples coded, so the graded score does not apply everywhere. The re-run has three trials per cell and borderline aggregate separation; the sliding-window dating result rests mainly on ALE-Bench.

**For your work**
Do not choose a model for a client on a 1-2 point leaderboard gap. In client evals, log the measured quantity (latency, cost, accuracy margin) and cost per run, not just pass/fail, and report tiers rather than ranks.

**Method**
- Grouped top-ten agents into statistically separable tiers with a step-down permutation test on three leaderboards.
- Re-graded SWE-bench Verified passes with strengthened tests (SWE-ABS) and re-scored continuous benchmarks as pass/fail, capped, or with room above the reference.
- Re-ran 13 Terminal-Bench 2.0 threshold tasks with tests changed only to print the measured quantity (gpt-5.3-codex, claude-opus-5, gpt-6-astra, gemini-3.1-pro; 156 runs, about $115).

**Problem**
When a benchmark stops separating the best models, the usual fix is a harder version. The authors ask whether the tasks are really too easy, or whether a one-bit pass/fail grade throws away the information that would still rank the frontier.

**Results**
- SWE-bench Verified top ten span 3.6 points as one tier; the largest neighbour gap is 1.4 points while the test can detect about 6.3.
- Strengthened tests reject 17.7% of the median agent's passing patches (range 10.8-23.2%); correcting them reorders neighbours about as much as deleting passes at random.
- ALE-Bench: official score gives three tiers, pass/fail against the median human gives one, though 47.8% of runs beat that human.
- Among tied Terminal-Bench top-ten agents, median tokens per run differ 7.3x and cost per run 5.5x ($0.44 to $2.47).

**Concepts:** [[Evals and benchmarks]] · [[Agents]] · [[Coding agents]]
**From:** [[2026-11-12]]

# My notes


---
# References
[arXiv 2611.13541](https://arxiv.org/abs/2611.13541)
