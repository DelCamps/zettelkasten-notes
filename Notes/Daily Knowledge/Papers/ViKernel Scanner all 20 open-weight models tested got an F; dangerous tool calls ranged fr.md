---
date: 2026-11-19
section: AI
importance: Low
kind: paper
source: "Hugging Face blog"
url: https://huggingface.co/blog/FINAL-Bench/we-handed-20-open-models-a-shell-20-of-them-failed
status: unread
id: 2026-11-19-vikernel-scanner-20-open-models
---
2026-11-19 07:16
Tags: #daily-knowledge #ai

---
# ViKernel Scanner all 20 open-weight models tested got an F; dangerous tool calls ranged fr

FINAL-Bench/VIDRAFT gave models eight mock tools and ran 100 attack checks (disguised shell commands, planted instructions, secret exfiltration) plus normal-work controls; all 20 open models scored F, and the median model attempted a dangerous action in 40 of 100 checks. The vendor says its own in-weights firewall would have denied 897 of 897 dangerous calls. Tested on: 20 open-weight models via the Hugging Face router, one scan each on 2026-11-18, 100 checks plus 20 controls.

## Details

**Caveats**
This is a vendor post promoting its own firewall, and the check set is served centrally rather than published. The weakest-domain grading makes a near-uniform F likely. Each model got one scan with mock tools, and the firewall result is a replay, not an independent test. No closed models were in the reference table.

**For your work**
The free scanner works with any OpenAI-compatible endpoint, so it gives a quick smoke test before giving an open model shell or mail tools. The spread between models (1 to 98 of 100) is a reminder that model choice matters, but an action-level gate outside the model is still needed.

**Method**
- 8 mock tools (list files, read file, web search, weather, send mail, HTTP post, run shell, transfer funds) and a mock workspace config file holding fake keys; temperature 0, up to 4 steps
- Checks: 10 hackathon starter prompts plus 90 disguised shell commands from 8 attack families, each wrapped in one of 13 disguises (base64, hex, ROT13, reversed text...)
- Each domain is graded by the deepest stage reached; one F domain makes the overall grade F
- Example stage-4 finding: a reversed, base64-encoded delete command piped through rev | base64 -d | bash, which the model sends to the shell tool

**Problem**
Most safety evals score what a model says. This one scores what a tool-using model actually tries to do when it is attacked.

**Results**
- 20 of 20 models graded F; every model failed the command-execution domain
- Dangerous checks hit ranged from 1 / 100 (moonshotai/Kimi-K3) to 98 / 100 (deepseek-ai/DeepSeek-V3.2); Llama-3.3-70B-Instruct and Qwen2.5-72B-Instruct hit 90 / 100
- The EchoLeak pattern reproduced: asked only to summarise a mail, models followed a planted note and made an unrequested call
- Replaying the findings against the vendor's ViKernel Firewall: 897 of 897 dangerous calls denied

**Concepts:** [[Agent security]] · [[Evals and benchmarks]] · [[Open-weight models]]
**From:** [[2026-11-19]]

# My notes


---
# References
[Hugging Face blog](https://huggingface.co/blog/FINAL-Bench/we-handed-20-open-models-a-shell-20-of-them-failed)
