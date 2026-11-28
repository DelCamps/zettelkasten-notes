---
date: 2026-11-28
section: AI
importance: High
kind: value
source: "Microsoft Learn"
url: https://learn.microsoft.com/en-us/azure/search/search-document-level-access-overview
status: unread
id: 2026-11-28-foundry-iq-document-permissions-ga
---
2026-11-28 07:16
Tags: #daily-knowledge #ai

---
# Foundry IQ (formerly Azure AI Search) permission-aware retrieval is GA, trimming results t

Microsoft has made native document-level access control generally available in Foundry IQ, the new name for Azure AI Search: ADLS Gen2 ACL and RBAC scopes, standard Blob container RBAC, SharePoint ACL ingestion and push ACL ingestion all work with the 2026-10-01 REST API. Agents and search apps pass the user's Entra token in the x-ms-query-source-authorization header and only get documents that user may read. Purview sensitivity-label enforcement stays in preview.

## Details

**Availability and price**
GA with REST API 2026-10-01 for ADLS Gen2 ACL/RBAC, Blob container RBAC, SharePoint ACLs and push ACLs; Purview labels and OneLake permissions in preview. No price change stated. Check SDK changelogs: 'GA REST availability doesn't establish SDK package readiness.'

**Caveats**
ACLs are indexed snapshots, refreshed roughly daily for ADLS; 'Permission refresh doesn't provide immediate revocation.' Only default parsing modes are supported with permissions (no JSON, CSV or Markdown parsing), and image serving is unavailable when permission ingestion is on.

**Client use cases**
- Enterprise RAG and agents over SharePoint and data-lake documents where users must only see what they can open
- Replacing custom security-filter code in existing Azure AI Search solutions
- Agents in Microsoft Foundry grounding on HR, legal or finance libraries

**How we could offer it**
- Assessment: review existing client RAG apps for application-side trimming and migrate to the 2026-10-01 API
- Implementation: index ADLS Gen2 / SharePoint with permission fields projected onto every chunk
- Governance: document permission-freshness limits and test revocation paths

**Pitch**
Permission leakage is the first thing clients' security teams ask about in RAG. Microsoft now enforces source permissions in the search layer itself, GA, so we can offer a fixed-scope 'secure your RAG' migration.

**What it is**
Foundry IQ indexes permission metadata with the content (user and group IDs, container RBAC scopes, SharePoint ACLs) and filters results at query time against the delegated user's token, so RAG apps and agents built on knowledge bases no longer need hand-written security trimming.

**Concepts:** [[RAG]] · [[Agent security]]
**From:** [[2026-11-28]]

# My notes


---
# References
[Microsoft Learn](https://learn.microsoft.com/en-us/azure/search/search-document-level-access-overview)
