---
date: 2026-11-17
section: AI
importance: Med
kind: paper
source: "arXiv 2611.17880"
url: https://arxiv.org/abs/2611.17880
status: unread
id: 2026-11-17-soteria-verified-plans
---
2026-11-17 07:16
Tags: #daily-knowledge #ai

---
# Soteria formally verifying an agent's plan before any tool call gave zero policy violation

Soteria turns policy documents into formal specifications, verifies a hierarchical plan against them before execution, and blocks any off-spec tool call at runtime while using the plan to recover. On tau2-Airline, tau2-Retail and Toolathlon it reached 100% conformance while baselines topped out at 93%. Tested on: 4 models from 3 providers (GPT-5.4-mini, Gemini 3 Flash, Claude Haiku 4.5, Claude Opus 4.6), 207 tasks across 3 benchmarks, pass@1 at temperature 0, against NeMo Guardrails, AgentSpec and ABC.

## Details

**Caveats**
Specifications need manual validation, and the authors corrected mis-encoded specs while auditing results; higher cost on conversational tasks because it re-plans each turn; mostly single runs.

**For your work**
For regulated client workflows (bookings, refunds, claims), encoding policy as checkable specs plus a deterministic monitor is a stronger offer than an LLM judge guardrail, and it keeps task success.

**Method**
- One-time setup: LLM-assisted formalisation of policy and tool contracts into specifications (24, 33 and 41 formulas per benchmark), validated by hand.
- A planner composes pre-verified sub-plans; a verifier checks tool preconditions, progress and policy compliance and feeds diagnostics back for repair (8 retries).
- A runtime SpecMonitor blocks violating calls; the executor follows the verified plan to recover.

**Problem**
Runtime guardrails can block an unsafe action but leave the agent stuck, so teams trade safety against task completion.

**Results**
- Success gains of 4.7-43.9 percentage points over the best baseline per model-benchmark pair, 1.7 times on average.
- Claude Opus 4.6 reached 88.0% on tau2-Airline and 90.4% on tau2-Retail, against 56.0% and 46.5% for the best baselines; Haiku 4.5 reached 70.0% vs 30.0%.
- On Toolathlon, unguarded Opus lost more than half its 30.2% raw utility to violations; Soteria scored 9.3-18.6% with zero violations.

**Concepts:** [[Agent security]] · [[Agents]] · [[AI safety]]
**From:** [[2026-11-17]]

# My notes


---
# References
[arXiv 2611.17880](https://arxiv.org/abs/2611.17880)
