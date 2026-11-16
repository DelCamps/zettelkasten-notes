---
date: 2026-11-06
section: AI
importance: Low
kind: news
source: "Google AI Studio changelog"
url: https://aistudio.google.com/docs/changelog#2026-11-05
status: unread
id: 2026-11-06-gemini-omni-1-2-flash-ga
---
2026-11-06 07:16
Tags: #daily-knowledge #ai

---
# Gemini Omni 1.2 Flash is GA with 30% cheaper video output; the Gemini API now reads PPT, O

Google made Gemini Omni 1.2 Flash generally available, with up to 15-second video generation, conversational editing and up to 6 reference images, 30% lower video output pricing and doubled paid-tier rate limits. The same changelog adds PPT, ODP and ODS input and lets tools return Office files, audio and video to the model.

## Details

**Caveats**
Changelog entry only; no quality benchmarks given. Silent re-routing of the 1.1 model on December 3 may change outputs and costs for existing apps.

**For your work**
Multimodal tool responses with Office files make document-heavy agents on Gemini simpler (tools can hand back a deck or spreadsheet directly); check any client app pinned to Omni 1.1 Flash before December 3.

**Method**
- Gemini Omni 1.2 Flash GA: video generation up to 15 seconds, conversational editing, up to 6 reference images
- From December 3, 2026, gemini-omni-1.1-flash requests route to gemini-omni-1.2-flash at its rates
- Gemini API now accepts PPT, ODP and ODS input; DOC files get page-image processing; function responses can return Office/OpenDocument files, audio and video, including file URIs

**Problem**
Developers building multimodal apps need cheaper video generation and the ability to feed common office formats, and tool outputs in those formats, straight to the model.

**Results**
- Video output pricing down 30%
- Paid-tier rate limits doubled

**Concepts:** [[Model releases and pricing]] · [[Google Cloud]]
**From:** [[2026-11-06]]

# My notes


---
# References
[Google AI Studio changelog](https://aistudio.google.com/docs/changelog#2026-11-05)
