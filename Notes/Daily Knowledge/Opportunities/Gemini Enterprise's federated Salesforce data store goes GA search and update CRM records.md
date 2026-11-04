---
date: 2026-11-04
section: AI
importance: Med
kind: value
source: "Gemini Enterprise release notes"
url: https://docs.cloud.google.com/gemini/enterprise/docs/release-notes
status: unread
id: 2026-11-04-gemini-enterprise-salesforce-federation
---
2026-11-04 07:16
Tags: #daily-knowledge #ai

---
# Gemini Enterprise's federated Salesforce data store goes GA search and update CRM records

Google made the Salesforce federated data store in Gemini Enterprise generally available. Users can search accounts, contacts, opportunities, cases, leads and custom objects from the assistant, and create, update or delete records without ingesting the data. Queries go to the Salesforce MCP server with each user's own OAuth token.

## Details

**Availability and price**
Generally available. Locations are chosen from the multi-region list, and us or eu support Google-managed or Cloud KMS keys. Billing follows Gemini Enterprise general or configurable pricing.

**Caveats**
The setup page does not say whether Salesforce record-level sharing rules are enforced, so verify this. With several federated sources, a query may go to all of them. It requires the SObject All MCP server in the Salesforce org.

**Client use cases**
- Sales teams asking about pipeline in plain language and updating opportunities from the assistant
- Service teams pulling case history alongside other connected sources
- Clients that cannot copy CRM data into another index

**How we could offer it**
- Pilot for Gemini Enterprise + Salesforce clients: read-only first, then enable write actions with approvals
- Governance: check Salesforce sharing rules, OAuth scopes and IP policies before rollout
- Skills needed: Salesforce admin, Gemini Enterprise connectors

**Pitch**
For Google-stack clients on Salesforce, Gemini Enterprise can now query and update CRM records live under each user's permissions, with no data copy. It is a low-risk sales-assistant pilot.

**What it is**
This is a Gemini Enterprise connector that federates to Salesforce instead of copying data. When a user asks something, Gemini Enterprise sends the query to the Salesforce MCP server and blends the results with other connected sources. Read actions (SOQL query, find, get schema, get related records, list recent records, get user info) are on by default. Create, update and delete actions are off by default and must be enabled by an admin. Auth is OAuth 2.0, either through a Google-managed AppExchange package or the client's own app, and every call uses the user's own access token.

**Concepts:** [[Google Cloud]] · [[Agents]]
**From:** [[2026-11-04]]

# My notes


---
# References
[Gemini Enterprise release notes](https://docs.cloud.google.com/gemini/enterprise/docs/release-notes)
