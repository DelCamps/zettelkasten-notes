---
date: 2026-11-08
section: AI
importance: Med
kind: paper
source: "Anthropic research"
url: https://www.anthropic.com/research/how-researchers-use-claude
status: unread
id: 2026-11-08-how-researchers-use-claude
---
2026-11-08 07:16
Tags: #daily-knowledge #ai

---
# Anthropic scientists use Claude where AI works best; data analysis is a third of Claude se

Anthropic's Economics team labelled 207,049 consumer research sessions by task and compared them with how researchers actually spend their time. Data analysis is 33.7% of Claude and 48.1% of Claude Code sessions, against 27.6% of researcher time, while data gathering is about 11.5% of sessions against 28.6% of time; tasks AI is best at get about 2x the expected use on Claude and about 4x on Claude Code. Tested on: 207,049 consumer-plan sessions (128,914 Claude Chat/Cowork, 78,135 Claude Code) from Aug 2 to Sep 30, 2026, plus a survey of 528 mostly life-science scientists; one vendor's products.

## Details

**Caveats**
Consumer plans only, over two months; labels and time shares come from LLM classifiers; use is not quality; the survey is self-selected grant applicants; scenarios are illustrative, not forecasts.

**For your work**
A useful evidence base when pitching AI for R&D or analytics teams: start with data analysis, statistics and writing, where use and capability are highest, rather than data gathering or bench work.

**Method**
- A classifier assigned each session a field and research task from the SciNet taxonomy (7,262 tasks, 34 fields, 318 subfields); only the labels were kept and results are reported in aggregate.
- Use ratio = a task's share of sessions divided by its share of researcher time (1 means use matches time spent).
- An LLM compared pairs of research steps on which AI could do better; a Bradley-Terry model turned this into task capability scores.
- A survey of 528 scientists and simple illustrative scenarios ($30 per agent hour vs $95 per researcher hour).

**Problem**
Where do researchers actually use AI across the research process, and does that use follow what AI is good at?

**Results**
- Use ratio rises with capability: about 0.2 in the lowest quintile, about 2.1 (Claude) and 3.9 (Claude Code) in the highest.
- Computer science is 11.9% of Claude and 32.7% of Claude Code sessions vs 4.3% of world researchers; writing is 32.0% of Claude sessions vs 16.0% of time.
- Under current capabilities AI could take on 27-52% of research time (median 38%), a 1.35x to 2.02x speed-up.
- About 40% of surveyed scientists expect AI to run full research projects by 2030, about 64% by 2035; 16% say never.

**Concepts:** [[Claude]] · [[AI for science and math]]
**From:** [[2026-11-08]]

# My notes


---
# References
[Anthropic research](https://www.anthropic.com/research/how-researchers-use-claude)
