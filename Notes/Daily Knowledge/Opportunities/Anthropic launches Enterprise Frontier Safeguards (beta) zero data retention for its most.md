---
date: 2026-11-24
section: AI
importance: Med
kind: value
source: "Claude Platform docs"
url: https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/setup-console
status: unread
id: 2026-11-24-claude-enterprise-frontier-safeguards
---
2026-11-24 07:16
Tags: #daily-knowledge #ai

---
# Anthropic launches Enterprise Frontier Safeguards (beta) zero data retention for its most

Enterprise Frontier Safeguards (EFS) gives eligible organisations Zero Data Retention on Claude's most capable models on Claude Platform, Claude Platform on AWS and Claude models on Google Cloud: Anthropic keeps no prompts or responses, and encrypted copies called Sealed Safety Data go to a bucket in the customer's cloud account. Two new organisation webhooks warn when that bucket fails or recovers Anthropic's daily check.

## Details

**Availability and price**
Beta, for eligible organisations, on Claude Platform, Claude Platform on AWS and Claude models on Google Cloud (Anthropic managed). The release note gives no price and does not mention Azure or EU-specific regions.

**Caveats**
- Beta and eligibility-gated
- The client must run and monitor its own storage; a failing bucket triggers a webhook and needs an operational response
- Microsoft Foundry and Bedrock-native deployments are not listed

**Client use cases**
- Banks, insurers and public-sector clients that need ZDR before they can use frontier Claude models
- Regulated workloads where the client wants the safety data under its own cloud keys and retention policies
- Unblocking Claude pilots that legal or security teams stopped over data retention

**How we could offer it**
- Data-protection assessment and EFS eligibility check for a client's Claude use cases
- Set-up of customer-owned storage, key management and webhook monitoring on AWS or Google Cloud
- Governance package: retention policy, DPIA input and audit evidence; skills: cloud security, Claude Platform admin

**Pitch**
Anthropic now offers zero data retention on its frontier models with the safety copies kept in the client's own bucket. That removes a common blocker for regulated clients, and we can package the set-up and governance.

**What it is**
A beta announced in the Claude API release notes on 23 November. EFS provides Zero Data Retention (ZDR) for eligible organisations using Claude's most capable models. Anthropic does not retain prompts or responses; instead, encrypted copies (Sealed Safety Data) are stored in customer-owned storage in the customer's own cloud account. A workspace on Anthropic-managed storage is not on EFS. New beta webhooks, external_storage.failed and external_storage.recovered, report the bucket's daily health check.

**Concepts:** [[Claude]] · [[AI safety]]
**From:** [[2026-11-24]]

# My notes


---
# References
[Claude Platform docs](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/setup-console)
