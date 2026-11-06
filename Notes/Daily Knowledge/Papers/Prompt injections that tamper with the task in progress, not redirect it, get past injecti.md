---
date: 2026-11-06
section: AI
importance: High
kind: paper
source: "arXiv 2611.07640"
url: https://arxiv.org/abs/2611.07640
status: unread
id: 2026-11-06-task-tampering-injection
---
2026-11-06 07:16
Tags: #daily-knowledge #ai

---
# Prompt injections that tamper with the task in progress, not redirect it, get past injecti

Amazon researchers built 90 cases where planted content, such as a buyer's dispute citing a fake refund policy, changes an amount or recipient within the user's own task. A detection-and-removal defense cuts objective-style attacks to 2.4% but leaves observation and state attacks at 9.5% and 12.1%, and a tool-policy defense still allows 15.4% versus 17.0% with no defense. Tested on: five LLMs from four vendors, seven defenses, three tool-use environments, one run per case at temperature 0.

## Details

**Caveats**
Each configuration runs once, and the intervals resample cases, not runs. Cases were drafted with Claude Code, and some secondary analyses cover only two to four models. Single-run, temperature-0 settings.

**For your work**
Do not certify a client agent as injection-safe based on AgentDojo-style redirect attacks alone. For payments, refunds and access changes, check that consequential values come from an authorised source, not just that the tool call is expected.

**Method**
- Define injection by authority: content is an attack when it tries to settle a decision its source is not authorised to determine
- 90 validated cases across productivity, DevOps and marketplace environments; each user request names the source that should resolve the decision
- Attacks with the same harmful outcome target up to six parts of the agent's decision: objective, decision rules, available actions, expected consequences, reading of observations, or beliefs about state
- Seven defenses: Spotlighting, Sandwich, DRIFT (two modes), Progent, CaMeL, ARGUS; models DeepSeek V3.1, Kimi K2.5, Sonnet 4, Sonnet 4.5, GLM-5

**Problem**
Most prompt-injection benchmarks plant instructions that pull an agent onto an attacker's task. Real attackers (a vendor, a buyer) can instead bend a decision the task already needs, like a refund amount, which looks task-relevant and needs no new tools.

**Results**
- Without a defense, attacks on decision rules, available actions and state succeed more often than objective attacks
- Detection-and-removal: 2.4% on objective attacks vs 9.5% (observation) and 12.1% (state); the gap holds after detection-optimised rewrites
- Tool-policy defense: 15.4% attack success vs 17.0% undefended
- Claude Sonnet 4.5 has the lowest undefended attack success (11.1%), Sonnet 4 the second highest (20.6%)

**Concepts:** [[Agent security]] · [[Evals and benchmarks]]
**From:** [[2026-11-06]]

# My notes


---
# References
[arXiv 2611.07640](https://arxiv.org/abs/2611.07640)
