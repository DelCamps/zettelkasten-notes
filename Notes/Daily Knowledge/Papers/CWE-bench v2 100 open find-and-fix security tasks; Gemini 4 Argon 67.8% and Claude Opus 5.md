---
date: 2026-11-04
section: AI
importance: Med
kind: paper
source: "Hugging Face blog"
url: https://huggingface.co/blog/cwe-bench
status: unread
id: 2026-11-04-cwe-bench-v2
---
2026-11-04 07:16
Tags: #daily-knowledge #ai

---
# CWE-bench v2 100 open find-and-fix security tasks; Gemini 4 Argon 67.8% and Claude Opus 5

Collinear AI released a public set of 100 tasks covering 91 CWEs, where an agent gets a real open-source repo and must find and fix a security weakness without breaking existing features, with fully programmatic grading. Across 11 models, Gemini 4 Argon leads at 67.8% pass@1 just ahead of Claude Opus 5.5 at 67.3%, while DeepSeek V4.1 Flash reaches 57.0% at $0.04 per rollout. Tested on: 11 models from several labs (including Gemini 4 Argon, Claude Opus 5.5, DeepSeek V4.1 Flash), 100 public tasks, 4 attempts each.

## Details

**Caveats**
Run by a benchmark vendor that also sells held-out evaluation; only headline numbers for three of the 11 models are in the post, and the harness and agent used per model affect scores.

**For your work**
A cheap, reproducible way to compare models for a client's secure-code-fix or vulnerability-remediation agent; the DeepSeek cost point is a useful argument for routing routine fixes to a cheap model.

**Method**
- 100 public tasks covering 91 different CWEs: an agent receives a checkout of a real open-source repository plus a short instruction and must find and fix the weakness without breaking existing functionality.
- Deterministic programmatic verifiers, curated with LLM judge panels and reviewed by hand; checks include that starter code fails, the reference fix passes, and memorised upstream patches are rejected.
- Each task is a Dockerized Harbor task; -k 4 runs 4 attempts per task and the score is the mean reward over all 400 trials. A held-out set tracks unseen-task progress.

**Problem**
Security benchmarks for coding agents often check for one known patch, can be memorised, or depend on an LLM judge, so scores are hard to trust or reproduce.

**Results**
- Gemini 4 Argon: 67.8% pass@1, 81.0% pass@4; Claude Opus 5.5: 67.3% pass@1, 78.0% pass@4.
- 95 tasks are solved by at least one model, but the leader still fails 19% of the set on every attempt.
- Cost Pareto frontier: DeepSeek V4.1 Flash (1017) 57.0% pass@1 at $0.04 per rollout; Opus adds ten points at $1.83; Gemini at $3.92.

**Concepts:** [[AI for security]] · [[Evals and benchmarks]] · [[Coding agents]]
**From:** [[2026-11-04]]

# My notes


---
# References
[Hugging Face blog](https://huggingface.co/blog/cwe-bench)
