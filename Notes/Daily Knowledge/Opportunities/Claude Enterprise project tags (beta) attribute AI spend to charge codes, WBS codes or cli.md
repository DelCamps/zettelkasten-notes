---
date: 2026-11-08
section: AI
importance: Med
kind: value
source: "Claude Help Center"
url: https://support.claude.com/en/articles/18251257-track-spend-by-project-with-tags
status: unread
id: 2026-11-08-claude-project-tags-cost-codes
---
2026-11-08 07:16
Tags: #daily-knowledge #ai

---
# Claude Enterprise project tags (beta) attribute AI spend to charge codes, WBS codes or cli

Anthropic now lets eligible Claude Enterprise organizations tag projects with codes they already use, such as a charge code or client-matter number, and see spend grouped by tag in settings, in a CSV export or through the Analytics API. A project can carry up to 16 tags, and Claude Code sessions are attributed by adding a project ID to settings.json.

## Details

**Availability and price**
Beta for Claude Enterprise, on automatically for eligible orgs. Not available with HIPAA, CMEK, zero or minimal data retention, non-US data storage, or Claude Desktop routed through the customer's own model provider. No extra price is stated.

**Caveats**
'Most' spend only: seat-covered usage isn't counted. Claude for Office, Chrome, the API, Claude Code on the web and Claude Code via Bedrock, Vertex AI or gateways aren't covered. There's no back-history, amounts may not match invoices, tags can't be locked and are visible org-wide, and the beta has no spend limits by tag. The non-US-storage exclusion matters for EU clients.

**Client use cases**
- Professional-services firms recharging AI cost to client matters or engagements
- Chargeback of AI spend to cost centres or WBS elements in large enterprises
- Feeding Claude spend into FinOps or ERP reporting through the Analytics API

**How we could offer it**
- AI FinOps setup: tag taxonomy, required tags and a CSV/API feed into the client's finance systems
- Bundle with Claude Enterprise rollout and ROI measurement work

**Pitch**
Know what each client, matter or cost centre spends on Claude, using the codes your finance team already runs on.

**What it is**
Owners create tags (name plus predefined or free values, optionally required on new projects), and project editors set them. Spend appears under Usage > Spend by project, grouped by tag, and can be exported as CSV. Beta Admin and Analytics APIs set tags and pull costs in daily buckets (up to 31 days per call). Coverage includes project chat, Cowork in a project, Cowork desktop tasks and Claude Code (terminal or desktop) with attributionProject set.

**Concepts:** [[Claude]]
**From:** [[2026-11-08]]

# My notes


---
# References
[Claude Help Center](https://support.claude.com/en/articles/18251257-track-spend-by-project-with-tags)
