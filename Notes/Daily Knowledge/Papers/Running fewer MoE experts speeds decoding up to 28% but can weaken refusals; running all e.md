---
date: 2026-11-05
section: AI
importance: Med
kind: paper
source: "arXiv 2611.06147"
url: https://arxiv.org/abs/2611.06147
status: unread
id: 2026-11-05-safestart-moe-expert-reduction
---
2026-11-05 07:16
Tags: #daily-knowledge #ai

---
# Running fewer MoE experts speeds decoding up to 28% but can weaken refusals; running all e

MoE serving tricks that run fewer experts per token are validated on accuracy, yet under a 'do not refuse' jailbreak they raised harmful compliance by 18.4 points on Qwen1.5-MoE, 9.5 on OLMoE and 6.6 on DeepSeek-V2-Lite, while MMLU fell by less than two points. SafeStart, a vLLM patch, runs all experts for the prompt and the first eight tokens and keeps at least 85% of the speedup. Tested on: 9 MoE models from 6 families in vLLM, 3 expert-reduction methods, 889 held-out requests with a pre-fixed analysis.

## Details

**Caveats**
Small and mid-size open MoE models (up to 57B) on one GPU type, and mostly one jailbreak style.

**For your work**
If a client self-hosts MoE models with aggressive serving optimisations, rerun refusal and jailbreak evals as well as accuracy before go-live.

**Method**
- Paired, noise-calibrated refusal audit of expert reduction in vLLM on one RTX A6000
- Located where the refusal change arises: in prefill and the first few decode steps
- SafeStart: a fused-kernel engine patch that uses all experts early and the reduced set afterwards, supporting top-k and threshold budgets

**Problem**
Expert reduction cuts MoE serving cost, but it is only checked against capability benchmarks. Does it erode safety behaviour?

**Results**
- Keeping about two thirds of experts gives 15-28% faster offline decoding at batch size 8; harmful compliance rose significantly on 3 of 9 models
- With SafeStart, the jailbreak change falls to between -2.1 and +1.3 points for three reduction methods on those three models
- On 889 held-out requests, truncation raised harmful compliance by 5.8-21.4 points versus 0.6-2.6 with SafeStart
- With about half the experts, SafeStart decodes 38-44% faster than the original model and removes at least 86% of the safety loss

**Concepts:** [[Inference efficiency]] · [[AI safety]] · [[Open-weight models]]
**From:** [[2026-11-05]]

# My notes


---
# References
[arXiv 2611.06147](https://arxiv.org/abs/2611.06147)
