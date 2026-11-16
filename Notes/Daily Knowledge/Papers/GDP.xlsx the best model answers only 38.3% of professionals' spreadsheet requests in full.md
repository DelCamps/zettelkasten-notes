---
date: 2026-11-16
section: AI
importance: High
kind: paper
source: "arXiv 2611.17766"
url: https://arxiv.org/abs/2611.17766
status: unread
id: 2026-11-16-gdp-xlsx-workbooks
---
2026-11-16 07:16
Tags: #daily-knowledge #ai

---
# GDP.xlsx the best model answers only 38.3% of professionals' spreadsheet requests in full

70 requests written by professionals in 13 domains over complete workbooks (2.18 million populated cells) are graded strictly against expert rubrics; Gemini 4 Argon leads at 38.3%, then Claude Opus 5.5 at 30.3% and Claude Sonnet 5.5 at 29.1%, with a median of 19.3%. Failures are mostly incomplete recall: missed tabs, cell comments, filtered rows and pasted diagrams. Tested on: 20 model configurations from 12 developers, five attempts per task, one OpenHands-based harness.

## Details

**Caveats**
Only 3 tasks are public; one agent harness; the judge is itself a model; scores date from the September 30, 2026 leaderboard.

**For your work**
For finance or audit workbook agents, add an explicit inventory step (list every tab, comment, filter and embedded image) and a completeness check before answering; loading sheets into data frames drops formats and comments that carry the evidence.

**Method**
- Professionals wrote requests from workflows where models had failed them, each with three review rounds
- Rubrics with completeness and exclusivity criteria: the answer set must be complete and contain nothing extra
- Agent runs in a container with Python, openpyxl, pandas, LibreOffice and OCR; an agentic judge can open the file to verify claims

**Problem**
Spreadsheet benchmarks check formulas or short answers, not whether an agent can answer a colleague's real question about a messy, inherited workbook.

**Results**
- Gemini 4 Argon 38.3%, Claude Opus 5.5 30.3%, Claude Sonnet 5.5 29.1%; no other configuration exceeds 25%
- In 21 tasks the answer depends on layout or formatting (fills, strikethrough, comments)
- 58 of the 70 requests never mention a tab or sheet

**Concepts:** [[Evals and benchmarks]] · [[Agents]] · [[Frontier models]]
**From:** [[2026-11-16]]

# My notes


---
# References
[arXiv 2611.17766](https://arxiv.org/abs/2611.17766)
