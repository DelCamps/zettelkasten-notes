---
date: 2026-10-23
section: AI
importance: High
kind: paper
source: "arXiv 2610.29932"
url: https://arxiv.org/abs/2610.29932
status: unread
id: 2026-10-23-frontiercs-2
---
2026-10-23 07:16
Tags: #daily-knowledge #ai

---
# FrontierCS 2 agents rebuild real CS research inside its repo

48 open-ended tasks across 13 domains. Each one removes a paper's contribution from its released code, and the agent has to rebuild it, scored on a held-out suite. Best of 12 agents was Claude Opus 5.5 at 58% of runs passed; 16 tasks were never solved by any run. Many runs beat the reference score but still regressed on some metric.

## Details

**Caveats**
Only one run per agent per task, and each model is tested in a single harness, so harness effects are mixed in. The case studies show the pass/score metrics can miss side costs such as circuit size and fail to reward bigger improvements.

**For your work**
The design is a good pattern for client evals: hold out the test suite, give the agent only a dev-score feedback loop, and require every metric to clear its threshold rather than relying on one aggregate score. It is also a reminder to check agent patches for regressions on secondary metrics even when the headline number improves.

**Method**
- Tasks built by subtraction: take a paper's released code, delete the code implementing its contribution (keeping the function signatures), and use the deleted code as the human reference.
- 48 tasks across 13 domains (ML systems, HPC, databases, security, robotics and more), plus a private set of more than 100 tasks still to come.
- The agent gets 5 hours in a sandbox with no network and can submit patches at any time for a development-suite score; the final patch is graded on a held-out suite.
- A run passes only if it beats the reference on every metric and every held-out workload.

**Problem**
Most open-ended coding benchmarks give an agent a problem statement and grade one program once. Real computer-science research means inheriting a working repo, changing one component, and beating the original authors' implementation on their own workloads. FrontierCS 2 tests that.

**Results**
- 12 agents, one run per task. Claude Opus 5.5 in Claude Code passed 58% of runs; every other agent passed fewer than half.
- 16 tasks were never passed by any agent.
- Most runs that beat the reference on the combined final score still missed a threshold on some metric or workload.
- On a shared capability scale, the median task is about as hard as the strongest agent can handle. DeepSeek V4.1 Flash leads at the smallest cost budgets, Opus 5.5 at the largest.

**Concepts:** [[Agent benchmarks]] · [[AI for research]]
**From:** [[2026-10-23]]

# My notes


---
# References
[arXiv 2610.29932](https://arxiv.org/abs/2610.29932)
