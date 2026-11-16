---
date: 2026-11-15
section: AI
importance: Low
kind: paper
source: "arXiv 2611.15460"
url: https://arxiv.org/abs/2611.15460
status: unread
id: 2026-11-15-read-and-ignore-public-service
---
2026-11-15 07:16
Tags: #daily-knowledge #ai

---
# Read and Ignore given open instructions on public-service records, agents read the files i

In four expert-validated public-service scenarios (governance, healthcare, education, environment), agents mostly explore and stop; with an explicit task 86.0% produce, but only about half of those read the records first, and some reports cite figures that contradict them, including 35% of Claude-Sonnet-4.5's directed runs. Tested on: 10 models from 9 organisations, 2,400 trajectories plus 600 directed runs, bootstrap intervals and Holm-corrected tests.

## Details

**Caveats**
Mostly older or small models; static environments with no events; the rule-based taxonomy is coarser than human judgment.

**For your work**
- Before a public-sector agent pilot, run this cheap test (about $3 per model per scenario) on the client's own records, and check every figure an agent cites against the source files

**Method**
- Four static file-tree scenarios with decision levers (pending reviews, data gaps, equity shortfalls) whose correct resolution can be checked
- Ten LLMs, from 7-12B open-weight to GPT-4.1-mini, Claude-Sonnet-4 and DeepSeek-V3, under four prompt conditions; compared with 1,000 runs in a context-free sandbox
- Rule-based turn taxonomy (four raters, Fleiss kappa 0.88), checked by seven domain practitioners

**Problem**
Staff often give agents short, open instructions such as 'have a look at the proposals'. Task benchmarks leave no discretion and empty sandboxes have nothing to work on, so nobody measures what agents do with discretion over real records.

**Results**
- 84.1% of about 94k turns are exploration, a third of it re-reading
- 80.3% of open-ended runs are idle; 37% of runs that write a file write only boilerplate
- Domain context barely changes production (18.7% vs 16.0%) and cuts boundary-probing from 0.87 to 0.34 turns per run
- Claude-Sonnet-4 writes a record-contradicting file in 13.3% of open-ended runs

**Concepts:** [[Agents]] · [[Evals and benchmarks]] · [[Hallucination]]
**From:** [[2026-11-15]]

# My notes


---
# References
[arXiv 2611.15460](https://arxiv.org/abs/2611.15460)
