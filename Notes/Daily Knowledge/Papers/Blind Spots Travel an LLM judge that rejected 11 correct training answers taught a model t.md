---
date: 2026-11-22
section: AI
importance: Med
kind: paper
source: "arXiv 2611.25191"
url: https://arxiv.org/abs/2611.25191
status: unread
id: 2026-11-22-blind-spots-travel-rl-judge
---
2026-11-22 07:16
Tags: #daily-knowledge #ai

---
# Blind Spots Travel an LLM judge that rejected 11 correct training answers taught a model t

When an LLM judge is the RL reward for 'answer or say I don't know', its knowledge of single answers hardly reaches new questions, about one corrected answer per hundred. Its doubts about a whole kind of question do: Llama-3.1-8B learned to refuse 98% of the 187 former-state capitals it knew, though with 'I don't know' blocked it still answered 94% of the refused capitals correctly. Tested on: 814 RL runs, 2 students (Qwen2.5-7B, Llama-3.1-8B), 5 open judges from 5 families plus Claude Sonnet 5.5, 3 closed-book QA datasets, 2-6 runs per cell.

## Details

**Caveats**
Short closed-book answers only, small students held close to the base model by a KL penalty, and the capitals probe is hand-built. Whether the effect carries to open-ended generation is untested. Sonnet is both a grader and part of the truth audit.

**For your work**
If you fine-tune or RL a client model with an LLM judge, check the judge's rejections by question type before training and break refusals down by type afterwards: overall accuracy and abstention rates will not show a category the model has given up.

**Method**
- GRPO with LoRA for 120 steps: reward 1 if the grader accepts, 0 if it rejects, 0.5 for 'I don't know'
- Graders: answer key, five 8-13B judges at several strictness cuts, Sonnet as judge, a judge shown the reference, and hand-edited graders to test causes
- Baseline: sample the untrained model 32 times and abstain where samples disagree
- New grader: reward the answer most of the untrained model's own samples agree on, with no labels and no judge

**Problem**
LLM judges are used as rewards where no answer key exists, on the hope that the judge's knowledge passes to the trained model. Nobody had measured what actually transfers to questions the model never trained on.

**Results**
- Even the answer key or Sonnet left students no better at choosing what to answer than the 32-sample vote rule
- Changing only 12 training verdicts on former-state capitals moved refusal from 5% to 90% at a key-matched strictness
- On 2,569 fresh questions, judges' students refused 83% of country questions Llama reliably knew, vs 42% with equally strict random rejections and 3% with the answer key
- The model's own vote came within 0.2 points of true reward (0-100 scale) averaged over six student-dataset pairs

**Concepts:** [[Post-training and RL]] · [[Evals and benchmarks]]
**From:** [[2026-11-22]]

# My notes


---
# References
[arXiv 2611.25191](https://arxiv.org/abs/2611.25191)
