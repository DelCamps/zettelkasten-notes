---
date: 2026-11-26
section: AI
importance: Med
kind: value
source: "AWS What's New"
url: https://aws.amazon.com/about-aws/whats-new/2026/11/transcribe-turbo-preview/
status: unread
id: 2026-11-26-amazon-transcribe-turbo
---
2026-11-26 07:16
Tags: #daily-knowledge #ai

---
# Amazon Transcribe Turbo (preview) for voice agents about 14% fewer word errors in English

AWS previewed Transcribe Turbo, a new speech-to-text model for batch and streaming, with word error rate down about 14% (relative) in English and 11% in other languages for streaming. For voice agents it adds semantic turn-taking (about 615 ms, 5% interruption rate) and runtime hints that lifted menu-routing accuracy from 87% to 97% on English customer-service data. Streaming covers English, Portuguese, French, Italian, German and Spanish, in US East (Ohio) only for now.

## Details

**Availability and price**
Public preview from 25 November 2026 for batch and streaming in US East (Ohio). English batch Turbo is GA in most AWS Regions; batch Portuguese, French, Italian, German, Spanish, Chinese, Japanese, Korean and Arabic are in preview. Turn-taking and hints are English-only at launch, other languages by end of December 2026. Turn-taking and hints carry no additional charge; base pricing is not stated. No EU region is mentioned.

**Caveats**
Preview only, in one US region, so EU-resident data is a blocker for now. Accuracy figures are AWS's own; the 87% to 97% routing result is on English customer-service data.

**Client use cases**
- Contact-centre voice agents (Amazon Connect or custom) for Spanish banks, insurers and utilities
- IVR menu routing with fewer misroutes
- Call transcription for QA and compliance analytics

**How we could offer it**
- Assessment: benchmark Turbo against the client's current ASR on their own call recordings in Spanish
- Pilot: one voice-agent flow using EndOfTurnDetection and hints
- Implementation: integrate with Connect or Bedrock-based agents; watch the region limit for EU data

**Pitch**
AWS's new speech model cuts transcription errors and makes voice agents interrupt callers less, with Spanish streaming supported at launch. It is a cheap upgrade for any client already running voice bots on AWS.

**What it is**
A next-generation Amazon Transcribe model. The base model needs no API or code changes. Two new streaming features for voice agents: semantic turn-taking, which decides a caller has finished from what they said and their prosody rather than silence; and runtime ASR hints, where the client sends expected menu options, names and entity types (date, phone, currency) before each turn. It also formats numbers, dates, currency, phone numbers and addresses by locale.

**Concepts:** [[AWS]] · [[Agents]]
**From:** [[2026-11-26]]

# My notes


---
# References
[AWS What's New](https://aws.amazon.com/about-aws/whats-new/2026/11/transcribe-turbo-preview/)
