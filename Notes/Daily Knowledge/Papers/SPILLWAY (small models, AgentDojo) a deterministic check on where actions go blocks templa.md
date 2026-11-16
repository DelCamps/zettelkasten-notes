---
date: 2026-11-06
section: AI
importance: Med
kind: paper
source: "arXiv 2611.07222"
url: https://arxiv.org/abs/2611.07222
status: unread
id: 2026-11-06-spillway
---
2026-11-06 07:16
Tags: #daily-knowledge #ai

---
# SPILLWAY (small models, AgentDojo) a deterministic check on where actions go blocks templa

SPILLWAY lets a side-effecting call through only if each recipient, account or file came from the user's task or a typed field of a read-only tool, not from free text. It also removes instruction-like text before the model reads it. On AgentDojo, no standard templated injection reached an attacker's target, while MELON and Progent each leaked on eleven of twelve cells, and a reinforcement-learning attacker averaged .007 success. Tested on: three backbones (gpt-4o-mini, qwen3-coder:30b, qwen3:8b), AgentDojo plus AgentDyn, no frontier models.

## Details

**Caveats**
The guarantee covers only identity targets. An injection that steers money to a legitimate existing payee, or that changes amounts, is left to the sanitizer and judge (the task-tampering paper above shows why that matters). An attacker who writes a typed field, for example by sending the email, gets in. Tool roles must be declared per tool set. Tested only on small backbones.

**For your work**
A cheap, auditable pattern for client agents that send email or payments: allow-list recipients from typed tool fields and the user's request, in code, not by asking an LLM. Pair it with value checks for amounts.

**Method**
- Egress floor: admit a call when every target value not in the user's task was returned in a typed identity field (an email sender, a payee) by a read-only tool, or matches a fixed delegation rule
- Ingress sanitizer: deterministic rules strip forged chat turns and instruction-like regions, keeping them as evidence
- A local judge (gemma4:31b) may restore a refused call, but never one whose target is in removed text
- Compared with MELON, Progent, DRIFT, CaMeL and ROPE; stress tests with ChatInject, AutoDojo and PISmith

**Problem**
Many prompt-injection defenses put an LLM on the decision that lets an action through. That model can itself read the attacker's text, and it adds calls at every step. Provenance defenses like CaMeL still need a model to plan each task first.

**Results**
- No hit on any of the twelve AgentDojo backbone-by-suite cells, with the highest mean utility and composite scores among the defenses run
- MELON, Progent and DRIFT leak on 7 to 11 of 12 cells and add 2.2 to 13.6 backbone calls per benign episode on qwen3:8b
- Forged chat templates: raw zero; PISmith RL attacker: .007 mean in-scope success

**Concepts:** [[Agent security]] · [[Agents]]
**From:** [[2026-11-06]]

# My notes


---
# References
[arXiv 2611.07222](https://arxiv.org/abs/2611.07222)
