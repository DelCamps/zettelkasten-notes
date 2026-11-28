---
date: 2026-11-28
section: AI
importance: Med
kind: paper
source: "Hugging Face blog (community)"
url: https://huggingface.co/blog/TonyDzi/kaper-tail-anchor-recency-bias-eval-2026-11-26
status: unread
id: 2026-11-28-tail-anchor-persona-recency
---
2026-11-28 07:16
Tags: #daily-knowledge #ai

---
# A 9-line tail anchor keeps a system persona alive in long skill files full passes rise fro

Persona rules placed only at the top of long procedural skill files faded out, which the author blames on recency bias. Repeating them in a 9-line block at the end raised full 6/6 passes from 0/28 with the header alone to 15/28 (53.6%), and the persona's verdict axis from 1/28 to 18/28. Tested on: 7 models from 7 families (GPT-6 Sol, Grok 4.3, GLM-5.3, DeepSeek V4 Pro, Qwen 3.7 Plus, MiniMax M3, Mistral Large 2512), 4 skills, 3 conditions, 84 single-turn runs.

## Details

**Caveats**
Self-reported community benchmark, not replicated. n=4 per model per condition cannot rank close models. Single-turn only, without tools; the author lists a multi-turn, tool-enabled test as a falsifier still to run.

**For your work**
- Cheap fix to try in long client system prompts and Agent Skills: restate the critical rules in a short block at the end, and add a regression eval for them.

**Method**
- Four production skills (devrel outreach, pipeline, objection handling, fundraising playbook) under three conditions: no header, top header only, header plus a 9-line tail anchor
- Six binary scoring axes per case, 504 scored axes in total
- Single-turn chat-completions harness with no tool executor, effort=medium, max_tokens=8192; the full run cost $0.9316

**Problem**
In a production agent, a strong persona defined at the top of a skill file disappeared from outputs once the skill grew long and procedural. Is a short reminder at the end enough to recover it?

**Results**
- Axes passed: 27.4% (no header), 75.0% (header only), 77.4% (header plus tail)
- Full 6/6 passes: 0/28, 0/28, 15/28
- GLM-5.3 scored 24/24 with the tail; DeepSeek V4 Pro fell to 12/24 because it emitted tool calls and stopped, and MiniMax M3 ran out of token budget

**Concepts:** [[Agents]] · [[Evals and benchmarks]]
**From:** [[2026-11-28]]

# My notes


---
# References
[Hugging Face blog (community)](https://huggingface.co/blog/TonyDzi/kaper-tail-anchor-recency-bias-eval-2026-11-26)
