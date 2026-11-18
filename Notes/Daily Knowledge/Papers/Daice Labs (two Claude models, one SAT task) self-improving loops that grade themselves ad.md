---
date: 2026-11-18
section: AI
importance: Low
kind: paper
source: "Hugging Face blog"
url: https://huggingface.co/blog/daicelabs/ri-is-not-rsi
status: unread
id: 2026-11-18-ri-is-not-rsi
---
2026-11-18 07:16
Tags: #daily-knowledge #ai

---
# Daice Labs (two Claude models, one SAT task) self-improving loops that grade themselves ad

In a study of self-improving systems, loops whose own gate judged success adopted a planted unsound solver option in every lineage and lost all certified utility (-0.392), while a gate that only credits proofs accepted by an independent checker rejected it. A fixed Claude Opus 5 loop raised certified held-out utility from 0.29 to 0.79, but letting the improver rewrite itself gave only an inconclusive mean gain, and self-reported feedback produced a certified disadvantage of -0.077 despite reported gains. Tested on: SAT refutation only (CaDiCaL 3.0.1 plus DRAT-trim checker), Claude Opus 5 and Haiku 5.5 from one provider, pilot-scale lineage counts.

## Details

**Caveats**
Community article, not peer reviewed. One domain, two models from one provider, small lineage counts; the authors say it is not general evidence of effective RSI.

**For your work**
Judge any agent or prompt-optimisation loop you build by a checker the loop cannot see or edit; a self-reported score will reward a shortcut.

**Method**
- Separate recursive improvement (fixed proposer) from self-improvement (the adopted proposer makes later changes), with a protected baseline the system cannot edit.
- Domain: refuting unsatisfiable SAT formulas with CaDiCaL 3.0.1 at 4,000 conflicts; DRAT-trim checks every proof, and only accepted proofs count.
- Three pilots: a mutation rule over solver options with a planted unsound option; a fixed language-model loop rewriting a lemma program; an improver that rewrites its own source. Certified vs self-reported gates, held-out formula families.

**Problem**
Claims that AI systems 'recursively self-improve' rarely separate a better output from a better improver, and many loops grade their own progress. A review of 653 records found 28 systems with RSI structure.

**Results**
- Pilot 1: all 20+20 self-reported lineages used the planted option; certified held-out gain -0.392, versus +0.006 and +0.002 under the certified gate.
- Pilot 2: Opus 5 with a fixed improver gained +0.493 in both runs from a 0.294 start; Haiku 5.5 gained +0.044 [-0.006, +0.112].
- Pilot 3: 7 of 20 self-rewriting lineages beat the seed (5 of 14 in a pre-specified confirmation run); protected selection +0.075, mean lineage advantage inconclusive, gains concentrated on parity formulas.
- Self-reported continuation: certified -0.077 [-0.119, -0.037], 8 of 10 lineages below the seed.

**Concepts:** [[Evals and benchmarks]] · [[AI safety]] · [[Agents]]
**From:** [[2026-11-18]]

# My notes


---
# References
[Hugging Face blog](https://huggingface.co/blog/daicelabs/ri-is-not-rsi)
