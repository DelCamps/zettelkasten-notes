---
date: 2026-10-31
section: AI
importance: Med
kind: news
source: "Gemini API docs"
url: https://ai.google.dev/gemini-api/docs/computer-use
status: unread
id: 2026-10-31-gemini-computer-use-ga
---
2026-10-31 07:16
Tags: #daily-knowledge #ai

---
# Gemini API Computer Use is now generally available, with per-action safety decisions

Google made the Gemini Computer Use tool generally available in the Interactions and GenerateContent APIs on 30 October. It covers browser, desktop and mobile environments, with per-action safety decisions and opt-in detection of prompt injection in screenshots.

## Details

**Caveats**
Google says Computer Use 'may contain errors and security vulnerabilities' and recommends close supervision and sandboxed environments. Pricing is on a separate page.

**For your work**
To pilot browser automation, turn on prompt-injection detection and route require_confirmation actions to a human-approval step. Log the intent field for audit trails.

**Method**
- Supported models: Gemini 4 Argon, Gemini 3.8 Flash (the recommended one), Gemini 3.5 Flash-Lite and Gemini 3 Flash Preview.
- Three environments: browser (20 actions), desktop (17) and mobile (10). Coordinates are normalised to 0-999 and the client scales them to the screen.
- Each proposed action can carry a safety_decision: allowed, require_confirmation or blocked. The app asks the user and returns safety_acknowledgement. There are seven policy categories, such as FINANCIAL_TRANSACTIONS, and some can be turned off with disabled_safety_policies.

**Problem**
Computer-use agents need a supported API surface and built-in guardrails before teams will put them into client workflows.

**Results**
- Prompt-injection detection is opt-in (off by default) for Gemini 3.5 Flash-Lite and later. It scans screenshots for hidden instructions and blocks the action.
- Actions also carry an intent field, which helps with logging and review.

**Concepts:** [[Computer-use agents]] · [[Agent security]]
**From:** [[2026-10-31]]

# My notes


---
# References
[Gemini API docs](https://ai.google.dev/gemini-api/docs/computer-use)
