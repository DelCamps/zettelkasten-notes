---
date: 2026-11-03
section: AI
importance: Med
kind: value
source: "AWS What's New"
url: https://aws.amazon.com/about-aws/whats-new/2026/10/connect-flows-mcp-tools/
status: unread
id: 2026-11-03-connect-flows-mcp-tools
---
2026-11-03 07:16
Tags: #daily-knowledge #ai

---
# Amazon Connect contact-centre flows can now call MCP tools through AgentCore Gateway

Amazon Connect Customer has a new 'External Tool' block that invokes Model Context Protocol tools directly in customer experience flows. The tools go through Amazon Bedrock AgentCore Gateway, so clients can reuse their agent tools without custom Lambda functions.

## Details

**Availability and price**
Available in 9 regions, including Europe (Frankfurt) and Europe (London). The announcement does not mention pricing.

**Caveats**
AWS-only, and it needs AgentCore Gateway. The announcement does not name the Spain or Ireland regions. Pricing and limits are in the admin guide, not the announcement.

**Client use cases**
- Banking contact centres looking up recent transactions mid-call
- Insurance or telco flows pulling case or claim history from the CRM
- Removing Lambda glue code from existing Connect estates

**How we could offer it**
- A 'one tool layer for agents and contact centre' architecture: AgentCore Gateway MCP tools shared by Connect flows and AI agents
- Migrate existing Lambda integrations in Connect flows to governed MCP tools

**Pitch**
Build each back-office integration once as an MCP tool, and use it from both your AI agents and your contact-centre flows.

**What it is**
An External Tool block in Amazon Connect flows that calls MCP tools exposed through Amazon Bedrock AgentCore Gateway. The same tools a client built for its AI agents can then serve its IVR and chat flows. AWS's example: fetch case history from a CRM or transaction details from a banking platform when a customer asks about a recent transaction.

**Concepts:** [[AWS]] · [[Agents]]
**From:** [[2026-11-03]]

# My notes


---
# References
[AWS What's New](https://aws.amazon.com/about-aws/whats-new/2026/10/connect-flows-mcp-tools/)
