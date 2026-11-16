---
date: 2026-11-12
section: AI
importance: Med
kind: value
source: "Microsoft Foundry blog"
url: https://devblogs.microsoft.com/foundry/content-understanding-adds-gpt-5-6-gpt-6-and-gpt-6-1-choose-the-right-model-for-your-workload/
status: unread
id: 2026-11-12-content-understanding-gpt-6
---
2026-11-12 07:16
Tags: #daily-knowledge #ai

---
# Azure Content Understanding adds GPT-5.6, GPT-6 and GPT-6.1; GPT-6.1 Sol is the recommende

Azure Content Understanding now supports the GPT-5.6, GPT-6 and GPT-6.1 families for document, text, speech and video extraction, with Microsoft's own benchmarks to choose between them. GPT-6 Astra edged Sol on GA document extraction (95.95% vs 95.74%) at about five times Sol's completion-token expense, so Microsoft recommends starting with GPT-6.1 Sol.

## Details

**Availability and price**
Available now in Content Understanding; check model availability per region. No list prices in the post; token expense is relative (Astra about 5x Sol, Luna much lower).

**Caveats**
Benchmarks are Microsoft's own; Preview results put Sol ahead of Astra (96.06% vs 95.58%), so 'don't assume the premium model wins'. Speech results are still under investigation. Costs exclude service processing charges.

**Client use cases**
- Invoice, contract and claims extraction with schema-only or 5-example setups
- Video analysis (ads, long recordings) where GPT-6 Sol led headline generation F1 at 86.40%
- Low-cost bulk extraction with GPT-6 Luna, which rose from 91.82% to 94.16% with five labeled examples

**How we could offer it**
- Model right-sizing review for existing Content Understanding / Document Intelligence pipelines
- A/B test harness on client documents: same analyzer and schema, only the model changes
- Combine with the agentic mode previewed on 9 November for hard multi-page documents

**Pitch**
Cut extraction cost without losing accuracy: we test the new models on your documents and pick the cheapest one that meets the bar.

**What it is**
Azure's document/media extraction service (part of Microsoft Foundry) can now run its analyzers on the newest OpenAI models. The post publishes comparative evaluations across documents, video and speech so teams can trade accuracy for cost per workload, and lets you override the model per request with the modelDeployments field.

**Concepts:** [[Structured outputs]] · [[Evals and benchmarks]] · [[Model releases and pricing]]
**From:** [[2026-11-12]]

# My notes


---
# References
[Microsoft Foundry blog](https://devblogs.microsoft.com/foundry/content-understanding-adds-gpt-5-6-gpt-6-and-gpt-6-1-choose-the-right-model-for-your-workload/)
