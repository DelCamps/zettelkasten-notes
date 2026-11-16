---
date: 2026-10-30
section: AI
importance: High
kind: news
source: "Mistral AI"
url: https://mistral.ai/news/mistral-large-4-oss/
status: unread
id: 2026-10-30-mistral-large-4-weights
---
2026-10-30 07:16
Tags: #daily-knowledge #ai

---
# Mistral releases the weights of Large 4, a 1-trillion-parameter open model, at $0.70$2.10

Mistral released the weights of an improved Mistral Large 4 ('Le Chonk'), a 1-trillion-parameter multimodal MoE, claiming the best open-weight coding results: 41% on Terminal-Bench 4.0 and 48% on the Artificial Analysis Coding Agent Index with 47% fewer tokens than GLM-5.3. API price is $0.70 input, $0.07 cached and $2.10 output per million tokens; it is also on Microsoft Foundry.

## Details

**Caveats**
All numbers are Mistral's; a technical report is still 'coming soon'. Mistral says it sees 'a potential for uplift to conduct real attacks' and is changing guardrails, which open weights cannot enforce.

**For your work**
A credible EU-trained open model for sovereign client deployments, available via Foundry; worth a cost run against GLM-5.3 on your agent evals, minding the MaaS licence clause.

**Method**
- Three more weeks of RL after the 6 October preview, aimed at coding and defensive security.
- Three reasoning modes: Low, Medium, High (default).
- Weights on Hugging Face under the Mistral Ecosystem Open-Weight license (modified MIT; Model-as-a-Service providers need a commercial license); deploy with vLLM or SGLang.

**Problem**
Open-weight models have trailed closed frontier models on agentic coding, and open models raise the question of cyber uplift without the provider's guardrails.

**Results**
- Terminal-Bench 4.0: 41%, up 13 points from the preview with 30% fewer output tokens.
- FrontierCode 2.0 (Cognition, private): 19.7%; Surge Code human preference ranks it behind only Claude Opus 5.5.
- Artificial Analysis Cyber Index 51%; 96.6% average refusal on malicious cyber requests; B3 Agent Security Benchmark resists 97.1% of attacks vs 93.3% in preview.
- BrowseComp 84.5%, Finch 73.3%.

**Concepts:** [[Open-weight models]] · [[Model releases and pricing]] · [[Coding agents]]
**From:** [[2026-10-30]]

# My notes


---
# References
[Mistral AI](https://mistral.ai/news/mistral-large-4-oss/)
