---
date: 2026-11-21
section: AI
importance: Med
kind: value
source: "Power BI blog"
url: https://community.fabric.microsoft.com/t5/Power-BI-Updates-Blog/Power-BI-at-Ignite-Building-on-the-momentum/ba-p/5422974
status: unread
id: 2026-11-21-power-bi-desktop-for-apps
---
2026-11-21 07:16
Tags: #daily-knowledge #ai

---
# Power BI Desktop for Apps (preview) describe an app and an agent builds it on a trusted se

Power BI Desktop for Apps is now in public preview. You pick a published semantic model, describe the app you want, and an agent builds it. The app can accept inputs, keep shared state and run workflows such as target setting and approvals, and it publishes to Fabric. Semantic views, also in public preview, let teams define governed metrics, including DAX measures, directly in OneLake on the open Apache Ossie standard, which Snowflake also backs.

## Details

**Availability and price**
Public preview. Apps in Power BI come to Power BI Pro customers in the coming weeks, with Premium Per User support in the months ahead. Fabric apps is generally available. No pricing given.

**Caveats**
Preview only. Pro and PPU support is not here yet. Apache Ossie is still incubating.

**Client use cases**
- Planning apps where managers enter targets, approve them and comment in context, on existing Power BI models
- Focused team portals that bundle the reports a team uses
- Operational workflow apps that act on what reports show, not just display it
- One metric definition reused across Fabric and, over time, Snowflake

**How we could offer it**
- Turn report estates into action apps: pick high-value reports and rebuild them as input-and-approval apps
- Semantic views pilot for clients that run both Fabric and Snowflake
- Training for BI teams moving from reports to agent-built apps

**Pitch**
Your BI team can now ship working business apps, not just dashboards, on the metrics the business already trusts, without a separate app platform.

**What it is**
A new app-building mode in Power BI Desktop, powered by Fabric apps (now GA). An agent builds the app from a natural-language description, and you refine it with direct edits and a design pane. It comes with new Fabric visuals that support cross-filtering, tooltips, keyboard navigation and screen readers. Semantic views separate business definitions from compute so that metrics can be reused across engines.

**Concepts:** [[Power BI and Fabric]] · [[Agents]]
**From:** [[2026-11-21]]

# My notes


---
# References
[Power BI blog](https://community.fabric.microsoft.com/t5/Power-BI-Updates-Blog/Power-BI-at-Ignite-Building-on-the-momentum/ba-p/5422974)
