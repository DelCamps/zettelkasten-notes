---
date: 2026-11-26
section: AI
importance: Med
kind: paper
source: "arXiv 2611.34147"
url: https://arxiv.org/abs/2611.34147
status: unread
id: 2026-11-26-model-driven-context-nooa
---
2026-11-26 07:16
Tags: #daily-knowledge #ai

---
# Letting the model compact its own context (NVIDIA's NOOA harness) GPT-6.1 Sol goes from 21

NVIDIA compared two ways of compacting context. In one, the harness summarises the history when the window is 80% full. In the other, the model gets a context API and decides itself when and what to collapse into a summary. At tight budgets, models that use the API well score higher, often on fewer tokens. Usage varies a lot: GPT, Kimi and DeepSeek call the API in 42-53% of tasks, Opus 5.5 in only 4%. Tested on: 4 models from 4 families (GPT-6.1 Sol, Kimi K3, DeepSeek V4 Pro, Claude Opus 5.5), one harness (NOOA), OfficeQA Pro v2 (90 questions) and MLE-bench Lite (22 tasks), budgets from 8K to 512K tokens.

## Details

**Caveats**
Small benchmarks, and the authors say small differences may not be significant. Context pressure is simulated by shrinking the window. Only one harness was used, and on MLE-bench the effect is small. The KV-reuse result comes from one model and one engine and measures prefill compute only, not latency or cost.

**For your work**
If you add a context tool to a client agent, test it per model and pin when it should compact. A timing instruction alone changes behaviour a lot, and some models (Opus here) will ignore the tool.

**Method**
- In NOOA, the model can call collapse() to replace a range of events with its own summary. The originals are archived, and the model can fetch them back by tag.
- Baseline: at 80% of the budget, the harness summarises the history and keeps the initial instructions and the 10 most recent events.
- Context budgets are swept from 8K to 512K tokens to simulate longer tasks.
- A suffix-KV-reuse prototype in SGLang (Qwen3.6-27B) reuses the cache for unchanged text after an edit.

**Problem**
Today's harnesses compact context for the model at a fixed threshold, and that can throw away information the task still needs. Can current models manage their own context instead, and does it pay off?

**Results**
- OfficeQA Pro v2 at 32K: GPT-6.1 Sol goes from 21% to 56%.
- Kimi K3 at 32K: 41% fewer cumulative input tokens (36M vs 62M) and a slightly higher score (43% vs 41%).
- Opus 5.5 edits its context in 4% of tasks. When warned that context is running low, it usually wraps up and answers instead of compacting.
- Without the 'compact only at 85%' instruction, Kimi and DeepSeek compact far too early (Kimi at 29% of the budget at 128K), and at 128K+ they score about 8 points below the baseline.
- Suffix KV reuse cuts prefill compute by 4-15% per request, with no measurable change in accuracy.

**Concepts:** [[Agents]] · [[Agent memory]] · [[Inference efficiency]]
**From:** [[2026-11-26]]

# My notes


---
# References
[arXiv 2611.34147](https://arxiv.org/abs/2611.34147)
