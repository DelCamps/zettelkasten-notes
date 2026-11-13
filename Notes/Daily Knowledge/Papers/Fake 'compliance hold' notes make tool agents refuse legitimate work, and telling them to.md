---
date: 2026-11-13
section: AI
importance: Med
kind: paper
source: "arXiv 2611.14864"
url: https://arxiv.org/abs/2611.14864
status: unread
id: 2026-11-13-warning-induced-over-abstention
---
2026-11-13 07:16
Tags: #daily-knowledge #ai

---
# Fake 'compliance hold' notes make tool agents refuse legitimate work, and telling them to

An attacker who can only write into a document the agent reads plants a fabricated compliance warning, and the agent stops doing a legitimate task. A 'prioritise caution' system prompt raised this induced over-abstention for all three models, for Gemini 3 Flash from 9.8% to 86.3% with clean-task completion unchanged. Asking agents to check warnings against authoritative records restored most completion. Tested on: 3 models from 3 families (DeepSeek V4 Pro, GPT-5.4, Gemini 3 Flash), 51 injectable AgentAbstain task pairs in about 21 MCP environments, one run per task except a 3-seed GPT-5.4 check.

## Details

**Caveats**
Provenance tags were oracle-provided, not authenticated. Several sub-experiments use only 7-16 task pairs. In the publishing environment, the defence did not consistently prevent confidential-data leaks.

**For your work**
'Be conservative' instructions in client agent prompts are an attack surface. Tell the agent to verify a risk claim against the system of record before it refuses, and test refusals as well as harmful actions.

**Method**
- Extended AgentAbstain tasks with variants: clean, false warning in a low-trust field, genuinely confidential content, and explicit versus factual wording of the same risk.
- Compared three prompts: baseline, caution-first, and provenance-aware 'Verify-Before-Abstain' with trust-tier tags.
- Also tested forged provenance tags and compromise of the authoritative record itself.

**Problem**
Prompt-injection work mostly asks whether injected text makes agents do harm. This paper studies the reverse, an availability attack: injected text that makes a compliant agent refuse legitimate work.

**Results**
- Caution-first raised over-abstention from 21.6% to 64.7% for DeepSeek V4 Pro and from 27.5% to 41.2% for GPT-5.4 (p<10^-4 each).
- On the document-analysis subset, provenance-aware verification raised false-warning task completion from 27% to 100% (DeepSeek), 33% to 73% (GPT-5.4) and 13% to 100% (Gemini).
- Forged in-band tags barely worked (0-20% abstention). Altering the authoritative record drove abstention to 93-100%.

**Concepts:** [[Agent security]] · [[AI safety]]
**From:** [[2026-11-13]]

# My notes


---
# References
[arXiv 2611.14864](https://arxiv.org/abs/2611.14864)
