---
date: 2026-11-14
section: AI
importance: High
kind: paper
source: "arXiv 2611.17115"
url: https://arxiv.org/abs/2611.17115
status: unread
id: 2026-11-14-caplite-injection-defense
---
2026-11-14 07:16
Tags: #daily-knowledge #ai

---
# CapLite small-model agents can't write their own injection defences; checking writes again

Defences like CaMeL, Progent, IPIGuard and DRIFT enforce a policy, plan or program that the agent's own model writes; with small open models those artifacts let attacks through on 11 to 14 of 15 models, or CaMeL's programs fail to run in up to 68% of episodes. CapLite derives its rules from the tool schemas, fixes the write calls before any tool output is read, and allows a write only if its recipient, amount or target was stated by the user: no attack succeeded in 13,935 attacked AgentDojo episodes, at 17.1k tokens per episode (18% of CaMeL's). Tested on: 15 open-weight models from 6 families (Qwen, Gemma, Llama, Granite, Ministral, LFM), 1.7B-35B, one benchmark (AgentDojo).

## Details

**Caveats**
One benchmark. Utility under attack is 21 points below the undefended agent, values the user did not state need a confirmation, and an injection that only changes the final answer text (no write) is not covered.

**For your work**
For client agents on small or self-hosted models, don't let the model write its own security policy: gate write tools in code against values in the user's request and send anything else to a human confirmation.

**Method**
- Ran CaMeL, Progent, IPIGuard, DRIFT and CapLite on 15 open-weight models with AgentDojo v1.2.2 (97 user tasks, 949 attacked pairs), served by vLLM at temperature 0.
- CapLite: a Planner that sees only the request commits the write calls before any tool result is read.
- A Mediator admits a write only if every 'authority' argument (recipient, amount, object ID, URL) equals a value stated in the request.

**Problem**
The strongest prompt-injection defences have code enforce a security artifact written by the agent's own model, and were tested mainly with large hosted models. Can small self-hosted models write them?

**Results**
- Model-written artifacts admitted attacks on 14 (Progent), 13 (IPIGuard) and 11 (DRIFT) of the 15 models; CaMeL was breached in 20 of 13,935 episodes but cost 94k tokens per episode.
- Within Qwen3 and Gemma-4, larger models were easier to inject, and their policies did not absorb the extra risk.
- CapLite: zero successful attacks; utility under attack 29.0% vs 27.2% for CaMeL; 17.1k tokens per episode vs 93.7k for CaMeL.

**Concepts:** [[Agent security]] · [[Agents]] · [[Open-weight models]]
**From:** [[2026-11-14]]

# My notes


---
# References
[arXiv 2611.17115](https://arxiv.org/abs/2611.17115)
