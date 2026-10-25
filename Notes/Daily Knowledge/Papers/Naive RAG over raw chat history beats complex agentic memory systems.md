---
date: 2026-10-24
section: AI
importance: High
kind: paper
source: "arXiv 2610.30755"
url: https://arxiv.org/abs/2610.30755
status: unread
id: 2026-10-24-naive-rag-memory
---
2026-10-24 07:16
Tags: #daily-knowledge #ai

---
# Naive RAG over raw chat history beats complex agentic memory systems

Dense retrieval plus reranking over unprocessed conversation history ranked first in 6 of 7 benchmark-model settings across LoCoMo, LongMemEval, MEME and MemoryAgentBench, beating the best agentic memory system by 0.13-5.53 points. The win comes from evidence coverage: summarised or transformed memory stores lose the raw values and relations needed to answer. Use Raw-RAG as the baseline before building a fancy memory layer.

## Details

**Problem**
Long-running chat agents often use 'agentic memory' systems that extract, summarise, update or graph the conversation history. The paper asks whether that complexity actually beats plain retrieval over the raw history.

**Method**
- Raw-RAG: split the timestamped history into 256-token windows with 32-token overlap, embed them, retrieve the top 128 by cosine similarity, rerank with a cross-encoder down to 15, and hand those to the reader LLM.
- Compared against 12 memory systems (EverMemOS, MemOS, Mem0, MemMachine, Memora and others) on LoCoMo, LongMemEval, MEME and MemoryAgentBench.
- Measured coverage (does the retrieved context contain enough evidence) separately from utilisation (accuracy when it does).

**Results**
- Ranked first in 6 of 7 benchmark-model settings, beating the best memory system by 0.13-5.53 points (for example, 89.07 vs 88.12 on LoCoMo with GPT-4o-mini, and 53.41 vs 47.88 on MemoryAgentBench with DeepSeek-V4-Flash).
- Making Mem0 append-only (no updates or deletes) raised LoCoMo accuracy from 67.36% to 69.42%. Adding atomic facts, summaries or graph expansion to Raw-RAG cost 19.62, 5.81 and 5.78 points. Removing the reranker cost 3.92.
- Raw-RAG had the highest coverage (45.29% and 76.35%). On a 1M-token conversation it took 0.33 hours to ingest, against 3.25-26.95 hours for the other systems.

**Caveats**
Tested only on offline conversation benchmarks, not interactive or operational settings. MemMachine won on MEME with DeepSeek-V4-Flash, and full context beat everything there by 19.98 points. Rebuilding the current state is left to the reader model, so weaker readers may still benefit from explicit memory. Keeping raw history raises storage and privacy concerns.

**For your work**
Before you build a memory layer for a client's assistant, set up chunked raw history with dense retrieval and a cross-encoder reranker as the baseline. Any summarisation or fact extraction should have to beat it. Keep the raw transcripts even if you add derived memories.

**Concepts:** Agent memory · [[RAG]] · Baselines
**From:** [[2026-10-24]]

# My notes


---
# References
[arXiv 2610.30755](https://arxiv.org/abs/2610.30755)
