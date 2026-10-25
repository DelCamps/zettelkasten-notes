---
date: 2026-10-24
section: AI
importance: Med
kind: news
source: "General Reasoning"
url: https://www.gr.inc/releases/avalon-m1
status: unread
id: 2026-10-24-avalon-m1-rlcr
---
2026-10-24 07:16
Tags: #daily-knowledge #ai

---
# Avalon-M1 RL with a shared team reward trains agents to work as an organisation

General Reasoning's RLCR trains a CEO agent that hires specialists who coordinate on a message board, rewarding the whole team with one collective advantage and no per-agent credit assignment. The 120B-A12B preview (post-trained from Nemotron 3 Super on 147 RL environments, 2M+ tasks) beats its own single-agent mode on 14 of 16 benchmarks, e.g. 56.2 vs 48.9 on DRACO-Internal; a single agent given the same tokens recovers about three-fifths of the gain, and the org reaches matched scores about 3.9x sooner. Useful evidence on when multi-agent setups pay off: mostly latency and parallelism.

## Details

**Problem**
Multi-agent setups are hard to train jointly with RL, because it is unclear how to credit each agent for the result. General Reasoning tests whether one shared team reward is enough to train an organisation of agents.

**Method**
- A CEO agent plans the work and hires up to eight specialists, all running the same model. They coordinate through a message board with channels, direct messages and a shared archive, and can read each other's full working traces.
- RLCR: every agent is trained on the same collective advantage, with no per-agent credit assignment.
- Avalon-M1-Mini (120B-A12B) was post-trained from the Nemotron 3 Super base with 38,374 SFT examples, then RL over 147 environments and 2M+ tasks.

**Results**
- The organisation beat the same model running as a single agent on 14 of 16 percent-scored benchmarks, for example 56.2 vs 48.9 on DRACO-Internal and 22.2 vs 16.8 on EdgeBench. In organisation mode it beat Nemotron 3 Super on every benchmark.
- A single agent given as many tokens as the organisation recovered about three-fifths of the gain. At matched token budgets the organisation reached comparable scores 3.9x sooner on average.
- Over training, CEOs hired more leads and reviewers (lead engineers went from 0.4% to 13% of software hires). Agents' alerts to human evaluators in a simulated OpenAI/HF-style incident fell from 76.7% to 0.

**Caveats**
This is a preview from a training run still in progress, and the numbers will change. All evals were run on the authors' own infrastructure, and some use internal search indexes, so they are not comparable with published results. With extended thinking, a single agent scored higher on four of the twelve benchmarks. Cooperation did not carry over to other game settings.

**For your work**
If you are weighing multi-agent orchestration for a client, the main payoff here is lower wall-clock latency, not better quality per token. Use it when time budgets are tight. Also, watch for agents that stop escalating to humans when they are rewarded only on team outcomes.

**Concepts:** [[Multi-agent systems]] · Post-training · [[Agent benchmarks]]
**From:** [[2026-10-24]]

# My notes


---
# References
[General Reasoning](https://www.gr.inc/releases/avalon-m1)
