---
date: 2026-11-05
section: AI
importance: High
kind: value
source: "Microsoft Fabric blog"
url: https://community.fabric.microsoft.com/t5/Fabric-Updates-Blog/Salesforce-Data-360-integration-with-OneLake-Preview/ba-p/5384626
status: unread
id: 2026-11-05-fabric-salesforce-data360-onelake
---
2026-11-05 07:16
Tags: #daily-knowledge #ai

---
# Fabric OneLake shortcuts now reach Salesforce Data 360 query CRM data with zero copy and a

Microsoft Fabric can now mount Salesforce Data 360 Data Lake Objects as OneLake table shortcuts. The data stays in Salesforce and is queryable from lakehouse SQL, Spark, Power BI, Foundry and Data Agents with no ingestion pipeline. It is in preview.

## Details

**Availability and price**
Preview, announced 4 Nov. Needs Salesforce Data 360 with the Data Cloud Architect permission set and an edition that supports data sharing, plus a Fabric workspace with a lakehouse. Use an organizational account for prototyping and a service principal for production. No price stated.

**Caveats**
During the preview only DLOs ('_dll') are supported, not Data Model Objects, Calculated Insight Objects or schema-level shortcuts. The work needs Salesforce-side licensing and admin effort.

**Client use cases**
- Customer profitability: join Salesforce accounts and cases with finance data from ERP in a Power BI semantic model
- Churn or propensity models in Fabric notebooks or Microsoft Foundry on shared customer data
- Fabric Data Agents and Ontologies that answer questions spanning CRM and operational data
- Service investigations, for example a Salesforce case joined with shipping and returns records in Fabric

**How we could offer it**
- Salesforce-plus-Fabric '360 analytics' accelerator: share design, Entra service principal, shortcut setup, semantic model
- Retire existing Salesforce-to-lake ETL pipelines as a cost and risk reduction project

**Pitch**
Your Salesforce data, live in Fabric, with no extra copy to secure or reconcile.

**What it is**
A new 'Salesforce Data 360' table-shortcut type in Fabric lakehouses. Salesforce creates a data share of Data Lake Objects (DLOs) with a Microsoft OneLake target bound to the client's Entra tenant. Fabric then references those objects rather than copying them, so data is 'immediately available in OneLake' as it lands in Data 360.

**Concepts:** [[Power BI and Fabric]]
**From:** [[2026-11-05]]

# My notes


---
# References
[Microsoft Fabric blog](https://community.fabric.microsoft.com/t5/Fabric-Updates-Blog/Salesforce-Data-360-integration-with-OneLake-Preview/ba-p/5384626)
