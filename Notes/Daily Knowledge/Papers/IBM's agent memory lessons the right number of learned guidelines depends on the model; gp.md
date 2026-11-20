---
date: 2026-11-20
section: AI
importance: Med
kind: paper
source: "arXiv 2611.26361"
url: https://arxiv.org/abs/2611.26361
status: unread
id: 2026-11-20-ibm-agent-memory-dose
---
2026-11-20 07:16
Tags: #daily-knowledge #ai

---
# IBM's agent memory lessons the right number of learned guidelines depends on the model; gp

IBM describes a pipeline, now in its CUGA agent and watsonx Orchestrate, that mines short lessons from an agent's own AppWorld runs and merges them into guidelines. Strong models kept improving with the full set (DeepSeek-V3.2 +9.5 points of task completion), but weak gpt-oss-120b did better with a selected subset than with all of them. The paper also reports silent failures: a popular guideline that broke pagination, dropped provenance and a swallowed HTTP 400 that failed every task behind a plausible log. Tested on: 6 models from 5 families, one benchmark (AppWorld), mostly single runs.

## Details

**Caveats**
Mostly single runs, with differences under about five tasks treated as noise; configurations chosen on the test split; support counts measure recurrence, not correctness; no staleness or contradiction handling.

**For your work**
Treat memory size as a per-model setting, keep full guidelines and select at delivery, and add loud assertions on call counts and error codes so harness failures cannot pass as model failures.

**Method**
- An LLM extracts one to three lessons per trajectory, from both successes and failures labelled by the evaluator
- Lessons are clustered and merged into guidelines that record a support count
- Guidelines are given in full, or by retrieval: a core with support of 3 or more plus the top-k most similar
- The same model acts as agent, extractor and consolidator; open-source in altk-evolve

**Problem**
Long-horizon agents fail in repeated procedural ways (wrong pagination, wrong entity, answering when no answer is wanted). Teams want agents to learn from their own history but do not know how much memory to inject.

**Results**
- Task completion gains: GPT-5.5 92.3 to 95.2, Opus 4.6 90.5 to 94.6, DeepSeek-V3.2 79.8 to 89.3, GLM-5 flat at 87.5
- gpt-oss-120b: 39.9 baseline, 51.2 with all 199 guidelines, 55.4 (mean of two runs) with about 29 selected
- Fixing a backfiring pagination guideline by hand lifted hard-tier completion from 66.7 to 73.0
- A claimed +1.2 win over the ACE method became a tie at about one-seventh the tokens once baselines were matched

**Concepts:** [[Agent memory]] · [[Agents]] · [[Evals and benchmarks]]
**From:** [[2026-11-20]]

# My notes


---
# References
[arXiv 2611.26361](https://arxiv.org/abs/2611.26361)
