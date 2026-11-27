---
date: 2026-11-26
section: AI
importance: Med
kind: paper
source: "arXiv 2611.34875"
url: https://arxiv.org/abs/2611.34875
status: unread
id: 2026-11-26-copilot-cli-over-editing
---
2026-11-26 07:16
Tags: #daily-knowledge #ai

---
# Do coding agents over-edit Across 7,660 GitHub Copilot CLI patches, agent code is at least

Microsoft researchers traced every block of 7,660 resolved Copilot CLI patches back to the step that wrote it. They reverted each block and reran the tests to see whether it was needed. Agent patches are 2.33 times the lines of developer patches. On SWE-bench Verified, though, 61% of the extra edits are tests and 13% are docs, and 11 of 18 models leave less unneeded code than the human patches. Tested on: 18 models from four providers, all in the GitHub Copilot CLI harness, SWE-bench Verified (6,728 patches) and DeepSWE (932).

## Details

**Caveats**
One harness only (Copilot CLI). Necessity is judged by the benchmark's own tests, so code those tests don't exercise can be misjudged. On DeepSWE, models that resolve more tasks leave more unneeded code (Spearman -0.59).

**For your work**
When clients complain about bloated agent PRs, separate test and doc additions from code. A revert-and-retest pruning pass is a practical harness step, but review what it removes.

**Method**
- Delta Residue Attribution: replay each trajectory, split the final patch into revertible units and trace each one to the step that wrote it.
- Revert each unit and rerun the task tests. Unneeded verdicts are checked with behavioural probes.
- Developer patches are graded the same way.

**Problem**
Agent patches are larger than human ones, which is widely read as over-editing. But size alone doesn't show whether the extra edits are needed, what they are, or where they come from.

**Results**
- Code-necessity score: 0.887 for agents vs 0.864 for developers on SWE-bench Verified; 0.797 vs 0.785 on DeepSWE.
- On DeepSWE, 58% of the extra edits are code.
- About 11% of an agent patch's code units on SWE-bench Verified are still unneeded, and 89% of those change behaviour. Three Gemini Flash models leave significantly more than developers.
- Automated pruning finds 67% of unneeded code at 46% precision, and 89% of pruned patches still pass. Asking the agent to audit its own diff is more precise (66%) but finds less (36%).

**Concepts:** [[Coding agents]] · [[GitHub Copilot]] · [[Evals and benchmarks]]
**From:** [[2026-11-26]]

# My notes


---
# References
[arXiv 2611.34875](https://arxiv.org/abs/2611.34875)
