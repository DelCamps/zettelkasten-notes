---
date: 2026-11-13
section: AI
importance: Low
kind: paper
source: "OpenAI Alignment blog"
url: https://alignment.openai.com/fuzzy-robustness/
status: unread
id: 2026-11-13-openai-fuzzy-robustness
---
2026-11-13 07:16
Tags: #daily-knowledge #ai

---
# OpenAI trains jailbreak resistance on attacks its own models find, and says GPT-6 Astra an

OpenAI's alignment team used a helpful-only GPT-5.6 Sol-family reasoning model as an automated red-teamer, in a PAIR-like loop with scaled test-time compute. It kept only jailbreaks that succeed across repeated tests ('worst@n') and used the hardened prompts for RL safety training, which OpenAI says went into GPT-6 Astra and Sol without more refusals of benign requests. Tested on: OpenAI models only (GPT-5.4 and 5.5 as defenders); run counts are not given and exact results are only in charts.

## Details

**Caveats**
Measures the model layer only, without production safeguards. Only one model family. Dataset size, n and run counts are not stated.

**For your work**
Little direct use. It does suggest newer GPT-6 models should hold up better against multi-turn misuse in client deployments, but keep your own guardrail layer.

**Method**
- An attacker model iteratively rewrites a seed prompt until defender models (GPT-5.4, GPT-5.5) give an unsafe answer. The worked example reaches harmful anthrax-dispersal help via a 'generic' airflow maths problem by attempt 21.
- Only attacks that succeed across repeated tests (worst@n) are kept, producing 'robustified' prompts for RL.
- A controlled RL study evaluates against fixed jailbreaks from a held-out attacker and the worst of 12 adaptive multi-turn attacker personas.

**Problem**
In dual-use areas such as cyber and biology, the line between safe and unsafe help is fuzzy, and models that refuse plain requests can still be talked into harmful help by persistent attackers.

**Results**
- Robustified prompts start training at much lower safety scores than the original seeds and improve over the run.
- The robustness-trained run beat the baseline on held-out fixed jailbreaks and on adaptive attackers. Exact values are only in figures.
- On the cyber fixed-jailbreak set, OpenAI's chart shows GPT-6 Astra well ahead of GPT-5.6 Sol (exact values only in the figure).

**Concepts:** [[AI safety]] · [[Post-training and RL]]
**From:** [[2026-11-13]]

# My notes


---
# References
[OpenAI Alignment blog](https://alignment.openai.com/fuzzy-robustness/)
