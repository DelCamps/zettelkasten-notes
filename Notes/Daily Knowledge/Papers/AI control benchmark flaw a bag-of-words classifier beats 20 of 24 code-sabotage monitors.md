---
date: 2026-11-02
section: AI
importance: Med
kind: paper
source: "arXiv 2610.41713"
url: https://arxiv.org/abs/2610.41713
status: unread
id: 2026-11-02-control-monitor-shortcuts
---
2026-11-02 07:16
Tags: #daily-knowledge #ai

---
# AI control benchmark flaw a bag-of-words classifier beats 20 of 24 code-sabotage monitors

On the standard APPS backdoor split, a TF-IDF classifier reaches AUROC 0.806 against a median monitor score of 0.610. It can do this because people wrote the honest code and older models wrote the backdoors, and because problems with backdoors have about half as many tests (20.95 vs 38.85). After invalid backdoors are removed, the apparent gap in how often a Sonnet 5 monitor catches older models' backdoors versus Sonnet 5's shrinks from 0.40 to 0.17. Tested on: one dataset (APPS backdoor), published scores of 24 open-weight monitors (0.4B-32B), two zero-shot Claude monitors run by the authors, one attacking model.

## Details

**Caveats**
The authors do not show that published monitors actually use these shortcuts. They ran only two monitors themselves, with one attack prompt, and the attacker results rest on 54-99 problems.

**For your work**
When you evaluate or sell a guardrail or monitor, report trivial baselines and shuffled-label scores next to it, and make sure both classes come from the same author.

**Method**
- Baselines that never run the code: bag-of-words logistic regression, and a 'no-code' classifier on three problem facts (difficulty, number of tests, statement length), each checked against 1,000 label shuffles.
- Rebuilt pairs where one model (Claude Sonnet 5 or Haiku 4.5) writes both classes, then swapped one class at a time to isolate the effect of authorship.
- Backdoor validity checks: is the trigger a legal input, and is the output actually wrong there?

**Problem**
AI-control monitors are scored on how well they separate honest from backdoored code. If the dataset leaks its labels, a high score proves little about catching sabotage.

**Results**
- The no-code classifier also beats 20 monitors (0.766).
- Bag-of-words scores 0.953 on human-honest vs Sonnet 5 backdoors, against 0.789 on the original pairs: it rewards a difference in authors.
- 17 of the 172 test backdoors have only an illegal trigger and 7 fail a public test. A Sonnet 5 monitor's catch rate goes from 77% vs 37% before the checks to 78% vs 61% after.
- Character count alone separates the classes in four of five agentic ControlArena settings (up to 0.802).

**Concepts:** [[AI safety]] · [[Evals and benchmarks]]
**From:** [[2026-11-02]]

# My notes


---
# References
[arXiv 2610.41713](https://arxiv.org/abs/2610.41713)
