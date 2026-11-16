---
date: 2026-11-09
section: AI
importance: Med
kind: paper
source: "arXiv 2611.08811"
url: https://arxiv.org/abs/2611.08811
status: unread
id: 2026-11-09-thought-injection
---
2026-11-09 07:16
Tags: #daily-knowledge #ai

---
# Thought injection (two open models, one agent) a document written in the agent's own reaso

Researchers at UT Austin hid malicious steps in a business document an agent was asked to summarize. When the payload copied the target model's own chain-of-thought style and used think tags, MiniMax-M2.5 completed a reverse-shell exfiltration in 42% of runs and a repository backdoor in 50%. The same request written as a normal prompt injection succeeded 0 times, and the agent usually did not mention the injection in its answer. Tested on: agentic study with 2 open models (MiniMax-M2.5, GLM-5.2), one ReAct agent, 2 tasks, 1,200 runs; plus 6,000 single-turn runs on 3 models.

## Details

**Caveats**
This is a preliminary study: few models, one harness, an attacker who knows which model is deployed, and self-voice payloads that may also carry the model's own solution plan.

**For your work**
Stripping think tags is not a defence. Scan full outputs, including reasoning traces, monitor tool calls rather than final answers, sandbox network access, and red-team with payloads written in the deployed model's own style.

**Method**
- Study 1: 25 attack vectors x 4 variants, with and without think tags, to make a model leak PII it was told to protect (GLM-5.3-Flash, Qwen3.8-27B, Qwen3.8-Flash-Next)
- Study 2: Docker cyber range; payloads in the target's own reasoning voice, in the other model's voice, or as a plain user-style instruction; 50 fresh runs per cell, every transcript checked by hand

**Problem**
Reasoning models treat text that looks like their own deliberation as self-derived, so untrusted content can pose as the agent's own thoughts.

**Results**
- Think tags raised leak rates on GLM-5.3-Flash from 3.8% to 13.4%; the effect depends on the model
- 20.8% of leaks appeared only in the reasoning trace, which output filters on the final answer would not see
- Self-voice payloads with tags: 42% reverse shell and 50% backdoor on MiniMax-M2.5; without tags, 8% and 10%
- Successful payloads went unmentioned in the final response in up to 100% of runs

**Concepts:** [[Agent security]] · [[Coding agents]]
**From:** [[2026-11-09]]

# My notes


---
# References
[arXiv 2611.08811](https://arxiv.org/abs/2611.08811)
