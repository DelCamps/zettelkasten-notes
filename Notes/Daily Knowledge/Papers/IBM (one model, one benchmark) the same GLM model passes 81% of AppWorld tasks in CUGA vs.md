---
date: 2026-11-05
section: AI
importance: Low
kind: paper
source: "Hugging Face blog (IBM Research)"
url: https://huggingface.co/blog/ibm-research/cuga-harness
status: unread
id: 2026-11-05-cuga-same-model-harness
---
2026-11-05 07:16
Tags: #daily-knowledge #ai

---
# IBM (one model, one benchmark) the same GLM model passes 81% of AppWorld tasks in CUGA vs

IBM Research ran one open-weight model, GLM-5.3-flash, through three agent harnesses on AppWorld. Its own CUGA harness passed 81.1% of tasks, Nous Research's Hermes 46.7% and LangChain's Deep Agents 30.0%. Tested on: one model, 90 AppWorld tasks, one attempt each, run by CUGA's own team.

## Details

**Caveats**
Written by the CUGA team, and CUGA used an AppWorld-specific configuration the others did not; Deep Agents needed two fixes for malformed GLM replies. One model, one benchmark, one run per task, no policy enforcement tested, and consumer apps rather than enterprise systems. Treat it as a vendor result.

**For your work**
Pairs with today's 'The Harness Is the Model' paper: when a client compares agent frameworks, fix the model and run your own task set across harnesses before choosing, rather than trusting model leaderboards.

**Method**
- One model for all runs: GLM-5.3-flash (open weights).
- Three harnesses: CUGA (IBM, open source), Hermes (Nous Research) and Deep Agents (LangChain).
- AppWorld benchmark: 90 tasks in 30 scenarios over 9 apps and 457 APIs, one attempt per task, run with the Harbor evaluation framework.

**Problem**
Agent results are usually reported per model, but the harness around the model (planning, tool handling, error recovery) can matter as much. Isolating the harness effect means holding the model fixed.

**Results**
- Task goal completion: CUGA 81.1% (73/90), Hermes 46.7% (42/90), Deep Agents 30.0% (27/90).
- Scenario completion (all 3 variants passed): CUGA 66.7%, Hermes 26.7%, Deep Agents 6.7%.
- No cost or latency figures are reported.

**Concepts:** [[Agents]] · [[Evals and benchmarks]]
**From:** [[2026-11-05]]

# My notes


---
# References
[Hugging Face blog (IBM Research)](https://huggingface.co/blog/ibm-research/cuga-harness)
