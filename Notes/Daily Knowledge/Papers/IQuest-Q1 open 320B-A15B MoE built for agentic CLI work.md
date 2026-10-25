---
date: 2026-10-24
section: AI
importance: Med
kind: paper
source: "arXiv 2610.30949"
url: https://arxiv.org/abs/2610.30949
status: unread
id: 2026-10-24-iquest-q1
---
2026-10-24 07:16
Tags: #daily-knowledge #ai

---
# IQuest-Q1 open 320B-A15B MoE built for agentic CLI work

Open-source sparse MoE with 15B active parameters and long context, trained with a coding-heavy curriculum, then SFT, domain RL and on-policy distillation across several agent scaffolds, with checkpoint merging. Reported scores include 83.2% on Terminal-Bench 2.1 and 57.5 on SWE-Bench Pro: a candidate self-hostable coding-agent backbone.

## Details

**Problem**
IQuest is releasing an open model built specifically for agentic work in command-line interfaces (coding, tool use, terminal tasks) that holds up across different agent harnesses.

**Method**
- A sparse MoE with 320B total and 15B active parameters (256 experts, 8 active), using hybrid 3:1 sliding-window and full attention. Pre-trained with Muon and muP, and a second stage that raises the share of coding data.
- Mid-training broadened the data mix and extended the context step by step. SFT used 240B+ and 50B+ tokens, followed by RL on episodes spanning Claude Code, Codex and their versions.
- Multi-teacher on-policy distillation from four frozen experts (UX, multi-harness, long-horizon, general), then merging of checkpoints across stages.

**Results**
- Terminal-Bench 2.1: 83.2 (Claude Opus-5 89.1, GLM-5.3 Flash 84.3). SWE-Bench Pro: 57.5 (Opus-5 79.2, GLM-5.3 Flash 59.4).
- DeepSWE v1.1 64.6, NL2Repo 63.0, CyberGym 84.5, BrowseComp 85.5, tau3-Banking 51.8 (above Opus-5's 44.7).
- Weaker on harder terminal suites: 17.9 on Terminal-Bench 3.0 and 22.7 on 4.0, against 42.7 and 53.9 for Opus-5.

**Caveats**
Text-only input. Tool calls use an IQuest-specific chat-template format that needs compatible serving parsers. The authors say it may overlook constraints or repeat failed attempts on real CLI tasks. Some competitor scores come from the authors' own testing, and IQuest-CLIBench is in-house.

**For your work**
A self-hostable backbone to try for coding or ops agents: 15B active parameters keeps serving cost down. Check that your serving stack parses its tool-call format before you benchmark it in your own harness.

**Concepts:** [[Open-weight models]] · [[Coding agents]] · [[Mixture of Experts]] · [[Post-training]]
**From:** [[2026-10-24]]

# My notes


---
# References
[arXiv 2610.30949](https://arxiv.org/abs/2610.30949)
