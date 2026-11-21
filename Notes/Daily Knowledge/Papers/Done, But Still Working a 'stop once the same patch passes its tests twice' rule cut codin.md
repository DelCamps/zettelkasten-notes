---
date: 2026-11-21
section: AI
importance: Med
kind: paper
source: "arXiv 2611.22901"
url: https://arxiv.org/abs/2611.22901
status: unread
id: 2026-11-21-done-but-still-working-stop-rule
---
2026-11-21 07:16
Tags: #daily-knowledge #ai

---
# Done, But Still Working a 'stop once the same patch passes its tests twice' rule cut codin

Replaying about 6,000 recorded SWE-bench Verified runs and scoring every intermediate patch, the authors find that after its first passing self-test, Qwen3.6-27B spends 42% of the run's cost in mini-SWE-agent and 66% in SWE-agent, and in mini-SWE-agent it usually submits the patch it already had. A twice-passed stop rule saved 23% at -1.0 points, and fine-tuning the agent to stop by itself saved 30% at -1.2 points over six seeds. Tested on: 8 open models (4 from outside the Qwen family), 2 scaffolds, SWE-bench Verified plus 7 extra repositories, preregistered tests.

## Details

**Caveats**
Open models only. The preregistered quality test did not establish non-inferiority at a 2-point margin, and a scoring-convention bug alone shifted some models by up to 7 points.

**For your work**
Measure what your agent spends after its tests pass. A twice-passed stop is a cheap thing to try, but check quality on your own scaffold. When comparing agent variants, replay the same runs instead of running fresh ones.

**Method**
- 'Anytime evaluation': replay each run's recorded commands in a sandbox, score every intermediate patch with hidden tests, and price each step, including cached tokens.
- Compare stop rules (first pass, twice passed, step caps, a learned policy) with running to the end on the same runs, which gives paired estimates.
- Split each rule's quality effect into how often it fires, how often the patch changes afterwards, and the net repair per change; then distill the rule into the agent by fine-tuning.

**Problem**
Coding agents keep testing, revising and cleaning up after their own tests pass. It was unclear how much this costs and whether stopping early hurts the final patch.

**Results**
- After the first passing self-test, Qwen3.6-27B ran 18 more commands; in mini-SWE-agent it then submitted the patch it already had in 80-87% of those runs.
- Hindsight bound: stopping at a passing self-test could save at most 25% in mini-SWE-agent and 57% in SWE-agent without losing quality.
- SWE-agent lost 2.8 points under stopping and mini-SWE-agent 0.3, because SWE-agent changed its patch after a pass in 40% of stopped runs against 10%.
- Paired comparison is 2-8 times more precise: detecting a 2-point change takes 56 tasks offline but about 1,200 online.

**Concepts:** [[Coding agents]] · [[Inference efficiency]] · [[Evals and benchmarks]]
**From:** [[2026-11-21]]

# My notes


---
# References
[arXiv 2611.22901](https://arxiv.org/abs/2611.22901)
