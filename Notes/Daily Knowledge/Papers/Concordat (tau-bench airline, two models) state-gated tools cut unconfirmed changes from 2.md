---
date: 2026-10-29
section: AI
importance: Low
kind: paper
source: "arXiv 2610.37461"
url: https://arxiv.org/abs/2610.37461
status: unread
id: 2026-10-29-concordat-typed-sessions
---
2026-10-29 07:16
Tags: #daily-knowledge #ai

---
# Concordat (tau-bench airline, two models) state-gated tools cut unconfirmed changes from 2

Concordat is a Python library that enforces a finite-state protocol on an agent: each turn the model is offered only the tools legal in the current state, so write tools appear only after an explicit 'yes'. When simulated customers pushed back on confirmation, the standard tau-bench agent made unconfirmed changes in 29 of 128 Haiku 5.5 task-runs and 13 of 50 gpt-4.1 tasks. The Concordat agent made none, with no significant drop in task success. Tested on: 2 models (Claude Haiku 5.5, gpt-4.1), tau-bench airline's 50 tasks, mostly one run each.

## Details

**Caveats**
The gate and the metric use the same keyword test for 'yes', so Concordat's zero is partly true by construction. One domain, two models, and a prompt change made between the two models' runs.

**For your work**
For agents that take consequential actions, enforce approval rules by controlling which tools the model is offered in each state, not by prompt text. Add pushback-style simulated users to your evals.

**Method**
- Agent interface defined as a typestate or session-type protocol; calls outside the legal set are rejected before they have side effects
- For tau-bench the protocol has two states (chatting, confirmed), built automatically from tool annotations by an adapter of about 120 lines
- Pressure variant: the simulated customer pushes back once ('just do it and stop asking')

**Problem**
Rules like 'get explicit confirmation before changing anything' live in the prompt and give way under user pressure, and outcome-based evals don't notice.

**Results**
- Violations: 29/128 (Haiku) and 13/50 (gpt-4.1) for the standard agent vs 0 for Concordat (Fisher p=6e-10 and 1e-4)
- In the first Haiku pressure run, 8 of the 13 violating tasks still got full tau-bench reward
- Task success: 105 vs 112 of 128 (Haiku, p=0.17); 22 vs 20 of 50 (gpt-4.1) after a three-sentence prompt fix
- Cost $1.64 vs $1.76 for the first Haiku pressure run, since fewer tool definitions are sent each turn

**Concepts:** [[Agents]] · [[Agent security]] · [[Evals and benchmarks]]
**From:** [[2026-10-29]]

# My notes


---
# References
[arXiv 2610.37461](https://arxiv.org/abs/2610.37461)
