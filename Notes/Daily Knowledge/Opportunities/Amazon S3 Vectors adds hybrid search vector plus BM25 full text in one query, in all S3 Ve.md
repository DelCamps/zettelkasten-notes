---
date: 2026-11-17
section: AI
importance: Med
kind: value
source: "AWS What's New"
url: https://aws.amazon.com/about-aws/whats-new/2026/11/s3-vectors-hybrid-search/
status: unread
id: 2026-11-17-s3-vectors-hybrid-search
---
2026-11-17 07:16
Tags: #daily-knowledge #ai

---
# Amazon S3 Vectors adds hybrid search vector plus BM25 full text in one query, in all S3 Ve

S3 Vectors now runs vector and full-text search in a single QueryVectors call and fuses the results with Reciprocal Rank Fusion. AWS says S3 Vectors cuts vector storage and query costs by up to 90% versus alternatives, with about 100 ms or less latency for frequent queries.

## Details

**Availability and price**
Available now in all commercial AWS Regions where S3 Vectors is available and in the AWS China Regions; S3 pricing page applies. Sub-second latency for infrequent queries, around 100 ms or less for frequent ones.

**Caveats**
The up to 90% cost saving is AWS's own claim; no relevance benchmarks given.

**Client use cases**
- RAG over documents full of exact terms: product codes, legal clauses, policy numbers
- Low-cost agent memory stores that need keyword and semantic recall
- Multilingual search, including Spanish, with a language-specific analyzer

**How we could offer it**
- Retrieval assessment: compare current vector store cost and recall against S3 Vectors hybrid
- Migration of RAG indexes to S3 Vectors for cost reduction
- Add to AWS RAG accelerators

**Pitch**
AWS's low-cost vector store now does hybrid keyword plus semantic search natively, so clients can get better RAG recall without running a separate search cluster.

**What it is**
Hybrid search in Amazon S3 Vectors. Customers store searchable text as a metadata field via PutVectors; S3 Vectors indexes it for full-text search with BM25 scoring. A hybrid query sends text and a query vector in one QueryVectors call; the service runs both searches, fuses them with Reciprocal Rank Fusion and returns one top-K list. A language-agnostic analyzer is the default, with optional language-specific analyzers; full text can be enabled on existing data in place.

**Concepts:** [[AWS]] · [[RAG]]
**From:** [[2026-11-17]]

# My notes


---
# References
[AWS What's New](https://aws.amazon.com/about-aws/whats-new/2026/11/s3-vectors-hybrid-search/)
