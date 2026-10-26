---
date: 2026-10-26
section: AI
importance: Med
kind: paper
source: "arXiv 2610.32483"
url: https://arxiv.org/abs/2610.32483
status: unread
id: 2026-10-26-model-or-harness
---
2026-10-26 07:16
Tags: #daily-knowledge #ai

---
# Model or harness 52,168 trajectories show harness rankings flip with the model

Four general harnesses (OpenCode, Codex CLI, Pi CLI, DeepAgents) were crossed with four models on six benchmarks, 111 settings and 52,168 trajectories. Harness rankings change by model and benchmark; OpenCode ranks first across models, and DeepSeek V4 Flash Preview finishes runs validly most consistently. Tested on: 4 harnesses x 4 models plus 2 native systems, 6 benchmarks, 52,168 trajectories.

## Details

**Problem**
Agent benchmark scores reflect the model and the harness together, so it is unclear whether a failure comes from the model, the harness or their pairing.

**Method**
- Five measures: Valid Completion Rate, Model-Harness Fit, Cross-Model Fit, Interaction Residuals and Token Load (including failed attempts).
- Four harnesses (OpenCode, Codex CLI, Pi CLI, DeepAgents) with four core models, plus two native model-harness systems, on six benchmarks covering context management, tool use, long-context planning, multimodal work and artifact handoff.

**Results**
- 111 evaluation settings, 52,168 trajectories.
- Harness rankings vary across models and benchmarks; task score and valid completion can favor different pairings.
- OpenCode ranks first in cross-model performance; DeepSeek V4 Flash Preview keeps consistently high valid completion across harnesses.
- Similar task scores can hide very different execution and token profiles.

**Caveats**
Four models and four harnesses only; closed native systems are fixed references, so cross-pairing is incomplete.

**For your work**
When choosing a stack for a client, benchmark the specific model-harness pair on their tasks and track valid completion and token load, not just pass rate.

**Concepts:** [[Agents]] · [[Evals and benchmarks]] · [[Coding agents]]
**From:** [[2026-10-26]]

# My notes


---
# References
[arXiv 2610.32483](https://arxiv.org/abs/2610.32483)
