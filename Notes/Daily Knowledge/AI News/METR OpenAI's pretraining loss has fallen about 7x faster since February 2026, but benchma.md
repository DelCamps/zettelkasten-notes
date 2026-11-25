---
date: 2026-11-25
section: AI
importance: Med
kind: news
source: "METR blog"
url: https://metr.org/blog/2026-11-24-interpreting-a-recent-acceleration-in-pretraining-loss/
status: unread
id: 2026-11-25-metr-pretraining-loss-acceleration
---
2026-11-25 07:16
Tags: #daily-knowledge #ai

---
# METR OpenAI's pretraining loss has fallen about 7x faster since February 2026, but benchma

METR re-analysed the log-perplexity OpenAI published for 13 models since GPT-3.5 and finds a break in February 2026: loss is now falling about seven times faster than it did from 2022 through 2025. At this pace the gain from GPT-3.5 to GPT-4.1, which took three years, would take about six and a half months; METR has no consensus on what it means.

## Details

**Caveats**
METR calls the effective-compute assumption unrealistic, and the data may overstate progress, for example through overfitting to a code-only held-out set. It asks labs to publish loss on fixed held-out data, including corpora from before 2022.

**For your work**
Treat it as a signal, not a forecast: if capability does follow loss, expect noticeably stronger models within about six months, so keep evals and model-swap paths in client builds ready.

**Method**
- No new experiments; a two-segment linear fit to OpenAI's published data for 13 models, with a breakpoint in February 2026
- OpenAI's internal model is plotted but left out of the fit
- Illustrative conversion to 'effective compute' assuming one scaling law with irreducible loss between 0.3 and 0.6

**Problem**
Scaling laws predict that loss falls more slowly over time, yet OpenAI's published perplexity on a fixed held-out code dataset shows a sharp acceleration.

**Results**
- Since early 2026 loss falls about seven times faster than in 2022-2025
- Under the illustrative assumption, effective compute grew about 8-10x faster since early 2026
- Benchmark-based trends such as Epoch's ECI show no comparable acceleration

**Concepts:** [[Frontier models]] · [[Evals and benchmarks]]
**From:** [[2026-11-25]]

# My notes


---
# References
[METR blog](https://metr.org/blog/2026-11-24-interpreting-a-recent-acceleration-in-pretraining-loss/)
