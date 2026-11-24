---
date: 2026-11-24
section: AI
importance: Low
kind: news
source: "Hugging Face blog"
url: https://huggingface.co/blog/agentic-evals
status: unread
id: 2026-11-24-hf-agentic-evals-guide
---
2026-11-24 07:16
Tags: #daily-knowledge #ai

---
# Hugging Face guide to building agentic evals validate every task with an oracle, a no-op a

A practical guide on defining the claim, adapting an existing task, checking the evaluation, reading traces and reporting scores, plus what to release openly. Its worked example adapts Terminal-Bench's raman-fitting task: gpt-oss-120b passed 11 of 24 rollouts, and a shortcut script that skipped the fitting still got the right answer on all 8 tasks, which forced the authors to add per-peak checks.

## Details

**Caveats**
- A guide with an eight-task case study, not a controlled study
- One harness and one provider set-up
- Some cited figures come from other organisations

**For your work**
A checklist you can reuse for client agent evals: always run an oracle, a no-op and a shortcut before trusting a task, and report pass^k (reliability) next to pass@k.

**Method**
- Anatomy: task, agent harness, evaluation harness, rollouts, traces and verifier, each inspectable separately
- Eight steps: define the claim, find a starting task, run it unchanged, adapt it, check it, read traces, report, compare
- Validation: an oracle must pass; a no-op agent and a deliberate shortcut must fail
- Report pass@k, pass^k and mean pass rate with task-clustered standard error

**Problem**
Agentic evaluations are easy to get wrong: tasks can be passed by shortcuts, graders miss failures, and single scores hide variance. Teams building their own evals lack a simple process.

**Results**
- Adapted raman-lab set: gpt-oss-120b passed 11 of 24 rollouts; pass@3 7/8, pass^3 1/8; mean 0.46
- Qwen3.8-27B, DeepSeek-V4.1-Flash and MiniMax-M3.1-Flash each passed all 24, so the set cannot rank them
- All six model runs cost under $5

**Concepts:** [[Evals and benchmarks]] · [[Agents]]
**From:** [[2026-11-24]]

# My notes


---
# References
[Hugging Face blog](https://huggingface.co/blog/agentic-evals)
