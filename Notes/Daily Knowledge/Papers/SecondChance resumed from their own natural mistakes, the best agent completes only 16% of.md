---
date: 2026-11-25
section: AI
importance: Med
kind: paper
source: "arXiv 2611.31586"
url: https://arxiv.org/abs/2611.31586
status: unread
id: 2026-11-25-secondchance-error-recovery
---
2026-11-25 07:16
Tags: #daily-knowledge #ai

---
# SecondChance resumed from their own natural mistakes, the best agent completes only 16% of

A checkpoint benchmark built from agents' real errors in tau2-bench, BFCL and AppWorld, resumed under four conditions (no help, error notice, error location, repair guidance) and scored on correction, task success, policy compliance and state preservation. Correcting is not recovering: with guidance, Llama-3.3-70B corrects 26% of tau2 errors but completes none, and 40 of 84 successful AppWorld continuations leave the error in place. Tested on: 12 models from OpenAI, Google, Alibaba, Meta and Mistral, 5,760 continuations.

## Details

**Caveats**
No Claude models. Task-success evaluators miss uncorrected errors, so the benchmark relies partly on an LLM judge.

**For your work**
Do not assume an agent will notice and undo its own wrong write. Build explicit verification and undo paths, and score state preservation, not just 'task done'.

**Method**
- Errors harvested from agents' own task attempts in three environments
- Different models resume from identical checkpoints under four assistance levels
- Metrics: correction, task success, policy compliance, environment-state preservation, durability and cost; semantic checks by a pinned Qwen3-235B judge

**Problem**
Recovery benchmarks inject artificial faults and score only final completion, so they cannot tell whether an agent fixed its own silent error, told the user, or hit something unfixable.

**Results**
- Best model GPT-6.1-sol: 16% unaided, 27% with a plan; no model above 21% unaided in any single environment
- Without a plan, nine models correct nothing
- Deleted records are almost never restored (2 of 60 runs with a plan)
- Weak models burn far more calls: Llama-3.3-70B 415 agent calls vs 21 for GPT-6.1-sol

**Concepts:** [[Agents]] · [[Evals and benchmarks]]
**From:** [[2026-11-25]]

# My notes


---
# References
[arXiv 2611.31586](https://arxiv.org/abs/2611.31586)
