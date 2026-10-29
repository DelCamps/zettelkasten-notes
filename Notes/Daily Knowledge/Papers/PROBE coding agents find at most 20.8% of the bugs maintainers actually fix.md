---
date: 2026-10-29
section: AI
importance: High
kind: paper
source: "arXiv 2610.35987"
url: https://arxiv.org/abs/2610.35987
status: unread
id: 2026-10-29-probe-bug-finding
---
2026-10-29 07:16
Tags: #daily-knowledge #ai

---
# PROBE coding agents find at most 20.8% of the bugs maintainers actually fix

PROBE takes 20 GitHub repos frozen at the start of 2025 and uses the 2,457 bugs maintainers fixed over the next 18 months as the answer key for whole-repo bug hunting. The best agent recovers 20.8% of them, none goes above 8.1% precision, and a single plain CLI session finds under 1%. Most findings that miss the key are still real bugs (84%), but they are a different kind of bug from what maintainers fix. Tested on: 10 models from 6 providers in their vendors' CLIs, 20 repos, one multi-pass harness plus ablations and reruns.

## Details

**Caveats**
The reference set is incomplete by design: even a perfect finder would score an estimated 26-47% precision. Agents only read code; many bugs maintainers fix only surface at runtime.

**For your work**
For AI code review or bug-audit work, expect many valid but low-priority findings. Chunked multi-pass audits beat one big session by about 10x. Reruns overlap only 57-63%, so taking the union or intersection of several runs is a cheap way to trade recall against precision.

**Method**
- Reference set: bugs present in the snapshot and fixed within 18 months, mined from commits; an LLM matcher hits 99% precision and 98% recall on expert-labelled pairs
- Multi-pass harness: the repo is split into file groups, each audited in its own session with a context doc and a call graph
- An LLM judge panel, checked against a human grader, rates the findings that miss the reference set

**Problem**
Nobody had measured whether coding agents can find, across a whole repository, the bugs that maintainers would actually spend time fixing.

**Results**
- Best recall is 20.8% (GPT-5.6 Sol, high effort, $1,185 per run); precision stays at or below 8.1% for every model
- Vanilla single-session agents get under 1% recall; the prior tool Hound gets less than half the harness's recall at 8.6x the cost
- More findings explain most of the recall (r=0.94); GPT-5.6 Luna at xhigh beats Sol at medium on cost, recall and precision
- Agents over-report local logic errors (19% of findings vs 10% of fixes) and under-report missing input handling (8% vs 18%)

**Concepts:** [[Coding agents]] · [[Evals and benchmarks]]
**From:** [[2026-10-29]]

# My notes


---
# References
[arXiv 2610.35987](https://arxiv.org/abs/2610.35987)
