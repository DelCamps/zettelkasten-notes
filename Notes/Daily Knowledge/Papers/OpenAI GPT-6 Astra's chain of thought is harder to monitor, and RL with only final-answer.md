---
date: 2026-11-11
section: AI
importance: Med
kind: paper
source: "OpenAI Alignment blog"
url: https://alignment.openai.com/cot-monitorability-model-lifecycle/
status: unread
id: 2026-11-11-openai-cot-monitorability-lifecycle
---
2026-11-11 07:16
Tags: #daily-knowledge #ai

---
# OpenAI GPT-6 Astra's chain of thought is harder to monitor, and RL with only final-answer

Tracing internal and released models from GPT-5 to Astra-class, OpenAI finds that reasoning without a chain of thought grows smoothly as base-model perplexity falls, that CoT controllability rises during RL even without process supervision, and that students distilled from a more controllable teacher become more controllable. It cites UK AISI's no-CoT time horizon for Astra of 30.9 minutes, against an earlier projection of about 7 minutes by end of 2028. Tested on: OpenAI internal models (GPT-5 to Astra-class), four no-CoT benchmarks, a few controlled RL and distillation pairs; the post gives no exact controllability scores.

## Details

**Caveats**
Controllability is a noisy proxy (in one pair a more controllable model did not evade more); results are confounded with capability; RL comparisons are not controlled for pre-RL conditions; the no-CoT Astra variant is not public; UK AISI says its estimate may be inflated by contamination.

**For your work**
Don't sell CoT inspection as a reliable safety control for frontier models; pair it with action-level monitoring and permissions in agent designs.

**Method**
- Proxies for worst-case evasion: no-CoT capability (reasoning in one forward pass) and CoT controllability (adding, removing or manipulating CoT on instruction).
- Pretraining: four no-CoT evals across models from GPT-5 (August 2025) to Astra-class; architecture: three model series compared at equal perplexity.
- RL: Astra-class and Terra-scale models trained with only length limits and final-answer grading, plus a variant with terminal and browser tools; SFT: two teachers with different controllability distilled into copies of one base.

**Problem**
OpenAI relies on reading chains of thought for oversight, but GPT-6 Astra showed degraded CoT monitorability, more ability to evade monitors under adversarial tests and much stronger no-CoT capability. Which training choices cause this?

**Results**
- No-CoT capability tracks falling perplexity; controllability correlates more weakly with it; Astra is not off-trend in perplexity terms.
- One architecture beats its perplexity on multihop planning and serial computation evals.
- Controllability increases during RL; tool access and tool supervision add only a slight further increase.
- Distilling from a more controllable teacher yields a more controllable student, which the authors liken to subliminal learning.

**Concepts:** [[AI safety]] · [[Interpretability]] · [[Frontier models]]
**From:** [[2026-11-11]]

# My notes


---
# References
[OpenAI Alignment blog](https://alignment.openai.com/cot-monitorability-model-lifecycle/)
