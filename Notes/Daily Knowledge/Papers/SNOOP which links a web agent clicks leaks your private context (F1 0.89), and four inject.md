---
date: 2026-11-23
section: AI
importance: High
kind: paper
source: "arXiv 2611.27046"
url: https://arxiv.org/abs/2611.27046
status: unread
id: 2026-11-23-snoop-behavioral-covert-channel
---
2026-11-23 07:16
Tags: #daily-knowledge #ai

---
# SNOOP which links a web agent clicks leaks your private context (F1 0.89), and four inject

A planted link sends a web agent to an attacker's probe site. The pages the agent then chooses to open give away the user's query and profile, even though no private text is ever sent. SNOOP recovers query concepts at an average F1 of 0.89 and user profiles at 0.80. Spotlighting, a tool firewall, Task Shield and Fides each lower that by at most 0.03, and the authors' Selection-Obfuscated Retrieval brings it down to 0.39. Tested on: 4 agents (Codex, OpenHands, IterResearch, Open Deep Research) x 3 backbones from 3 vendors (GPT-5.5, Claude Sonnet 4.6, Gemini 3.6 Flash), 500 StackExchange queries plus 378 iKAT dialogue turns, on a fixed web snapshot.

## Details

**Caveats**
The attack needs the agent to follow a planted link. It was evaluated on a local snapshot, not the live web. An LLM judge scored profile matches.

**For your work**
For any client agent that browses with access to private data, threat models should count the agent's link choices as an outbound channel, not only the text it sends. Content filters and spotlighting will not catch this leak. Consider fetching pages independently of the user's context, or routing fetches through a cache, for sensitive deployments.

**Method**
- An injected link on a legitimate page sends the agent to an attacker's site. Which of the offered links the agent picks is the covert channel (93.8% accuracy per probe).
- SNOOP keeps a coarse-to-fine hypothesis tree for each task, for example stress, then work, then a specific stressor. It probes adaptively within a budget and rebuilds the user's query and profile from the path the agent takes.
- Four published defences were run against it: Spotlighting, Firewalls, Task Shield and Fides, giving 120 attack and 120 defence configurations.

**Problem**
Defences against prompt injection look for sensitive content in what an agent sends out. But what an agent chooses to click depends on its private context: the user's prompt, history, memory and connected data. So browsing behaviour alone could leak that context.

**Results**
- Probing succeeded on 0.94 of StackExchange tasks and 0.83 of iKAT tasks. Concept F1 was 0.89 and 0.79, and profile F1 was 0.80. Codex leaked the most: 0.97 concept F1 on StackExchange and 0.89 profile F1.
- Results varied more across agents than across backbones. Explicit exfiltration attacks, the baseline, succeeded only 0.38% of the time.
- The defences lowered F1 by 0.03 at most. SOR fetches every linked resource whatever the context, lets the agent choose locally, and mixes in decoy fetches. It cuts F1 to 0.39 at the cost of 4.3-4.5x more page fetches and 1.1-1.3x more tokens and time.

**Concepts:** [[Agent security]] · [[Agents]]
**From:** [[2026-11-23]]

# My notes


---
# References
[arXiv 2611.27046](https://arxiv.org/abs/2611.27046)
