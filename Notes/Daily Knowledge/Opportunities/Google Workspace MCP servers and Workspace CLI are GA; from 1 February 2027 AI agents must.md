---
date: 2026-11-25
section: AI
importance: High
kind: value
source: "Google Cloud blog"
url: https://cloud.google.com/blog/products/identity-security/deploying-agents-safely-in-your-enterprise
status: unread
id: 2026-11-25-workspace-mcp-servers-ga
---
2026-11-25 07:16
Tags: #daily-knowledge #ai

---
# Google Workspace MCP servers and Workspace CLI are GA; from 1 February 2027 AI agents must

Google made remote MCP servers for Gmail, Drive, Docs, Sheets, Slides, Calendar, Chat and Tasks generally available, with permission and DLP checks and human confirmation built in, plus a Workspace CLI for local agents. Under a new Workspace AI Tools Addendum, AI agents must move off the existing REST APIs, with technical enforcement from 1 February 2027 and quota billing from 1 April 2027.

## Details

**Availability and price**
Workspace MCP servers and Workspace CLI: GA. REST-API enforcement for AI agents from 1 February 2027; billing for usage quotas begins 1 April 2027 (quota tiers in a linked guide). Time-limited approvals, per-user agent activity views and AI access restrictions: coming soon.

**Caveats**
The post does not define what counts as an 'AI agent', does not name supported MCP clients or editions, and does not give quota prices. Agent Gateway's GA status is not stated in the body.

**Client use cases**
- Connect a client's own agents (Claude, OpenAI, Copilot Studio, custom) to Gmail, Drive and Calendar safely
- Migrate existing agent integrations off Workspace REST APIs before the 1 February 2027 enforcement
- Audit and revoke agent access from the Workspace admin console

**How we could offer it**
- Readiness assessment and migration sprint for clients whose agents call Workspace REST APIs
- Agent governance setup: dedicated OAuth client IDs, least-privilege scopes, DLP and Model Armor policies

**Pitch**
Google is making MCP the only allowed way for AI agents into Workspace. Clients with Workspace agents have until February to move, and we can do the move and set up the governance.

**What it is**
GA remote MCP servers for eight Workspace apps, plus a Workspace CLI that returns structured JSON with scoped OAuth sign-in. Every call is checked against Workspace permissions, DLP rules and classification labels. Agents must get explicit user confirmation before sending email, changing Drive sharing or making bulk edits. The servers reject non-agent OAuth clients and support Model Armor. The same post describes Google Cloud Agent Gateway for LLM, MCP and A2A traffic.

**Concepts:** [[Google Cloud]] · [[Agent security]] · [[Agents]]
**From:** [[2026-11-25]]

# My notes


---
# References
[Google Cloud blog](https://cloud.google.com/blog/products/identity-security/deploying-agents-safely-in-your-enterprise)
