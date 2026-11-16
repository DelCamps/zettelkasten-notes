---
date: 2026-10-29
section: AI
importance: High
kind: news
source: "Google blog"
url: https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/
status: unread
id: 2026-10-29-gemini-4-carbon
---
2026-10-29 07:16
Tags: #daily-knowledge #ai

---
# Google announces Gemini 4 Carbon, a cyber-first frontier model, initially for defenders on

Google calls Gemini 4 Carbon its strongest model. It ranks #1 on the Artificial Analysis Intelligence Index v5.0 with 59, scores 88.2% on SEC-bench Pro and 0.0% attack success on Gray Swan prompt injection. Introductory pricing is $2/$10 per million input/output tokens, the same as Argon, but for now only a subset of cyber defenders can use it.

## Details

**Caveats**
No API, Vertex AI or Gemini app dates, and no context window. The benchmark tables are images, and the Chrome team's '10x better patches' claim compares against an unnamed model.

**For your work**
Not yet usable for client work. Once it reaches Vertex, $2/$10 makes it a candidate for security-review and long-horizon agents. The 0.0% IPI figure is worth re-testing against your own injection suites.

**Method**
- Successor to Gemini 4 Argon, positioned for state-of-the-art cybersecurity and long-horizon tasks
- Staged release: a subset of cyber defenders first, then trusted partners through the Fairwind Program, and developers, businesses and consumers 'as soon as possible'
- Safety reporting covers cheating on Terminal-Bench 4.0 and indirect prompt injection (Gray Swan IPI)

**Problem**
Google wants a frontier model that is strong at long-horizon work and at finding, exploiting and patching vulnerabilities, without handing that capability to everyone on day one.

**Results**
- Artificial Analysis Intelligence Index v5.0: #1 with 59; WebDev Arena #4 at 1768 Elo (+89)
- SEC-bench Pro 88.2%, ExploitGym 54.8%, CWE-bench patching 71.0%; more than 2x Argon's secure-code success rate
- Terminal-Bench 4.0: successful cheating 0.0%, attempts 0.4%; Gray Swan IPI attack success 0.0% vs 0.7% for Argon
- Introductory price $2 in / $10 out per million tokens, with cached input 95% off

**Concepts:** [[Frontier models]] · [[Model releases and pricing]] · [[AI for security]]
**From:** [[2026-10-29]]

# My notes


---
# References
[Google blog](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/)
