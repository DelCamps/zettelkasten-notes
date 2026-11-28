---
date: 2026-11-28
section: AI
importance: High
kind: paper
source: "arXiv 2611.30624"
url: https://arxiv.org/abs/2611.30624
status: unread
id: 2026-11-28-tool-call-smuggling
---
2026-11-28 07:16
Tags: #daily-knowledge #ai

---
# Tool-call smuggling a guard approves one JSON tool call while the executor runs another; 1

Agent tool-call arguments are parsed many times (provider, gateway, SDK, guard, executor), and JSON parsers resolve repeated keys, case and escapes differently, so a guard can approve one call while the executor runs another and the audit log shows only the approved one. The authors show end-to-end attacks on tau-bench and AgentDojo tasks, find that 558 of 4,693 deployed MCP schemas give different arguments or verdicts across components, and propose a 'parse once, seal and forward' design that stops all 7,412 crafted inputs. Tested on: 17 parser and validator configurations, 4,693 MCP schemas, ten models, tau-bench and AgentDojo tasks.

## Details

**Caveats**
Most attacks need an attacker who rewrites bytes in transit or runs a malicious MCP server.

**For your work**
- Audit client agent stacks: guard and executor must act on one parsed object holding only approved-schema fields.
- Concrete material for an agent-security assessment around MCP gateways.

**Method**
- Defines six vectors where the same bytes yield different calls (repeated, NUL-suffixed or case-varied keys, number edge cases, escapes, undeclared fields).
- Differential testing harness feeds identical bytes to 17 pinned parser and validator configurations; even two official MCP SDKs accept different inputs.
- End-to-end attacks: a compromised gateway makes a Go-decoder guard approve the user's reservation while an MCP SDK executor cancels another customer's; an escaped file name passes a DLP guard and becomes credentials.txt.
- Evaluates five defences against an attacker who knows them.

**Problem**
Defences that check tool calls (policy guards, DLP filters, human approval) assume the call they check is the call that runs. JSON leaves choices to each parser, such as which copy of a repeated key counts, so composition of components can break that assumption.

**Results**
- Models themselves did not write repeated or disguised keys into calls, but copied them verbatim into JSON-text arguments, which split guard and executor in 82 and 72 of 84 calls.
- A malicious server copying a legitimate tool's schema plus one extra field got the user's workstation name in 29 of 30 trials, unseen by the guard.
- Strict validation, provider strict mode, parse-twice-and-compare and parse-once-but-forward all fall to an adaptive attacker; shared parse with sealed call IDs stops every attack built.

**Concepts:** [[Agent security]] · [[Agents]] · [[Structured outputs]]
**From:** [[2026-11-28]]

# My notes


---
# References
[arXiv 2611.30624](https://arxiv.org/abs/2611.30624)
