---
date: 2026-10-27
section: AI
importance: Med
kind: paper
source: "arXiv 2610.33201"
url: https://arxiv.org/abs/2610.33201
status: unread
id: 2026-10-27-whowins-instruction-conflicts
---
2026-10-27 07:16
Tags: #daily-knowledge #ai

---
# Instruction conflicts order inside a message beats the system role

With 1,887,356 scored replies, WhoWins shows that when two conflicting lines share a message the first wins 72.42-94.66% of the time, and on Qwen models a policy sent first in the system message loses most conflicts to later lines. In tool and file-write tasks a system policy wins less often than the same text sent as a labelled user message. Tested on: 14 open-weight models (Qwen3, Qwen3.5, gpt-oss; 0.6B-122B), thinking on and off, 1,080 scenarios.

## Details

**Caveats**
Open-weight models only; closed models trained on explicit hierarchies may behave differently.

**For your work**
Do not rely on the system role alone to protect operator rules in agents: restate critical policies near the action (e.g. in tool descriptions) and test conflicts with your actual model.

**Method**
- 1,080 code-scored scenarios across five task types, each with up to five mutually exclusive instructions.
- Seven controlled experiments that change only how instructions are delivered (position, role, label, message split).
- Tests whether pairwise wins predict outcomes in larger conflict sets.

**Problem**
Agents receive instructions from the operator, repo config files, the user, tool results and memory; the 'instruction hierarchy' assumes the system prompt wins, but position, role and label are always confounded.

**Results**
- Same message: the first of two conflicting lines wins 72.42-94.66%; split across messages it keeps 22.95-62.65%.
- System-first policy loses most conflicts in all Qwen model-modes but wins most on gpt-oss when it acts.
- In tool and file-write tasks the system policy wins less often than as a labelled user message, by 6.41 to 48.75%.
- At most 2.92% of replies flag or hedge the conflict.

**Concepts:** [[Agent security]] · [[Agents]] · [[Evals and benchmarks]]
**From:** [[2026-10-27]]

# My notes


---
# References
[arXiv 2610.33201](https://arxiv.org/abs/2610.33201)
