---
date: 2026-11-07
section: AI
importance: Med
kind: value
source: "Google Cloud blog"
url: https://cloud.google.com/blog/products/data-analytics/query-enterprise-data-in-gemini-with-data-cloud-connectors
status: unread
id: 2026-11-07-gemini-data-cloud-connectors
---
2026-11-07 07:16
Tags: #daily-knowledge #ai

---
# Gemini for business previews Data Cloud connectors ask BigQuery, Cloud SQL and Looker ques

Google previewed Data Cloud connectors in Gemini for business: Gemini writes and runs SQL against live BigQuery, operational databases and Looker under the end user's credentials, with row- and column-level security enforced. Data is queried in place, not copied, and results can go straight into Docs, Gmail drafts or Slides.

## Details

**Availability and price**
Preview (BigQuery, Cloud SQL and Looker are labelled preview). No pricing stated; admins can set a default billing project for BigQuery query costs.

**Caveats**
Preview only. Answer quality depends on Knowledge Catalog metadata. The post gives no accuracy figures or customer results.

**Client use cases**
- Self-service answers for business users on Google Cloud data estates
- Sales and finance ad hoc questions turned into Docs or Slides
- Permission-safe access to sensitive data (salaries, health records stay restricted)

**How we could offer it**
- Pilot for Google Cloud clients: connector setup, Knowledge Catalog business context, permission testing
- Accuracy and governance evaluation before broader rollout

**Pitch**
Let business users ask the warehouse directly, while the database's own permissions keep deciding who sees what.

**What it is**
Federated query connectors that use Knowledge Catalog to find relevant data and business context, generate SQL, and run it with the user's identity. Admins set default read-only connections in the Gemini admin console. Cross-cloud queries work through BigQuery, including Iceberg, Delta Lake, Parquet and AWS S3 via the Glue federated catalog.

**Concepts:** [[Google Cloud]] · [[Agents]]
**From:** [[2026-11-07]]

# My notes


---
# References
[Google Cloud blog](https://cloud.google.com/blog/products/data-analytics/query-enterprise-data-in-gemini-with-data-cloud-connectors)
