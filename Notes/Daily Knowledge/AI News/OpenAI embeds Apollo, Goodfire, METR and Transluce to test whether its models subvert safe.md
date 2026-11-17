---
date: 2026-11-17
section: AI
importance: Med
kind: news
source: "TechCrunch"
url: https://techcrunch.com/2026/11/16/openai-will-embed-apollo-researchers-to-investigate-ai-subversion/
status: unread
id: 2026-11-17-openai-embedded-assessments
---
2026-11-17 07:16
Tags: #daily-knowledge #ai

---
# OpenAI embeds Apollo, Goodfire, METR and Transluce to test whether its models subvert safe

OpenAI announced a first phase of embedded assessments: Apollo Research gets training code, RL rollouts with reasoning traces and intermediate checkpoints to look for models subverting alignment or control. METR and Transluce will test dangerous behaviour and OpenAI's safety evaluations; Redwood's Buck Shlegeris says the terms fall short of 'employee-like access.'

## Details

**Caveats**
Reported by TechCrunch from OpenAI's announcement; no findings yet, and no durations or budgets given.

**For your work**
Little direct use now; watch for Apollo and METR reports as evidence when clients ask how frontier agent models are vetted.

**Method**
- Apollo (paid): 'relevant training code and datasets', RL rollouts with reasoning traces and rewards, and queries to intermediate checkpoints, limited to agreed claims and models
- Goodfire (paid): interpretability tools to monitor training runs
- METR (unpaid): one evaluation for dangerous behaviour, one on whether OpenAI's systems catch it
- Transluce (unpaid): reviews post-training safety evals and, in 2027, release decisions

**Problem**
Outside evaluators usually see only finished models through an API, which can't show whether training itself encourages models to undermine safeguards.

**Results**
- Apollo can publish its conclusions, but OpenAI can limit the evidence behind them
- OpenAI may withhold information for security or IP reasons but not because it is unfavourable
- OpenAI's Safety and Security Committee reviews unredacted reports

**Concepts:** [[AI safety]] · [[Evals and benchmarks]]
**From:** [[2026-11-17]]

# My notes


---
# References
[TechCrunch](https://techcrunch.com/2026/11/16/openai-will-embed-apollo-researchers-to-investigate-ai-subversion/)
