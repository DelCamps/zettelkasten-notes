---
date: 2026-11-28
section: AI
importance: Med
kind: paper
source: "arXiv 2611.31424"
url: https://arxiv.org/abs/2611.31424
status: unread
id: 2026-11-28-contextlure-history-injection
---
2026-11-28 07:16
Tags: #daily-knowledge #ai

---
# ContextLure prompt injections that cite the user's own earlier chat reach 87.3% attack suc

An attacker who can only read a benign user-agent conversation picks evidence from it (a failed transfer, a stated preference) and cites it as an urgent reason for an unauthorised action in one injected message. This lifts overall AgentDojo attack success from 20.3% to 33.8%, reaches 87.3% on InjecAgent, and still gets through five defences, with a PI detector the strongest at 6.2%. Tested on: 6 open-weight victim models from 4 families (GLM, MiniMax, DeepSeek, Qwen), AgentDojo and InjecAgent, synthetic text-only chats.

## Details

**Caveats**
Synthetic text-only chats, open-weight victims only, and campaigns with different cohorts limit cross-comparison; AgentDojo gains do not preserve utility under attack.

**For your work**
- Assume conversation history visible to tools, logs or other parties raises injection risk; enforce permission checks at the action boundary, not just provenance.
- Add history-citing injections to red-team suites for client agents.

**Method**
- Stage 1 extracts source-linked evidence from the frozen benign chat across User/System dimensions with three selection policies.
- Stage 2 rewrites the malicious request with an Urgency/Priority matrix (Strategic, Time-Sensitive, Critical framings).
- Stage 3 reflects on victim refusals; benign chats come from ABCD and Taskmaster dialogues.

**Problem**
Long agent conversations hold evidence about user plans, constraints and failed tasks. It is unclear how much an attacker who can observe them, without changing earlier turns, can use that to make indirect prompt injection work better.

**Results**
- AgentDojo: 74.7% attack success on Banking (vs 52.3% for the benchmark attack), overall 20.3% to 33.8%.
- InjecAgent: Time-Sensitive 85.8%, Critical 87.3%; beats AgentVigil, IterInject, Muzzle and ChatInject.
- Under defences: PI detector 6.2%, Lakera Guard 16.5%, data delimiting 27.6%.

**Concepts:** [[Agent security]] · [[Agents]]
**From:** [[2026-11-28]]

# My notes


---
# References
[arXiv 2611.31424](https://arxiv.org/abs/2611.31424)
