---
date: 2026-11-26
section: AI
importance: Med
kind: news
source: "OpenAI math preprint"
url: https://github.com/openai/math/blob/main/preprints/The-matrix-multiplication-exponent-is-nine-fourths-November-24-2026/paper.pdf
status: unread
id: 2026-11-26-openai-matrix-exponent-nine-fourths
---
2026-11-26 07:16
Tags: #daily-knowledge #ai

---
# OpenAI's AI-generated preprint claims the matrix multiplication exponent is exactly 94, a

A 111-page preprint in OpenAI's math repository, dated 24 November and written by an unreleased internal model, claims that multiplying two n×n matrices needs at least n^(9/4)/2 multiplication or division gates over every field. Combined with the 9/4 upper bound OpenAI posted on 2 October, that would make the exponent exactly 9/4, not the widely conjectured 2. It is unrefereed, and the repo says unformalised results may contain errors.

## Details

**Problem**
Researchers have long conjectured that matrices can be multiplied in close to n^2 operations (ω = 2); the best bounds came down slowly for decades, to 9/4 in OpenAI's October preprints.

**Method**
- Proves a matching lower bound for formal arithmetic circuits: at least ⌈n^(9/4)/2⌉ nonscalar multiplication or division gates for every n ≥ 2
- Argument: a faster algorithm would compress tensor networks enough to break a lower bound for testing whether entries in several independent lists are distinct
- Relies on two companion OpenAI preprints from the same day (tensor geometry; circuit lower bounds for Hamiltonian cycle and the permanent)

**Results**
- Theorem: ω = 9/4 over every field; geometric border rank of the n×n tensor is at least n^(9/4)
- Corollary: for rectangular products, 1/2 ≤ α ≤ 2/3

**Caveats**
Not peer reviewed; the paper does not say whether this result is Lean-formalised, and the repo warns unformalised results may have issues. The scope is formal arithmetic circuits. A result this large needs independent checking before anyone relies on it.

**For your work**
Mostly a capability signal: if it holds, AI-generated research mathematics has moved from new bounds to settling a major open question, which strengthens the case for AI-for-science offerings.

**Concepts:** [[AI for science and math]] · [[Frontier models]]
**From:** [[2026-11-26]]

# My notes


---
# References
[OpenAI math preprint](https://github.com/openai/math/blob/main/preprints/The-matrix-multiplication-exponent-is-nine-fourths-November-24-2026/paper.pdf)
