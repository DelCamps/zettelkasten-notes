---
date: 2026-11-09
section: AI
importance: Med
kind: value
source: "Microsoft Fabric blog"
url: https://community.fabric.microsoft.com/t5/Fabric-Updates-Blog/Build-more-connected-workflows-with-Fabric-Actions-and-Business/ba-p/5377911
status: unread
id: 2026-11-09-fabric-business-actions-pipelines
---
2026-11-09 07:16
Tags: #daily-knowledge #ai

---
# Fabric pipelines can now call Fabric operations and 25 more business apps as steps (Fabric

Microsoft Fabric Data Factory adds Fabric Actions and Business Actions activities in preview. Pipelines can run Fabric REST operations, such as notebook runs, semantic model refreshes and OneLake shortcuts, with built-in credential handling. They can also trigger steps in business apps, now with 25 additional third-party connectors for CRM, documents, e-signature, security and more.

## Details

**Availability and price**
Public preview. The post does not give pricing or regional details.

**Caveats**
Preview, so not yet for production commitments. Most of the new connectors are niche third-party apps, and the list of supported Fabric operations is still growing.

**Client use cases**
- Refresh a semantic model and notify owners once new data lands
- Generate and send contracts or invoices for e-signature straight from data pipelines
- Close the loop from data to CRM updates without custom integration code

**How we could offer it**
- Add 'data-to-action' automation to Fabric implementation projects
- Replace a client's custom API glue in pipelines with supported activities

**Pitch**
Fabric pipelines can now trigger the business step that follows the data, without custom API code. This makes our Fabric projects end in actions, not just reports.

**What it is**
These are two pipeline activities in Fabric Data Factory. Fabric Actions invokes supported Fabric REST API operations across Lakehouse, Warehouse, Notebook, Copy Job, Dataflow, Eventhouse, Eventstream, semantic models, OneLake shortcuts, Workspaces and Capacity, without hand-built REST calls or auth plumbing. Business Actions connects pipelines to business applications and adds 25 third-party connectors, including D7SMS, Formstack Documents, Pipeliner CRM, Commercient, Nitro Sign, RiskIQ and WP Connectr.

**Concepts:** [[Power BI and Fabric]]
**From:** [[2026-11-09]]

# My notes


---
# References
[Microsoft Fabric blog](https://community.fabric.microsoft.com/t5/Fabric-Updates-Blog/Build-more-connected-workflows-with-Fabric-Actions-and-Business/ba-p/5377911)
