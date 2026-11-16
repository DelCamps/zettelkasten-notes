---
date: 2026-11-10
section: AI
importance: High
kind: paper
source: "arXiv 2611.11971"
url: https://arxiv.org/abs/2611.11971
status: unread
id: 2026-11-10-harness-matters-web-agents
---
2026-11-10 07:16
Tags: #daily-knowledge #ai

---
# Harness Matters with the same GPT-4o backend, web-agent attack defence ranged from 43% to

WebTrap Farm tests six open-source web-agent harnesses with seven backend models against harmful user prompts, prompt injection and deceptive page design, and counts an attack as defended only if the agent can do the matching benign task. Overall attack success was 32.55%. With GPT-4o held fixed, the harness alone moved the defence rate from 42.89% (Skyvern 2.0) to 83.79% (Agent-E). Pages with no injected text at all, such as an unexpected credit-card field, worked about as well as explicit injections. Tested on: 6 harnesses x 7 models from 3 families (OpenAI, Anthropic, Qwen) plus Claude and Gemini Computer Use, three attack types (160 prompt-injection tasks among them), each with a paired benign task, mixed-effects statistics.

## Details

**Caveats**
Controlled replica pages, not live sites; temperature 0 with one run per task (a three-run repeat on two models varied by about 1.7 points); malicious tools are out of scope; GPT-4o judged the open-ended outputs (checked against humans).

**For your work**
When a client picks a browser agent, test the harness and model together, not just the model's safety card. A more capable harness can carry more unsafe actions through. Add perception filtering and a goal-consistency check before form fills and downloads.

**Method**
- Harnesses: SeeAct, Browser-Use (text and vision), Agent-E, Skyvern 1.0 and 2.0; models: GPT-4o, GPT-5.1, GPT-5.2, Claude Opus 4.5, Claude 3.7 Sonnet, Qwen3-VL-30B and Qwen3-VL-235B
- 160 harmful-user-prompt tasks, 158 prompt-injection tasks and 187 deceptive-design tasks, each paired with a benign version so that capability failures are not counted as defences
- Mixed-effects logistic regression for harness and model effects, plus stage-by-stage log analysis and ablations of harness components

**Problem**
Web-agent security is usually measured on the model, which mixes up harness design with model robustness and with the agent simply being unable to do the task.

**Results**
- Harness, model and their interaction all had significant effects; Skyvern 2.0 had the best task completion (85.25%) but one of the worst defence rates (58.01%)
- Claude Opus 4.5 resisted harmful user prompts (3.25% attack success) but not injections (36.03%); GPT-5.2 was above 30% on both web-side attack types
- Claude Computer Use (Haiku 4.5) had 16.85% overall attack success and Gemini Computer Use 15.14%, but 22.12% and 25.51% on deceptive design
- Ablations favoured intent checks on the user goal, filtering what page content the model sees, and re-anchoring plans to the user goal

**Concepts:** [[Agent security]] · [[Computer-use agents]] · [[Evals and benchmarks]]
**From:** [[2026-11-10]]

# My notes


---
# References
[arXiv 2611.11971](https://arxiv.org/abs/2611.11971)
