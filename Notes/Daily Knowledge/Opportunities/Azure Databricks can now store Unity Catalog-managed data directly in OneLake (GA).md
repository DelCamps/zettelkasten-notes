---
date: 2026-11-07
section: AI
importance: High
kind: value
source: "Microsoft Fabric Updates Blog"
url: https://community.fabric.microsoft.com/t5/Fabric-Updates-Blog/Use-OneLake-as-native-storage-for-Azure-Databricks-Generally/ba-p/5377939
status: unread
id: 2026-11-07-onelake-databricks-native-storage
---
2026-11-07 07:16
Tags: #daily-knowledge #ai

---
# Azure Databricks can now store Unity Catalog-managed data directly in OneLake (GA)

Microsoft made OneLake external-location support for Azure Databricks Unity Catalog generally available on the Fabric side. Supported managed tables, volumes, views, materialized views and streaming tables can now live in OneLake, so Databricks and Fabric work on one copy of the data. OneLake Security is on by default for these storage items.

## Details

**Availability and price**
Generally available from the Microsoft Fabric side. Needs a capacity-backed Fabric workspace. The post gives no pricing.

**Caveats**
There is no single permission model: access must be configured in both Databricks and Fabric. Only 'supported' Unity Catalog objects are covered; check the tutorial for scenarios before committing.

**Client use cases**
- Clients running both Databricks and Fabric/Power BI who keep sync pipelines and duplicate copies
- Data platform consolidation onto one physical storage layer for analytics and AI agents
- Least-privilege access design across Unity Catalog and OneLake Security

**How we could offer it**
- Fixed-scope architecture assessment: map which Databricks data should move to OneLake and which pipelines can be retired
- Implementation and identity design (managed identity or service principal, OneLake Security roles, Unity Catalog grants)
- Bundle with Fabric data agents or Copilot work on the same data

**Pitch**
Stop paying to copy the same data between Databricks and Fabric: one storage layer, both engines, controlled access.

**What it is**
A GA integration where a Unity Catalog external location points to an 'Azure Databricks Storage' item in a Fabric workspace, and a catalog or schema uses it as managed storage. Databricks keeps compute and Unity Catalog; OneLake holds the data and Fabric-side access controls.

**Concepts:** [[Power BI and Fabric]]
**From:** [[2026-11-07]]

# My notes


---
# References
[Microsoft Fabric Updates Blog](https://community.fabric.microsoft.com/t5/Fabric-Updates-Blog/Use-OneLake-as-native-storage-for-Azure-Databricks-Generally/ba-p/5377939)
