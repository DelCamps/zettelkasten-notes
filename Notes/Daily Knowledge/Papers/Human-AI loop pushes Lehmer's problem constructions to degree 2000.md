---
date: 2026-10-23
section: AI
importance: Low
kind: paper
source: "arXiv 2610.30277"
url: https://arxiv.org/abs/2610.30277
status: unread
id: 2026-10-23-lehmer-human-ai
---
2026-10-23 07:16
Tags: #daily-knowledge #ai

---
# Human-AI loop pushes Lehmer's problem constructions to degree 2000

A 5-parameter Generalized Boyd construction, found with an AI search and a symbolic verifier, gives polynomials with Mahler measure below Boyd's limit point for every even degree up to 2000. Previous systematic constructions only reached degree 180.

## Details

**Problem**
Lehmer's 1933 problem asks whether the Mahler measure of an integer polynomial can be made arbitrarily small. Small-measure irreducible polynomials had been constructed systematically only up to even degree 180, and Boyd's one-parameter family skips nearly 50% of target degrees because it factors.

**Method**
- A human researcher works with Gemini (including Gemini 4 Argon) inside Google Antigravity. The agent builds the numerical and symbolic solvers, launches distributed sweeps on Google Cloud CPU/GPU clusters, and runs exact irreducibility checks over Q separately from the fast search workers.
- Searches combine reinforcement learning, evolutionary search, priority search and periodic tilings with defects.
- Factoring cyclotomic parts out of the search optima showed 95.5% of them (d >= 30) collapse onto Boyd's two-variable polynomial, which led to a five-parameter Generalized Boyd construction that solves directly for any target even degree.

**Results**
- Verified irreducible polynomials with Mahler measure below Boyd's limit point (about 1.255434) for every even degree from 12 to 2000 (995 degrees).
- Holds 99.6% of best-known records, including every degree from 166 up.
- Beats 6 of 91 published values (degrees 178, 188, 190, 202, 242, 250) and matches 85.

**Caveats**
This does not settle Lehmer's conjecture. The constructions approach Boyd's limit point from below, and whether much smaller measures exist at high degree is still open.

**For your work**
Little direct use, though the architecture is a useful pattern for agents: keep fast candidate generation separate from an exact asynchronous verifier, so workers never stall waiting on the slow checker.

**Concepts:** [[AI for math]] · Human-AI collaboration
**From:** [[2026-10-23]]

# My notes


---
# References
[arXiv 2610.30277](https://arxiv.org/abs/2610.30277)
