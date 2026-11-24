---
date: 2026-11-24
section: AI
importance: Low
kind: paper
source: "Google DeepMind blog"
url: https://deepmind.google/blog/finding-faster-quantum-algorithms-with-agents-and-formal-verification/
status: unread
id: 2026-11-24-deepmind-quantum-algorithms-lean
---
2026-11-24 07:16
Tags: #daily-knowledge #ai

---
# Google DeepMind teams of Gemini 4 agents, checked by the Lean prover, cut the cost of know

Each problem got its own team of Gemini 4 agents; every proposed improvement had to pass the Lean theorem prover before entering a shared notebook, and agents from different teams met every four hours to swap ideas. Results include an 11.8x lower computing cost for an inertial-confinement fusion simulation (5,650 to 4,338 error-corrected qubits), 8x for a light-sensitive molecule and 2.5x for cytochrome P450; the Lean library and solutions are open-sourced.

## Details

**Caveats**
- The authors say these simulations would still need more resources than the first error-corrected machines are likely to have
- Blog summary of a paper first posted earlier in November
- Gains are on Google's own cost metric

**For your work**
Little direct use, but a clear pattern to copy: pair agents with a hard verifier (tests, type checker, prover) and only let verified results into shared memory.

**Method**
- One independent team of Gemini 4 agents per problem
- Every improvement verified in Lean before it enters a shared notebook
- Agents from all teams meet every four hours in a virtual conference to exchange ideas

**Problem**
Quantum algorithms for chemistry and physics simulation need far more error-corrected qubits and operations than early fault-tolerant machines will offer. Improving them by hand is slow, and LLM-suggested optimisations are hard to trust without proof.

**Results**
- Fusion (inertial confinement): 11.8x lower computing cost; memory from 5,650 to 4,338 error-corrected qubits
- Light-sensitive molecule simulation 8x cheaper; cytochrome P450 2.5x, with qubits from 481 to 333
- A Grover implementation 2.57x faster; an arcsin state-loading routine 290x faster

**Concepts:** [[AI for science and math]] · [[Multi-agent systems]]
**From:** [[2026-11-24]]

# My notes


---
# References
[Google DeepMind blog](https://deepmind.google/blog/finding-faster-quantum-algorithms-with-agents-and-formal-verification/)
