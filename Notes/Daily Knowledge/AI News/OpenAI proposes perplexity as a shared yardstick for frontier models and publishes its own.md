---
date: 2026-11-23
section: AI
importance: Med
kind: news
source: "OpenAI"
url: https://openai.com/index/perplexity-and-intelligence/
status: unread
id: 2026-11-23-openai-perplexity-common-limits
---
2026-11-23 07:16
Tags: #daily-knowledge #ai

---
# OpenAI proposes perplexity as a shared yardstick for frontier models and publishes its own

OpenAI chief scientist Jakub Pachocki proposes that frontier labs compare models by pretraining perplexity and agree 'common limits' they won't cross until monitoring milestones are reached. OpenAI published its internal log-perplexity numbers: about 0.99 for GPT-3.5, 0.91 for GPT-4, below 0.8 for current models, and an expected next window of about 0.68-0.7.

## Details

**Caveats**
OpenAI itself notes perplexity is hard to compare across labs, does not measure tasks directly and ignores chain-of-thought gains. A proposal, not an agreement.

**For your work**
Useful context for client AI-risk discussions, but it does not change model choice: keep evaluating on your own tasks.

**Method**
- Use perplexity (cross-entropy loss) on a lab's main evaluation set as a common metric for comparing developers and informing safety standards
- Labs jointly set norms for pre-deployment evaluation, red-teaming of safety cases and transparency
- Agree limits based on perplexity and other measurements, not to be crossed until a concrete monitoring milestone, such as a successor to chain-of-thought monitors, is reached

**Problem**
There is no shared, hard-to-game measure for how capable a lab's newest model is, which makes coordinated safety limits hard to set.

**Results**
- OpenAI log-perplexity on its main internal set: GPT-3.5 about 0.99, GPT-4 about 0.91, current models below 0.8
- A model at about 0.76 produced notable results on open math problems; next window expected at about 0.68-0.7
- OpenAI says its loss curve accelerated steeply in 2026, mostly from long-term research and compute, less from AI automation

**Concepts:** [[AI safety]] · [[Frontier models]]
**From:** [[2026-11-23]]

# My notes


---
# References
[OpenAI](https://openai.com/index/perplexity-and-intelligence/)
