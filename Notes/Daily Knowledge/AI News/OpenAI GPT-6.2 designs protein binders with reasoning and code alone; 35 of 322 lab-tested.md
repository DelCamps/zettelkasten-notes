---
date: 2026-11-26
section: AI
importance: Med
kind: news
source: "OpenAI"
url: https://openai.com/index/gpt-6-models-demonstrate-intrinsic-protein-design-capabilities/
status: unread
id: 2026-11-26-gpt6-protein-design
---
2026-11-26 07:16
Tags: #daily-knowledge #ai

---
# OpenAI GPT-6.2 designs protein binders with reasoning and code alone; 35 of 322 lab-tested

OpenAI reports that GPT-6 models designed protein shapes and sequences using only reasoning and general-purpose code, then tested them in a wet lab with partner Onava. 35 of 322 minibinders bound five targets, and redesigned antibody fragments bound in 66-70% of cases; on PoseBusters docking GPT-6.2 scored 93% against 50% for DiffDock-L. Structure prediction remains weak (TM-score 0.26 against 0.93 for ESMFold2).

## Details

**Problem**
Protein design normally relies on specialised models such as RFdiffusion and ProteinMPNN; OpenAI tested whether a general LLM can do the design itself.

**Method**
- GPT-6.2 (pre-release) and an unnamed internal model designed backbones and sequences without calling biology models for generation
- Specialised models were still used in the lab workflow to suggest sequences (SolubleMPNN, ProteinMPNN) and filter candidates (Boltz-2, ESMFold2 and others)
- Wet-lab binding tests with Onava; computational benchmarks against RFdiffusion, Proteina, DiffDock and ESM models

**Results**
- Minibinders: 35 of 322 bound (10.9%) across PD-L1, IL-7Rα, TrkA, VEGF-A and IL-17A
- Antibody loop redesign: 128 of 182 (70%) bound; therapeutic antibody fragments 179 of 272 (66%)
- Docking (PoseBusters): GPT-6.2 93%, internal model 96%, DiffDock-L 50%; motif scaffolding: internal 43.7% vs RFdiffusion 27.8%
- Structure prediction from sequence: GPT-6.2 TM-score 0.26 vs ESMFold2 0.93

**Caveats**
The lab pipeline still used specialised models, so this is not end-to-end zero-shot design. Some results may reflect memorisation of public structures. Binding is only a first step; specificity, stability and safety are untested. Hit rates are not comparable with the original RFdiffusion study.

**For your work**
Useful for pharma and life-science conversations: general frontier models are becoming credible design assistants, but specialised tools still win on structure prediction.

**Concepts:** [[AI for science and math]] · [[Frontier models]]
**From:** [[2026-11-26]]

# My notes


---
# References
[OpenAI](https://openai.com/index/gpt-6-models-demonstrate-intrinsic-protein-design-capabilities/)
