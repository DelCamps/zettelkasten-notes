---
date: 2026-10-23
section: AI
importance: Low
kind: paper
source: "arXiv 2610.30120"
url: https://arxiv.org/abs/2610.30120
status: unread
id: 2026-10-23-alps-encoder
---
2026-10-23 07:16
Tags: #daily-knowledge #ai

---
# ALPS one ViT-B encoder for world models

Its patch tokens are trained for physical-state prediction, text alignment and pixel reconstruction at once. It matches the ~3.5x larger V-JEPA 2-L on LIBERO state probing and reaches 85.5% LIBERO policy success with frozen tokens.

## Details

**Caveats**
Only ViT-B and simulation benchmarks; no real robots. ImageNet zero-shot accuracy (73.4) trails PE-Core (78.4). With no video pretraining it is less sensitive to fine-grained temporal actions.

**For your work**
Little direct use unless a client project involves robotics or embodied agents. In that case it is a single encoder that handles language instructions and visual inspection of predicted frames.

**Method**
- Stage 1: train a ViT-B/16 from scratch on DataComp-1B images with contrastive alignment, captioning, pixel reconstruction and dense cross-view correspondence losses, all on the same patch tokens.
- Stage 2: cross-view self-distillation on 5M single images, where a student predicts a frozen Stage 1 teacher's patch tokens across crops, scales and photometric changes.
- Trained on still images and text only, with no video or interaction data; compared against 15 public encoders, all frozen.

**Problem**
World models usually sit on a frozen visual encoder, but current encoders tend to give only one or two of: physical-state information, language alignment, and pixel reconstruction. Pushing an image-text encoder toward state information can damage its language alignment.

**Results**
- Lowest aggregate LIBERO state-probe error among ViT-B encoders (.829 vs .864 for C-RADIOv3 and .870 for DINOv3), matching the ~3.5x larger V-JEPA 2-L.
- 85.5% mean LIBERO policy success with frozen tokens and its own text tower (83.4% with BERT instructions).
- Stage 2 cuts state error by 17% while moving retrieval by at most 0.5 points; the same refinement costs SigLIP 2 and CLIP 4-12 points.
- 90% PushT and 92% Wall planning success (both ties for best); predicted future tokens can be decoded back into images.

**Concepts:** World models · Vision encoders
**From:** [[2026-10-23]]

# My notes


---
# References
[arXiv 2610.30120](https://arxiv.org/abs/2610.30120)
