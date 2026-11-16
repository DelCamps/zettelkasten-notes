---
date: 2026-11-05
section: AI
importance: High
kind: paper
source: "arXiv 2611.05806"
url: https://arxiv.org/abs/2611.05806
status: unread
id: 2026-11-05-office-extraction-divergence
---
2026-11-05 07:16
Tags: #daily-knowledge #ai

---
# Office files can show a human one thing and the LLM another all 8 tested assistants and co

An NTU study shows that the text extractors behind LLM apps read Word, Excel and PowerPoint files differently from Office, so a file that looks clean can feed the model hidden text, drop visible footers, or skip number formats (a total shown in thousands reaches the model 1,000 times larger). With no injected instruction, five attacks fooled the systems in 64% of 400 trials, and every system fell for at least one; the authors' Prism defence rebuilds the human view and blocked every case. Tested on: 4 chat assistants (ChatGPT, Claude, Gemini, M365 Copilot) and 4 coding agents (Codex, Claude Code, Antigravity, Copilot CLI), 10 trials per attack, plus 3 models in a controlled test.

## Details

**Caveats**
Only a few documents per scenario; products tested as of October 2026. Prism flags 2.6% of benign files, and its render oracle takes about 12 s per document.

**For your work**
Any RAG or agent pipeline using markitdown-style loaders is exposed. Apply display formats and strip hidden content before ingestion, especially for financial spreadsheets.

**Method**
- Static plus dynamic analysis of 10 widely used extractors: 19 OOXML channels expose text a human cannot see, and 12 drop text a human can see
- Five attacks: hidden injection, silent omission (e.g. footer), formatting divergence (number formats), spatial order inversion on slides, and sub-word regrouping
- Prism defence: a static interpreter rebuilds the displayed text from the OOXML spec, and a render oracle handles reading order

**Problem**
LLM apps read Office files through text extractors, not the rendered page. Where the two disagree, an attacker can show the model a different document from the one the human reviews, and injection filters see no instructions to flag.

**Results**
- 64% attack success overall and 75% against chat assistants; Gemini 100%, Claude and M365 Copilot 80%, ChatGPT 40%; Copilot CLI 86%, Codex 82%, Claude Code 24%, Antigravity 22%
- Formatting divergence misled 7 of 8 systems in at least 9 of 10 trials
- With naive extraction, GPT-5.6, Claude Opus 5.5 and Gemini 4 were misled in all 84 answers on 28 new payloads; with Prism's text they were misled in none
- In 2,229 real files, 7% of spreadsheets show a value that differs materially from the stored one, and 71% of decks have speaker notes

**Concepts:** [[Agent security]] · [[RAG]] · [[Microsoft 365 Copilot]]
**From:** [[2026-11-05]]

# My notes


---
# References
[arXiv 2611.05806](https://arxiv.org/abs/2611.05806)
