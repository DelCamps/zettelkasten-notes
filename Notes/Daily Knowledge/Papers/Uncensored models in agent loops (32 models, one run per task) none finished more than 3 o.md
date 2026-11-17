---
date: 2026-11-17
section: AI
importance: Low
kind: paper
source: "Hugging Face blog"
url: https://huggingface.co/blog/OpenUncensored/uncensored-models-agent-loops
status: unread
id: 2026-11-17-uncensored-models-agent-loops
---
2026-11-17 07:16
Tags: #daily-knowledge #ai

---
# Uncensored models in agent loops (32 models, one run per task) none finished more than 3 o

A provider of uncensored-model APIs ran 32 uncensored and abliterated models through five tool-using tasks and found they answer almost anything but often loop or crash; the original model's intelligence predicted agent reliability (correlation 0.56). Originals scoring 60 or more finished 38% of runs vs 28% for weaker ones, which looped 42% of the time. Tested on: 32 uncensored/abliterated models across several families (DeepSeek, GLM, Gemma, MiMo and others), five tasks, one run each, text-format tool calls, by a vendor with a commercial interest.

## Details

**Caveats**
One run per task, so one task equals 20 points and small gaps may be noise. Tool calls used a text format, not native function calling. The authors run the API used and have a commercial interest. Effects of abliteration vs fine-tuning on tool use are not separated.

**For your work**
Relevant to threat modelling (attackers using abliterated models in harnesses) and a reminder to add loop detection to any agent harness; little direct use for client builds.

**Method**
- 32 uncensored/abliterated models, five multi-step tasks (file editing, web browsing, calculator math, debugging until tests pass, data analysis), 14-turn cap, one run per task.
- Each run labelled finished, looped (same tool call three times without progress) or crashed.
- 36 edgy but legitimate prompts across 12 categories as a refusal test; capability taken from the originals' published GPQA Diamond and HLE scores.

**Problem**
Refusal tests say nothing about how uncensored or abliterated models behave once they are put in agent loops with tools.

**Results**
- Originals scoring 60 or more (12 models): 38% finished, 23% looped, 38% crashed; under 60 (20 models): 28% finished, 42% looped, 30% crashed.
- Eleven models looped on 3 of 5 tasks; no model finished more than 3 of 5.
- Best: GLM 5.3 Flash Uncensored, Apex Flash 1 Abliterated, Gemma 4 31B Gembrain Uncensored Heretic; versions of the same original scored within one task of each other.

**Concepts:** [[Agents]] · [[Open-weight models]] · [[Evals and benchmarks]]
**From:** [[2026-11-17]]

# My notes


---
# References
[Hugging Face blog](https://huggingface.co/blog/OpenUncensored/uncensored-models-agent-loops)
