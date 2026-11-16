---
date: 2026-11-12
section: AI
importance: Med
kind: news
source: "Google DeepMind blog"
url: https://deepmind.google/blog/introducing-alphaproof-code/
status: unread
id: 2026-11-12-alphaproof-code-signal
---
2026-11-12 07:16
Tags: #daily-knowledge #ai

---
# DeepMind's AlphaProof Code Gemini agents wrote over six million lines of Lean to verify Si

Google DeepMind's AlphaProof Code pairs human experts with Gemini Carbon agents to formally verify the compiled code of Signal's cryptographic protocol in Lean, writing over six million lines of proof in four weeks. Agents flagged about one percent of the codebase for human review, and the system proved two reintroduced, previously fixed bugs insecure. The verification artifacts are open-sourced.

## Details

**Caveats**
No new bugs reported; the 'first time' claims are DeepMind's own. AlphaProof Code itself is not released as a product, specifications still depend on expert review, and DeepMind says scaling it needs more research.

**For your work**
A strong signal that agent-written, machine-checked proofs are becoming practical for security-critical code. Worth watching for clients in finance or defence who need assurance on crypto or protocol code; the spec-review step is where human expertise stays essential.

**Method**
- Several models translate Signal's security goals into formal specifications; human experts review every one.
- Agents powered by Gemini Carbon write proofs in Lean, which mechanically checks each one.
- The agents audit their own proofs and flag areas for human review (about one percent of the codebase); Lean checks the rest.
- Proofs target the compiled code, e.g. that messages stay protected before and after a temporary device compromise.

**Problem**
Formal verification gives machine-checked guarantees that code meets its security goals, but writing proofs for real compiled code has taken expert teams years, so it has been limited to small components or designs rather than shipped code.

**Results**
- Over six million lines of Lean in four weeks.
- About one percent of the codebase needed human review.
- Two real, previously fixed bugs reintroduced into an isolated copy were each caught with a machine-checked proof of insecurity.
- Verification artifacts open-sourced at google-deepmind.github.io/code-verification, with a technical paper.

**Concepts:** [[AI for security]] · [[AI for science and math]] · [[Agents]]
**From:** [[2026-11-12]]

# My notes


---
# References
[Google DeepMind blog](https://deepmind.google/blog/introducing-alphaproof-code/)
