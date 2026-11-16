---
date: 2026-11-01
section: AI
importance: Med
kind: value
source: "AWS What's New"
url: https://aws.amazon.com/about-aws/whats-new/2026/10/step-functions-workflows-ai-agent-tools/
status: unread
id: 2026-11-01-step-functions-agent-tools
---
2026-11-01 07:16
Tags: #daily-knowledge #ai

---
# AWS lets agents call existing Step Functions workflows as MCP tools through AgentCore Gate

Existing AWS Step Functions Standard and Express workflows can now be exposed as tools to AI agents through Amazon Bedrock AgentCore Gateway, which speaks MCP. The agent decides when to run a workflow and with what input; Step Functions then runs every step exactly as defined, so policies like refund approvals stay deterministic. Available wherever AgentCore Gateway is, at standard rates.

## Details

**Availability and price**
All AWS Regions where AgentCore Gateway is available. Standard Step Functions and AgentCore Gateway rates; no separate price. Announced 29 Oct 2026.

**Caveats**
The post does not list the regions explicitly, so EU availability depends on AgentCore Gateway's regional footprint. An agent can still pass bad inputs: validation belongs in the workflow. Microsoft-stack clients would use Logic Apps or Power Automate equivalents instead.

**Client use cases**
- Customer-support agent starts a refund workflow; the eligibility check, manager approval and credit steps run in a fixed order.
- Operations agent reports overnight workflow failures and the failing step.
- Wrapping existing back-office processes (KYC, claims, onboarding) so an agent can trigger them without being able to skip controls.

**How we could offer it**
- Assessment: inventory clients' existing Step Functions workflows that are good agent tools.
- Implementation: expose them through AgentCore Gateway with least-privilege IAM and input validation.
- Governance: logging and audit of which agent ran which workflow. Skills: AWS Step Functions, AgentCore, MCP, IAM.

**Pitch**
AWS now lets an agent trigger a client's existing, audited workflows as tools while the workflow itself keeps the controls. It is a low-risk way to put agents in front of real processes on AWS accounts we already serve.

**What it is**
A connector target in AgentCore Gateway that turns Step Functions state machines into MCP tools. Agents can start workflows and also look up workflow runs, for example to tell an on-call engineer which runs failed overnight and at which step. Step Functions orchestrates over 220 AWS services.

**Concepts:** [[AWS]] · [[Agents]]
**From:** [[2026-11-01]]

# My notes


---
# References
[AWS What's New](https://aws.amazon.com/about-aws/whats-new/2026/10/step-functions-workflows-ai-agent-tools/)
