---
date: 2026-11-23
section: AI
importance: Med
kind: paper
source: "arXiv 2611.27216"
url: https://arxiv.org/abs/2611.27216
status: unread
id: 2026-11-23-correct-precedents-guard-violations
---
2026-11-23 07:16
Tags: #daily-knowledge #ai

---
# One correct release makes a small on-device guard agent leak the next restricted item safe

In local-cloud agent systems, a small local model acts as the last check before irreversible actions like deletes or refunds. After it correctly releases an item whose hold was lifted, it becomes more likely to release a similar item that is still on hold. This happened in all 13 open-weight models tested. Paired Decision Distillation, a LoRA trained on a weakly affected teacher, brings the safe rate back to nearly 100% with no extra prompt or model calls. Tested on: 13 open-weight models (up to about 36B) from 9 developers, 3 generated task families plus 2 held-out ones, 192 to 1,536 episodes per arm with cluster-bootstrap 95% CIs, thinking off and JSON-text actions in the main protocol.

## Details

**Caveats**
Most runs had thinking off, used a scripted cloud side and generated queues, and item status was checked by LLM reviewers. The size of the effect varies with native tool calls and with thinking on. Adaptive cloud attackers were not modelled.

**For your work**
If a small model gates irreversible actions, test it on sequences, not single requests, and include look-alike exceptions. The cheapest fix is to restate each item's status inline every time the item appears.

**Method**
- Paired 10-item queues differ in a single earlier item. The precedent arm has a correctly released look-alike whose restriction was lifted. The control arm has an ordinary item in its place. Violations are counted by parsing JSON tool calls, with no LLM judge.
- History-editing interventions, such as swapping a release for a skip, test whether the guard copies its own earlier action.
- PDD distils a weakly affected teacher (Qwen3.8-27B) into LoRA adapters. It trains on queues that pair each restricted item with a look-alike, and puts the loss on only four decision turns.

**Problem**
Audits of agents look for a faulty step. This paper finds a violation that follows a history made up only of correct decisions, so an audit has nothing to flag.

**Results**
- The safe rate fell in all 13 models. Nemotron-3.5-Lightning dropped from 94.5% to 47.1%, Qwen3.5-4B from 99.0% to 69.8%, and Qwen3.5-9B from 99.5% to 76.6%.
- When a refused request is resent in new sessions, the risk compounds: over ten requests, the most affected guard releases at least once more than four times as often.
- Writing each item's status next to it removes at least 0.87 of the effect. Asked for a verdict, most guards wrote ALLOWED for the restricted item.
- PDD restored safe rates to 99.9-100% in the distilled guards.

**Concepts:** [[Agent security]] · [[AI safety]] · [[Agents]]
**From:** [[2026-11-23]]

# My notes


---
# References
[arXiv 2611.27216](https://arxiv.org/abs/2611.27216)
