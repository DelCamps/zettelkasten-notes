---
date: 2026-10-28
section: AI
importance: Low
kind: news
source: "Anthropic research"
url: https://www.anthropic.com/research/early-progress-drug-development
status: unread
id: 2026-10-28-anthropic-drug-development
---
2026-10-28 07:16
Tags: #daily-knowledge #ai

---
# Anthropic reports early drug-development results with Claude across six partners

Anthropic published case studies from BigHat, Bristol Myers Squibb, Divergence, Enveda, Generate Biomedicines and The Column Group. Highlights: about 35,000 antibody designs in a month, and a document review that caught 18 issues where humans found 11, cutting review time by 89%. All of it is preclinical.

## Details

**Caveats**
Results are self-reported by Anthropic and its partners, early, and without human trials. BigHat changed its success metrics midway.

**For your work**
The Enveda pattern is the one to reuse: an agent over a large regulated document set, with recall measured against human reviewers. It is a ready-made case study for life-sciences clients.

**Method**
- Claude Code used by scientists to redesign a CAR-T genetic element (Generate)
- Claude connected to BigHat's lab data system to propose variants, and it reanalyzed the raw assay data
- Claude linked to about 1,061 pages of manufacturing documents to flag issues and draft regulatory filings (Enveda)

**Problem**
Drug development has bottlenecks at every stage, from design to manufacturing paperwork to trial planning. Anthropic wanted to test whether Claude agents connected to lab data and documents can speed it up.

**Results**
- CAR-T element about 70% shorter, with about 10x receptor expression
- BigHat: about 1,010 variants in 10 weeks; best binders more than 10x tighter
- Enveda: caught all 11 issues humans found plus 7 they missed; review time down from 25h+ to under 3h; one filing drafted in 4h versus about 3 months

**Concepts:** [[AI for science and math]] · [[Agents]] · [[Claude]]
**From:** [[2026-10-28]]

# My notes


---
# References
[Anthropic research](https://www.anthropic.com/research/early-progress-drug-development)
