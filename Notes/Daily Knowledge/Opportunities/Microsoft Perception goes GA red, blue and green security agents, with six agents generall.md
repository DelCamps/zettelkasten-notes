---
date: 2026-11-20
section: AI
importance: High
kind: value
source: "Microsoft Security blog"
url: https://www.microsoft.com/en-us/security/blog/2026/11/17/security-for-the-agentic-era-powered-by-microsoft-perception/
status: unread
id: 2026-11-20-microsoft-perception-ga
---
2026-11-20 07:16
Tags: #daily-knowledge #ai

---
# Microsoft Perception goes GA red, blue and green security agents, with six agents generall

Microsoft Perception, which orchestrates security agents through playbooks in Defender, is now generally available. The Recon Agent, four blue-team agents (alert triage, attack investigation, detection authoring, threat intelligence) and the Posture Prioritization Agent are GA; the Web App Pen Test and Risk Reduction agents are in preview.

## Details

**Availability and price**
Perception, ISOC core capabilities, Recon Agent, four blue-team agents and Posture Prioritization Agent are GA; Risk Reduction Agent, Web App Pen Test Agent, playbook integrations and full SIEM breadth are preview. Eligible Defender Suite, Microsoft 365 E5 and E7 customers get Sentinel SIEM features, 90-day default Defender retention and more than 500 connectors. No prices or regions are stated.

**Caveats**
No quantified customer results in the post. Several key pieces (playbook integrations, pen testing, risk reduction) are still preview. Cost dashboards exist, which suggests consumption billing to check.

**Client use cases**
- Automated alert triage and attack investigation for an overloaded SOC
- Exposure prioritisation and remediation across multicloud estates
- Detection authoring and threat intelligence enrichment
- Web app pen testing tied to GitHub fixes (preview)

**How we could offer it**
- Assessment: map a client's SOC workflows to Perception agents and set guardrails and approval points
- Pilot: blue-team agents on live Defender incidents, measuring triage time
- Managed security service with PwC owning playbooks, approvals and reporting

**Pitch**
Microsoft's security agents are now GA inside Defender, which many of our clients already license. We can bring them in with the guardrails, approvals and playbooks a regulated SOC needs.

**What it is**
An agentic security operations layer in Microsoft Defender. Red-team agents look for attack paths, blue-team agents triage and investigate, and green-team agents prioritise and fix exposures. Playbooks coordinate them, including two exposure-reduction playbooks across Microsoft, AWS and Google Cloud and a 'protect web app' playbook that runs a pen test and drives the fix to code in GitHub.

**Concepts:** [[AI for security]] · [[Agents]]
**From:** [[2026-11-20]]

# My notes


---
# References
[Microsoft Security blog](https://www.microsoft.com/en-us/security/blog/2026/11/17/security-for-the-agentic-era-powered-by-microsoft-perception/)
