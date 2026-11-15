---
date: 2026-11-15
section: AI
importance: Med
kind: paper
source: "Ai2 blog"
url: https://allenai.org/blog/xybench
status: unread
id: 2026-11-15-ai2-xybench
---
2026-11-15 07:16
Tags: #daily-knowledge #ai

---
# Ai2's XYBench five frontier and open models answer the misguided question instead of the r

XYBench has 8,115 real questions where the user asks about a flawed approach (Y) instead of the real goal (X). On Stack Overflow questions the five models steered users to the real goal in 47-60% of answers against 79% for top human answers, even though all of them picked the goal-focused answer 71-84% of the time when shown two options. Tested on: 5 models from 5 providers (Claude Sonnet 4.6, GPT-5, Gemini 3.1 Pro, Qwen3.5-9B, DeepSeek-V4 Pro), single turn, Sonnet 4.5 as judge checked against two humans on 500 answers.

## Details

**Caveats**
English, mostly procedural problems, single turn, one response per question, and an LLM judge from one of the tested families.

**For your work**
- Add XY-style cases to client assistant evals (support, IT helpdesk): score whether the bot questions the premise, not just whether it answers.
- A judge model may rate this better than the generator produces it, so use it as a reviewer step.

**Method**
- 8,115 questions: 1,557 Stack Overflow, 184 Stack Exchange, 102 hand-curated, 6,272 generated from WikiHow guides.
- Three metrics: solution to stated vs intended request, emphasis of the answer, misconception identification.
- Claude Sonnet 4.5 judge; human agreement 97.5-100% on solution presence, 84.6-93.3% on misconception, 74.2-79.8% on emphasis.
- Oracle run giving the model the true goal; a pick-the-better-answer test.

**Problem**
Users often ask how to make a wrong approach work (the XY problem); useful assistants should spot the misconception and redirect.

**Results**
- Stack Overflow: stated-request fixes in 75-86% of answers, real-goal fixes in 59-71%.
- Answers focused mainly on the real goal: 35-41% for models vs 55% for top human answers.
- Telling Sonnet 4.6 the goal raised real-goal fixes 59% to 67% but cut misconception identification 47% to 34%.
- Judging is easier than writing: models pick the goal-focused answer 71-84% of the time.

**Concepts:** [[Evals and benchmarks]]
**From:** [[2026-11-15]]

# My notes


---
# References
[Ai2 blog](https://allenai.org/blog/xybench)
