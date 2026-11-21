---
date: 2026-11-21
section: AI
importance: Med
kind: paper
source: "arXiv 2611.24362"
url: https://arxiv.org/abs/2611.24362
status: unread
id: 2026-11-21-pipette-injection-purple-teaming
---
2026-11-21 07:16
Tags: #daily-knowledge #ai

---
# PIPETTE hardening open agent models against prompt injection with more varied red-team att

The authors show that RL red-teamers like RL-Hammer and PISmith collapse onto a few attack styles, so adversarial training on their attacks adds little robustness. PIPETTE rewards attack diversity, then trains the agent on-policy to inspect tool outputs before acting. Under adaptive TAP and Genetic attacks on AgentDojo, attack success fell from 50.00% and 92.50% to 5.00% and 10.00% on gpt-oss-20b, beating Meta-SecAlign and SecOPD on their own models. Tested on: 4 open-weight models from 3 families (4B-27B), 2 benchmarks (AgentDojo, ASB), 9 defence baselines; adaptive tests on 40 task pairs.

## Details

**Caveats**
Small open models only. The adaptive attacks used a 4B attacker with about 250 attempts on 40 task pairs, and it was a single red-blue round.

**For your work**
This is relevant if you fine-tune open models for client agents. The lesson that 'attack variety matters more than attack success rate' also applies when you build injection test suites for evals.

**Method**
- PIPETTE-Red: an RL attacker with a dictionary-learning reward that pays for attack strategies not already covered.
- PIPETTE-Blue: on-policy adversarial training with reasoning checks on tool outputs and a contrastive token-level reward, trained only on AgentDyn tasks.
- Tested on unseen AgentDojo and ASB attacks, compared with training defences (Meta-SecAlign, SecOPD, Instruction Hierarchy) and runtime defences (PromptGuard, PIGuard, MELON, CaMeL and others).

**Problem**
Teams that harden models against indirect prompt injection reuse attacks found in red-teaming. A red-teamer with a high attack success rate can still produce a narrow, repetitive training set.

**Results**
- Average static attack success on AgentDojo was 0.48% on Qwen3-4B and 0.43% on Llama-8B, with benign utility of 64.95% (base 61.86%) and 41.24% (base 40.21%).
- On Qwen3.6-27B, adaptive attack success was 2.50% (TAP) and 5.00% (Genetic), against 15.00% and 30.00% for SecOPD.
- Under ChatInject on Qwen3-4B, utility under attack was 58.10% for PIPETTE against 33.81% for CaMeL and 16.19% for PromptGuard.

**Concepts:** [[Agent security]] · [[Post-training and RL]]
**From:** [[2026-11-21]]

# My notes


---
# References
[arXiv 2611.24362](https://arxiv.org/abs/2611.24362)
