---
date: 2026-11-21
section: AI
importance: Med
kind: news
source: "OpenAI"
url: https://openai.com/index/combatting-adversarial-distillation/
status: unread
id: 2026-11-21-openai-adversarial-distillation
---
2026-11-21 07:16
Tags: #daily-knowledge #ai

---
# OpenAI updated safeguards cut red-team extraction of GPT-6.2 Astra's hidden reasoning from

OpenAI describes how it fights adversarial distillation, where another model learns from its outputs without the safeguards: classifiers on inputs, outputs and tool-call arguments, API limits on reusing protected reasoning, and enforcement against account networks that ranges from thousands to tens of thousands of accounts a week. In adaptive black-box red-teaming across six attacker models, extracting protected reasoning from an earlier request fell from 54.0% on GPT-6 Astra with the original safeguards to 0.2% on GPT-6.2 Astra; a study found students trained on exact traces generally beat those trained on summaries in cyber tasks.

## Details

**Caveats**
All evaluations are internal with no external replication; success rates cover only the tested attacks. The transfer study uses one student and one recipe, and exact benchmark scores appear only in charts.

**For your work**
Expect reasoning traces from OpenAI models to stay hidden or summarized via the API, and tighter monitoring of bulk output use; client pipelines that distil from GPT outputs should check the terms and these new controls.

**Method**
- Request-level defenses: adversarial training, input and output classifiers including tool-call arguments, and API limits on reusing protected reasoning across users, organizations and model families.
- Campaign-level defenses: investigating coordinated extraction, enforcing against account networks, sharing indicators with other providers.
- Evaluation with replays of past attacks plus adaptive automated red-teaming, black-box and white-box.
- Cyber transfer study: students fine-tuned on exact reasoning traces vs reasoning summaries, then given light RL.

**Problem**
Rivals can train a second model on a frontier model's outputs, especially its chain-of-thought, copying capabilities such as cyber skills without the original safeguards.

**Results**
- Extracting protected reasoning from an earlier request: 54.0% (GPT-6 Astra, original safeguards) to 0.2% (GPT-6.2 Astra).
- From the current request: 22.9% to 0.9%.
- After fine-tuning, exact-trace students generally outperformed summary-trained ones; after RL they still scored higher at the largest inference budget on ExploitBench and SEC-bench Pro.

**Concepts:** [[AI safety]] · [[Agent security]] · [[Frontier models]]
**From:** [[2026-11-21]]

# My notes


---
# References
[OpenAI](https://openai.com/index/combatting-adversarial-distillation/)
