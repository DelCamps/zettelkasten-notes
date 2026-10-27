---
date: 2026-10-27
section: AI
importance: High
kind: news
source: "GitHub changelog"
url: https://github.blog/changelog/2026-10-26-github-copilot-assisted-permissions-generally-available
status: unread
id: 2026-10-27-copilot-terra-assisted-permissions
---
2026-10-27 07:16
Tags: #daily-knowledge #ai

---
# Copilot GPT-6.1 Terra arrives and LLM-judged 'assisted permissions' go GA

GitHub made assisted permissions generally available in Copilot CLI, the Copilot app and VS Code: an LLM reviews each command, file path or URL request, lets clearly safe ones run and asks you about the rest. GPT-6.1 Terra is also now in the Copilot model picker for Pro, Pro+, Max, Business and Enterprise, billed at provider list price.

## Details

**Caveats**
No premium-request multiplier is stated for Terra; it is billed at list price under usage-based billing. GitHub does not publish how the permission classifier was evaluated or its error rate.

**For your work**
For client rollouts, recommend 'Assisted' with 'Allow All' blocked as the enterprise default, and check the model policy if a client does not want new models auto-enabled.

**Method**
- Assisted mode: a language model classifies each tool request (run a command, access a path, open a URL); requests judged clearly safe proceed, others wait for approval.
- Turn it on with /permissions then 'assisted' in Copilot CLI, the Tool permissions mode picker in the Copilot app, or the permissions picker in VS Code.
- Enterprise admins can block 'Allow All' while keeping Assisted, disable Assisted, and set the default mode for new sessions (falls back to manual approval if the default is blocked).
- GPT-6.1 Terra: available across VS Code, Visual Studio, Copilot CLI, cloud agent, the Copilot app, github.com, GitHub Mobile, JetBrains, Xcode and Eclipse, with a gradual rollout.

**Problem**
Agent permission prompts either interrupt developers constantly or get switched to 'Allow All'; GitHub wants a middle mode, and a cheaper OpenAI model for everyday agent work.

**Results**
- GitHub says Terra solved noticeably more terminal and C# tasks than GPT-5.6 Terra in early testing (no numbers given).
- Under default model enablement, Terra is switched on automatically for Business and Enterprise unless an admin turned off the global default.

**Concepts:** [[GitHub Copilot]] · [[Agent security]] · [[Coding agents]]
**From:** [[2026-10-27]]

# My notes


---
# References
[GitHub changelog](https://github.blog/changelog/2026-10-26-github-copilot-assisted-permissions-generally-available)
