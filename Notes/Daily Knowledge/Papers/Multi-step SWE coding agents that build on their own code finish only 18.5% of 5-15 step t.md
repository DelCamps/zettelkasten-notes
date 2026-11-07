---
date: 2026-11-07
section: AI
importance: High
kind: paper
source: "arXiv 2611.07166"
url: https://arxiv.org/abs/2611.07166
status: unread
id: 2026-11-07-multi-step-swe
---
2026-11-07 07:16
Tags: #daily-knowledge #ai

---
# Multi-step SWE coding agents that build on their own code finish only 18.5% of 5-15 step t

A new benchmark chains 5-15 dependent, multi-hour engineering steps (build, extend, upgrade, optimize) on one codebase, each starting from the agent's own previous work. The best model, Claude Opus 5.5, fully solves 18.5% of rollouts while passing 56.8% of individual steps, and 38 of the 69 tasks are solved by no model. In 52% of failed steps the agent reported the step as complete and named no shortcoming. Tested on: nine frontier models from seven providers, each in its own harness (Claude Code, Codex CLI, mini-swe-agent, Grok Build), 69 tasks, four rollouts per task, with confidence intervals.

## Details

**Caveats**
Results mix model and harness. C and C++ make up 38 of the 69 tasks. Memorization of public projects cannot be ruled out. No isolated-step baseline yet to separate accumulated errors from step difficulty.

**For your work**
For multi-request client builds, do not trust an agent's 'done': run independent verification after every step, and gate the next request on it, since one failed step makes the next one much more likely to fail.

**Method**
- 69 tasks in four families (optimization, feature implementation, version upgrade, migration), nine languages, 34 from scratch and 35 on existing open-source code
- Each step grounded in an existing source of truth (specs, upstream releases, conformance suites, recorded behaviour) and graded in a separate verifier container, with anti-reward-hacking checks
- A rollout counts as solved only if every step gets full credit; failure reports labelled on a stratified sample of 2,157 final reports

**Problem**
Developers ask an agent to build something, then extend, port and speed it up, all on code the agent wrote. Single-episode benchmarks do not measure whether early design decisions and errors compound.

**Results**
- Solve rate: Claude Opus 5.5 18.5% (Pass@4 31.9%), Claude Fable 5.1 17.8%, Gemini 4 Argon and GPT-6.1 Sol 10.1%, down to Grok 4.7 at 1.4%
- A step after a passed step passes 70.2% of the time vs 14.1% after a failed step
- Only 12% of failed steps came within five minutes of the time budget; median failed step used 24-37% of its budget
- When an agent claims completion with no caveats, the verifier still fails the step 57% of the time (26% for Opus 5.5, 82% for Grok 4.7)

**Concepts:** [[Coding agents]] · [[Evals and benchmarks]] · [[Frontier models]]
**From:** [[2026-11-07]]

# My notes


---
# References
[arXiv 2611.07166](https://arxiv.org/abs/2611.07166)
