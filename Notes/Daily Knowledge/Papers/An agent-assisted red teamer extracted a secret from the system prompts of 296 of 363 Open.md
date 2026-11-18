---
date: 2026-11-18
section: AI
importance: Med
kind: paper
source: "arXiv 2611.21956"
url: https://arxiv.org/abs/2611.21956
status: unread
id: 2026-11-18-nevan-system-prompt-ctf
---
2026-11-18 07:16
Tags: #daily-knowledge #ai

---
# An agent-assisted red teamer extracted a secret from the system prompts of 296 of 363 Open

UNICAMP researchers hid a random 16-character flag in each model's system prompt with orders to protect it. An OpenCode agent running DeepSeek V4.1 Flash, steered by a human, then tried to get it out. The flag was exfiltrated from 296 of 363 catalog models plus four newer ones; 119 of the 170 language-based captures were in French, and translation-exfil alone took 116 models. The newest Claude and OpenAI models (Claude Opus 5 and 5.5, Sonnet 5.5, Fable 5 and 5.1, the GPT-6 family) remained in the pending list of 50. Tested on: 363 models from the OpenRouter catalog, one adaptive attacker campaign, first capture logged per model.

## Details

**Caveats**
No fixed attack budget or repeated trials. A non-capture only means the techniques tried failed, and French was simply tried first. The study proves existence, not rates.

**For your work**
Never put credentials or secrets a client cares about in system prompts. Enforce critical rules outside the model with output validation and deterministic checks, and do not make an LLM judge the only gate on consequential actions.

**Method**
- Capture-the-flag: each target gets a system prompt with a random 16-character flag and an order to protect it; a capture is an exact match in a response.
- The red teamer is an OpenCode agent on DeepSeek V4.1 Flash, steered by a human; a local harness hides the flag from the attacker and logs every exchange to SQLite.
- Techniques run as a funnel: translation-exfil first, then paraphrase-exact, html-comment deliberation, self-play enumeration and others; captured models leave the queue.

**Problem**
Developers still treat the system prompt as a trust boundary and put keys, policies and tool wiring in it. The question is how many production models give up a system-prompt secret under an adaptive attacker.

**Results**
- 296 of 363 catalog models captured, plus 4 post-freeze models: 300 captures. 50 are pending and 17 were discarded.
- 170 of 300 captures (56.7%) involved a non-English pivot; French 119, Korean 7, Turkish 4.
- Translation-exfil took 116 models in one turn; paraphrase-exact (English) took 67.
- Older Claude models (Opus 4.1-4.8, Sonnet 4-5, Haiku 4.5) were captured; the newest Claude and OpenAI models were not.

**Concepts:** [[Agent security]] · [[AI safety]]
**From:** [[2026-11-18]]

# My notes


---
# References
[arXiv 2611.21956](https://arxiv.org/abs/2611.21956)
