---
date: 2026-11-26
section: AI
importance: Med
kind: value
source: "OpenAI API changelog and pricing"
url: https://developers.openai.com/api/docs/pricing
status: unread
id: 2026-11-26-openai-healthcare-model-configs
---
2026-11-26 07:16
Tags: #daily-knowledge #ai

---
# OpenAI adds healthcare model configurations to the Responses API GPT-6.2 Astra and Sol wit

OpenAI released healthcare configurations of GPT-6.2 Astra, GPT-6.2 Sol, GPT-6 Astra and GPT-6.1 Sol in the Responses API. Each pairs the model with a harness tuned for clinical questions, and its web search uses a dedicated index of medical sources. The pricing page lists gpt-6.2-astra-healthcare at $8/$40 and gpt-6.2-sol-healthcare at $2/$10 per million input/output tokens.

## Details

**Availability and price**
Released in November 2026 in the Responses API (API changelog). Standard prices per million tokens (input/output): gpt-6.2-astra-healthcare $8/$40, gpt-6.2-sol-healthcare $2/$10, gpt-6-astra-healthcare $10/$50, gpt-6.1-sol-healthcare $2/$10. These match the listed prices for the corresponding general GPT-6.2 models. Regional processing (data residency) endpoints cost extra.

**Caveats**
The changelog gives no benchmarks, regions or HIPAA/BAA terms for these configurations, and the harness is not described in detail. It is not a medical device; outputs still need clinical review.

**Client use cases**
- Clinical-guideline and drug-information assistants for hospitals and insurers, with answers grounded in medical sources
- Medical-affairs and pharmacovigilance research for pharma clients
- Triage and pre-authorisation helpers where open-web search is a compliance concern

**How we could offer it**
- Assessment: compare the healthcare configuration with the base model plus the client's own RAG on their clinical questions
- Pilot: one clinical Q&A workflow with clinician review and an evaluation set
- Governance: BAA/HIPAA or EU equivalents, data residency, human-in-the-loop sign-off

**Pitch**
OpenAI now sells clinically tuned GPT-6.2 at the same price as the general model, so a healthcare client can test grounded medical answers without building a medical search index first. We can run the side-by-side evaluation and the governance.

**What it is**
New model IDs in the Responses API: gpt-6.2-astra-healthcare, gpt-6.2-sol-healthcare, gpt-6-astra-healthcare and gpt-6.1-sol-healthcare. Each combines an existing OpenAI model with a harness built for clinical questions. When these configurations call web search, they search a dedicated index of medical sources instead of the open web.

**Concepts:** [[OpenAI enterprise]] · [[Model releases and pricing]] · [[RAG]]
**From:** [[2026-11-26]]

# My notes


---
# References
[OpenAI API changelog and pricing](https://developers.openai.com/api/docs/pricing)
