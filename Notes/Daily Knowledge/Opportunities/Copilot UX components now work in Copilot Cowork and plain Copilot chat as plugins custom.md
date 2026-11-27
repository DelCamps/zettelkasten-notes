---
date: 2026-11-27
section: AI
importance: Med
kind: value
source: "Microsoft 365 Developer blog"
url: https://devblogs.microsoft.com/microsoft365dev/copilot-ux-components-now-available-in-cowork-with-plugins-spfx-roadmap-update-for-november-2026/
status: unread
id: 2026-11-27-copilot-ux-components-cowork
---
2026-11-27 07:16
Tags: #daily-knowledge #ai #update

---
# Copilot UX components now work in Copilot Cowork and plain Copilot chat as plugins custom

Microsoft says Copilot UX components (custom SPFx React components, GA since 28 October) can now be packaged as plugins and are supported in Copilot Cowork and standard Copilot chat. Copilot detects the user's intent and renders the right component with no agent to open, for example approving vacation requests or booking a room inline. Admins deploy, scope or block plugins in the Microsoft 365 admin center under Agents > Tools.

## Details

**What it is**
Copilot UX components can now be packaged as a plugin together with skills, and Copilot brings in the right component automatically in standard chat and in Cowork. Components are React and JavaScript built with SPFx and hosted in the customer's own tenant. Plugins use the same package format as Teams apps and Office add-ins.

**Client use cases**
- Intranet-in-Copilot: a daily priorities dashboard, lunch menus, room booking and recognition
- HR and IT self-service with inline approvals (vacation, access requests)
- Line-of-business front ends (expenses, travel, case handling) shown inside Copilot chat

**How we could offer it**
- Build: an SPFx and plugin factory for a client's top 5-10 employee journeys, reusing their existing SharePoint and SPFx skills
- Governance: a plugin rollout model (who gets what, block lists) in the Microsoft 365 admin center
- Roadmap: position SharePoint single page apps (preview with SPFx 1.25) for full intranet portals

**Pitch**
Clients' intranet and approval apps can now show up inside Copilot chat and Cowork when an employee asks, without anyone finding the right agent first. We can turn their existing SPFx work into Copilot experiences and govern them centrally.

**Availability and price**
Supported and available now. Users need a Microsoft Copilot licence. The plugin package is currently built manually; build settings are expected with SPFx 1.25 (planned December 2026 / January 2027).

**Caveats**
Packaging is manual for now. Automatic sync to Teams is still planned as a fast follow. Mobile support is still rolling out gradually. The source is a developer blog, with no Message Center rollout dates.

**Concepts:** [[Microsoft 365 Copilot]] · [[Agents]]
**From:** [[2026-11-27]]

# My notes


---
# References
[Microsoft 365 Developer blog](https://devblogs.microsoft.com/microsoft365dev/copilot-ux-components-now-available-in-cowork-with-plugins-spfx-roadmap-update-for-november-2026/)
