---
date: 2026-10-25
section: AI
importance: Med
kind: paper
source: "arXiv 2610.31593"
url: https://arxiv.org/abs/2610.31593
status: unread
id: 2026-10-25-simulated-control-evals
---
2026-10-25 07:16
Tags: #daily-knowledge #ai

---
# Simulated control evals an LLM fakes the environment and predicts monitor safety within 3

Instead of building a full sandbox, an LLM simulates tool responses so AI-control evaluations (attacker vs monitor) can run on deployment-like tasks. On LinuxArena, simulated evals predicted safety with 3.6 points RMSE across five monitors at a 5% audit budget, vs 10.1 for a separate executed setting (BashArena), using under 5% as many task draws.

## Details

**Caveats**
Validated only on LinuxArena; simulated trajectories remain somewhat distinguishable from real ones. Assumes a trusted simulator; an untrusted one could collude with the attacker.

**For your work**
A practical way to red-team a client's agent monitoring without building a full replica environment: have a model simulate the tools and run attack/monitor rounds on the client's own task mix, then spot-check with a few real executions.

**Method**
- Simulated control evaluations (SCEs): a language model simulates tool outputs in place of real execution, so attack and monitoring can be studied on any deployment's task set.
- Validated on LinuxArena where real execution gives ground truth, compared with BashArena and with natural variation inside LinuxArena.
- Also tests whether attack strategies discovered in simulation improve monitors on held-out real attacks.

**Problem**
Control evaluations test whether monitors and safeguards stop a deliberately misbehaving model, but they run in purpose-built settings whose tasks and infrastructure differ from the real deployment, so results extrapolate poorly.

**Results**
- Safety predicted with 3.6 percentage points RMSE across five monitors at a 5% audit budget, vs 10.1 for BashArena.
- Over tenfold lower KL divergence from execution for attack strategies and attacker/monitor reasoning.
- Explains 78-85% of between-environment variance in attack success, monitor scores and safety; beats BashArena with under 5% of the task-pair draws.
- Simulated strategies improve monitors on held-out attacks about as much as executed ones.

**Concepts:** [[AI safety]] · [[Evals and benchmarks]] · [[Agent security]]
**From:** [[2026-10-25]]

# My notes


---
# References
[arXiv 2610.31593](https://arxiv.org/abs/2610.31593)
