---
date: 2026-10-31
section: AI
importance: High
kind: value
source: "Microsoft Foundry blog"
url: https://devblogs.microsoft.com/foundry/microsoft-copilot-harness-in-foundry/
status: unread
id: 2026-10-31-foundry-copilot-harness
---
2026-10-31 07:16
Tags: #daily-knowledge #ai

---
# Azure AI Foundry gets the Microsoft Copilot harness managed agent loop, skills, MCP tools

On 28 October Microsoft put the Microsoft Copilot harness in Foundry Agent Service into public preview. Microsoft runs the agent loop and sandbox, and you supply skills, MCP and Foundry tools, and a source-controlled agent definition; long-running resilience for hosted agents is now GA. It's the fastest Azure-native route to production agents for clients on the Microsoft stack, and runtime is free until billing starts on 1 December 2026.

## Details

**What it is**
A managed execution system for agents that reason, call tools and run long tasks. You define the agent declaratively, for example in an azure.yaml file deployed with azd using the microsoft_copilot_preview harness type, and Foundry handles working context, model and tool steps, policy limits, file and code work, and built-in subagents. It has four building blocks: reusable skills (instructions, scripts and resources), connected Foundry and MCP tools with explicit authentication and approvals, execution and delegation, and versioned agent definitions. You can also build in the Foundry portal, in Foundry Toolkit for VS Code, or in the GitHub Copilot app with the Foundry plugin. Separately, hosted agents gain GA long-running resilience: Foundry detects interruptions and restarts work with its original input.

**Client use cases**
- Research and report agents (web search plus Code Interpreter) for strategy or risk teams, delivered as an Azure resource inside the client's tenant
- Back-office process agents that call client systems through MCP servers, with approvals configured per tool
- Migrating PoC agents built on LangGraph or custom loops to a managed harness that is easier to operate and govern
- Long-running document-processing jobs that survive restarts on hosted agents

**How we could offer it**
- Agent factory offering: a reference azure.yaml, a skills library and MCP tool connectors that we reuse across clients and version in their repos
- Agent platform assessment: when to use a prompt agent, the Copilot harness or a hosted agent, plus cost modelling before December billing starts
- Managed service for the agents we deploy: evals, monitoring and checkpoint/idempotency design for long-running work (skills: Azure, azd, MCP, agent evals)

**Pitch**
Microsoft now runs the agent loop for us in Foundry: we bring skills and MCP tools, they run the sandbox and subagents, and runtime is free until 1 December. That's an ideal moment to build two or three reusable client agents on the Microsoft stack and turn them into a repeatable 'agent factory' offer.

**Availability and price**
Copilot harness: public preview, selected when you create an agent. Long-running resilience for hosted agents: GA. Harness runtime is free before 1 December 2026. From then, sandbox compute costs USD $0.0994 per vCPU-hour and memory $0.0118 per GiB-hour, on a consumption basis. Model inference and other tools are billed separately, and prices may vary by region and agreement. Supported regions and models are listed in the docs, not in the post.

**Caveats**
This is a preview, so check region support, including EU regions for data residency, and preview limits before promising anything. You can't yet switch an existing agent to the harness after creation. With resilience, the application still has to save checkpoints and avoid duplicate actions, because conversation history alone doesn't restore work. Competitors: AWS Bedrock AgentCore harness, Google Vertex AI Agent Engine, OpenAI AgentKit.

**Concepts:** [[Agents]] · [[Multi-agent systems]] · [[Model releases and pricing]]
**From:** [[2026-10-31]]

# My notes


---
# References
[Microsoft Foundry blog](https://devblogs.microsoft.com/foundry/microsoft-copilot-harness-in-foundry/)
