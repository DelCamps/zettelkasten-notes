---
date: 2026-10-31
section: AI
importance: Med
kind: paper
source: "arXiv 2610.34894"
url: https://arxiv.org/abs/2610.34894
status: unread
id: 2026-10-31-what-outcome-rl-buys
---
2026-10-31 07:16
Tags: #daily-knowledge #ai

---
# Most of what outcome RL buys is finishing within the token budget, not new reasoning

Comparing 20 released RL reasoning models with the thinking models they started from, the authors split each pass@1 gain into finishing before the budget runs out, being right once finished, and solving new problems. Where the budget binds, finishing is 82% of the change at 4k and 8k tokens; new problems add at most 2.1 points, and only 3.5% of 144 physics 'RL-only' wins held up on re-checking. Tested on: 20 released outcome-RL models (1.5B-32B) built on DeepSeek-R1-Distill-Qwen, Qwen3 and OpenMath-Nemotron bases, physics and math sets at fixed budgets, 8 samples per problem, plus one 8B controlled RL run.

## Details

**Caveats**
Thinking bases only, at most 32B; eight samples per problem; the controlled run has one seed and one model family.

**For your work**
When comparing reasoning models or effort settings, report the share of answers that finish within your token cap alongside accuracy; a model that stops sooner can look smarter.

**Method**
- Exact split of the pass@1 change into finishing, reliability and reach (net of problems only the base solves).
- Each pair read at the recipe's own training cap and the next budget above it, on 300 physics problems, MATH-500 and 276 recent contest problems.
- Problems only one model solves are resampled and read by hand; a controlled 8B run supplies the physical setup in five ways.

**Problem**
Every pass@1 is scored under a token budget, so a reported RL gain mixes answering in time, answering correctly, and genuinely new capability.

**Results**
- Given more tokens, the base closes most of the finishing gap itself.
- Where the base already finishes, the gain is reliability, even on problems both finish.
- Nine of ten new RL steps a human confirmed also appear in the base's samples.
- Hint-based recipes QuestA and KnowRL reach at most 0.018 net; supplying the setup in the 8B run did not beat plain RL.

**Concepts:** [[Post-training and RL]] · [[Evals and benchmarks]]
**From:** [[2026-10-31]]

# My notes


---
# References
[arXiv 2610.34894](https://arxiv.org/abs/2610.34894)
