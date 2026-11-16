---
date: 2026-11-16
section: AI
importance: Med
kind: paper
source: "arXiv 2611.17955"
url: https://arxiv.org/abs/2611.17955
status: unread
id: 2026-11-16-webarena-pro
---
2026-11-16 07:16
Tags: #daily-knowledge #ai

---
# WebArena-Pro Claude Code with Opus 5.5 and Codex with GPT 6.1 Sol tie at 62.3% on 300 web

A new Mila-led benchmark of 300 tasks on 20 self-hosted web apps, including audio and video, finds coding-agent harnesses far ahead of generic browser agents: Claude Code with Claude Opus 5.5 and Codex with GPT 6.1 Sol both score 62.3%, while the best GenericAgent setups reach 30.3%. Tested on: 300 tasks on 20 apps; three coding-agent harnesses with models from three developers vs GenericAgent with several models.

## Details

**Caveats**
Harness, model and tools are confounded, and the shared step budget does not equalize cost; Opus 5.5 was not tested in the generic harness. Paper text and table differ on the Kimi score (60.3% vs 60.7%).

**For your work**
For browser automation, a coding-agent harness matters more than the model; budget step limits and give agents explicit media tools.

**Method**
- 300 tasks in six domains (productivity, communication, analytics, business operations, design and media, travel): 204 single-site, 96 cross-site; 221 text/vision and 79 audio/video
- Each task runs in isolation; tasks human-validated after LLM triage
- Non-omni agents get transcribe() and extract_frames(); omni models get listen() and watch()
- 50-step budget; Qwen 3.6 27B rubric judge with about 89.5% pooled human agreement

**Problem**
Reproducible web-agent benchmarks cover few app types and ignore audio and video; live benchmarks drift between runs.

**Results**
- Claude Code + Opus 5.5 and Codex + GPT 6.1 Sol: 62.3%; OpenCode + Kimi 3.1 Pro: 60.7%; GenericAgent best: 30.3% (Gemma4 31B, Gemini 3.1 Pro omni)
- Same model, different harness: Claude Opus 4.7 in GenericAgent scored 25.3%
- Media tools lifted Claude Code from 14.0% to 48.8% on media-dependent tasks
- 878 of 1,683 failed runs (52.2%) hit the 50-step limit; Codex run cost about USD 166

**Concepts:** [[Evals and benchmarks]] · [[Computer-use agents]] · [[Coding agents]]
**From:** [[2026-11-16]]

# My notes


---
# References
[arXiv 2611.17955](https://arxiv.org/abs/2611.17955)
