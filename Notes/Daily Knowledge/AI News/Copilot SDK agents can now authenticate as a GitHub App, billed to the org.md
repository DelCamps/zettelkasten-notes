---
date: 2026-10-28
section: AI
importance: High
kind: news
source: "GitHub changelog"
url: https://github.blog/changelog/2026-10-27-github-copilot-supports-server-to-server-authentication
status: unread
id: 2026-10-28-copilot-server-to-server-auth
---
2026-10-28 07:16
Tags: #daily-knowledge #ai

---
# Copilot SDK agents can now authenticate as a GitHub App, billed to the org

GitHub Copilot now supports server-to-server authentication for GitHub Apps installed on an organization, in public preview. Services and agents built on the Copilot SDK can call Copilot with a short-lived installation token instead of a signed-in user's credentials. Usage is billed to the owning organization, and its model policies and budgets apply.

## Details

**Caveats**
This is a preview. The post gives no plan requirements, quotas or price changes, so you still pay through the org's premium-request budget. The detail is in the linked docs on server-to-server tokens.

**For your work**
This is the clean way to run a Copilot-SDK agent as a client service: a workload identity with org-level billing and an audit trail, with no personal seats. Worth proposing for any PwC client pilot that uses Copilot as the model backend.

**Method**
- Give a GitHub App the new read-only 'Copilot Requests' organization permission
- Install the app on the organization
- Pass a short-lived installation access token to the Copilot SDK
- Admins see app usage in AI usage CSV reports under the app_client_id field, and revoke it by suspending or uninstalling the app

**Problem**
Until now, an agent or backend service built on the Copilot SDK had to run under a person's Copilot identity. That ties automation to one employee's seat, makes usage hard to attribute, and breaks when that person leaves.

**Results**
- Public preview, announced 27 Oct 2026
- Usage is attributed and billed to the organization that owns the installation
- Org model policies, budgets and spending controls apply to app traffic

**Concepts:** [[GitHub Copilot]] · [[Agents]] · [[Agent security]]
**From:** [[2026-10-28]]

# My notes


---
# References
[GitHub changelog](https://github.blog/changelog/2026-10-27-github-copilot-supports-server-to-server-authentication)
