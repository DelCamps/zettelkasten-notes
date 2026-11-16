---
date: 2026-11-04
section: AI
importance: Med
kind: paper
source: "Hugging Face blog (Ai2)"
url: https://huggingface.co/blog/allenai/statebench
status: unread
id: 2026-11-04-statebench
---
2026-11-04 07:16
Tags: #daily-knowledge #ai

---
# StateBench frontier models drop to 13% or lower when long documents chain state changes

Ai2's StateBench tests whether models track entities as they change through long documents, at four difficulty levels from fixed values to swaps by reference. Gemini 3.8 Flash, Claude Opus 5.5 and GPT-6 Sol and Luna handle simple overwrites but fall to 13% or lower on the longest hardest problems; small recurrent and hybrid models trained on the task generalise far beyond their training length, while transformers never learn the hardest level. Tested on: Gemini 3.8 Flash, Claude Opus 5.5, GPT-6 Sol and Luna, open Olmo 3 and Olmo Hybrid 7B plus 275M and 2.7B models, and 275M models trained from scratch.

## Details

**Caveats**
Synthetic variable-assignment tasks with a fixed number of entities; real documents introduce new entities over time, which the benchmark does not cover.

**For your work**
Do not trust a model to compute a running state (balances, ownership chains, config overrides) from a long document; have the agent extract updates into structured rows and compute state in code.

**Method**
- Four levels grounded in Krohn-Rhodes theory: r-trivial (value never changes), aperiodic (latest overwrite wins), soluble (x = x + 5 style updates), general finite (x = y, swaps).
- All four versions derive from the same assignment sequence, so only the update type changes; the same problem is also given in several formats (RULER-style, spreadsheet edits).
- Tested open pretrained models, four frontier models, and 275-million-parameter transformers, hybrids and Gated DeltaNet models trained on up to 256 assignments and tested up to 64,000.

**Problem**
Agents and RAG apps read long logs, code and contracts where values are reassigned or depend on other values; existing state-tracking tests focus only on the hardest cases.

**Results**
- All four frontier models do well on r-trivial and aperiodic, but accuracy falls to 13% or lower on the longest general finite problems.
- Pretrained open models stay at chance on general finite problems; format alone flipped small models from near ceiling to near chance.
- Trained directly, Gated DeltaNet and hybrids generalise almost perfectly on three levels out to tens of thousands of assignments; the flexible Gated DeltaNet stays near perfect to roughly 10 times its training length; transformers never learn general finite.

**Concepts:** [[Evals and benchmarks]] · [[Frontier models]]
**From:** [[2026-11-04]]

# My notes


---
# References
[Hugging Face blog (Ai2)](https://huggingface.co/blog/allenai/statebench)
