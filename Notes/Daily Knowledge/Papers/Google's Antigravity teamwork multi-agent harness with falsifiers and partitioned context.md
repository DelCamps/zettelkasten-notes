---
date: 2026-11-15
section: AI
importance: Med
kind: paper
source: "Google Research blog"
url: https://research.google/blog/advancing-science-engineering-with-antigravitys-teamwork-feature/
status: unread
id: 2026-11-15-google-teamwork-open-problems
---
2026-11-15 07:16
Tags: #daily-knowledge #ai

---
# Google's Antigravity teamwork multi-agent harness with falsifiers and partitioned context

Google Research reports results from /teamwork, an Antigravity multi-agent harness that pairs parallel exploration with checkers such as the Lean 4 proof checker and unmodified test suites, and gives each agent only the files and tools it needs. Claimed results include a full proof of the 2013 Courtade-Kumar conjecture, about 1.8 million lines of Lean formalizing the Weil conjectures, and about 800,000 lines of Rust ported from the Zircon kernel that pass all kernel unit tests. Tested on: Gemini 4 models only, many separate case studies with human experts, no controlled harness comparison.

## Details

**Caveats**
Company blog with self-reported case studies; no ablation separating harness from model, and most math results still need peer review. Some features are not yet external.

**For your work**
- Copy the two design rules in client agents: every step needs an objective checker, and reviewers get fresh context without the producer's reasoning.
- For migration work, schedule modules after dependencies compile and test against the untouched original suite.

**Method**
- Parallel candidates checked by dedicated falsifiers: Lean 4, unmodified test suites, simulators, hardware counters.
- Context partitioned by construction: each agent gets only the files and tools for its step; critics and auditors review from clean contexts.
- Declarative natural-language patterns (long proof, document review, rewrite, /boost solve-and-verify loop) routed per prompt and refined from past run transcripts.

**Problem**
Single model attempts are unpredictable and long multi-day tasks lose detail as context grows.

**Results**
- Math: Courtade-Kumar conjecture proved, formalised in Lean (50 million lines); Weil conjectures formalised in about 1.8M lines across 28,800 subagent calls.
- Chemistry: 30 agents with a spectral simulator reached 95% top-1 NMR structure match, nearly double single-agent.
- Code: libgav1 ported to about 170k lines of Rust with bit-exact parity, later 20-30% faster than the C++; DuoDiscover 4.09x geomean speedup on 17 JAXBench kernels.
- Ops: 24% less TPU preemption on some hardware via Borg scheduling changes.

**Concepts:** [[Multi-agent systems]] · [[AI for science and math]] · [[Coding agents]]
**From:** [[2026-11-15]]

# My notes


---
# References
[Google Research blog](https://research.google/blog/advancing-science-engineering-with-antigravitys-teamwork-feature/)
