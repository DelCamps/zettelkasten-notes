---
date: 2026-11-02
section: AI
importance: High
kind: value
source: "Microsoft Fabric Updates Blog"
url: https://community.fabric.microsoft.com/t5/Fabric-Updates-Blog/Govern-your-Microsoft-Fabric-data-estate-from-one-place-with-the/ba-p/5377369
status: unread
id: 2026-11-02-fabric-govern-skills
---
2026-11-02 07:16
Tags: #daily-knowledge #ai

---
# Microsoft Fabric OneLake catalog Govern experience goes GA, plus Govern Skills that let an

The Govern tab in the OneLake catalog is now generally available, putting tenant health, domains, capacities, workspaces, tags and policies in one place. Microsoft also shipped Govern Skills in Skills for Fabric, so an agent such as GitHub Copilot in VS Code can run a governance health check, explain findings and, after confirmation, remediate (for example bulk-assign workspaces to domains).

## Details

**What it is**
A centralized governance page in Fabric (tenant view and owner view, insights report, domain, capacity, workspace and tag management, plus a Policies Center in preview) and a set of AI skills covering three pillars: Health, Protect (sensitivity label coverage) and Trust (descriptions, tags, endorsements). Each skill follows audit, explain, recommend, remediate, uses supported Fabric admin APIs, and asks for confirmation before sensitive or destructive actions.

**Client use cases**
- Baseline governance health check of a client's Fabric estate
- Cleaning up unassigned workspaces, empty domains and inactive items before a Copilot or data agent rollout
- Raising sensitivity label and endorsement coverage
- Custom governance dashboards built on the admin monitoring semantic model

**How we could offer it**
- Fabric governance assessment delivered with Govern Skills, with prioritized findings and a remediation plan
- Implementation: domain model, policies, labels, endorsements
- Managed service: recurring agent-run health checks with human approval of changes

**Pitch**
Before your data agents go live, we run an agent-assisted governance check of your whole Fabric estate and fix the gaps with you, every change approved by your admins.

**Availability and price**
Govern experience in the OneLake catalog: GA. Policies Center: preview. Govern Skills: available in Skills for Fabric. The governance report is available to all tenants regardless of license or size. No pricing stated.

**Caveats**
Initial skills are strongest on Health; Protect and Trust coverage and remediation are still expanding. Where a signal cannot be measured, the skill points to the Govern tab or Microsoft Purview instead.

**Concepts:** [[Power BI and Fabric]] · [[Agents]]
**From:** [[2026-11-02]]

# My notes


---
# References
[Microsoft Fabric Updates Blog](https://community.fabric.microsoft.com/t5/Fabric-Updates-Blog/Govern-your-Microsoft-Fabric-data-estate-from-one-place-with-the/ba-p/5377369)
