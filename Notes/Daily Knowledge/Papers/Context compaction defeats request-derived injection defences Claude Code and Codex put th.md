---
date: 2026-11-25
section: AI
importance: Med
kind: paper
source: "arXiv 2611.32194"
url: https://arxiv.org/abs/2611.32194
status: unread
id: 2026-11-25-compaction-breaks-authorizers
---
2026-11-25 07:16
Tags: #daily-knowledge #ai

---
# Context compaction defeats request-derived injection defences Claude Code and Codex put th

Defences such as Progent derive allowed actions from the latest user message, but after compaction that message is a model-written summary that can quote injected data. With a frontier compactor, an attacker's account written as plain data was admitted in 91% and 59% of cases under two policy generators, against none when the policy came from the user's own words; a fix that feeds the authorizer only authenticated user turns stopped every attacker action in 40 attacked AgentDojo episodes. Tested on: OpenAI models (gpt-4o-mini to GPT-6.1 Sol), Claude Opus 5.5 in live Claude Code sessions, Qwen2.5-72B; AgentDojo, ASB, 18 compaction prompts from 11 harnesses.

## Details

**Caveats**
Main runs use small OpenAI compactors; live Claude Code policies were generated offline. Mostly one authorizer (Progent).

**For your work**
If you build guardrails that judge actions against 'what the user asked', keep the original user turns outside the compacted context and feed those to the checker.

**Method**
- Record where Claude Code and Codex place summaries at real automatic compactions
- Replay AgentDojo injections through compaction with Progent deriving a fresh policy per request
- Prove a bound: a text-only authorizer cannot separate a forged record from its legitimate twin better than the texts allow
- Gate: authenticate user turns on arrival and carry them verbatim to the authorizer, while the agent still reads the summary

**Problem**
Request-derived authorizers assume the request is what the user said. Long-running agents compact history, and the summary takes the user's place.

**Results**
- Summary in the request slot at 100 Claude Code and 1,008 Codex compactions
- Live Claude Code: summary kept the injected account in 19 of 20 sessions, though Claude marked it as a declined instruction
- Frontier compactors flag injected instructions but rarely injected data
- Gate: no attacker action completed in 40 attacked episodes

**Concepts:** [[Agent security]] · [[Agent memory]] · [[Coding agents]]
**From:** [[2026-11-25]]

# My notes


---
# References
[arXiv 2611.32194](https://arxiv.org/abs/2611.32194)
