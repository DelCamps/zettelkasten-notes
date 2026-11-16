---
date: 2026-10-30
section: AI
importance: Med
kind: paper
source: "arXiv 2610.40396"
url: https://arxiv.org/abs/2610.40396
status: unread
id: 2026-10-30-role-spoofing-probes
---
2026-10-30 07:16
Tags: #daily-knowledge #ai

---
# Role spoofing tool output that fakes chat structure passes as the user, even on Opus 5 and

Injected tool output that mimics both the style and the chat-template structure of a user turn got models to carry out the attacker's task at 63.1% to 103.6% of the rate they did for real user requests on AgentDojo, and with JSON-escaped tool output still at 82.6% (GPT-5.4) and 83.6% (Opus 5). Linear probes trained on conversations with random content detected the spoofing better than probes trained on real injections. Tested on: six frontier models from three providers on AgentDojo plus a custom tool testbed, with mechanism and probe work on open models such as Qwen3.5-27B.

## Details

**Caveats**
The main threat model lets the attacker inject unescaped text; probes need model internals and only catch role spoofing, not other injections.

**For your work**
Escape or strip chat-template look-alikes from tool and web content before it reaches the model; escaping alone is not enough, so keep tool permissions narrow.

**Method**
- Role-spoofing injections with fake special-token structure and user-style content in AgentDojo's workspace family, normalised by how often the model does the same task when the user asks
- "Who said what" probes that separate content cues from structure cues, plus a toy training pipeline
- Per-token linear role probes that flag tool output the model believes came from the user

**Problem**
Models should know who said what from special tokens, yet text in a tool result can still be treated as the user speaking.

**Results**
- Simple testbed: attack success above 95% for every model except Gemini 3.1 Pro at 72.5%
- AgentDojo ratio: Claude Opus 4.8 63.1%, GPT-5.4 96.2%, Gemini 3.1 Pro 96.3%
- Fine-tuning Qwen3.5-27B against content-based injections did not stop structure-based ones
- Role probes beat the injection-trained probe baselines at false positive rates between 0-1%

**Concepts:** [[Agent security]] · [[Interpretability]]
**From:** [[2026-10-30]]

# My notes


---
# References
[arXiv 2610.40396](https://arxiv.org/abs/2610.40396)
