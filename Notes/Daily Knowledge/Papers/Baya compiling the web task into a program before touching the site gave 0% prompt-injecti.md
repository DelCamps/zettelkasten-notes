---
date: 2026-11-07
section: AI
importance: Med
kind: paper
source: "arXiv 2611.06039"
url: https://arxiv.org/abs/2611.06039
status: unread
id: 2026-11-07-baya-compile-then-execute
---
2026-11-07 07:16
Tags: #daily-knowledge #ai

---
# Baya compiling the web task into a program before touching the site gave 0% prompt-injecti

Baya has the model write a Python program against a trusted website API before it sees any live page, so injected text can fill values or choose pre-defined branches but cannot add new actions. It reached 77.8% aggregate utility on WebArena Verified vs 55.1% for browser-only ReAct and 66.7% for API-enabled ReAct, and 0% attack success on WASP vs 16.2% and 25.5%. Tested on: Claude Sonnet 4.6, Gemini 3.5 Flash and GPT-5.6 Luna (DeepSeek V4 Flash for security) as compilers via Claude Code, Antigravity and Codex, 581 valid WebArena Verified tasks, 84 WASP attack instances.

## Details

**Caveats**
Needs a hand-built trusted API per website and only handles tasks whose control flow can be fixed in advance. Higher per-task latency and tokens than ReAct on unseen tasks. Attacks are WASP templates, not adaptive attackers; 84 instances is a small sample.

**For your work**
For enterprise agents over known internal systems (ERP, ticketing, CRM) you control the API, so plan-then-execute over a typed API is a realistic injection defence to propose, and it can raise utility too. Cache compiled programs for recurring workflows to cut cost.

**Method**
- Per-site Trusted Website API built once (GitLab, Shopping, Shopping Admin, Postmill), with contracts for schemas and undocumented constraints
- Planner compiles the user request into a program; only the program processes live content
- Optional runtime LLM calls return only typed values with no tool access; compared with ReAct (browser-only and API-enabled with the same API docs) and Untrusted Content Masking

**Problem**
ReAct-style web agents pick each action after reading pages that mix trusted and untrusted content, which makes their control flow hijackable by injected instructions.

**Results**
- Utility with Claude Sonnet 4.6: 81.9% vs 59.0% and 52.3% for the ReAct variants; Baya ranks first or ties in nine of twelve model-environment cells
- 0% intermediate and end-to-end ASR in every model and site; ReAct intermediate ASR up to 52.8%
- Only 13 of 627 generated programs (2.1%) contained an LLM-call path
- On GitLab vs UCM: 92.9% vs 75.3% utility, both at 0% ASR

**Concepts:** [[Agent security]] · [[Computer-use agents]] · [[Agents]]
**From:** [[2026-11-07]]

# My notes


---
# References
[arXiv 2611.06039](https://arxiv.org/abs/2611.06039)
