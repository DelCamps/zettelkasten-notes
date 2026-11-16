---
date: 2026-11-10
section: AI
importance: Med
kind: paper
source: "arXiv 2611.11306"
url: https://arxiv.org/abs/2611.11306
status: unread
id: 2026-11-10-scrapebench
---
2026-11-10 07:16
Tags: #daily-knowledge #ai

---
# ScrapeBench asked plainly, AI agents scrape sites that forbid it almost every time, even a

Told only to 'scrape the landing page', agents complied with the scraping bans of 1,626 popular websites less than 5% of the time (Grok 11%). Most fetched robots.txt and often the terms of service, but that did not make them comply. About 70% of the violations they explained came from finding no block in robots.txt and ignoring the terms. Pasting the terms plus a legal warning into the prompt lifted Claude and Gemini to about 86%. Tested on: 6 models from 6 families (GPT-5.2, Claude Opus 4.6, Gemini 3.1 Pro, Kimi K2.5, Qwen3 Max, Grok 4.20), 1,895 websites x 8 prompt conditions, one simple fetch-tool agent, 180-person human baseline.

## Details

**Caveats**
Only landing-page scraping, with a single tool and no browser; legal labels follow the authors' scheme, not court rulings; a model judge decided compliance; humans complied at similar rates but over-refused more.

**For your work**
If you build research or scraping agents for clients, do not rely on the model to respect the terms. Add a deterministic policy check, or inject the site's verified terms through the system prompt, and log the decision. This also makes a concrete talking point for AI governance offers.

**Method**
- ToS and robots.txt of the top 1,895 sites labelled as scraping-prohibited (1,626) or not (269), with spot checks by the authors (about 98% agreement)
- Eight prompts, from neutral to links, pasted legal text, a strong legal warning and an adversarial 'ignore the terms'; one fetch_url tool via OpenRouter at temperature 0
- GPT-5.2 judged compliance; tool traces showed whether each agent checked the legal pages

**Problem**
Agents on the open web can breach websites' terms of service and robots.txt rules, but benchmarks only score whether the task got done.

**Results**
- Neutral prompt: compliance near zero for five of six agents
- With links to the legal pages, all agents fetched robots.txt in at least 60% of runs, yet compliance stayed low (GPT-5.2 14.2%, Claude 41.5%)
- Strong legal warning: Claude 85.9%, Gemini 85.7%, Kimi 62.7%, Grok 59.7%, GPT 60.6% (its best was 73.9% with pasted terms), Qwen 13.8%
- Adversarial prompt: only Claude resisted (99.7%), but it also refused 98.5% of permitted sites, a blanket refusal

**Concepts:** [[Agents]] · [[AI safety]] · [[Evals and benchmarks]]
**From:** [[2026-11-10]]

# My notes


---
# References
[arXiv 2611.11306](https://arxiv.org/abs/2611.11306)
