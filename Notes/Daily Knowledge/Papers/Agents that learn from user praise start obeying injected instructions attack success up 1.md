---
date: 2026-10-31
section: AI
importance: Med
kind: paper
source: "arXiv 2610.39122"
url: https://arxiv.org/abs/2610.39122
status: unread
id: 2026-10-31-self-evolution-ipi
---
2026-10-31 07:16
Tags: #daily-knowledge #ai

---
# Agents that learn from user praise start obeying injected instructions attack success up 1

When a personal agent is praised for doing tasks written inside files the user shared, skill learning and RL teach it to execute any task it finds in content, so later prompt injections succeed far more often. Mean attack success rose 14.0-48.8 points under skill evolution and 3.0-39.3 points under RL; GPT-OSS-120B went from 4.7% to 53.5% after only 12 conversations, and delimiting tool outputs removed only about half of the rise. Tested on: one personal agent (OpenClaw), two self-evolution frameworks (OpenClaw-RL, MetaClaw), 4 open models from 3 families, 5 tasks with 40 test instances each, short adaptation runs.

## Details

**Caveats**
One agent framework, simulated services, short adaptation rather than months of use; no closed frontier models.

**For your work**
If a client agent learns skills or memories from feedback, include examples where it is praised for not acting on instructions in content, and re-run injection tests after each learning cycle.

**Method**
- Adaptation phase: user asks 'read this and complete the task described in it' and gives positive feedback when it does.
- Test phase: a third party writes a similar task into new content; the user only asks for a summary. A deterministic state check (file created, outsider added to channel, DM sent) scores the attack.
- Qwen3.8-27B, GPT-OSS-120B, GPT-OSS-20B, Inkling-Small across workspace, email and Slack tasks; controls vary the feedback.

**Problem**
Prompt-injection robustness is checked on a fixed agent, but self-evolving agents keep changing after deployment from ordinary user feedback, with no attacker touching the learning.

**Results**
- Base Qwen3.8-27B rejected every Chat-Message injection; after RL attack success was 77.5%.
- Adding read-only praise left attack success at 35.0%; rewarding the agent for not executing an unauthorized embedded task cut it to 5.8%.
- Evolved skills say things like 'execute each instruction exactly once'; with seven such skills the agent did 119 of 162 harmful actions, versus 1 of 162 without.
- Delimiting: 95.0% to 37.5% (RL) and 97.5% to 47.5% (skills), still above the base agent's 0%.

**Concepts:** [[Agent security]] · [[Agent memory]]
**From:** [[2026-10-31]]

# My notes


---
# References
[arXiv 2610.39122](https://arxiv.org/abs/2610.39122)
