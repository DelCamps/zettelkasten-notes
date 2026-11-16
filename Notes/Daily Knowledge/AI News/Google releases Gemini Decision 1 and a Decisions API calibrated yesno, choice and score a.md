---
date: 2026-11-12
section: AI
importance: Med
kind: news
source: "Gemini API docs"
url: https://aistudio.google.com/docs/decisions-api
status: unread
id: 2026-11-12-gemini-decision-api
---
2026-11-12 07:16
Tags: #daily-knowledge #ai

---
# Google releases Gemini Decision 1 and a Decisions API calibrated yesno, choice and score a

Google released gemini-decision-1 and the Decisions API, which answer up to 1,000 typed questions about text, images, audio, video or PDFs with calibrated probabilities instead of generated text. Only input is billed, at $0.10 per million tokens on the paid tier, with a free tier.

## Details

**Caveats**
Gemini Developer API only (v1beta); no context caching, Batch, Flex or Priority. Google gives no latency or calibration benchmark figures; question instructions are text only.

**For your work**
A cheap replacement for LLM-as-classifier steps (ticket routing, guardrail checks, rubric grading in evals) that returns probabilities you can threshold directly instead of parsing JSON.

**Method**
- Send an input plus a map of 1 to 1,000 questions of type noul (yes/no), choice (2-255 options) or score (2-255 levels)
- All questions run in one forward pass, so latency 'stays nearly flat' as questions are added
- Returns a probability per option and a confidence (estimated chance the top answer is right); output tokens are always 0

**Problem**
Classifying, routing or grading with a chat model means generating and parsing text, which adds latency, cost and brittle parsing.

**Results**
- Context window of 262,144 tokens across input and questions
- Inline inputs up to 100 MB (50 MB for PDFs)
- Pricing: $0.10 per 1M input tokens paid tier; free tier available
- Hugging Face published a shared 'decision models' interface the day before (10 November), so this is becoming a common API shape

**Concepts:** [[Model releases and pricing]] · [[Structured outputs]] · [[Evals and benchmarks]]
**From:** [[2026-11-12]]

# My notes


---
# References
[Gemini API docs](https://aistudio.google.com/docs/decisions-api)
