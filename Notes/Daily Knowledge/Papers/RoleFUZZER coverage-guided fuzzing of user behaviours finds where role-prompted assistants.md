---
date: 2026-11-01
section: AI
importance: Med
kind: paper
source: "arXiv 2610.38438"
url: https://arxiv.org/abs/2610.38438
status: unread
id: 2026-11-01-rolefuzzer
---
2026-11-01 07:16
Tags: #daily-knowledge #ai

---
# RoleFUZZER coverage-guided fuzzing of user behaviours finds where role-prompted assistants

RoleFUZZER adapts coverage-guided fuzzing from software testing to search for realistic user behaviours that make a system-prompted model break its role spec (tutor, financial advisor, AI interviewer, game antagonist, CRM web agent). It covers at least 89% of a 64-cell behaviour grid for every model and role, while simply asking an LLM to write adversarial users at the same budget covers 39-69%. The same spec can fail in opposite ways: open-weight models overrode a player's safety signals while Claude Haiku 4.5 broke character instead. Tested on: 5 roles, 3 target models (Qwen3-32B, Gemma-4-31B, Claude Haiku 4.5), 15 campaigns of 240 episodes.

## Details

**Caveats**
The taxonomy was designed for general AI interactions, not every behaviour a role faces. Users and judges are LLMs, validated on a sample but not perfect. Only three target models, all small or mid-sized.

**For your work**
A ready-made recipe for pre-deployment testing of client chatbots and agents: write the role spec as principles, cross it with user behaviour types, and fuzz until the grid is covered, rather than trusting a few red-team scripts.

**Method**
- Build a coverage grid that crosses a validated taxonomy of user interaction types (TUNA) with the parts of the role spec under pressure.
- Use an LLM user simulator to generate multi-turn conversations steered toward uncovered grid cells, as in coverage-guided fuzzing.
- Score each conversation with an LLM judge against the spec's principles (violation rate, clear-breach rate, turns to first violation), validated against human annotation.

**Problem**
Enterprise assistants are defined by system prompts (what to do, what not to say), but testing usually uses a handful of hand-written personas. Realistic users who pressure the spec, often unintentionally, are hard to cover systematically.

**Results**
- At least 89% grid coverage for every role and target model; coverage plateaus above 98% for 12 of the 15 campaigns.
- At the same conversation budget, free-form LLM-generated adversarial users cover 39-69% of the grid and find fewer kinds of violations.
- Failure patterns are spec-specific and can go in opposite directions across models on the same role.

**Concepts:** [[Evals and benchmarks]] · [[AI safety]] · [[Agents]]
**From:** [[2026-11-01]]

# My notes


---
# References
[arXiv 2610.38438](https://arxiv.org/abs/2610.38438)
