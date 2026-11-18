---
date: 2026-11-18
section: AI
importance: Med
kind: news
source: "Claude Platform docs"
url: https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections
status: unread
id: 2026-11-18-claude-linked-billing
---
2026-11-18 07:16
Tags: #daily-knowledge #ai

---
# Claude API Linked billing (beta) apps built on Claude can bill each request to the custome

Anthropic launched Linked billing in beta. A customer links their Claude Platform organization to your app once through OAuth, and a billing_policy field on each /v1/messages or /v1/chat/completions request decides whether the customer or you pays. Customers can set a spend cap or unlink at any time. Requests still run in your organization, under your data terms.

## Details

**Caveats**
Your rate limits, retention and keys apply, not the customer's: no customer ZDR, BAA or CMEK, so it is unsuitable for HIPAA or CMEK workloads. Many enterprises buy Claude through Azure or AWS and would not qualify.

**For your work**
This is a cleaner commercial model for PwC-built Claude tools: the client's Claude organization pays and sees the spend. Check how each client buys Claude first.

**Method**
- Create an OAuth app in the Claude Console with 'Bill and link to organizations'. There are no client secrets: the back end authenticates with workload identity federation and an operator service account.
- The customer clicks 'Link your Claude organization' and approves. Each request then sets billing_policy with bill_to: "user_profile" or "self". Beta header: user-profiles-billing-2026-10-01.
- If a request marked for the customer can't be billed to them, it is refused rather than billed to you (403 user_profile_not_billable or 402).

**Problem**
Firms building Claude apps for clients either carry the token bill themselves or ask each client for their own API keys.

**Results**
- Supported on /v1/messages and /v1/chat/completions. Message Batches is not supported, and customer-billed requests can't use billable code execution.
- Only organizations that pay Anthropic directly qualify: not cloud-marketplace (AWS, Google Cloud, Azure) or subscription-only organizations.

**Concepts:** [[Claude]] · [[Model releases and pricing]]
**From:** [[2026-11-18]]

# My notes


---
# References
[Claude Platform docs](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections)
