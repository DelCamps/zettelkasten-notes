---
date: 2026-11-05
section: AI
importance: High
kind: value
source: "Claude docs / ClaudeDevs"
url: https://claude.com/docs/connectors/building/enterprise-managed-auth
status: unread
id: 2026-11-05-claude-plugin-auto-connect
---
2026-11-05 07:16
Tags: #daily-knowledge #ai

---
# Claude Team and Enterprise can now auto-connect plugins at sign-in, even without Okta, wit

Anthropic now lets Team and Enterprise admins set up plugins (MCP connectors) once, and members are connected the first time they use one, with no OAuth screen. Besides the Okta-based route, a new beta lets Claude itself sign the identity assertion. Claude checks only that the user is a member of the organization, not SSO or MFA.

## Details

**Availability and price**
Team and Enterprise plans. The Claude-issued route is in beta. It isn't offered to organizations that sign in to Claude through Okta, which use the identity-provider route. Announced 3 Nov. No extra price stated.

**Caveats**
Claude-issued assertions say nothing about SSO, MFA or groups. Users are matched by email, so a server must sign someone in only on a verified address or domain. Tokens already issued stay valid after a user leaves until they expire. Press reports disagree on how many connectors launched with support (7 vs 14).

**Client use cases**
- Roll out Claude with Atlassian, Notion, Figma, Datadog and similar tools across a whole department, with no per-user OAuth setup
- Clients without Okta (for example on Entra ID) can still give users zero-touch connectors
- ISVs and clients with their own MCP servers can add 'Auto-connect' support to their listing

**How we could offer it**
- Claude Enterprise rollout package: pick connectors, decide between the identity-provider and Claude-issued routes, set custom roles, offboarding runbook
- Build EMA support into client MCP servers: jwt-bearer grant, trusted-issuer allowlist per tenant, the nine validation checks, lookup by verified email

**Pitch**
Connectors stop being a per-user chore: admins switch them on once and every employee has them on first use.

**What it is**
Enterprise Managed Auth (EMA) for connectors. Claude sends the connector's authorization server a signed identity assertion (ID-JAG JWT, RFC 7523 jwt-bearer grant) and gets back an access token without asking the user. The assertion comes from either the customer's identity provider (Okta today) or, in the new beta, from Claude itself under an issuer URL per organization (https://identity.anthropic.com/issuers/<id>). Claude-issued assertions expire within a minute and Claude renews them silently.

**Concepts:** [[Claude]] · [[Agent security]] · [[Agents]]
**From:** [[2026-11-05]]

# My notes


---
# References
[Claude docs / ClaudeDevs](https://claude.com/docs/connectors/building/enterprise-managed-auth)
