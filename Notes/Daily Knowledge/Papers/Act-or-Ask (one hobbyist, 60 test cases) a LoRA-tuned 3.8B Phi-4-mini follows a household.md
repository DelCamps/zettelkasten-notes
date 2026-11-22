---
date: 2026-11-22
section: AI
importance: Low
kind: paper
source: "Hugging Face blog (community)"
url: https://huggingface.co/blog/someshrahul/act-or-ask
status: unread
id: 2026-11-22-act-or-ask
---
2026-11-22 07:16
Tags: #daily-knowledge #ai

---
# Act-or-Ask (one hobbyist, 60 test cases) a LoRA-tuned 3.8B Phi-4-mini follows a household

A personal project trains Phi-4-mini-instruct (3.8B) to decide whether a home assistant should ACT, ASK an adult, or DECLINE, from seven short lines of context, using 16,797 training lines built from 11 written rules. On 60 new blind-labelled situations (149 lines with rewordings) it follows the policy 99.3% of the time, against 49.7% for the same model with all rules pasted into its prompt, and wrongly says ACT 1.0% of the time instead of 16.2%. Tested on: one 3.8B model against its own prompted baseline, 60 test situations, one labeller, one type of US household.

## Details

**Caveats**
Small test set, generated training data, a single labeller who also wrote the rules, and the post says an AI assistant helped write the code. The author's own blind answers matched his rules in only 45 of the 60 cases.

**For your work**
A useful pattern for agent action gating: a small, separate classifier that sees structured context instead of the chat, with the reason for asking stated in JSON. The same kind of gate could check high-risk tool calls in client agents, and media-originated commands map to prompt injection.

**Method**
- 176 hand-labelled situations and 11 written rules; the rules then labelled 6,309 generated situations, reworded into 16,797 lines in varied voices.
- One LoRA pass on Phi-4-mini-instruct (3.8B); the output is one JSON line with the decision and what is missing.
- The gate never sees the chat; commands coming from media such as TV or web pages are declined unless they target comfort devices.

**Problem**
Agents that control real devices or tools need to know when to act, when to ask a person first, and when to refuse. Prompting a model with a list of rules is the usual approach, but the model may not apply them reliably.

**Results**
- Follows the household policy: 99.3% against 49.7% for the prompted base model.
- Says ACT when the policy says ASK or DECLINE: 1.0% against 16.2%.
- ASK reason matches the policy: 100% against 14.5%; the prompted baseline never output DECLINE where it was required.
- The Q4_K_M GGUF version takes about 3.7 seconds per decision on a MacBook Air.

**Concepts:** [[Agent security]] · [[Post-training and RL]]
**From:** [[2026-11-22]]

# My notes


---
# References
[Hugging Face blog (community)](https://huggingface.co/blog/someshrahul/act-or-ask)
