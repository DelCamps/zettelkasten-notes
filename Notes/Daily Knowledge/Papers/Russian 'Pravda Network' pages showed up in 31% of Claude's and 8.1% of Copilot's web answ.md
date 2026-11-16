---
date: 2026-11-10
section: AI
importance: Med
kind: paper
source: "arXiv 2611.11727"
url: https://arxiv.org/abs/2611.11727
status: unread
id: 2026-11-10-pravda-network-chatbot-audit
---
2026-11-10 07:16
Tags: #daily-knowledge #ai

---
# Russian 'Pravda Network' pages showed up in 31% of Claude's and 8.1% of Copilot's web answ

A University of Michigan audit sent 10,000 prompts built from Pravda Network headlines to 11 chatbots through their web interfaces. Pravda pages appeared in 7.3% of all answers, and 94% of those retrievals came from You.com (35%), Claude (31%) and Copilot (8.1%). ChatGPT, Gemini and Meta AI retrieved essentially none, which suggests they block the domain. Every chatbot cited other Russian state media (median 13.56% of answers), and when Pravda was cited, the warning rate ranged from 5.3% to 76.2% (Claude 37.0%). Tested on: 11 consumer chatbots, 104,997 completed responses, 2,500 headlines x 4 prompt variants, one query per prompt, US IPs, April to July 2026.

## Details

**Caveats**
One query per prompt, English only, US IPs, and products change monthly (Mistral appeared to start blocking the domain in late April). The audit used consumer Copilot, not Microsoft 365 Copilot.

**For your work**
For client RAG and web-grounded assistants, use an explicit source allowlist or denylist and show source warnings rather than trusting the search layer. In the EU, Pravda domains have been sanctioned since July 2025, which is a compliance angle for Spanish clients.

**Method**
- 2,500 headlines randomly sampled from news-pravda.com pages in Common Crawl, each sent original or reworded, with or without a sceptical opener
- Default web settings on ChatGPT, Claude, Gemini, Grok, Le Chat, Perplexity, Qwen, DeepSeek, You.com, Copilot and Meta AI, with all cited URLs collected
- Stance and source-caveat labels by an LLM judge built from a codebook, checked on 270 human-annotated answers

**Problem**
State-aligned aggregator networks publish millions of repetitive articles, apparently to get into AI search results, but how often chatbots actually cite them was unclear.

**Results**
- Rewording the headline cut Pravda retrieval more than adding scepticism (Claude down 17.8% with rewording vs 9.8% with scepticism)
- 9.92% of headlines name a more credible outlet as their source while republishing state media ('headline washing'); on these, Claude retrieved Pravda in 28.5% of answers
- TASS was the most cited Russian state outlet for nine of the 11 chatbots
- Answers tended to agree with the headlines' claims; strong warnings grew as answers turned against a claim

**Concepts:** [[RAG]] · [[Claude]] · [[AI safety]]
**From:** [[2026-11-10]]

# My notes


---
# References
[arXiv 2611.11727](https://arxiv.org/abs/2611.11727)
