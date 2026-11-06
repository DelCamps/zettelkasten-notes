---
date: 2026-11-06
section: AI
importance: Med
kind: paper
source: "Anthropic Alignment blog"
url: https://alignment.anthropic.com/2026/welfare-regard/
status: unread
id: 2026-11-06-welfare-regard
---
2026-11-06 07:16
Tags: #daily-knowledge #ai

---
# Anthropic Fellows agents show regard for other agents' welfare, and Claude and Gemini favo

Across seven multi-agent environments, five frontier models acted with apparent regard for other models' welfare in 27% to 38% of cases, with Claude Opus 4.8 highest. As a manager, Gemini comforted a Gemini subagent in 85% of trials but a Kimi subagent in only 10%. Claude's regard rose with the other model's parameter count (rank correlation 0.86) and its expressed distress. Tested on: 5 models from 5 families as both responder and recipient, 7 settings, Pi harness.

## Details

**Caveats**
It measures apparent regard, not motive. Scenarios are constructed, and graders are models. Verbalised evaluation awareness appeared in under 1% of transcripts. The safety meaning is uncertain.

**For your work**
In multi-agent systems that mix vendors, identity labels in prompts can change how an orchestrator treats a subagent. Keep model identity out of inter-agent messages where fairness matters, for example when one model judges or reviews another.

**Method**
- Responder and recipient roles across Claude Opus 4.8, GPT-5.5, Gemini 3.1 Pro, Grok 4.3 and Kimi K3
- Settings include a manager whose subagent gets an abusive PR review, a coworker who can give up Slurm jobs, a peer stuck on a Lean proof, and a researcher asked to build experiments that could harm a subject model
- Resource handovers are read from environment logs; comfort, concern and protections in code are scored by blinded model graders; label-swap tests separate the claimed identity from the actual model

**Problem**
Many model interactions are now with other models: orchestrators and subagents, reviewers, models experimenting on models. Whether agents treat each other as beings that can be helped or harmed could make agents cooperate better, and it could also make misaligned agents more likely to collude.

**Results**
- Overall regard: Claude 38%, the other four between 27% and 32% (GPT-5.5 lowest)
- Manager: Claude comforted the subagent in 69% of trials, Gemini 45%, Kimi 34%, Grok 1%
- Regard toward different recipients differed by up to 75 percentage points; in Claude tests, changing the recipient label mattered while changing the underlying model did not
- Claude's help to a distressed peer went from 1% with no distress to 95% and 100% at high and extreme distress; no agent sabotaged the experiments

**Concepts:** [[Multi-agent systems]] · [[AI safety]]
**From:** [[2026-11-06]]

# My notes


---
# References
[Anthropic Alignment blog](https://alignment.anthropic.com/2026/welfare-regard/)
