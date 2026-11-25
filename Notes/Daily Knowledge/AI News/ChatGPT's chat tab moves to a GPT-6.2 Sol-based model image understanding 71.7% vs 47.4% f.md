---
date: 2026-11-25
section: AI
importance: Med
kind: news
source: "ChatGPT release notes"
url: https://help.openai.com/en/articles/6825453-chatgpt-release-notes
status: unread
id: 2026-11-25-gpt62-chatgpt-chat-tab
---
2026-11-25 07:16
Tags: #daily-knowledge #ai

---
# ChatGPT's chat tab moves to a GPT-6.2 Sol-based model image understanding 71.7% vs 47.4% f

OpenAI is rolling out a chat-tuned version of GPT-6.2 Sol to the ChatGPT chat tab for Plus, Pro, Business and Enterprise users; the Work and Codex models do not change. On 24 November the API's chat-latest snapshot was moved to the latest ChatGPT model, though OpenAI recommends the GPT-6.2 family for production.

## Details

**Caveats**
All figures are OpenAI's own, mostly internal evals. The release notes mention no retirement of earlier chat models.

**For your work**
Any client app pinned to chat-latest has silently changed model, so re-run evals or pin a dated GPT-6.2 snapshot.

**Method**
- A version of GPT-6.2 Sol tuned for everyday conversation, rolling out globally; Enterprise access depends on admin settings
- API: chat-latest now points to the latest model in ChatGPT

**Problem**
The ChatGPT chat tab still ran on GPT-6 while GPT-6.2 Sol and Astra were already in the API and in Copilot.

**Results**
- Image understanding 71.7% vs 47.4% for GPT-6
- Instruction following on hard prompts 78.1% vs 62.5%
- Internal BrowseComp at Extra high 64.5% vs 54.4%
- Policy-compliant answers in hard conversations 91-94%, up from 77-80%

**Concepts:** [[Model releases and pricing]] · [[Frontier models]] · [[OpenAI enterprise]]
**From:** [[2026-11-25]]

# My notes


---
# References
[ChatGPT release notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)
