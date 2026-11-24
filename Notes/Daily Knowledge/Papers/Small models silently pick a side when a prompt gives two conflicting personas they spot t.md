---
date: 2026-11-24
section: AI
importance: Low
kind: paper
source: "arXiv 2611.27444"
url: https://arxiv.org/abs/2611.27444
status: unread
id: 2026-11-24-silent-arbitration-persona-conflicts
---
2026-11-24 07:16
Tags: #daily-knowledge #ai

---
# Small models silently pick a side when a prompt gives two conflicting personas they spot t

When one prompt assigns two opposing personas with equal authority, five small-to-mid-size models acknowledged the incompatibility in 72% of direct checks but surfaced it in only 22% of task responses. Dominance of one persona explained 45% of answers, and 35% of answers labelled compromises still leaned one way; prompt framing changed the visible arbitration more than paraphrasing did. Tested on: five small-to-mid models from five providers (Gemini Flash-Lite, Gemma 3 12B, GPT-4o mini, Llama 3.1 8B, Qwen3 8B), eight conflict types, English single-turn prompts.

## Details

**Caveats**
- Only small and mid-tier models, English, single turn
- Labels rely on an LLM judge
- Eight persona pairs do not cover all instruction conflicts

**For your work**
When you compose system prompts from several sources (client policy, persona, tool instructions), give explicit priority rules and test for conflicts; otherwise the model will quietly pick one without telling anyone.

**Method**
- Eight persona-conflict types grounded in published source material, each assigned jointly in one prompt
- Measure conflict acknowledgment, resolution strategy (dominance, compromise, separation, refusal) and directional stance
- Label with an LLM judge (DeepSeek-v3.2) chosen from a five-judge panel, with a GLM-5.2 re-scoring check

**Problem**
System prompts increasingly stack roles, values and style instructions that can conflict with no priority rule (for example 'act for the buyer' and 'act for the seller'). How models resolve such co-authoritative conflicts, and whether they tell the user, is rarely evaluated.

**Results**
- Conflicts acknowledged in 72% of direct checks but surfaced in only 22% of task responses
- Dominance in 45% of dual-persona responses; 35% of 'compromise' responses retain a directional lean
- Re-scoring with GLM gives a similar pattern (dominance 47%)

**Concepts:** [[Evals and benchmarks]] · [[AI safety]]
**From:** [[2026-11-24]]

# My notes


---
# References
[arXiv 2611.27444](https://arxiv.org/abs/2611.27444)
