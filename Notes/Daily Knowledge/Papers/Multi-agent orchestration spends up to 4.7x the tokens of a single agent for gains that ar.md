---
date: 2026-11-12
section: AI
importance: Low
kind: paper
source: "arXiv 2611.12953"
url: https://arxiv.org/abs/2611.12953
status: unread
id: 2026-11-12-agent-architecture-tradeoffs
---
2026-11-12 07:16
Tags: #daily-knowledge #ai

---
# Multi-agent orchestration spends up to 4.7x the tokens of a single agent for gains that ar

Holding the model, tasks and tools fixed and varying only the architecture, an Amazon team compared single-agent, skill-augmented, orchestrated and swarm designs across 13 enterprise standard operating procedures. No architecture was statistically separable in aggregate; every coordinated design spent 1.4-4.7x the tokens and 2.6-5.8x the latency of the single agent for small, rarely significant gains, making the single agent the efficient default. Implementation quality mattered more than single vs multi-agent: a redesigned orchestrator was the only arm to significantly beat the baseline (75.6% vs 67.4%). Tested on: SOP-Bench (13 enterprise SOPs, 2,124 tasks per arm), 8 architecture arms, one model family (Claude Opus 4.8, stable across Opus 4.6/4.7/4.8).

## Details

**Caveats**
One benchmark (SOP-Bench) with synthetic deterministic mock tools, and every arm runs on one model family (Claude Opus); the authors make no claim the ranking, cost multipliers or the v1-to-v2 reversal generalize across families.

**For your work**
Directly relevant to selling agent architectures to PwC clients: start with a single function-calling agent as the default, and only add orchestration or skills when a specific complex, branching SOP shows a success gain that justifies several times the token and latency cost. Skill quality, judged by a rubric, can help or quietly hurt.

**Method**
- Four designs across eight arms (function-calling single agent, skill-augmented, centralized orchestration v1/v2, triage swarm at three blueprint levels), with model, tasks and tools held fixed.
- Introduced a skill-definition quality rubric to build matched high- and low-quality skill corpora.
- Ran all arms on the 13 SOPs common to every arm (2,124 tasks each) on a pinned code revision, model fixed at Claude Opus 4.8.

**Problem**
Enterprises reach for multi-agent orchestration and skill libraries to run long, branching standard operating procedures, but there was little controlled evidence on when the extra architecture is worth its cost.

**Results**
- Per-SOP success ranged from under 10% to near 100%; no architecture was statistically separable in aggregate.
- Every coordinated arm spent 1.4-4.7x the tokens and 2.6-5.8x the latency of the single agent; gains were usually small and rarely significant, so the single agent is Pareto-optimal.
- High-quality skills lifted success to 73.1% from 67.4%, while degraded skills fell below the baseline.
- A targeted redesign (orchestration-v2: full SOP and tools per worker plus a re-dispatch round) was the only arm to significantly beat the baseline (75.6% vs 67.4%, odds ratio 1.72, p=0.007) and also the most expensive (4.7x tokens).

**Concepts:** [[Multi-agent systems]] · [[Agents]] · [[Inference efficiency]]
**From:** [[2026-11-12]]

# My notes


---
# References
[arXiv 2611.12953](https://arxiv.org/abs/2611.12953)
