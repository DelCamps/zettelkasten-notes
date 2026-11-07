---
date: 2026-11-07
section: AI
importance: High
kind: paper
source: "Anthropic engineering"
url: https://www.anthropic.com/research/components-of-agent-memory
status: unread
id: 2026-11-07-anthropic-agent-memory-dreaming
---
2026-11-07 07:16
Tags: #daily-knowledge #ai

---
# Anthropic on agent memory an offline 'dreaming' pass builds a wiki that lifts search-based

Anthropic lays out a memory hierarchy for agents (transcripts, notes, wikis, always-loaded context) and an offline 'dreaming' pass that checks notes against transcripts and builds wikis. On 25 questions over about 350,000 internal files, wiki plus search scored 61% vs 53% for search alone; on a legal benchmark, parallel agents sharing one page kept only 41 of 57 facts, while one page per agent kept 57 of 57. Tested on: Claude models on CL-Bench 1.0, Pokémon Red (one run per model), an internal corpus of 25 questions and Harvey LAB legal tasks.

## Details

**Caveats**
Vendor post with Claude models only. Pokémon results come from single runs. The wiki gave no gain when the answer sat in one searchable document, and one wiki grew larger than its source corpus. Dreaming costs compute.

**For your work**
Practical design rules for client agents with memory: keep the injected layer small, give each parallel agent its own page, pair a wiki with search rather than replacing it, and do not micromanage what strong models save. Older models do need prompts to read memory first.

**Method**
- Four layers: searchable transcripts, model-written notes, linked wikis, and a small always-injected context
- 'Dreaming': offline sessions that check notes against transcripts, prune, build wiki pages and promote facts upward
- Steering tests: fixed rules on what to save (e.g. 'record only failures') vs letting the model judge

**Problem**
How should agents keep knowledge between sessions without memory turning into an out-of-date pile that costs more to search than it saves?

**Results**
- Internal corpus (about 350,000 files, about 420M tokens): wiki alone went from 13% to 48% as dreaming scaled from 2 to 128 sessions; wiki plus search 61% vs search alone 53%
- Harvey LAB merger questions needing several documents: 87% with the wiki vs 73% with search alone
- Shared page written by parallel agents kept 41 of 57 facts (72%); one page per contract, quoting terms word for word, kept 57 of 57
- Sonnet 5 read its memory before answering 9 out of 10 times unprompted; Sonnet 4.6 under half the time. 'Record only failures' cut the memory gain for Opus 5 and Opus 4.7

**Concepts:** [[Agent memory]] · [[Agents]] · [[Claude]]
**From:** [[2026-11-07]]

# My notes


---
# References
[Anthropic engineering](https://www.anthropic.com/research/components-of-agent-memory)
