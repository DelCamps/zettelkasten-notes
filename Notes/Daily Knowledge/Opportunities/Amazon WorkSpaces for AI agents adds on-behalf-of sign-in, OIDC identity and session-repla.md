---
date: 2026-11-17
section: AI
importance: High
kind: value
source: "AWS What's New"
url: https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-workspaces-AI-agents-connect-govern
status: unread
id: 2026-11-17-workspaces-agents-obo-replay
---
2026-11-17 07:16
Tags: #daily-knowledge #ai

---
# Amazon WorkSpaces for AI agents adds on-behalf-of sign-in, OIDC identity and session-repla

AWS added governance features to WorkSpaces for AI agents: agents can sign in through any OIDC identity provider, act as the signed-in user with that user's permissions and Group Policies, and leave a session-replay video plus plain-language transcript in the customer's own S3 bucket. Setup can now be done by a coding assistant such as Claude Code, Codex or Kiro, and AgentCore agents connect with AWS credentials alone.

## Details

**Availability and price**
Announced as available now (AWS What's New, 16 November 2026). No price or region list in the announcement.

**Caveats**
The post does not give pricing, regions or which features are preview.

**Client use cases**
- Agents that work through ERP transactions or a claims queue in existing desktop apps
- Audit-ready evidence of agent actions for compliance teams
- Agents running under a named employee's identity and policies instead of a shared service account

**How we could offer it**
- Pilot: move one desktop process from proof of concept to governed production
- Identity and audit design: OIDC, OBO, replay storage and key management
- Managed review of session replays as part of an agent governance service

**Pitch**
AWS now gives computer-use agents the same identity, policy and audit trail as employees, including video replay in the client's own bucket; that removes the main blocker we hear on desktop-automation pilots.

**What it is**
New capabilities for Amazon WorkSpaces for AI agents, the cloud desktops computer-use agents work in. Agents can sign in through any OIDC identity provider, in addition to SAML. On-behalf-of (OBO) sign-in lets an agent work as the signed-in user, with that user's directory identity, permissions and Group Policies. Session replay turns screenshots into a video paired with a plain-language transcript, stored in the customer's S3 bucket and encrypted with their own keys. Coding assistants guided by AWS MCP skills can build the WorkSpace; Bedrock AgentCore agents connect without agent code; new tools let an agent run a series of actions in one call.

**Concepts:** [[AWS]] · [[Computer-use agents]] · [[Agent security]]
**From:** [[2026-11-17]]

# My notes


---
# References
[AWS What's New](https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-workspaces-AI-agents-connect-govern)
