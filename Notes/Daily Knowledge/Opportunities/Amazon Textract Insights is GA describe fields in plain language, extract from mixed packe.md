---
date: 2026-11-27
section: AI
importance: Med
kind: value
source: "AWS Machine Learning blog"
url: https://aws.amazon.com/blogs/machine-learning/announcing-amazon-textract-insights-verifiable-generative-ai-for-documents/
status: unread
id: 2026-11-27-textract-insights
---
2026-11-27 07:16
Tags: #daily-knowledge #ai

---
# Amazon Textract Insights is GA describe fields in plain language, extract from mixed packe

AWS made Amazon Textract Insights generally available, a generative AI API that extracts fields you describe in natural language from a document or a mixed multi-document packet. One asynchronous call splits a file of up to 3,000 pages into sub-documents, matches each to a JSON Schema blueprint and returns every value with a confidence score plus the page and bounding box it came from. It handles English, French, German, Italian, Portuguese and Spanish and is priced per page, not per token.

## Details

**What it is**
A new Amazon Textract API (StartDocumentInsights). Blueprints are JSON Schemas whose fields have natural-language descriptions and are either read verbatim or inferred. You can start from AWS public blueprints (W-2, Form 1040, passport and more) or write your own. With splitting on, it separates a mixed packet, matches each part to a blueprint and writes the results to S3. No training is needed.

**Client use cases**
- Mortgage and loan files: payslips, bank statements and handwritten notes in one scan
- Insurance claims and medical bills
- KYC and onboarding packs
- Audit evidence that must be traceable to its page

**How we could offer it**
- Pilot: write blueprints for a client's top document types and tune the confidence threshold on a sample of their own files
- Implementation: an IDP pipeline in which low-confidence fields go to human review and the rest post straight to downstream systems
- Governance: KMS keys, a check on cross-region inference and an audit trail built on the grounding data

**Pitch**
AWS now sells auditable document extraction as one managed API: every value comes back with a confidence score and the page it came from. We can replace clients' hand-built OCR-plus-LLM pipelines and push straight-through processing further in lending, claims and onboarding.

**Availability and price**
Generally available. Priced per page, no minimum commitment (rates not given). Accepts PDF, PNG, JPEG and TIFF. Inference is routed within the caller's geography. The supported Regions are not listed, and the post says Insights is not yet in Tokyo or Zurich.

**Caveats**
EU availability for Insights is not stated, so check it before offering this to Spanish clients. Only six languages are supported, confidence thresholds must be tuned on each client's own documents, and AWS gives no accuracy figures.

**Concepts:** [[AWS]] · [[Structured outputs]] · [[Hallucination]]
**From:** [[2026-11-27]]

# My notes


---
# References
[AWS Machine Learning blog](https://aws.amazon.com/blogs/machine-learning/announcing-amazon-textract-insights-verifiable-generative-ai-for-documents/)
