---
date: 2026-11-13
section: AI
importance: Med
kind: paper
source: "arXiv 2611.16289"
url: https://arxiv.org/abs/2611.16289
status: unread
id: 2026-11-13-satisfix-spec-satisficing
---
2026-11-13 07:16
Tags: #daily-knowledge #ai

---
# SatisFix asking coding agents to list where they bent the spec, then recheck, adds 5-7 poi

Coding agents often consider the right implementation, then talk themselves into a weaker one ('arguably not preserving, but likely acceptable'). SatisFix steps in once before the agent writes code: it asks the agent, cast as an advisor to the task maintainers, to report where it handled a requirement differently from the spec, then makes it recheck every reported choice against the task text. It lifted pass@1 by an average of 5.09 points on DeepSWE and 7.06 points on the hard subset of SWE-bench Pro. Tested on: 5 models from 5 families (GPT-5.6-Luna, DeepSeek V4 Flash, Qwen3.8-27B, Gemma 4 26B A4B, Muse Glimmer 30B), 2 harnesses (mini-swe-agent, OpenHands), 4 runs per setting on DeepSWE.

## Details

**Caveats**
It intervenes only once per task, at a time the agent itself picks. The maintainer framing tells the agent something untrue, and its effect on later messages was not measured.

**For your work**
This is cheap to copy as a hook or prompt step in Claude Code or Copilot agent workflows: before the first edit, ask the agent which requirements it is interpreting loosely and make it recheck them against the ticket.

**Method**
- Elicitation: a message framed as coming from the task maintainers asks the agent which requirements it handled differently, and why, without asking it to call anything a mistake.
- Reconsideration: the agent is put back in the developer role, lists alternatives for every reported choice, checks each against the task description and repository, then finishes the task.

**Problem**
Self-review methods such as Self-Refine ask the agent to judge its own work while it still holds the reasoning that made the weak choice look fine, so it accepts the choice again.

**Results**
- GPT-5.6-Luna on DeepSWE: 44.25% (base) to 50.22%. The best of Self-Refine, DeCRIM and ProgCo reached 46.24%.
- SatisFix cost $0.897 per task, less than half of Self-Refine, which used about 3x the input tokens of the base agent.
- DeepSeek V4 Flash: 53.32% to 57.08%, with 14.0% lower token cost. On OpenHands the gain was 4.43 points.

**Concepts:** [[Coding agents]] · [[Agents]]
**From:** [[2026-11-13]]

# My notes


---
# References
[arXiv 2611.16289](https://arxiv.org/abs/2611.16289)
