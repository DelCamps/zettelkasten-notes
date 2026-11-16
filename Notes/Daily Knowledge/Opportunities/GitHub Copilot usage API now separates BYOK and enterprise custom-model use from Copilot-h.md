---
date: 2026-11-05
section: AI
importance: Low
kind: value
source: "GitHub changelog"
url: https://github.blog/changelog/2026-11-03-byok-and-enterprise-custom-models-in-the-copilot-usage-api
status: unread
id: 2026-11-05-copilot-usage-api-byok
---
2026-11-05 07:16
Tags: #daily-knowledge #ai

---
# GitHub Copilot usage API now separates BYOK and enterprise custom-model use from Copilot-h

Copilot's usage metrics API now reports bring-your-own-key and local-model use (for example Ollama or LM Studio) separately, and flags admin-configured enterprise custom models. Before this, that usage was blended into Copilot-hosted totals.

## Details

**Availability and price**
Live 3 Nov for owners, billing managers and roles with 'View Copilot Metrics'. The Copilot usage metrics policy must be on. No extra cost.

**Caveats**
Local BYOK numbers are a lower bound because they depend on client telemetry and some providers don't report tokens. Enterprise custom-model counts are observed server-side and more complete. There is no backfill for earlier days.

**Client use cases**
- Check compliance with BYOK and local-model policies across a developer estate
- Attribute AI coding cost across Copilot-hosted models and the client's own Azure OpenAI, Anthropic or local keys
- Compare adoption across tools and models for AI-SDLC ROI reporting

**How we could offer it**
- Add the fields to a Copilot adoption and FinOps dashboard in Power BI
- Use them as evidence in AI governance reviews of developer tooling

**Pitch**
See which coding-agent traffic goes to your own keys and models, not just to Copilot's.

**What it is**
New fields in the Copilot usage metrics API. 'used_local_byok' and 'totals_by_local_byok' cover keys or local models that developers configure in Copilot CLI or the Copilot app. An 'is_custom_enterprise_model' flag in 'totals_by_client' covers custom models that admins configure in GitHub and that route through GitHub to the provider.

**Concepts:** [[GitHub Copilot]]
**From:** [[2026-11-05]]

# My notes


---
# References
[GitHub changelog](https://github.blog/changelog/2026-11-03-byok-and-enterprise-custom-models-in-the-copilot-usage-api)
