---
date: 2026-11-12
section: AI
importance: Med
kind: paper
source: "Hugging Face blog (Figma)"
url: https://huggingface.co/blog/figma-ai/motion-graphics-bench
status: unread
id: 2026-11-12-motiongraphicsbench
---
2026-11-12 07:16
Tags: #daily-knowledge #ai

---
# MotionGraphicsBench animating an existing SVG design, the best model (GPT-6 Astra) passes

Figma and Stanford give models a finished static SVG plus a motion prompt and ask for GSAP animation code, then grade each output with a deterministic per-task verification program. GPT-6 Astra at maximum effort leads at 67.7% pass@1, only four models top 50%, and the mean across all settings is 30.3%. The verifiers agree with human judges 93.3% of the time, against 83.3% for a GPT-6 Astra visual judge. Tested on: 32 models from 12 providers (11 families incl. GPT, Claude, Gemini, Qwen, DeepSeek, GLM), 47 model-setting combinations, 100 tasks.

## Details

**Caveats**
Only 100 expert-curated tasks and one output format (GSAP); the checkers were built with GPT-6 Astra agents, which may favour that model; human validation covers only four settings and disagreed with the checkers on 12 of 180 cases, mostly over-strict timing or geometry checks.

**For your work**
A clean pattern for grading generative UI or design output: write a programmatic checker per task and validate it against humans before trusting it, rather than using a vision model as judge.

**Method**
- 100 tasks derived from real Lottie animations (LottieAnimation-660K): each gives a complete static SVG and an edit prompt; prompts drafted by an LLM and approved by human reviewers.
- Models write GSAP JavaScript, rendered into SVG frames.
- Each task has a deterministic Python checker built by a multi-agent pipeline; a run passes only if every check passes.

**Problem**
Existing vector-graphics benchmarks (SVG-Bench, VGBench) cover static images, and text-to-animation tests mix drawing with motion, so it is hard to tell how well models add motion to a design that already exists.

**Results**
- Pass@1 ranges from 6.0% to 67.7% across 47 settings (mean 30.3%); GPT-6 Astra (max effort) is top.
- Best setting per model: proprietary average 38.8%, open-weight 21.8%; best open models GLM 5.3 (max) 39.8% and Qwen 3.8 (xhigh) 39.4%.
- Pass@32 for 15 models spans 38.0% to 95.0% (51,200 attempts), so retries help a lot.
- On 180 held-out animations the checkers reach 93.3% agreement with humans vs 83.3% for a GPT-6 Astra VLM judge; rejection recall 96.7% vs 84.4%.

**Concepts:** [[Evals and benchmarks]] · [[Frontier models]]
**From:** [[2026-11-12]]

# My notes


---
# References
[Hugging Face blog (Figma)](https://huggingface.co/blog/figma-ai/motion-graphics-bench)
