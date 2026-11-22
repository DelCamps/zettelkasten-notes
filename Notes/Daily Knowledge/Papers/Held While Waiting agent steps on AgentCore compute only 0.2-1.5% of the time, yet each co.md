---
date: 2026-11-22
section: AI
importance: Med
kind: paper
source: "arXiv 2611.26480"
url: https://arxiv.org/abs/2611.26480
status: unread
id: 2026-11-22-held-while-waiting-agentcore
---
2026-11-22 07:16
Tags: #daily-knowledge #ai

---
# Held While Waiting agent steps on AgentCore compute only 0.2-1.5% of the time, yet each co

Deployed LangGraph and Strands agents waited a median of 2.7 seconds per model reply and computed for an estimated 5 to 40 milliseconds, so 1,000 conversations hold 1,000 environments to do the work of 2 to 15 cores. Leaving a 33-second conversation to the 15-minute idle timeout holds 28 times more environments than closing it, and in simulation 64 conversations per environment needed 59 times fewer environments with at most 40 ms added at the 99th percentile. Tested on: one workload (tau-bench retail), 3,549 deployed steps from 384 sessions, Claude models on Bedrock, 2 frameworks, AgentCore and Lambda, 9 platforms' docs; single AWS author.

## Details

**Caveats**
One workload with benchmark-executed tools, one model family, contexts up to 10k tokens; the sharing gain is simulated, and the counts are what the customer holds, not the provider's cost. Platform facts date from 27 October 2026, before AWS's mid-November runtime update.

**For your work**
For client agents on AgentCore or Foundry, close sessions explicitly when a conversation ends and size against session quotas, not CPU. Use per-session isolation where tools or generated code need a sandbox, and budget for it.

**Method**
- Measured framework CPU per step with a mocked network socket (not a stubbed model), inside AgentCore, Lambda and on desktops
- Combined it with real Bedrock latencies and checked against deployed agents on tau-bench retail
- Discrete-event simulation of about 1,000 concurrent sessions under isolation, sharing and timeout policies
- Survey of nine platforms' public docs, including AgentCore, Microsoft Foundry hosted agents and Vertex AI Agent Engine

**Problem**
Managed agent runtimes stop billing CPU while an agent waits on the model, but still reserve a dedicated isolated environment per session that counts against a quota. Capacity, not compute cost, becomes the limit.

**Results**
- Roughly 70 to 600 environments held per busy core
- Compute is a few per cent of the token bill at published prices, so cost is a weak argument against serverless agents
- AgentCore's default limit is 5,000 active sessions (2,500 in most regions); Foundry hosted agents also give each session a dedicated sandbox
- Three measurement traps (stubbing the model, timing 'the model call', running steps back to back) each gave plausible but too-low CPU numbers; after a realistic wait a step cost 1.9 to 4.7 times as much

**Concepts:** [[Agents]] · [[AWS]]
**From:** [[2026-11-22]]

# My notes


---
# References
[arXiv 2611.26480](https://arxiv.org/abs/2611.26480)
