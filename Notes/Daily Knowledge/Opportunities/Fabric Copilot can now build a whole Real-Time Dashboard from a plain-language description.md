---
date: 2026-11-03
section: AI
importance: Med
kind: value
source: "Microsoft Fabric blog"
url: https://community.fabric.microsoft.com/t5/Fabric-Updates-Blog/From-a-prompt-to-an-operational-dashboard-Generate-Real-Time/ba-p/5380258
status: unread
id: 2026-11-03-fabric-rtd-copilot-generate
---
2026-11-03 07:16
Tags: #daily-knowledge #ai

---
# Fabric Copilot can now build a whole Real-Time Dashboard from a plain-language description

Microsoft Fabric has added 'Generate with Copilot (Preview)' to Real-Time Dashboards. You describe the operational view you want over an Eventhouse database. Copilot shows its plan, takes refinements in a chat, then creates an editable dashboard of KQL-backed tiles.

## Details

**Availability and price**
Preview. Requires Copilot in Fabric and data in an Eventhouse. The post does not state pricing or regions.

**Caveats**
Preview feature. Microsoft says to check the generated queries, data relationships and measure definitions before using the dashboard for operational decisions. It only works on Eventhouse (KQL) data, not general Power BI semantic models.

**Client use cases**
- Operations control rooms: footfall, queues, transport and gate load (Microsoft's stadium example)
- IoT and manufacturing line monitoring over streaming telemetry
- Fraud, payments or contact-centre live KPIs
- Quick prototypes in discovery workshops, before a full build

**How we could offer it**
- A 'live ops dashboard in a day' workshop on top of an Eventstream and Eventhouse setup
- Bundle it with Real-Time Intelligence implementation work and a validation checklist for the queries and measures Copilot produces

**Pitch**
Describe the operational question in plain words and get a working real-time dashboard on your streaming data the same day, then we harden it with you.

**What it is**
A conversational Copilot flow in Fabric Real-Time Intelligence. From an Eventhouse database you choose New Real-Time Dashboard, then Generate with Copilot. You describe the goal, signals, comparisons and layout, check how Copilot read the request, and Copilot creates a dashboard you can keep editing: visual types, queries and tiles.

**Concepts:** [[Power BI and Fabric]]
**From:** [[2026-11-03]]

# My notes


---
# References
[Microsoft Fabric blog](https://community.fabric.microsoft.com/t5/Fabric-Updates-Blog/From-a-prompt-to-an-operational-dashboard-Generate-Real-Time/ba-p/5380258)
