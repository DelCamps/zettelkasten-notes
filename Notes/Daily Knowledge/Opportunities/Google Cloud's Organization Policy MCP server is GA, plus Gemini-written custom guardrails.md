---
date: 2026-11-16
section: AI
importance: Med
kind: value
source: "Google Cloud blog"
url: https://cloud.google.com/blog/products/identity-security/ai-powered-cloud-governance-whats-new-in-organization-policy/
status: unread
id: 2026-11-16-gcp-org-policy-mcp-ga
---
2026-11-16 07:16
Tags: #daily-knowledge #ai

---
# Google Cloud's Organization Policy MCP server is GA, plus Gemini-written custom guardrails

Google made generally available an Organization Policy MCP server that lets agents discover constraints, compute effective policy and create policies, and natural-language authoring of custom constraints with Gemini. The catalogue holds over 100 predefined policies, and custom constraints now cover Agent Runtime, Agent Search and Agent Studio.

## Details

**Availability and price**
Generally available, per the post. Custom constraints are supported across many Google Cloud services, including Agent Runtime, Agent Search, Agent Studio on Gemini platform, Cloud Run and GKE. The post gives no pricing or region details.

**Caveats**
Giving an agent CreatePolicy rights is itself a risk; keep writes behind approval and dry-run. Google Cloud only, and not Microsoft-stack.

**Client use cases**
- Continuous cloud posture audits and drift detection run by an agent
- Checking whether a planned change is compliant before deployment
- Writing guardrails for the client's own AI agent platforms (Agent Runtime, Agent Studio)
- Exemption management with an audit trail

**How we could offer it**
- Cloud guardrail assessment mapped to CIS and PCI samples from Google's Professional Services library
- Build a governance agent over the MCP server with human approval for policy writes
- Managed service: periodic posture reports and dry-run testing of new constraints

**Pitch**
Your cloud guardrails can now be read, tested and drafted by agents, with Gemini writing the policy code. We set up the controls so policy changes stay reviewed and auditable.

**What it is**
Two GA features in Google Cloud Organization Policy. First, an MCP server whose tools "allow autonomous agents and pipelines to interact directly with Organization Policy": ListConstraints and GetCustomConstraint for discovery, GetEffectivePolicy to calculate the effective policy after hierarchy inheritance and tag conditions, and CreatePolicy and CreateCustomConstraint for management. Second, administrators can "author custom Organization Policy in natural language through a Gemini prompt" instead of writing CEL, and Gemini can generate compliant and non-compliant test resources for dry-run validation. Google's example is a coding agent that builds a dashboard of enforced constraints and exempted folders and projects.

**Concepts:** [[Google Cloud]] · [[Agent security]] · [[Agents]]
**From:** [[2026-11-16]]

# My notes


---
# References
[Google Cloud blog](https://cloud.google.com/blog/products/identity-security/ai-powered-cloud-governance-whats-new-in-organization-policy/)
