---
date: 2026-11-12
section: AI
importance: Med
kind: paper
source: "arXiv 2611.13336"
url: https://arxiv.org/abs/2611.13336
status: unread
id: 2026-11-12-veritas-verifier-harness
---
2026-11-12 07:16
Tags: #daily-knowledge #ai

---
# The harness, not the model, decides verifier quality a verifier-writing scaffold took Clau

Self-improving agents need a verifier to judge each attempt, but most real tasks arrive without one and asking a coding agent to write a test underperforms. Veritas is a scaffold that generates verifiers using an evidence header, a library of unstated domain rules, and authoring principles. With the model fixed, its verifiers agreed with official verdicts better than seven plain harnesses on all four execution-scored benchmarks, and plain harnesses ranged from 0.16 to 0.73 agreement on the same model, showing the harness matters as much as the model. Tested on: 6 benchmarks, 7 baseline harnesses, model fixed at GLM-5.2 for the full comparison plus 3 other model families against vendor harnesses; each config run once.

## Details

**Caveats**
Each configuration is run once (repeats only in an appendix) and the execution benchmarks have 33-138 tasks. Only GLM-5.2 is compared against all seven harnesses. Most judged candidates are constructed rather than real agent attempts, and official verdicts are treated as ground truth though they can be wrong.

**For your work**
When building agentic evals or self-improving loops for clients, the scaffold that writes the checker matters as much as the model behind it. The three ingredients (declare the observable evidence, encode unstated domain policy, give authoring principles) are directly reusable for auto-generating client-specific verifiers.

**Method**
- Added three mechanisms to a coding agent: an evidence header stating what the verifier will observe, a library of domain rules tasks leave unstated, and authoring principles refined by a self-improvement loop.
- Compared against seven plain harnesses (Codex CLI, OpenCode, pi, Terminus 2, Hermes, Claude Code, Gemini CLI) with the model held at GLM-5.2.
- Certified each benchmark's official verifier first and measured Cohen's kappa against official verdicts, counting a missing verdict as an error.

**Problem**
Recursive self-improvement is gated by the verifier that scores each round. Hand-written verifiers do not scale to real-world tasks, and a plain coding agent writes poor ones because the verifier sees different evidence than the agent, must enforce unstated domain policy, and has no tests of its own to run.

**Results**
- Best agreement on all four execution-scored benchmarks (kappa 0.79 vs 0.73 for the strongest baseline on tau2-bench) and at or near best on two pairwise benchmarks.
- Plain harnesses ranged from kappa 0.16 to 0.73 on tau2-bench with the same model, so the harness alone swings verifier quality widely.
- Added unchanged to other harnesses, the mechanisms took Claude Code from 0.24 to 0.59 on Terminal-Bench (making it the best there) and improved 9 of 12 harness-benchmark pairs.
- Beat the vendor's own harness for two of three other model families.

**Concepts:** [[Agents]] · [[Evals and benchmarks]] · [[Coding agents]]
**From:** [[2026-11-12]]

# My notes


---
# References
[arXiv 2611.13336](https://arxiv.org/abs/2611.13336)
