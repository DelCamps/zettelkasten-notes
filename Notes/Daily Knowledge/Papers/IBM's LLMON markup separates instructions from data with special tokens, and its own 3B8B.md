---
date: 2026-11-13
section: AI
importance: Low
kind: paper
source: "Hugging Face blog (IBM Granite)"
url: https://huggingface.co/blog/ibm-granite/llmon-an-llm-native-markup-language-now-in-granite
status: unread
id: 2026-11-13-ibm-llmon-markup
---
2026-11-13 07:16
Tags: #daily-knowledge #ai

---
# IBM's LLMON markup separates instructions from data with special tokens, and its own 3B8B

IBM Granite released LLMON, an XML-like prompt markup whose delimiters are reserved single tokens. An execution block binds each instruction to the data it acts on, and anything not bound is meant to be read, never obeyed. On the OPI benchmark, the two preview models avoided 47% more attacks than the best frontier model IBM tested and 95% more than the best open model, with general capability reported on par with Granite 4.1 Instruct. Tested on: IBM's own granite-4.1-3b/8b LLMON previews against unnamed frontier and open models, static indirect injections only (OPI, with similar trends on ASB and StruQ).

## Details

**Caveats**
Experimental preview, not for production. The compared models are not named in the text. Adaptive multi-turn attacks are untested. IBM itself calls the separation 'a learned behavior, not an enforced guarantee'.

**For your work**
It is worth watching as a design pattern: binding instructions to data at the token level rather than in the prompt text. Not deployable for clients yet, and a small model with learned separation does not replace tool-permission controls.

**Method**
- Six delimiters added to the tokenizer as reserved tokens, short two-token block IDs, and an exec block naming the instruction, its inputs, its requirements and where the output goes.
- Post-trained from Granite 4.1 base on an instruction corpus re-serialised into LLMON, with decoy unbound instructions, then five GRPO stages and DPO on a thousand on-policy preference pairs built from injection attempts.
- Ships a chat template, lossless JSON-to-LLMON converters and a ScienceWorld LoRA example for custom tag vocabularies.

**Problem**
Prompts mix instructions, retrieved documents, tool outputs and requirements as flat text or JSON, whose structural characters also appear in normal text. Models cannot reliably tell what to obey from what to read, which is what prompt injection exploits.

**Results**
- OPI robustness: 47% more attacks avoided than the best tested frontier model and 95% more than the best open-source model. Exact percentages appear only in charts.
- Some benchmarks saw attack success fall to nearly zero.

**Concepts:** [[Agent security]] · [[Structured outputs]] · [[Open-weight models]]
**From:** [[2026-11-13]]

# My notes


---
# References
[Hugging Face blog (IBM Granite)](https://huggingface.co/blog/ibm-granite/llmon-an-llm-native-markup-language-now-in-granite)
