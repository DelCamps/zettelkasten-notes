---
date: 2026-11-05
section: AI
importance: Med
kind: news
source: "OpenAI API changelog"
url: https://developers.openai.com/api/docs/changelog
status: unread
id: 2026-11-05-gpt-image-2-6
---
2026-11-05 07:16
Tags: #daily-knowledge #ai

---
# OpenAI ships GPT-Image-2.6 Sunburst and Flare SVG and animated GIF output and markup-guide

OpenAI released two image models, gpt-image-2.6-sunburst and gpt-image-2.6-flare, with adjustable complexity, SVG generation, animated GIF generation and markup-guided editing. The API price for both is $5 per 1M text-input tokens, $8 per 1M image-input tokens and $30 per 1M output tokens.

## Details

**Caveats**
Neither model page explains how Sunburst and Flare differ. No benchmarks are published, and there is no per-image price, only per-token.

**For your work**
SVG output is useful for generated diagrams and slide icons in document and deck agents. Budget by output tokens, and test whether Flare's interactive positioning means lower latency before choosing a snapshot.

**Method**
- Two snapshots: gpt-image-2.6-sunburst and gpt-image-2.6-flare, the latter described as suited to interactive generation and editing
- New 'complexity' setting, SVG output and animated GIF output
- Markup-guided editing: draw on the image to direct an edit, also added for supported GPT Image 2.5 models
- Only on v1/images/generations and v1/images/edits, not in Chat Completions, Responses or Batch

**Problem**
Image models have produced raster images only, and edits were driven by text alone. Teams that need vector assets, simple animations or precise local edits had to post-process.

**Results**
- Text input $5 per 1M tokens ($1.25 cached), image input $8 per 1M ($2 cached), output $30 per 1M, the same for both snapshots
- Rolled out across ChatGPT, Codex and the API on 4 Nov
- OpenAI describes it as faster generation with more precise editing, but the model pages give no speed or quality figures

**Concepts:** [[Model releases and pricing]] · [[OpenAI enterprise]]
**From:** [[2026-11-05]]

# My notes


---
# References
[OpenAI API changelog](https://developers.openai.com/api/docs/changelog)
