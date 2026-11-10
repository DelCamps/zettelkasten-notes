---
date: 2026-11-10
section: AI
importance: Low
kind: paper
source: "Hugging Face blog (community)"
url: https://huggingface.co/blog/timofeyk/borrowed-thoughts-can-a-small-model-reason-with
status: unread
id: 2026-11-10-borrowed-reasoning-traces
---
2026-11-10 07:16
Tags: #daily-knowledge #ai

---
# Borrowed thoughts a 27B model's reasoning pasted into Qwen3-8B lifts it ~30 points on code

A solo researcher pasted reasoning traces from Qwen3.8-27B into Qwen3-8B's thinking slot, so the 8B only writes the answer. This lifted it from 51.1% to 80.9% on 300 LiveCodeBench problems and from 45.4 to 63.7 EM on MuSiQue. But two 8B models fine-tuned on 2,033 of those traces wrote traces that made the executor worse (18.2% and 33.3%), and the executor followed bad reasoning as faithfully as good. Tested on: Qwen3-8B executor with Qwen3.8-27B and two LoRA-tuned 8B trace writers (one family), LiveCodeBench (300) and MuSiQue (300), 3 samples per problem with paired bootstrap CIs, one RTX 4090.

## Details

**Caveats**
Single study by one author. One model family, quantized models, and possible contamination of LiveCodeBench and MuSiQue. No speed or cost claim: generating the 27B traces took about 19.5 hours.

**For your work**
Splitting reasoning from answering (a big model plans, a small model executes) can work, but the small model follows bad reasoning without question. Check the planner's output, not just the executor's, and don't expect SFT on a few thousand traces to teach a small model to reason.

**Method**
- Three setups for Qwen3-8B: thinking switched off, its own thinking, or an outside trace placed in its thinking block, after which it writes only the answer.
- Traces came from Qwen3.8-27B or from two 8B trace writers trained with rank-64 LoRA on 2,033 filtered 27B traces.
- Code was graded with LiveCodeBench's grader in a locked-down sandbox; QA used MuSiQue's official exact-match score. 95% paired bootstrap CIs.

**Problem**
Can the reasoning step be split from the answer step, so that one model writes the reasoning and another (the executor) writes only the answer? And can a small model be trained to write that reasoning well?

**Results**
- 27B traces: +29.8 on code (CI +24.3 to +35.1) and +18.2 EM on QA. On hard problems the score rose from 20.6 to 65.7.
- Given complete traces, the 8B scores within 1 point of the 27B. The cost (-7.7) comes from traces cut off at 30k tokens.
- The code inside the 27B traces passed only 29.3% on its own, against 80.9% once the 8B wrote the final code.
- Traces from the trained 8B writers dropped the executor to 18.2% and 33.3%, against 50.0% with its own thinking (30-problem probe).

**Concepts:** [[Post-training and RL]] · [[Inference efficiency]] · [[Evals and benchmarks]]
**From:** [[2026-11-10]]

# My notes


---
# References
[Hugging Face blog (community)](https://huggingface.co/blog/timofeyk/borrowed-thoughts-can-a-small-model-reason-with)
