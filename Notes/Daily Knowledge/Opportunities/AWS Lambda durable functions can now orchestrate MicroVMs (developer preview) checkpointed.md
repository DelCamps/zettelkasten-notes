---
date: 2026-11-26
section: AI
importance: Low
kind: value
source: "AWS What's New"
url: https://aws.amazon.com/about-aws/whats-new/2026/11/lambda-durable-microvm/
status: unread
id: 2026-11-26-lambda-durable-microvms
---
2026-11-26 07:16
Tags: #daily-knowledge #ai

---
# AWS Lambda durable functions can now orchestrate MicroVMs (developer preview) checkpointed

A new extension to the AWS Durable Execution SDK lets one durable Lambda function start, stop and run tasks on several Lambda MicroVMs in parallel, with checkpoints, retries and token refresh. AWS pitches it for running untrusted or agent-generated code in isolated sandboxes, such as software factories, security scanners and CI/CD jobs. It is a developer preview for TypeScript and Python, not for production.

## Details

**Availability and price**
Developer preview from 25 November 2026, TypeScript and Python SDKs, in all Regions that support both Lambda durable functions and Lambda MicroVMs (Regions not listed). Pricing not stated on the page.

**Caveats**
AWS says developer preview features may change and should not be used for production workloads.

**Client use cases**
- Sandboxed execution for coding agents that write and run code
- Agentic security scanners that need isolated, resumable jobs
- Long CI/CD or data jobs that must survive failures

**How we could offer it**
- Architecture: reference design for an agent code-execution sandbox on AWS
- Pilot: move one client agent's tool execution into MicroVMs and measure cost and recovery

**Pitch**
AWS is giving agents a serverless, crash-safe sandbox for running the code they write, which addresses a common security objection to coding agents.

**What it is**
Durable operations for Lambda MicroVMs: the durable function manages the MicroVM lifecycle, runs each task as a checkpointed durable operation, retries failed tasks and refreshes MicroVM tokens. SQS or EventBridge can trigger it. An optional worker library in the MicroVM image receives tasks, sends heartbeats and reports results. Tasks can run alone or in a shared session that shares files and memory.

**Concepts:** [[AWS]] · [[Agent security]] · [[Coding agents]]
**From:** [[2026-11-26]]

# My notes


---
# References
[AWS What's New](https://aws.amazon.com/about-aws/whats-new/2026/11/lambda-durable-microvm/)
