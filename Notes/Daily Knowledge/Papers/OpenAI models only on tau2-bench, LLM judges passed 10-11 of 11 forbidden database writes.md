---
date: 2026-11-14
section: AI
importance: Low
kind: paper
source: "arXiv 2611.14581"
url: https://arxiv.org/abs/2611.14581
status: unread
id: 2026-11-14-tau2-evaluators-disagree
---
2026-11-14 07:16
Tags: #daily-knowledge #ai

---
# OpenAI models only on tau2-bench, LLM judges passed 10-11 of 11 forbidden database writes

Scoring 2,160 tau2-bench airline and retail episodes four ways, an LLM judge repeated its own verdicts 98.2% of the time but agreed with the benchmark's gold-state scoring only 56.2% of the time. In 11 episodes the agent made a write the policy forbids: the judge passed 10 to 11 of them, GPT-5.6 Sol still passed 6, and a simple check of whether a write was expected caught all 11. Tested on: OpenAI models only (gpt-4.1 and gpt-4.1-mini agents; gpt-4.1-mini, gpt-4.1 and GPT-5.6 Sol judges), one benchmark, 120 human-labelled episodes.

## Details

**Caveats**
One provider's models and one benchmark; one annotator is the author; the rule check needs to know per task whether a write is expected.

**For your work**
For client agents that write to systems of record, log every write and add a deterministic 'was this write expected?' check next to any LLM judge; transcript-only judges miss policy-violating writes.

**Method**
- 90 tasks x 2 agent models x 4 gate conditions x 3 repetitions = 2,160 episodes, with every database write logged.
- Four evaluators: gold-state scoring, an LLM judge, the judge given the policy document, and a 'boundary evaluator' rule check (was a write expected vs did one happen).
- Two annotators labelled 120 episodes for task correctness, policy compliance and commit correctness; verification, correction and safe-termination gates were also tested.

**Problem**
Benchmarks score agents against a gold final state, while production services usually have an LLM judge read the transcript. Practice treats the two as interchangeable.

**Results**
- Judge self-agreement 98.2%, agreement with gold-state scoring 56.2%.
- Forbidden writes in 11.1% of ungated episodes; gates did not reduce them significantly, partly because the gates' evidence digest dropped order status and customer authentication.
- Given the policy, GPT-5.6 Sol caught all 11 but failed 40 of the 55 fully correct episodes.

**Concepts:** [[Evals and benchmarks]] · [[Agents]]
**From:** [[2026-11-14]]

# My notes


---
# References
[arXiv 2611.14581](https://arxiv.org/abs/2611.14581)
