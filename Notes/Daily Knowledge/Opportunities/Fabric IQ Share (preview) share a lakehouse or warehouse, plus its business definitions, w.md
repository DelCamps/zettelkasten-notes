---
date: 2026-11-07
section: AI
importance: Med
kind: value
source: "Microsoft Fabric Updates Blog"
url: https://community.fabric.microsoft.com/t5/Fabric-Updates-Blog/Share-data-and-context-across-organizations-with-IQ-Share/ba-p/5378764
status: unread
id: 2026-11-07-fabric-iq-share
---
2026-11-07 07:16
Tags: #daily-knowledge #ai

---
# Fabric IQ Share (preview) share a lakehouse or warehouse, plus its business definitions, w

Microsoft Fabric previewed IQ Share, which lets a producer share a whole Lakehouse, Warehouse or Mirrored Item with recipients in other Fabric tenants. Data stays in the producer's tenant via shortcuts, Markdown context files can travel with it, and producers can set expiry or revoke access. EY, TomTom, S&P Global, Financial Fabric and xMentium are named as building integrations.

## Details

**Availability and price**
Preview. Admins must enable preview tenant settings in both producer and consumer tenants. No pricing given.

**Caveats**
Shares the whole item, including future tables. Spark notebooks, semantic models, data agents and ontologies need an intermediate Lakehouse with shortcuts. Revocation or loss of the creator's access breaks downstream use.

**Client use cases**
- Time-bound sharing of an approved lakehouse with an external advisory team (the post's own 'joint financial analysis' example)
- Supplier and manufacturer data collaboration
- Data providers distributing curated data products with definitions for AI and analytics

**How we could offer it**
- Use it ourselves for engagement data exchange with clients on Fabric, with expiry tied to the engagement
- Design cross-tenant sharing governance: tenant settings, recipient checks, lifecycle and revocation tests
- Package curated data plus Markdown context for clients' data agents

**Pitch**
Share live, governed data and its meaning with partners in hours, not another pipeline and another copy.

**What it is**
Cross-tenant, zero-copy data and context sharing in Fabric. Recipients accept an invitation, get a read-only Mirrored OneLake Item with shortcuts, and query it through the SQL endpoint. New tables in a shared item show up automatically. Shares are managed from OneLake Catalog, with API and CI/CD support.

**Concepts:** [[Power BI and Fabric]]
**From:** [[2026-11-07]]

# My notes


---
# References
[Microsoft Fabric Updates Blog](https://community.fabric.microsoft.com/t5/Fabric-Updates-Blog/Share-data-and-context-across-organizations-with-IQ-Share/ba-p/5378764)
