---
date: 2026-11-23
section: AI
importance: Low
kind: value
source: "AWS What's New"
url: https://aws.amazon.com/about-aws/whats-new/2026/11/data-hub-billing-cost-management-preview/
status: unread
id: 2026-11-23-aws-finops-agent-data-hub
---
2026-11-23 07:16
Tags: #daily-knowledge #ai

---
# AWS FinOps Agent gets Data Hub (preview) SQL over 13 months of hourly, resource-level cost

AWS previewed Data Hub in Billing and Cost Management, a managed data layer that lets the AWS FinOps Agent query 13 months of hourly, resource-level cost and usage data in the CUR 2.0 schema with SQL. The agent can find the resources behind a cost change, break spend down by team or tag, and show hour-by-hour changes, with no export or pipeline to build.

## Details

**Availability and price**
Preview, launched in US East (N. Virginia), covering cost data from all regions. No charge for Data Hub during preview. EU hosting not stated.

**Caveats**
Preview only, single launch region, and the post gives no accuracy figures for the agent's answers.

**Client use cases**
- Explaining sudden cloud cost jumps, including AI and GPU spend, down to the resource
- Chargeback by team or cost allocation tag
- Hourly cost and usage trends for a resource during a migration or launch

**How we could offer it**
- FinOps assessment that adds the agent to an existing cost review process
- Tagging and cost-allocation clean-up so the agent's breakdowns are meaningful
- Managed FinOps service that uses the agent for first-line analysis

**Pitch**
Ask in plain language why the AWS bill went up and get the resources and teams behind it, with no cost pipeline to build.

**What it is**
A managed cost-data store that AWS provisions, refreshes daily and maintains, using the published CUR 2.0 schema with resource identifiers and cost allocation tags. Set up from the management account, it covers every account in the organisation. The AWS FinOps Agent uses it to answer cost questions in SQL.

**Concepts:** [[AWS]] · [[Agents]]
**From:** [[2026-11-23]]

# My notes


---
# References
[AWS What's New](https://aws.amazon.com/about-aws/whats-new/2026/11/data-hub-billing-cost-management-preview/)
