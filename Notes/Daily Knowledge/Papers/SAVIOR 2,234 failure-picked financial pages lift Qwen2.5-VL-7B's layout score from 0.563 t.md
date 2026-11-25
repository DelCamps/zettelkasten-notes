---
date: 2026-11-25
section: AI
importance: Med
kind: paper
source: "Hugging Face blog"
url: https://huggingface.co/blog/nchhaya/savior-what-breaks-ocr-on-financial-documents
status: unread
id: 2026-11-25-savior-financial-ocr
---
2026-11-25 07:16
Tags: #daily-knowledge #ai

---
# SAVIOR 2,234 failure-picked financial pages lift Qwen2.5-VL-7B's layout score from 0.563 t

Hyperbots and IIT Bombay audited why OCR fails on financial documents (rotated text, fine print, multi-column order, logos, bad scans) and LoRA-tuned Qwen2.5-VL on 2,234 pages chosen because OCR failed on them. The tuned 7B reaches 0.929 word recall and 0.707 on a new layout metric (PaIRS), against 0.607 for Gemini-2.5-Flash and 0.583 for GPT-4o, and it holds up under 4-bit quantization. Tested on: OCR systems from 9 vendors (Qwen, Google, OpenAI, Mistral, DeepSeek, Ai2, Nanonets, PaddleOCR, dots.ocr), 509-document SAVIOR-Bench plus 105 downstream QA questions.

## Details

**Caveats**
Authors built both the training data and the benchmark; SAVIOR-Bench images only on request; downstream QA is small (105 questions, 50 documents); human annotators agree only 0.761 on similarity.

**For your work**
For finance document-extraction projects, a few thousand pages picked from your own OCR failures can beat larger frontier models, and a small open model can run on client infrastructure.

**Method**
- Audit a held-out set to label failure causes before collecting data
- SAVIOR-Train: 2,234 mostly real documents selected because OCR failed on them; synthetic additions are only orientation variants
- LoRA (rank 32) on the last vision-encoder layer and decoder of Qwen2.5-VL-3B and 7B
- New PaIRS metric scores pairwise spatial relations between words, so reading-order and layout errors count

**Problem**
OCR models that top public benchmarks still break on invoices and financial statements, because hard cases such as logos (0.35% of olmOCR-Bench attributes) barely move public scores.

**Results**
- Qwen2.5-VL-7B + SAVIOR: recall 0.929, PaIRS 0.707, QA F1 0.896; base 7B: 0.909, 0.563, 0.839
- Gemini-2.5-Flash PaIRS 0.607, GPT-4o 0.583, Mistral OCR 0.538, DeepSeek-OCR 0.503
- The 3B model matches the 7B on PaIRS (0.707); the 7B runs about 980 tokens/second on an A100 at 4-bit
- Nanonets-OCR-s has high recall (0.904) but 0.534 precision, showing recall alone misleads

**Concepts:** [[Post-training and RL]] · [[Evals and benchmarks]] · [[Open-weight models]]
**From:** [[2026-11-25]]

# My notes


---
# References
[Hugging Face blog](https://huggingface.co/blog/nchhaya/savior-what-breaks-ocr-on-financial-documents)
