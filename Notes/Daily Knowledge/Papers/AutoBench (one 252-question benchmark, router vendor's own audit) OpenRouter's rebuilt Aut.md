---
date: 2026-11-18
section: AI
importance: Low
kind: paper
source: "Hugging Face blog"
url: https://huggingface.co/blog/PeterKruger/openrouters-new-auto-router-is-worse-than-the-old
status: unread
id: 2026-11-18-openrouter-auto-router-audit
---
2026-11-18 07:16
Tags: #daily-knowledge #ai

---
# AutoBench (one 252-question benchmark, router vendor's own audit) OpenRouter's rebuilt Aut

Rescoring routers on the same frozen set of long open-ended questions, AutoBench found OpenRouter's new Auto Router (shipped 6 November) at 65.2% at its high setting versus 79.1% for the previous version, with default, low and medium at or below a random pick. Conifer (74.8%) and dari (79.1%) also failed to beat always calling GPT-5.6 Luna (85.3% at $0.0043 per question), while the author's own AutoBench Router scored 86.8-88.6%. Tested on: one 252-question benchmark of long open-ended questions, one freeze date, a 20-model pool; the author sells the winning router.

## Details

**Caveats**
Strong conflict of interest: the author builds and sells the top router, and the post is partly an ad. One benchmark and one date; routers see different pool sizes; the dari chat path matched its select-only path on only 18% of 50 prompts.

**For your work**
Before putting a router in a client architecture, test it against a fixed-model baseline and random-in-pool on the client's own prompts; a vendor change behind the same slug can quietly drop quality.

**Method**
- Same frozen question set as an October audit (252 questions, 20-model pool), scored with a quality metric called Delta-Hit and billed cost per question.
- Routers: new OpenRouter Auto Router (four settings), Conifer, dari and the author's AutoBench Router; baselines are always-Luna, always-Sol and random-in-pool.
- 95% percentile intervals from 10,000 bootstrap resamples; a Router Index at beta = 0.2 combines quality and cost.

**Problem**
Commercial LLM routers promise to pick the right model per request, but may not beat always calling one mid-priced model, or a random pick from their own pool.

**Results**
- New Auto Router: high 65.2%, default 58.1%, low 60.3%, medium 57.9%; it agrees with the previous router on only 1-12% of picks, and the first listed candidate wins about 82-88% of the time.
- Conifer 74.8% at $0.0052, +14.6 over random in its 17 models; dari 79.1%, but random in its 8 models already scores 73.9% (+5.2).
- Router Index: Luna 56.1, dari 39.3, Conifer 30.5, new Auto high 1.6; AutoBench Router 60.8 / 60.3 / 59.8.

**Concepts:** [[Evals and benchmarks]] · [[Model releases and pricing]] · [[Inference efficiency]]
**From:** [[2026-11-18]]

# My notes


---
# References
[Hugging Face blog](https://huggingface.co/blog/PeterKruger/openrouters-new-auto-router-is-worse-than-the-old)
