---
date: 2026-11-23
section: AI
importance: Med
kind: paper
source: "Hugging Face blog (OpenMed)"
url: https://huggingface.co/blog/OpenMed/spanish-notes-pii-scope
status: unread
id: 2026-11-23-openmed-spanish-clinical-pii
---
2026-11-23 07:16
Tags: #daily-knowledge #ai

---
# OpenMed's four open CPU models for Spanish clinical notes 98.57 character F2 at masking pa

OpenMed released four Apache-2.0 models that run on CPU. Two hide identifiers in Spanish clinical notes: GLiNER2.5 PII fully masked 936 of 946 critical identifiers on 91 held-out MEDDOCAN reports. Two mark negated or uncertain findings: the mmBERT model scored 93.42 macro F1, against 80.40 for a TF-IDF baseline. A worked example shows the misses that remain, such as reading 'cannot be ruled out' as ruled out. Tested on: GLiNER2.5 and mmBERT models against base-model, earlier-OpenMed and lexical baselines, on 91 Spanish MEDDOCAN reports, 1,277 held-out Spanish clinical sentences and 588 synthetic finance documents in seven languages.

## Details

**Caveats**
The test sets are small, and the demo note is a single invented example. The finance and multilingual results come from synthetic documents, and German names stay weak (61.68% fully masked). Masking 'Madre' can change the clinical meaning of a sentence. The vendor tested its own models.

**For your work**
These are on-prem, CPU-only models for de-identifying Spanish health records before a RAG or analytics project. Keep a human review of dates, institutions and relatives, and of 'cannot be ruled out' phrasing.

**Method**
- Fine-tuned two PII maskers (GLiNER2.5, 287.4M parameters; mmBERT, 307.5M) and two negation and uncertainty taggers (mmBERT 307.5M; GLiNER2.5 Decide 1B, 1.19B)
- Scored PII masking once on 91 held-out MEDDOCAN case reports (2,065 identifiers), by character, with F2 so that a miss counts twice as much as an extra mask; CIs from a paired bootstrap
- Scored the scope taggers on 2,028 marked words from cardiology and traumatology sentences kept out of training, against zero-shot, word-only and TF-IDF baselines

**Problem**
Before hospitals can search or analyse Spanish discharge notes, the notes must be stripped of patient identifiers. Keyword search then still returns patients whose condition was ruled out or only suspected.

**Results**
- PII: GLiNER2.5 scored 98.57 character F2 and mmBERT 98.12, against 84.64 for the earlier OpenMed model (+13.92 points, 95% CI +12.80 to +15.10) and 35.77 for the base model
- Reports with any identifier character left: 19 of 91 (GLiNER2.5) and 28 of 91 (mmBERT). Misses cluster in professions, institutions and relatives (40 of 44 relatives masked by GLiNER2.5)
- Scope: mmBERT 93.42 and Decide 1B 91.83 macro F1, against 80.40 for TF-IDF; uncertainty is the weakest class (F1 87.10 and 84.83)
- On the demo note, mmBERT read 'No puede descartarse una neoplasia' as negated (score 0.91), which would drop a suspected lung-cancer patient from a cohort query

**Concepts:** [[Open-weight models]] · [[Evals and benchmarks]]
**From:** [[2026-11-23]]

# My notes


---
# References
[Hugging Face blog (OpenMed)](https://huggingface.co/blog/OpenMed/spanish-notes-pii-scope)
