---
date: 2026-11-12
section: AI
importance: Med
kind: news
source: "GitHub changelog"
url: https://github.blog/changelog/2026-11-10-github-app-support-for-enterprise-copilot-seat-management
status: unread
id: 2026-11-12-copilot-seat-management-github-apps
---
2026-11-12 07:16
Tags: #daily-knowledge #ai

---
# GitHub Apps can now assign and remove enterprise Copilot seats via a new 'Enterprise Copil

Enterprise GitHub Apps can now call the enterprise-level Copilot seat management APIs to decide which users and enterprise teams hold Copilot seats. Access needs a new fine-grained App permission, 'Enterprise Copilot license management'.

## Details

**Caveats**
Admin plumbing only; enterprise accounts only. The changelog gives no rollout details beyond availability.

**For your work**
For clients rolling out Copilot at scale, licence assignment and reclamation (e.g. inactive users) can now be automated with a least-privilege App, which helps keep seat spend under control.

**Method**
- A new enterprise fine-grained GitHub App permission: 'Enterprise Copilot license management'
- Apps with it can use the enterprise Copilot seat management REST APIs (API version 2026-03-10) for users and enterprise teams

**Problem**
Automating Copilot licence assignment at enterprise level previously required personal access tokens tied to an admin, which is brittle and hard to audit.

**Results**
- Seat provisioning can be driven by an identity/HR workflow app instead of a human admin token
- No change to Copilot pricing or plans

**Concepts:** [[GitHub Copilot]]
**From:** [[2026-11-12]]

# My notes


---
# References
[GitHub changelog](https://github.blog/changelog/2026-11-10-github-app-support-for-enterprise-copilot-seat-management)
