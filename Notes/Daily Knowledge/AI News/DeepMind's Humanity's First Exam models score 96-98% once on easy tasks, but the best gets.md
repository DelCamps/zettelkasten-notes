---
date: 2026-11-26
section: AI
importance: Med
kind: news
source: "Google DeepMind"
url: https://blog.google/innovation-and-ai/models-and-research/google-deepmind/humanitys-first-exam/
status: unread
id: 2026-11-26-humanitys-first-exam
---
2026-11-26 07:16
Tags: #daily-knowledge #ai

---
# DeepMind's Humanity's First Exam models score 96-98% once on easy tasks, but the best gets

Google DeepMind released Humanity's First Exam (HFE), 544 elementary text and image prompts in 136 four-prompt families, scored on whether a model answers every variant correctly on every run. The top five of 18 models reach 96-98% pass@1 but average 85.8% on this family pass^4, led by GPT-6.2 Astra at 92.4%; Claude Fable 5.2 scores 73.7%, Opus 5.5 63.0% and Gemini 3.5 Flash-Lite 18.6%. Visual perception accounts for 73% of wrong answers.

## Details

**Caveats**
Built and run by Google; prompts were filtered to make frontier models fail, so absolute scores are not a general reliability rate. Only about 20% of prompts are public. Thought-token counts are not comparable across providers.

**For your work**
Use pass^k on task variants, not pass@1, when you sign off an agent for a client workflow, and treat image reading (charts, scans, screenshots) as the weakest link.

**Method**
- 544 prompts across 20 foundational subcategories; each family has a seed plus three close variants
- Seeds had to fail at least once in four rollouts on a calibration panel (Gemini 3.1 Flash-Lite and Pro, Claude Opus 4.7, Sonnet 4.6, GPT-5.5) and pass Simplicity, Relatability and Shock Value checks
- Main metric: family pass^4, i.e. all four variants correct on all four runs; 'Family Reliability Gap' = family pass@4 minus family pass^4
- Single-turn only, no tools or agent harness

**Problem**
Standard benchmarks measure peak ability (pass@1 or pass@k) on hard tasks and hide whether a model gets simple things right every time, which is what automated workflows need.

**Results**
- Top five models: 96% to 98% pass@1 and 100% family pass@4, but family pass^4 of 80.5% to 92.4% (average 85.8%)
- Family pass^4: GPT-6.2 Astra 92.4%, GPT-6.2 Sol 86.9%, Gemini 4 Neon 85.8%, Claude Fable 5.2 73.7%, Sonnet 5.5 67.6%, Opus 5.5 63.0%, Haiku 5.5 41.6%
- Reliability gap ranges from 7.6 to 80.1 points across all 18 models
- 73% of wrong answers are visual perception, where more reasoning effort helps much less than on text and symbolic tasks

**Concepts:** [[Evals and benchmarks]] · [[Frontier models]]
**From:** [[2026-11-26]]

# My notes


---
# References
[Google DeepMind](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/humanitys-first-exam/)
