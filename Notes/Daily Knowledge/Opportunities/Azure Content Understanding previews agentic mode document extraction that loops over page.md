---
date: 2026-11-10
section: AI
importance: Med
kind: value
source: "Microsoft Foundry Blog"
url: https://devblogs.microsoft.com/foundry/when-one-pass-isnt-enough-agentic-mode-in-azure-content-understanding/
status: unread
id: 2026-11-10-content-understanding-agentic-mode
---
2026-11-10 07:16
Tags: #daily-knowledge #ai

---
# Azure Content Understanding previews agentic mode document extraction that loops over page

Microsoft Foundry's Content Understanding adds an agentic extraction mode (preview). Instead of one read-and-fill pass, the model works in a loop with tools to move through text and tables, inspect visual evidence, calculate and validate results, then returns the same schema-based structured fields.

## Details

**Availability and price**
Public preview, announced 9 Nov 2026. The post gives no regions or pricing. It says agentic mode uses more tokens and usually takes longer than standard mode.

**Caveats**
Preview API version only. The post shows examples, not accuracy benchmarks. It recommends starting with standard mode and comparing the two on real files.

**Client use cases**
- Totals and reconciliations across tables that span pages in long financial or regulatory filings (the post's example: agency outlays from a 137-page Treasury bulletin)
- Reading values off charts in reports and investor decks
- Consolidating a table spread over 19 pages, such as an event or transaction log, then counting or summing rows by condition
- Contract and policy extraction where complex rules decide which values count

**How we could offer it**
- Upgrade existing document-AI pipelines: run standard and agentic mode side by side on a client's representative files and route only hard documents to agentic mode
- Bundle with confidence and grounding scores and human review for audit, tax and finance-operations workflows

**Pitch**
For documents where the answer has to be assembled and calculated, not just copied out, agentic mode gives schema-based output with fewer manual fixes, and we can tell clients which documents justify the extra cost.

**What it is**
A new 'Agentic Extraction' workflow kind for Content Understanding analyzers. Set API version 2026-06-01-preview and add "workflow": "agentic" under config, or choose it in Content Understanding Studio. Standard single-pass mode stays the faster, cheaper default.

**Concepts:** [[Agents]] · [[Structured outputs]]
**From:** [[2026-11-10]]

# My notes


---
# References
[Microsoft Foundry Blog](https://devblogs.microsoft.com/foundry/when-one-pass-isnt-enough-agentic-mode-in-azure-content-understanding/)
