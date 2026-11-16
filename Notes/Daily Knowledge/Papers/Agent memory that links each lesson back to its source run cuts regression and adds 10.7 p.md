---
date: 2026-11-12
section: AI
importance: Med
kind: paper
source: "arXiv 2611.14320"
url: https://arxiv.org/abs/2611.14320
status: unread
id: 2026-11-12-wikitrace-memory
---
2026-11-12 07:16
Tags: #daily-knowledge #ai

---
# Agent memory that links each lesson back to its source run cuts regression and adds 10.7 p

External memory lets agents learn from past runs, but it can also cause 'memory-induced degradation', failing tasks they would have solved without it. WikiTrace stores each distilled lesson with a link down to the summary and raw trajectory it came from, so the agent can check a lesson against its evidence before acting. It beat four prior memory methods on every suite and was the only one that never dropped below no-memory. Tested on: 8 suites across 5 agentic benchmarks (ALFWorld, ScienceWorld, PlanCraft, AppWorld, tau3-bench Retail), 3 trials each, 2 backbones from 2 families (DeepSeek-V4-Flash and GLM-5.3-flash).

## Details

**Caveats**
Memory is built from binary success/failure labels, so a lesson's diagnosis can still be wrong; the link lets the agent check but does not verify. All insights are placed in the first message, so the prompt grows with memory and retrieval at larger scale is left open. Degradation and descent labels come from an LLM judge reading the agent's stated reasoning.

**For your work**
A concrete pattern for client agents that learn from experience: keep the evidence behind each remembered rule and let the agent audit a rule before following it, and track regression separately so a memory upgrade cannot quietly break tasks that already worked.

**Method**
- Three linked layers: a concise insight links to a summary of why its run succeeded or failed, which links to the raw trajectory.
- On a new task the agent starts from all insights and, when one lacks detail, conflicts with another, or came from a failed run, descends the links with terminal tools to fill in or correct it before acting.
- Measured Gain (failures turned to successes) and Regression (successes turned to failures) separately, not just average accuracy.

**Problem**
Memory systems distil past trajectories into short lessons but hand the agent the lesson without the run it came from, so a wrong or misapplied lesson silently derails tasks the agent could otherwise solve.

**Results**
- Averaged 90.2 across eight suites versus 79.5 for no memory (+10.7 points) and beat an 'insights only' baseline by 3.2 points.
- Cut regression from 6.5% to 4.5%, and was the only memory method to match or beat no-memory on every suite.
- With a second backbone (GLM-5.3-flash) it averaged 92.7, +21.5 over no memory, while each prior method fell below no-memory on at least one suite.

**Concepts:** [[Agent memory]] · [[Agents]] · [[Evals and benchmarks]]
**From:** [[2026-11-12]]

# My notes


---
# References
[arXiv 2611.14320](https://arxiv.org/abs/2611.14320)
