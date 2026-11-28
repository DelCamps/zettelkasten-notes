---
date: 2026-11-28
section: AI
importance: Med
kind: paper
source: "arXiv 2611.30494"
url: https://arxiv.org/abs/2611.30494
status: unread
id: 2026-11-28-llm-context-engineers
---
2026-11-28 07:16
Tags: #daily-knowledge #ai

---
# Automatic context engineering (GEPA, ACE, TF-GRPO) does not reliably beat chain-of-thought

A unified benchmark re-runs LLM-driven context engineering methods (GEPA, TextGrad, TF-GRPO, ACE) under the same settings and finds no single winner, often no gain over plain chain-of-thought or in-context examples, and no reliable improvement from larger or newer models. Gains appear mostly where failure modes are homogeneous, and part of the reported gains come from better format adherence. Tested on: 3 models from 3 families at 8B scale (Qwen3, Gemma 4, Ministral 3) plus Qwen scaling runs, 5 tasks including AppWorld, 5 seeds.

## Details

**Caveats**
Main benchmark uses small open models only; frontier models not tested.

**For your work**
- Before selling automated prompt or playbook optimisation, run it against a CoT and few-shot baseline on the client's own data and check whether gains are only format fixes.

**Method**
- Benchmark across maths (MATH500), multi-hop (HotpotQA), instruction following (IFBench), retrieval (MiddleMatch) and agentic tasks (AppWorld).
- Official codebases for GEPA, TextGrad, TF-GRPO and ACE, compared with CoT and ICL baselines; each run with 5 seeds.
- Scaling studies from Qwen3-0.6B to Qwen3-235B-A22B and Qwen1.5-7B to Qwen3.5-9B; failure-mode diversity measured by embedding LLM-diagnosed failure causes.

**Problem**
Methods that let an LLM write instructions or playbooks from offline trials report gains on disjoint benchmarks and models, so it is unclear when they actually help.

**Results**
- Gains versus baselines range from -7.30 to +22.20 points depending on model and dataset; big gains are mostly on MiddleMatch.
- A bigger reflector model can cause more gain but also more loss; scaling does not rescue failures.
- On MATH500 with Gemma, gains nearly vanish once an LLM extractor fixes answer format (e.g. TF-GRPO +6.10 to +1.50).

**Concepts:** [[Evals and benchmarks]] · [[Agents]]
**From:** [[2026-11-28]]

# My notes


---
# References
[arXiv 2611.30494](https://arxiv.org/abs/2611.30494)
