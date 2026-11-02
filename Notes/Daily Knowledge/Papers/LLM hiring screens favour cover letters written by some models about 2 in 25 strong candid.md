---
date: 2026-11-02
section: AI
importance: Med
kind: paper
source: "arXiv 2610.41866"
url: https://arxiv.org/abs/2610.41866
status: unread
id: 2026-11-02-llm-hiring-writer-bias
---
2026-11-02 07:16
Tags: #daily-knowledge #ai

---
# LLM hiring screens favour cover letters written by some models about 2 in 25 strong candid

When the same candidate's cover letter is written by different models, evaluator models show a consistent ranking of writers: Gemini 3.5 Flash letters do best, and the two local 8B models are marked down by every evaluator, with self-preference on top. In the worst writer-evaluator pairing, about 1.8 of 25 high-fit candidates are pushed down purely by the mismatch. Tested on: 11 writer models (OpenAI, Anthropic, Google, DeepSeek, Meta), 9 evaluator models from 4 providers, 10 jobs, 50 candidates per job, 4 scoring runs each.

## Details

**Problem**
Applicants write with LLMs and employers screen with LLMs. Does the choice of model change outcomes regardless of how qualified the candidate is?

**Method**
- Real CVs and job ads; for each job, 50 CVs split into high-fit and moderate-fit tiers by embedding similarity.
- 11 writers produce 5,500 cover letters; 9 API-hosted models score them on CV only, letter only, and CV + letter.
- A per-candidate residual removes candidate quality and evaluator strictness; a rank-displacement analysis checks whether letters overturn each evaluator's own CV-only ranking.

**Results**
- As a writer, GPT-4o-mini beats its successor GPT-5-mini in the letter-only condition.
- Letter only: Claude Sonnet 4.6 is the most neutral evaluator (9.6) and Gemini 3.5 Flash the most biased (11.2). With the CV included, Gemini 3.5 Flash is the most neutral (6.3) and DeepSeek V3.2 the most biased (14.9).
- Stylistic features (semantic fit to the job ad, readability) explain the preferences, with little room left for an unmeasured writer 'fingerprint'.

**Caveats**
'Local' and 'small' are the same models by design (both around 8B), so the local penalty may simply reflect size. Fit tiers come from cosine similarity, and most models tested are mini/flash tiers.

**For your work**
For HR-screening clients (a high-risk use under the EU AI Act), audit the evaluator model across writer models, score the CV and letter together, and monitor style features rather than trusting one judge.

**Concepts:** [[Evals and benchmarks]]
**From:** [[2026-11-02]]

# My notes


---
# References
[arXiv 2610.41866](https://arxiv.org/abs/2610.41866)
