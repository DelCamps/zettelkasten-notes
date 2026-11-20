---
date: 2026-11-20
section: AI
importance: Med
kind: paper
source: "Hugging Face blog"
url: https://huggingface.co/blog/animesh1986/traceground-what-a-model-free-check-catches-in-rea
status: unread
id: 2026-11-20-traceground-grounding-check
---
2026-11-20 07:16
Tags: #daily-knowledge #ai

---
# traceground a model-free grounding checker caught 80% of planted errors on held-out answer

An independent researcher released traceground, a deterministic Python checker (standard library only, no API key) that compares an agent's answer with its sources and tool calls and flags unsupported numbers, quotes, field assignments, units and tools that were mentioned but never called. On held-out planted errors it caught 262/327 (80%). On the RAGTruth test split, 7 of its 172 high-severity findings were false alarms (4%). Tested on: answers from 6 models in 3 families (RAGTruth, 2,675 answers) plus a live test of 2 gpt-oss models on 20 questions.

## Details

**Caveats**
It does not check claims made in words, which is most of what RAGTruth marks, and needs sources or tool calls to say anything. It flags true facts not drawn from tools. Rules were tuned on the held-out set after a first blind run, so only the RAGTruth results are fully blind. Single author, version 0.1.0.

**For your work**
A cheap, deterministic post-check for numbers and tool arguments in agent answers (finance, ops reports) before or alongside an LLM judge.

**Method**
- Deterministic, model-free checks of an answer against its sources or tool-call trace: unsupported numbers, quotes, values and arguments, plus field assignment, units, failed calls presented as successes and tools mentioned but never called
- Live agent test: gpt-oss-120b and gpt-oss-20b answered 20 held-out questions with made-up deterministic tools
- RAGTruth test split: 2,675 answers (QA 875, Summary 900, Data-to-text 900) from GPT-3.5, GPT-4, Llama-2 7B/13B/70B and Mistral 7B
- Planted-error tests: 657 development answers and 327 held-out answers

**Problem**
Agents can call the right tools and still answer wrongly: a value in the wrong field, the wrong currency, wrong tool arguments, arithmetic slips, or a failed call reported as a success. A check that only asks whether each number appears in the evidence misses these.

**Results**
- Planted errors caught: 600/657 (91%) in development, 262/327 (80%) held-out
- RAGTruth: 172 high-severity findings, 7 of them false alarms (4%)
- Of 306 human-marked spans containing a digit, it flagged 85 (28%)
- Precision against human marks: 59% to 90% by task; a hand review found many real issues the human marks missed

**Concepts:** [[Hallucination]] · [[Evals and benchmarks]] · [[Agents]]
**From:** [[2026-11-20]]

# My notes


---
# References
[Hugging Face blog](https://huggingface.co/blog/animesh1986/traceground-what-a-model-free-check-catches-in-rea)
