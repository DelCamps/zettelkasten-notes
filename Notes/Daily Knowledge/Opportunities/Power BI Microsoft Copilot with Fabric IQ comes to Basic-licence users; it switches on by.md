---
date: 2026-11-24
section: AI
importance: High
kind: value
source: "Power BI blog"
url: https://community.fabric.microsoft.com/t5/Power-BI-Updates-Blog/Power-BI-November-2026-Feature-Summary/ba-p/5414287
status: unread
id: 2026-11-24-power-bi-copilot-basic-licence
---
2026-11-24 07:16
Tags: #daily-knowledge #ai

---
# Power BI Microsoft Copilot with Fabric IQ comes to Basic-licence users; it switches on by

Microsoft is extending Microsoft Copilot in Power BI and Fabric (preview) to users without an M365 Copilot Premium licence: with just a Basic licence they can ask questions grounded in Power BI semantic models through Fabric IQ. On 8 December 2026 the tenant default flips to Microsoft Copilot on and standalone Power BI Copilot off, and support for standalone Power BI Copilot on the web, Teams and mobile is planned to end by the end of January 2027.

## Details

**Availability and price**
Microsoft Copilot in Power BI and Fabric is in preview; Basic licences include Fabric IQ but not Work IQ (Premium adds Work IQ and advanced models). Default flips on 8 December 2026; standalone Power BI Copilot support planned to end by end of January 2027 (official deprecation dates to follow). The post gives no prices and does not mention EU-specific availability.

**Caveats**
- Still preview, and Microsoft says official deprecation and retirement dates are not yet announced
- Answer quality depends on the client's semantic models; poorly modelled data will give poor answers at scale
- Admin choices already made are preserved, so tenants must check what their current setting is

**Client use cases**
- Give every Power BI viewer natural-language Q&A over certified semantic models without buying Copilot Premium seats for all of them
- Plan the 8 December default change: decide per tenant whether to keep Microsoft Copilot on, and communicate it to users
- Clean up semantic models (descriptions, synonyms, measures) so Fabric IQ answers are trustworthy when thousands of Basic users start asking
- Migrate teams that rely on standalone Power BI Copilot or app-scoped Copilot before the January retirements

**How we could offer it**
- Readiness assessment: tenant settings, licence mix (Basic vs Premium), which models are 'AI-ready'
- Semantic-model hardening sprint plus an answer-quality eval set per domain, then a governed rollout
- Change management and admin runbook for the 8 December default flip; skills: Power BI modeling, Fabric admin, Copilot governance

**Pitch**
From 8 December, Microsoft Copilot switches on by default across Power BI tenants and even Basic-licence users can query semantic models with it. We can offer a short readiness and model-quality package so clients turn it on safely instead of by accident.

**What it is**
The November 2026 Power BI feature summary announces the next step in replacing standalone Power BI Copilot with Microsoft Copilot. Users with only a Basic licence get Fabric IQ inside Microsoft Copilot in the Power BI service: they can find reports by name, link or attachment, ask questions grounded in semantic models with follow-ups, and return to conversation history. Premium adds Work IQ (emails, meetings, chats, documents) and advanced model access. Report Copilot, Copilot in web modeling and the DAX query view stay. App-scoped Copilot in workspace apps is retired in January 2027.

**Concepts:** [[Power BI and Fabric]] · [[Microsoft 365 Copilot]]
**From:** [[2026-11-24]]

# My notes


---
# References
[Power BI blog](https://community.fabric.microsoft.com/t5/Power-BI-Updates-Blog/Power-BI-November-2026-Feature-Summary/ba-p/5414287)
