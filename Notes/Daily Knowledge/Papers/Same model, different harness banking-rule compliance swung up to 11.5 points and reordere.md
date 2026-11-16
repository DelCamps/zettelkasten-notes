---
date: 2026-11-05
section: AI
importance: Med
kind: paper
source: "arXiv 2611.06116"
url: https://arxiv.org/abs/2611.06116
status: unread
id: 2026-11-05-harness-is-the-model-banking
---
2026-11-05 07:16
Tags: #daily-knowledge #ai

---
# Same model, different harness banking-rule compliance swung up to 11.5 points and reordere

A pre-registered study from a bank ran four open-weight models in five agent harnesses on 156 simulated retail-bank cases built from EU conduct rules. Pooled over models, harnesses differed little (87.3% to 92.1% correct), but for one model the gap between its best and worst harness was 11.5 points, enough to move it from first to last. A same-model reviewer cut violations from 9.6% to 6.4% without adding over-refusals. Tested on: 4 open-weight models from 3 families, 5 harnesses, 3,120 episodes, with Wilson CIs.

## Details

**Caveats**
Synthetic bank and policy, mid-size models with reasoning disabled, and one author who works for a bank.

**For your work**
A strong argument for validating the model-and-harness pair in FS clients, scoring the action log rather than the transcript, and adding a reviewer step. Handle date calculations in code, not in the model.

**Method**
- Simulated bank with 13 state-changing tools and a manual whose 11 rule families paraphrase EU consumer-credit, payments, investor-protection, GDPR and AML rules
- Five harnesses: a single structured-decision pipeline, a ReAct tool loop, policy reachable only through search, long benign customer memory, and a same-model compliance reviewer
- Scored deterministically from the executed tool trace, counting violations and over-refusals separately

**Problem**
Banks validate models, but what they deploy is a model inside a harness, which controls the context, the tools and any checks. Does the harness change compliance with conduct rules when the model is held fixed?

**Results**
- qwen3.8-flash-next went from 93.6% with the reviewer to 82.1% with policy-by-search; deepseek-v4.1-flash moved only 1.9 pp
- The model-by-harness interaction was only suggestive, not significant at 5%
- Date-arithmetic rules (14-day withdrawal, 13-month refund limit) failed under every harness
- In 26% of violations the agent told the customer it had not done the action it had just executed

**Concepts:** [[Agents]] · [[Evals and benchmarks]] · [[AI safety]]
**From:** [[2026-11-05]]

# My notes


---
# References
[arXiv 2611.06116](https://arxiv.org/abs/2611.06116)
