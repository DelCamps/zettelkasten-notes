---
date: 2026-10-25
section: AI
importance: Med
kind: paper
source: "arXiv 2610.31404"
url: https://arxiv.org/abs/2610.31404
status: unread
id: 2026-10-25-agentphishing
---
2026-10-25 07:16
Tags: #daily-knowledge #ai

---
# AgentPhishing four of nine email agents comply with over 45% of adaptive phishing

Agents that handle stock phishing emails safely fail against attacks optimised for them: PhishOpt evolves reusable email-generation 'skills' per agent, and in a nine-agent evaluation four detected under 10% of phishing and complied with more than 45% of malicious requests. A universal skill built from Cialdini persuasion principles transfers to held-out agents.

## Details

**Caveats**
Synthetic single-message attacks; scores chosen actions and drafted replies, not executed real-world harm. LLM-judged realism and persuasion labels add measurement error; results depend on model versions.

**For your work**
For any client agent that triages inboxes or tickets, test it with adaptive, persuasion-driven attacks, not static phishing sets, and gate sensitive actions (sending data, payments, credential replies) behind confirmation regardless of what the agent's own classifier says.

**Method**
- AgentPhishing benchmark scores both phishing detection and malicious-request compliance of LLM email agents.
- PhishOpt optimises reusable email-generation skills against each target agent under fixed benchmark and realism constraints.
- Generated emails are annotated with Cialdini's persuasion principles (authority, urgency, reciprocity, etc.) to build a single universal attack skill.

**Problem**
Email and computer-use agents read and act on untrusted messages. Existing phishing datasets test detection by classifiers, not whether an agent that reads a persuasive email will actually do what it asks (send data, click, reply with secrets).

**Results**
- Agents can handle pre-existing phishing emails safely yet fail under adapted attacks.
- Of nine agents, four show detection below 10% and compliance above 45%.
- The universal skill exposes vulnerabilities across several held-out agents without target-specific optimisation.
- Detection failure and compliance are distinct: an agent can flag an email and still comply.

**Concepts:** [[Agent security]] · [[Computer-use agents]] · [[Evals and benchmarks]]
**From:** [[2026-10-25]]

# My notes


---
# References
[arXiv 2610.31404](https://arxiv.org/abs/2610.31404)
