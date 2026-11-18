---
date: 2026-11-18
section: AI
importance: Med
kind: paper
source: "arXiv 2611.22179"
url: https://arxiv.org/abs/2611.22179
status: unread
id: 2026-11-18-rag-in-a-trenchcoat
---
2026-11-18 07:16
Tags: #daily-knowledge #ai

---
# RAG in a Trenchcoat a minimal hybrid-RAG memory matches the best memory systems on LongMem

BRIDGE stores a note for each conversation block, retrieves with BM25 plus cosine search and shows results in date order. It matches the previous best on LongMemEval-S and BEAM within bootstrap confidence intervals and beats the best memory baseline on EverMemBench by 5.7-6.3 points, using one LLM call per ingested block and one per query. On new probes that need a remembered rule the request never mentions, no design wins everywhere: LangMem's atomic facts win rule application, while BRIDGE wins pattern induction. BRIDGE's rule failures come from the reader ignoring a rule it did retrieve, and putting standing directives at the top of the context fixed most of them. Tested on: 3 memory benchmarks, 5 probes x 20 scenarios plus 87 added scenarios, 3 reader families, 3 graders, 3-4 repeated runs.

## Details

**Caveats**
Only 20 scenarios per probe, so the authors ignore differences under about 15 points. The main reader is GPT-4.1-mini, and probes are LLM-generated and LLM-graded.

**For your work**
Start client memory features with simple hybrid RAG and chronological rendering before buying graph memory. Pull standing rules into a labelled block at the top of the prompt, and test applied memory, not just recall.

**Method**
- BRIDGE: an extractor LLM writes an XML note per block (seeing the 10 previous notes); raw text and note are both kept; hybrid BM25 + cosine with reciprocal rank fusion selects the top 10 blocks.
- Top 3 are shown raw, the rest as summaries, re-sorted chronologically for one reader call.
- Five adversarial probes (rule application, style and procedure induction, multi-turn) compared against Mem0, Graphiti, LangMem and an Oracle.

**Problem**
Agent memory systems keep adding extraction, supersession, reflection and graphs on top of RAG, but recall benchmarks may not show whether any of it helps an agent act on what it remembers.

**Results**
- Parity within confidence intervals with the previous best on LongMemEval-S and BEAM, +5.7 to 6.3 on EverMemBench; uses 17-154x fewer reader tokens than full-context baselines.
- Removing the chronological re-sort costs 7.7 points on knowledge-update questions.
- Over repeated runs, BRIDGE trails LangMem by 36 points on rule application and leads it by 31 on procedure induction.
- Perfect routing between designs would give 82.8% against LangMem's 69.2%, but request-only routing is no better than guessing (49-61%).

**Concepts:** [[Agent memory]] · [[RAG]] · [[Evals and benchmarks]]
**From:** [[2026-11-18]]

# My notes


---
# References
[arXiv 2611.22179](https://arxiv.org/abs/2611.22179)
