---
date: 2026-11-22
section: AI
importance: Med
kind: paper
source: "arXiv 2611.25470"
url: https://arxiv.org/abs/2611.25470
status: unread
id: 2026-11-22-toolpulse-cache-side-channel
---
2026-11-22 07:16
Tags: #daily-knowledge #ai

---
# ToolPulse an unprivileged process on the same machine can rebuild Claude Code and Codex to

The model runs in the vendor's cloud, but the agent's tools (cp, git, sed and so on) run locally on shared system libraries. A co-located, unprivileged process can therefore watch the CPU cache with Flush+Reload and recover which tools the agent runs and when. From those traces it guessed the user's task category with 87.77% and 91.39% accuracy on Terminal-Bench 1 and 2, and flagged encryption or model-training steps with recall above 96%. Tested on: 11 models from 3 families (OpenAI, Anthropic, GLM) in 2 harnesses (Codex, Claude Code), three hardware platforms, one public-cloud server for the end-to-end runs.

## Details

**Caveats**
The attacker must already run on the same physical CPU and share the tool binaries. The paper only locates sensitive steps and does not carry out a full key or model extraction. Concurrent agents interleaving traces are left to future work. Disclosed to OpenAI and Anthropic.

**For your work**
When clients run coding agents on shared build servers, jump hosts or multi-user VMs, the tool activity leaks even though prompts never leave the vendor API. Put agents on dedicated VMs or containers with private file-backed pages, and add this to agent threat models next to prompt injection.

**Method**
- Flush+Reload on code pages of shared tool binaries and libraries, plus algorithms to pick the right cache line, remove duplicate hits and infer some tool arguments
- Tool Recovery Attack watches 100 tools at once and logs each invocation with a timestamp
- Task Profiling Attack classifies the user's intent from the recovered sequence; Trigger Localization Attack flags when sensitive tools run so a finer attack (key or model extraction) can be timed
- Prime+Probe was also tested; it works across VMs but was too slow and noisy for end-to-end use

**Problem**
Earlier cache side-channel attacks on LLMs assumed the attacker shares hardware or model files with the inference process, which does not hold for cloud-hosted models. Coding agents, however, execute their tools on the user's own machine.

**Results**
- Tool Recovery F1 ranged from 93.1% (gpt-6-astra) to 98.8% (gpt-5.6-sol) across the 11 models, with each agent's sandbox enabled
- Monitoring the top 100 of 378 observed tools gave the same 89.81% task-profiling accuracy as monitoring all of them; top 20 dropped it to 74.21%
- Trigger localization: 96.49% recall for key-extraction steps and 98.61% for model-extraction steps, cutting monitoring overhead to 19.54% and 14.21%
- Replaying 24 hours of tool noise from a server shared by about 20 users lowered task profiling to 85.61% mean accuracy

**Concepts:** [[Agent security]] · [[Coding agents]]
**From:** [[2026-11-22]]

# My notes


---
# References
[arXiv 2611.25470](https://arxiv.org/abs/2611.25470)
