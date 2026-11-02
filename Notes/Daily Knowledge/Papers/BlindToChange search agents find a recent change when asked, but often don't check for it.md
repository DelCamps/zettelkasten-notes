---
date: 2026-11-02
section: AI
importance: High
kind: paper
source: "arXiv 2610.41435"
url: https://arxiv.org/abs/2610.41435
status: unread
id: 2026-11-02-blindtochange
---
2026-11-02 07:16
Tags: #daily-knowledge #ai

---
# BlindToChange search agents find a recent change when asked, but often don't check for it

When a request names a recent event (e.g. a person's death), agents almost always get it right; when the event only matters implicitly (recommend a speaker), they often recommend the dead person. On deaths, the median gap in the providers' own harnesses is 40.5 points at low effort and 27.5 at high effort, and in 13 of the 15 configurations over 75% of these failures come from the agent never searching to check. Tested on: 8 frontier models from 8 providers, native and shared search harnesses, low and high reasoning effort, up to 200 probes per model per event type, two event types.

## Details

**Problem**
Search benchmarks like BrowseComp state what must be found. Real requests ('plan my trip') leave the agent to notice which of its own assumptions may be out of date.

**Method**
- Events after each model's knowledge cutoff are pulled automatically from Wikidata (deaths and ends of official tenures), so the benchmark can be refreshed.
- Each event gets a direct probe (asks about it) and an indirect probe (a recommendation request where the event rules out an obvious candidate); only probes where the model named that candidate without search are kept.
- Every model runs in its provider's native search harness where one exists, and in a shared Inspect AI harness with one Exa search tool and a system prompt telling it to search before time-sensitive answers.

**Results**
- Direct accuracy on deaths is at least 96.5% in nearly all configurations; indirect accuracy is lower in every configuration but one.
- Claude-Opus-4.7 shows the largest gap, 70.0 points (shared harness, low effort); it issues no search on 23% of death probes at high effort, against under 8% for other models.
- GPT-5.4 at low effort issues no search for 58.5% of death probes; at high effort it searches on 97.5% and beats every other model.
- Tenures show smaller median gaps (18.7 and 15.0 points), apparently because models check office-holders more readily.

**Caveats**
Only two event types, both about public figures. Answers are graded by whether the ruled-out candidate is left out of a long answer. The authors only speculate that a 'verify your assumptions' prompt would help; they did not test it.

**For your work**
Search or RAG agents for clients will repeat stale facts unless verification is built in. Add an explicit 'list and check time-sensitive assumptions' step, and add indirect probes to eval suites, since BrowseComp-style scores don't measure this.

**Concepts:** [[Agents]] · [[Evals and benchmarks]] · [[RAG]]
**From:** [[2026-11-02]]

# My notes


---
# References
[arXiv 2610.41435](https://arxiv.org/abs/2610.41435)
