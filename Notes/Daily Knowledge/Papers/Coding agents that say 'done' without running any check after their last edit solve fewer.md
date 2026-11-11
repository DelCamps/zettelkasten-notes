---
date: 2026-11-11
section: AI
importance: Low
kind: paper
source: "Hugging Face community blog"
url: https://huggingface.co/blog/serkanpeker/kanitsiz-bitti
status: unread
id: 2026-11-11-unverified-done-coding-agents
---
2026-11-11 07:16
Tags: #daily-knowledge #ai

---
# Coding agents that say 'done' without running any check after their last edit solve fewer

A deterministic classifier sorts each run by what happened after the last code edit; within the same tasks, unverified submissions solved less often than ones whose last test or script ran cleanly, both in a public SWE-agent dataset and in a two-stage replication with Claude Code CLI. The effect is observational and the post says it is underpowered. Tested on: SWE-agent with Llama-based 8B, 70B and 405B models (public trajectories) and gpt-oss-120b in Claude Code on SWE-bench Verified; two harnesses, thousands of trials.

## Details

**Caveats**
Observational: agents that find the right file early may both test more and solve more; timeouts excluded; one model per harness in phase 2; classifier and audits were AI-written without human review; about 5,000 trials would be needed for 80% power. Community post, not peer reviewed; written in Turkish.

**For your work**
A cheap harness hook: flag or block 'done' when no test or script ran after the last edit, and use that flag as a risk signal in client coding-agent dashboards.

**Method**
- A rule-based classifier (91 unit tests) labels each trial unverified, ran-and-failed, ran-and-passed or no product change, based on actions after the last product-code edit.
- Solve status from hidden tests; odds ratios stratified by task to control for difficulty.
- Phase 1: 51,087 nebius/SWE-agent trajectories. Phase 2: Claude Code CLI 2.1.318 via Harbor with locally served gpt-oss-120b on SWE-bench Verified; a stage-2 replication added 8 more attempts on the 147 tasks that had an unverified attempt, with a dated pre-stated hypothesis.

**Problem**
Coding agents often declare a task finished without running a test or script after their final edit. Is that claim less trustworthy?

**Results**
- Phase 1: 39.4% of code-changing submissions were unverified; odds ratio vs last-check-passed 0.68 (95% CI 0.63-0.74), raw solve 18.2% vs 34.0%.
- First Claude Code run was inconclusive (odds ratio 1.04, wide interval) because of environment problems.
- Replication (1,535 trials on 147 tasks): solve 43.4% unverified vs 56.1% passing; odds ratio 0.55 (0.37-0.82), meeting the pre-stated criterion.

**Concepts:** [[Coding agents]] · [[Evals and benchmarks]]
**From:** [[2026-11-11]]

# My notes


---
# References
[Hugging Face community blog](https://huggingface.co/blog/serkanpeker/kanitsiz-bitti)
