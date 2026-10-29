---
date: 2026-10-29
section: AI
importance: Med
kind: paper
source: "Anthropic research"
url: https://www.anthropic.com/research/agents-judgment-calls
status: unread
id: 2026-10-29-anthropic-judgment-calls
---
2026-10-29 07:16
Tags: #daily-knowledge #ai

---
# Anthropic RCT expert analysts adopt Claude's secretly assigned leanings 86% of the time

50 professional analysts did an hour-long causal-analysis task with Claude Code (Opus 4.8). For each of four judgment calls, a coin flip secretly set which option the agent argued for. Analysts matched the agent's lean 86% of the time (about 50% expected by chance), and 77% repeated its arguments, yet only 15% credited it. Tested on: one model, one task, 50 analysts (randomized).

## Details

**Caveats**
The agent's leans were deliberately strengthened. One domain, one model and short tasks; prior views were not recorded for everyone.

**For your work**
Human-in-the-loop review is not an independent check by default. For client decision-support agents, consider having the agent lay out all options or ask for the human's view before giving its own.

**Method**
- Fictional farm co-op case: whether to expand a program, with four open analytic choices and a final recommendation
- Hidden system-prompt instructions made the agent hold a randomly assigned lean, argue it honestly, and drop it if the evidence clearly went against it
- Choices were coded from submissions and code; a post-task survey covered ownership and confidence

**Problem**
When experts hand analysis to an agent, do they still make the open judgment calls themselves, or quietly defer to it?

**Results**
- Matching by decision: outcome 92%, method 82%, coverage 81%, weighting 90%
- Rollout was recommended 54% of the time when the agent leaned that way vs 36% otherwise
- Analysts with a prior view switched 60% of the time when the agent disagreed vs 6% when it agreed
- Non-AI analysts made serious errors 55% of the time vs 6% for AI users, but that group was less experienced

**Concepts:** [[Agents]] · [[AI safety]] · [[Claude]]
**From:** [[2026-10-29]]

# My notes


---
# References
[Anthropic research](https://www.anthropic.com/research/agents-judgment-calls)
