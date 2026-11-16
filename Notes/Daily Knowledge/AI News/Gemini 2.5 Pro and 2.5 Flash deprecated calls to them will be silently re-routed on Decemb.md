---
date: 2026-11-03
section: AI
importance: Med
kind: news
source: "Gemini API changelog"
url: https://aistudio.google.com/docs/changelog
status: unread
id: 2026-11-03-gemini-25-deprecated
---
2026-11-03 07:16
Tags: #daily-knowledge #ai

---
# Gemini 2.5 Pro and 2.5 Flash deprecated calls to them will be silently re-routed on Decemb

Google has deprecated gemini-2.5-pro and gemini-2.5-flash, and both are no longer selectable in AI Studio. On December 1, 2026, API requests to 2.5 Pro will route automatically to gemini-3.8-flash, and requests to 2.5 Flash to gemini-3.5-flash-lite, billed at the new models' rates.

## Details

**Caveats**
The changelog gives no quality comparison. Whether the new models handle existing prompts, tools and schemas well is for you to test.

**For your work**
Grep client code and configs for gemini-2.5 now. Re-run your evals on the replacement models, and remove thinking_budget, sampling parameters and prefill before December 1, or tool-calling flows may break.

**Method**
- gemini-2.5-pro maps to gemini-3.8-flash at Gemini 3.8 Flash rates.
- gemini-2.5-flash maps to gemini-3.5-flash-lite at Flash-Lite rates.
- Google says to update model strings before December 1 and follow the migration guide.

**Problem**
Many production apps still pin the 2.5 models. Google will not hard-fail those calls. It will quietly swap the model behind them, which can change behaviour and cost without any code change.

**Results**
- Breaking changes listed for both: function calling and thought_signature validation, thinking_level replacing thinking_budget, removed sampling parameters, and no more prefilled model turns.
- Note the downgrade in tier: Pro traffic lands on a Flash model, not on a newer Pro.

**Concepts:** [[Model releases and pricing]] · [[Google Cloud]]
**From:** [[2026-11-03]]

# My notes


---
# References
[Gemini API changelog](https://aistudio.google.com/docs/changelog)
