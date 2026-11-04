---
date: 2026-11-04
section: AI
importance: Med
kind: news
source: "Claude Help Center / Claude Platform release notes"
url: https://support.claude.com/en/articles/16266773-how-claude-marks-ai-generated-content
status: unread
id: 2026-11-04-claude-text-watermark
---
2026-11-04 07:16
Tags: #daily-knowledge #ai

---
# Claude text watermark now covers Opus 4.7, Sonnet 4.6 and Mythos 5 under the EU AI Act Art

Anthropic says text from Claude Mythos 5, Opus 4.7 and Sonnet 4.6 now carries its invisible text watermark, adding to models launched since August 2, 2026, as part of signing the EU AI Act's Article 50(2) Code of Practice. On Sonnet 4.6, setting temperature, top_p or top_k to non-default values may drop the watermark, and detection is only in private preview for regulators, researchers and enterprises with their own compliance duties.

## Details

**Caveats**
A detected mark is not conclusive (Claude may only have translated or proofread), and heavy editing, translation, very short passages or stripped file metadata remove the signal.

**For your work**
For EU clients with Article 50 obligations, document which Claude models and sampling settings their apps use, drop custom temperature on Sonnet 4.6 if marking matters, and apply for detector access.

**Method**
- An imperceptible watermark is woven into generated text at the model level, so it applies on every Claude surface and on AWS, Google Cloud and Microsoft Foundry; it adds no tokens or hidden characters.
- Files Claude generates carry C2PA Content Credentials, checkable with the free Claude Content Checker.
- Detection API is in private preview for eligible organisations, including enterprises verifying their own Claude outputs.

**Problem**
Article 50 of the EU AI Act requires machine-readable marking of AI-generated content, and companies deploying Claude need to know which outputs are marked and how to check them.

**Results**
- Models launched in the EU on or after August 2, 2026 are marked from launch; older models are being added, and Mythos 5, Opus 4.7 and Sonnet 4.6 now carry it.
- Rollout on Amazon Bedrock for some models completes by November 10.
- Text from Opus 4.6 or Sonnet 4.6 with non-default temperature, top_p or top_k may not carry a detectable mark.

**Concepts:** [[Claude]] · [[AI safety]]
**From:** [[2026-11-04]]

# My notes


---
# References
[Claude Help Center / Claude Platform release notes](https://support.claude.com/en/articles/16266773-how-claude-marks-ai-generated-content)
