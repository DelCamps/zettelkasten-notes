---
date: 2026-11-06
section: AI
importance: High
kind: value
source: "Claude blog"
url: https://claude.com/resources/articles/claude-enterprise-security-updates
status: unread
id: 2026-11-06-claude-enterprise-security-center
---
2026-11-06 07:16
Tags: #daily-knowledge #ai

---
# Claude Enterprise adds a security center, GA inference hooks for DLP tools, a parent admin

Anthropic shipped a bundle of security and admin controls for Claude Enterprise: prompt and pre-tool-call inference hooks (GA) that route prompts and tool calls to the client's existing security vendor, a security center (beta) that scores settings against Anthropic's recommended baseline, a parent-organization console at admin.claude.com (beta), self-serve IP allowlists and member sign-out (beta), and EDR sensors inside the Cowork VM (beta, Team and Enterprise).

## Details

**Availability and price**
Inference hooks are generally available; security center, centralized management, member sign-out, self-serve IP allowlist and Desktop settings management are in beta. EDR in Cowork is beta on macOS and Windows for Claude Team and Enterprise, and also for the Claude desktop app on Amazon Bedrock, Google Cloud Vertex AI and Microsoft Foundry. No prices are given; contact sales.

**Caveats**
Several pieces are beta. The security center is guidance, not a certification. Centralized management setup cannot be undone. EDR covers only the local Cowork VM, not cloud Cowork sessions, and runs in detection mode only. Member sign-out does not end API keys, running cloud sessions or scheduled routines.

**Client use cases**
- Let a bank or insurer route every Claude prompt and agent tool call through its existing DLP stack before rollout
- Give the CISO an auditable baseline report for Claude settings ahead of an internal audit
- Run Claude across several subsidiaries or after an acquisition with one parent console and separate identity providers
- Stop shadow IT by blocking personal Claude accounts on managed laptops

**How we could offer it**
- Security and governance assessment of a client's Claude Enterprise tenant against the security center baseline
- Implementation: wire inference hooks to the client's DLP/security vendor and set up EDR in Cowork
- Managed service: periodic attestation reviews and auditor reports

**Pitch**
Anthropic now lets clients plug Claude Enterprise into their own DLP and EDR tools and get an auditor-ready settings report; we can sell a fixed-scope 'secure Claude rollout' that configures and evidences this.

**What it is**
A set of governance features for Claude Enterprise across chat, Cowork and Claude Code. Inference hooks (generally available) send prompts, and tool calls before they run, to the client's security tool so existing DLP and security policies apply. The security center (beta) compares each setting with Anthropic's recommended value, rechecks on every page load, records attestations and accepted risks, and exports an auditor report; the sample dashboard shows '13 of 16 controls passed'. Centralized management (beta) adds a parent console at admin.claude.com for SSO, SCIM, domains, groups and Compliance API keys across many organizations, with several identity providers. Access controls add member sign-out everywhere via the Admin API, a self-serve IP allowlist, Desktop settings management, blocking personal Claude accounts on managed machines and folder limits. EDR sensors can run inside the local Cowork VM in detection mode.

**Concepts:** [[Claude]] · [[Agent security]]
**From:** [[2026-11-06]]

# My notes


---
# References
[Claude blog](https://claude.com/resources/articles/claude-enterprise-security-updates)
