---
date: 2026-11-20
section: AI
importance: Low
kind: paper
source: "Hugging Face blog"
url: https://huggingface.co/blog/Dharma-AI/predicting-fine-tuning-time
status: unread
id: 2026-11-20-predicting-fine-tuning-time
---
2026-11-20 07:16
Tags: #daily-knowledge #ai

---
# FLOP estimates explain little of fine-tuning wall-clock time (R² 0.31 at best); a CatBoost

Dharma-AI logged 272 supervised fine-tuning runs (about 7,382 GPU-hours) on a shared H200 pool and found the usual FLOP-based duration estimate misses setup, evaluation, checkpointing and I/O. A CatBoost regressor using 24 features known before dispatch cut mean absolute error from 12.41 h to 1.71 h. Tested on: 272 SFT runs, models up to 15B, LoRA and full fine-tuning, one GPU type (H200) in one company cluster.

## Details

**Caveats**
SFT only (no RLHF, DPO or RLVR), one GPU type and one production environment. Only 13 runs exceeded 60 hours, where errors widen (median 5.19 h). Queue time is excluded. The full paper is not yet out.

**For your work**
Useful if you plan or quote fine-tuning jobs for clients: budget for overheads well beyond the FLOP estimate.

**Method**
- Treat end-to-end duration as supervised regression on pre-dispatch information: hyperparameters, dataset sizes, model identifiers, GPU allocation
- Add overhead features (evaluation volume, checkpoint count and size, per-GPU load) and the FLOP estimate as one feature
- Compare Linear Regression, Ridge, XGBoost and CatBoost against FLOP baselines at 30%, 45% and 60% MFU and an extended Calculon analytical model
- 5-fold stratified cross-validation over 272 runs on 1, 2 or 4 H200s

**Problem**
Schedulers on shared GPU clusters need job-duration estimates before dispatch, and the common FLOP-based estimate counts only training compute.

**Results**
- FLOP baseline at 30% MFU: R² 0.31, MAE 12.41 h; at 60% MFU: R² 0.01
- Calculon: R² -0.51, MAE 20.36 h; its estimates had a median of 11% of observed wall-clock time
- CatBoost (24 features): R² 0.98, MAE 1.71 h, median absolute error 0.51 h; XGBoost R² 0.97
- 80% of predictions within 2.20 h and 90% within 4.31 h; durations ranged from 1.6 to 172.4 h

**Concepts:** [[Post-training and RL]] · [[Inference efficiency]]
**From:** [[2026-11-20]]

# My notes


---
# References
[Hugging Face blog](https://huggingface.co/blog/Dharma-AI/predicting-fine-tuning-time)
