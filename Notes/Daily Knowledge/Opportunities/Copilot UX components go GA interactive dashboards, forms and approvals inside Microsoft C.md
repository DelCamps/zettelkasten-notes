---
date: 2026-11-03
section: AI
importance: High
kind: value
source: "Microsoft 365 Developer blog"
url: https://devblogs.microsoft.com/microsoft365dev/copilot-ux-components-are-generally-available-bring-interactive-experiences-into-copilot/
status: unread
id: 2026-11-03-copilot-ux-components-ga
---
2026-11-03 07:16
Tags: #daily-knowledge #ai

---
# Copilot UX components go GA interactive dashboards, forms and approvals inside Microsoft C

Microsoft has made Copilot UX components generally available worldwide with SPFx 1.24. A declarative agent can now show interactive web UI such as forms, approvals and live dashboards in the Copilot canvas. Components use the MCP Apps model, and SPFx hosts them inside the client's Microsoft 365 tenant with built-in SSO, so there is no separate web server to run.

## Details

**Availability and price**
GA worldwide with SPFx 1.24 in Copilot on browser and desktop, including Copilot in Teams. Users need a Microsoft Copilot add-on license. The components themselves have no consumption charges, but APIs they call (for example Work IQ) may.

**Caveats**
No mobile support at GA. Cowork, the new Copilot plug-in model and other surfaces are planned, not available. At GA the agent and its components must ship together in one SPFx solution. Connected APIs may need extra permissions or consent.

**Client use cases**
- Approval cards for expenses, contracts or access requests inside Copilot chat
- Line-of-business dashboards (sales pipeline, case status) a user can open without leaving Copilot
- Multi-step intake forms, for example onboarding or incident reporting, driven by an agent
- Reusing existing SharePoint web parts or Teams tabs as Copilot experiences, since the same SPFx code runs in all of them

**How we could offer it**
- Package 'agent + UI' accelerators (approvals, KYC intake, audit request tracker) as SPFx solutions and deploy them to many client tenants
- Modernise clients' existing SPFx and SharePoint estates into Copilot-ready components
- Add a governance review of the connected APIs' permissions and consent

**Pitch**
Stop sending people out of Copilot to another portal: we put your approvals, forms and dashboards inside the Copilot chat, hosted in your own tenant with your existing sign-in.

**What it is**
Interactive web experiences (dashboards, forms, approvals, live business data) that a declarative agent shows in Microsoft Copilot, inline or full screen. They implement the MCP Apps model and ship with the agent in one SPFx solution. SPFx hosts and routes them in the customer tenant, and they run as the signed-in user.

**Concepts:** [[Microsoft 365 Copilot]] · [[Agents]]
**From:** [[2026-11-03]]

# My notes


---
# References
[Microsoft 365 Developer blog](https://devblogs.microsoft.com/microsoft365dev/copilot-ux-components-are-generally-available-bring-interactive-experiences-into-copilot/)
