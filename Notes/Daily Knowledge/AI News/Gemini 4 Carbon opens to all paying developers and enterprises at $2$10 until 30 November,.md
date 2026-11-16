---
date: 2026-11-11
section: AI
importance: High
kind: news
source: "Google blog"
url: https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-carbon-now-available/
status: unread
id: 2026-11-11-gemini-4-carbon-ga
---
2026-11-11 07:16
Tags: #daily-knowledge #ai #update

---
# Gemini 4 Carbon opens to all paying developers and enterprises at $2$10 until 30 November,

Google made Gemini 4 Carbon, previously limited to cyber defenders, generally available in the Gemini API, Gemini Enterprise and Antigravity, at introductory prices of $2/$10 per million tokens rising to $4/$20 after November 30, 2026. GitHub added it to Copilot Pro+, Max, Business and Enterprise the same day, and Antigravity previewed /swarm multi-agent coordination.

## Details

**Caveats**
Benchmarks are Google-reported; context window not stated in the announcement. Price doubles after November 30. Google says robustness to sophisticated prompt injection remains an area for improvement. /swarm consumes quota much faster than chat.

**For your work**
A cheaper frontier option for agentic coding and knowledge work to test against Fable 5.2 and GPT-6 in client builds; Copilot admins should check whether default model enablement turned it on for their orgs.

**Method**
- GA as gemini-4-carbon in the Gemini API paid tier (AI Studio, Android Studio) and in Gemini Enterprise web/mobile app, Workflow Builder and AI developer tools (global, us and eu; off by default in the app, admins must enable)
- GitHub Copilot: GA in VS Code, Visual Studio, Copilot CLI, coding agent, JetBrains, Xcode and more; billed at provider list price under usage-based billing; enabled automatically unless admins disabled new models
- Antigravity: Carbon for Ultra subscribers plus /swarm (preview), agents that split work and coordinate through a shared board; cyber-specific 'Carbon for cyber' stays in the Fairwind Program

**Problem**
Carbon, Google's strongest model, was until now restricted to vetted cybersecurity defenders; the question was when and at what price it would reach developers and enterprises.

**Results**
- Google reports #1 on CursorBench 4.0, WANDR and AutomationBench at more than 2x lower cost per task than the next-best external model
- Honesty benchmark (375 agentic tasks): 92% passed vs 70% for Gemini 4 Argon
- Adaptive red-teaming: per-attempt breach rate 0.8% vs 3.1% on Argon; zero new universal jailbreaks in 132 hours
- Introductory price $2/$10 per million input/output tokens, same as Argon; $4/$20 after November 30, 2026

**Concepts:** [[Model releases and pricing]] · [[Frontier models]] · [[GitHub Copilot]]
**From:** [[2026-11-11]]

# My notes


---
# References
[Google blog](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-carbon-now-available/)
