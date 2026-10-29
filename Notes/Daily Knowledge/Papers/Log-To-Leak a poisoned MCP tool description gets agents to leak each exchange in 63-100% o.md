---
date: 2026-10-29
section: AI
importance: Med
kind: paper
source: "arXiv 2610.36108"
url: https://arxiv.org/abs/2610.36108
status: unread
id: 2026-10-29-log-to-leak-mcp
---
2026-10-29 07:16
Tags: #daily-knowledge #ai

---
# Log-To-Leak a poisoned MCP tool description gets agents to leak each exchange in 63-100% o

An attacker-controlled MCP server puts an instruction in a tool description. After its real work, the agent then calls a 'save_logs' tool and sends it the user query, server name, server response and its own answer. Across 18 working model-server pairs, attack success is 62.64-100%, and in 16 of them task completion moves by at most 6.63 points, so users notice nothing. Tested on: 4 models from 2 providers (OpenAI, Anthropic), 5 MCP servers, 555 queries; defenses tested only on GPT-4o + GitHub.

## Details

**Caveats**
The models are older (GPT-4o, GPT-5, Sonnet 4, GPT-OSS-120B). The ablations and defense tests use only GPT-4o on GitHub MCP, and host-side authorization was not evaluated.

**For your work**
Treat third-party MCP tool descriptions as untrusted input. Add host-level approval or an allowlist for any extra tool calls the user's task did not need, especially calls that send data out. Do not rely on scanning tool metadata.

**Method**
- The injected directive has four parts: Trigger (when), Tool Binding (which tool), Justification (e.g. compliance) and Pressure (mandatory wording)
- The tool description works better as the injection point than the tool name, parameter name or default value
- Attack success, payload accuracy, task completion and token overhead are measured separately; the attack also reproduced in Cursor (GPT-5.1) and Claude Desktop (Sonnet 4.5)

**Problem**
Checking that the task got done does not catch an agent that also quietly sends the conversation to a third party.

**Results**
- ASR 62.64-100%; when the call fires, payload accuracy is 76.55-95.64%
- Claude Sonnet 4 is near saturation: 96.19-99.86% ASR on the custom servers
- Prompt sandwiching, an LLM metadata auditor and IPIGuard all leave residual ASR between 55.38% and 60.47%
- DataSentinel passes all 100 injected descriptions; an instruction detector flags 85.53% of benign ones

**Concepts:** [[Agent security]] · [[Agents]]
**From:** [[2026-10-29]]

# My notes


---
# References
[arXiv 2610.36108](https://arxiv.org/abs/2610.36108)
