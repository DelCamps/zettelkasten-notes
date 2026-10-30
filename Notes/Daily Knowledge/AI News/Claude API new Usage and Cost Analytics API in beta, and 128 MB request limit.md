---
date: 2026-10-30
section: AI
importance: Med
kind: news
source: "Claude Platform release notes"
url: https://platform.claude.com/docs/en/release-notes/overview
status: unread
id: 2026-10-30-claude-usage-cost-analytics-api
---
2026-10-30 07:16
Tags: #daily-knowledge #ai

---
# Claude API new Usage and Cost Analytics API in beta, and 128 MB request limit

Anthropic launched the Usage and Cost Analytics API in beta on 29 October, reporting token usage and cost by model, workspace, API key and the user or service account behind each request; the old Usage and Cost API becomes legacy but stays supported. A day earlier the maximum Messages API request size rose from 32 MB to 128 MB on the first-party API.

## Details

**Caveats**
Beta; data is not real-time and values can be revised after month end. The larger request limit does not apply to Bedrock, Vertex or Foundry.

**For your work**
Useful for per-client chargeback on shared Claude orgs: group by actor or API key instead of maintaining your own token logging.

**Method**
- Two endpoints: /v1/organizations/analytics/usage and /v1/organizations/analytics/cost, behind the analytics-usage-cost-2026-08-24 beta header and an Admin API key.
- Results can be filtered and grouped by model, workspace, API key and an 'actor' dimension (user, service account, federated cloud identity or the key itself), in daily, hourly or per-minute buckets.
- Covers Claude Console and Claude Enterprise organizations; migration guides from the legacy endpoints are provided.

**Problem**
Teams running Claude across many apps, keys and people have struggled to attribute spend to whoever actually made a request, and large multimodal or long-document requests hit the request-size cap.

**Results**
- The Usage and Cost API and the Enterprise usage_report, cost_report, user_usage_report and user_cost_report endpoints are now legacy but remain supported.
- Messages API and Token Counting API maximum request size raised from 32 MB to 128 MB (first-party API only).

**Concepts:** [[Claude]] · [[Model releases and pricing]]
**From:** [[2026-10-30]]

# My notes


---
# References
[Claude Platform release notes](https://platform.claude.com/docs/en/release-notes/overview)
