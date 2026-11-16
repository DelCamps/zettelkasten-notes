---
date: 2026-10-28
section: AI
importance: Med
kind: paper
source: "arXiv 2610.36589"
url: https://arxiv.org/abs/2610.36589
status: unread
id: 2026-10-28-infradev
---
2026-10-28 07:16
Tags: #daily-knowledge #ai

---
# InfraDev best coding agent resolves 38.9% of real Megatron, vLLM and verl changes

A benchmark of 36 tasks rebuilt from real pull requests to Megatron-LM, vLLM and verl asks agents for multi-file, multi-GPU infrastructure changes. GPT-6 Sol leads at 38.9%; hidden probes reject 32% of submissions that pass every official test, and with the original PR descriptions as prompts no model resolves a single task. Tested on: 6 models from 5 providers (no Claude), 36 tasks.

## Details

**Caveats**
Small task count (36), so differences of one or two tasks move the numbers a lot. No Claude model tested. The authors note possible degradation of the served GPT-5.6 Sol during their run window.

**For your work**
Strong evidence that passing the repo's own tests is not proof a coding agent's patch is right: add targeted probes (memory, timing, traffic) in your agent evals. The 'turn failure analysis into a skill' trick is directly reusable for Claude Code skills.

**Method**
- 36 tasks from merged PRs across training, inference and RL frameworks, each spanning many files and run across many GPUs.
- Hidden probes check requirements the original tests leave unchecked, plus a prompt that states every interface the probes call without leaking the solution.
- A shared execution environment reuses dependencies and artifacts, cutting storage by 52-57% and build time by 13-14%.

**Problem**
Coding agents are starting to work on the infrastructure that trains and serves models, but benchmarks cover single kernels or single-GPU jobs and grade with tests that often accept wrong patches.

**Results**
- Resolved rate ranges from 25.0% (GLM 5.3) to 38.9% (GPT-6 Sol); GPT-6 Sol cost $5.37 per run versus $17.98 for GPT-5.6 Sol.
- Probes reject 32% of submissions that pass every official test.
- Inference tasks are hardest: every model resolves only one of ten.
- Turning the failure analysis into an agent skill raises a frontier model's resolved rate on Megatron-LM tasks by 10.5%.

**Concepts:** [[Coding agents]] · [[Evals and benchmarks]]
**From:** [[2026-10-28]]

# My notes


---
# References
[arXiv 2610.36589](https://arxiv.org/abs/2610.36589)
