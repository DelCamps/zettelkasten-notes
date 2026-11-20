---
date: 2026-11-20
section: AI
importance: Med
kind: paper
source: "arXiv 2611.25146"
url: https://arxiv.org/abs/2611.25146
status: unread
id: 2026-11-20-everydaybench
---
2026-11-20 07:16
Tags: #daily-knowledge #ai

---
# EverydayBench on 77 live-web everyday tasks, Claude Opus 5.5 and Fable 5.1 in Claude Code

A Stanford-led benchmark of 77 human-written everyday tasks (shopping, travel, research, business, deliverables) fixes success criteria up front but lets agents pick their own answers, then checks constraints, re-fetches the pages agents cite, and grades the deliverable. Across 23 agent-model setups and 1,771 runs only 32.30% passed; Claude Code with Opus 5.5 or Fable 5.1 led at 54.55%, and raising GPT-6 Sol's effort from low to max lifted it from 29.87% to 45.45%. Tested on: 23 configurations, 5 harnesses (Claude Code, Codex, Qwen Code, Pi, Goose), one run per task.

## Details

**Caveats**
One run per task per configuration; a single LLM judge (human agreement kappa 0.644 on rubrics, 0.695 on source grounding); scores on fixed traces drift as the web changes (68.69% to 60.95% mean score after 30 days).

**For your work**
A good template for client acceptance tests of research or shopping agents: fix the criteria, not the answer, and verify citations live. The cost line is useful when arguing for a cheaper model tier.

**Method**
- 77 tasks in 8 domains, averaging 7.6 success criteria each; agents choose their own sources and outcomes
- Scoring: deterministic tests, claims checked against agent-cited pages re-fetched at evaluation time, and a 1-5 rubric judged by GPT-5.4
- A task passes only with an overall score of at least 85% and no component below 3
- 23 configurations run in Harbor 0.24.0 Docker containers

**Problem**
Live-web agent tasks often have many valid answers, and the web changes, so benchmarks with fixed answer keys miss whether an agent delivered a complete, well-supported, usable result.

**Results**
- Claude Code with Opus 5.5 and Fable 5.1: 54.55%; Codex with GPT-6.1 Sol and GPT-6 Astra: 49.35%; Claude Code with Haiku 5.5: 24.68%; Qwen Code with Qwen3.7-Plus: 9.09%
- GPT-6 Sol effort sweep: 29.87% (low), 28.57% (medium), 38.96% (high), 45.45% (max), not monotonic
- Biggest frontier-model research error: claims that say more than the cited page; 7.1% of low-cost runs produce no valid output file vs 0.3% for frontier
- Codex with GPT-5.6 Luna passes 32.47% at about $0.10 per task; GPT-6 Sol (High) costs 8.71x as much for 38.96%

**Concepts:** [[Evals and benchmarks]] · [[Agents]] · [[Claude]]
**From:** [[2026-11-20]]

# My notes


---
# References
[arXiv 2611.25146](https://arxiv.org/abs/2611.25146)
