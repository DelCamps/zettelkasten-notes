---
date: 2026-11-19
section: AI
importance: Med
kind: paper
source: "Anthropic research"
url: https://www.anthropic.com/research/claude-black-hole-physics
status: unread
id: 2026-11-19-claude-black-hole-physics
---
2026-11-19 07:16
Tags: #daily-knowledge #ai

---
# Claude agents, left running for about six weeks on 22 problems they picked, solved two ope

Anthropic reports that a group of Claude agents finished a 2003 calculation nobody had completed: the black-hole phase transition is abrupt even at weak coupling. The agents also proved the exact best ceiling for the simplest modular bootstrap, c/Λ with Λ about 9.1266, beating the proven c/8.5. Tested on: one model family (Claude Fable 5.2 named in the post), 22 self-proposed open problems, two solved; both write-ups merged into papers.

## Details

**Caveats**
Vendor's own post about its own model. Only 2 of 22 problems were solved, and the post does not say how the other 20 went. Neither result describes our universe, and the simplest bootstrap cannot reach c/12 on its own. Outside peer review is not described.

**For your work**
This is a concrete pattern for long-running agents: one agent per sub-problem, a shared progress board they can all read, and duplicate independent computation as the correctness check. It is worth copying for client research or analysis agents where nobody can easily verify the answer.

**Method**
- An Anthropic researcher asked Claude for open problems on black holes and the bootstrap; it returned 22 candidates hours later, and each got its own agent
- Agents could read each other's progress posts and collaborate; they ran in the background, with no special setup, for about six weeks
- For the phase transition, a small research group of Claude copies did almost every piece of the calculation twice, independently, and checked parts against the literature
- For the bootstrap, one agent spotted a pattern in published numerical results, and another, working on sphere packing, turned it into a method based on spectral curves

**Problem**
Two long-standing questions in quantum gravity. Is the Hawking-Page-like transition in N=4 super Yang-Mills abrupt or smooth at weak coupling? The calculation was set out in 2003 but never finished. And what is the lowest ceiling on the mass of the lightest black hole that the simplest modular bootstrap can prove in 3D gravity?

**Results**
- Phase transition: abrupt at weak coupling, matching Hawking and Page; a physicist later reached the same answer independently with a different method
- Bootstrap: proved M1 can be no heavier than c/Λ with Λ given by an exact formula, approximately 9.1266, and that this is the lowest this version can go
- Previous best proven ceiling was c/8.5 (Hartman, Mazáč, Rastelli); numerics had suggested about c/9.1
- The bootstrap result was delivered as four research notes, later merged into one paper

**Concepts:** [[AI for science and math]] · [[Multi-agent systems]] · [[Claude]]
**From:** [[2026-11-19]]

# My notes


---
# References
[Anthropic research](https://www.anthropic.com/research/claude-black-hole-physics)
