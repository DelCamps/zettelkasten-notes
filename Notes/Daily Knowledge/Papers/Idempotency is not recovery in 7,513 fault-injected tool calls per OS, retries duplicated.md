---
date: 2026-11-19
section: AI
importance: Med
kind: paper
source: "arXiv 2611.23353"
url: https://arxiv.org/abs/2611.23353
status: unread
id: 2026-11-19-idempotency-not-recovery
---
2026-11-19 07:16
Tags: #daily-knowledge #ai

---
# Idempotency is not recovery in 7,513 fault-injected tool calls per OS, retries duplicated

A fault-injection study of what happens when an agent's tool call is interrupted after it may already have changed an external system. A runtime with fail-closed authorisation, a durable action ledger, target-side idempotency keys, reconciliation and sealed evidence recorded 0/200 repeated effects versus 117/200 for simpler designs, but ran at about one-seventh of fail-open throughput. Tested on: one controlled single-host runtime on Windows and Linux, 10 fault classes, 96 captured responses from two models (not compared), 7,513 trials per platform.

## Details

**Caveats**
One implementation by the authors on a toy target (alerts, tickets, case states), single host, no comparison with existing agent frameworks; the two platforms are not independent replications.

**For your work**
For agents that write to client systems, idempotency keys alone are not enough: you also need a durable record of in-flight actions and a reconciliation step that asks the target what actually happened. Budget for the throughput cost.

**Method**
- Agent runtime with authorisation before dispatch, a reservation/in-flight/completed action ledger, SHA-256 idempotency keys checked by the target, post-crash reconciliation against target-side evidence, and an HMAC-sealed evidence journal.
- Ten injected fault classes (stale authority, crashes at several points, response loss, ledger and evidence-write failures, replay, tampering) against a controlled SQLite target with its own effect oracle.
- Four configurations and three ablations, 44 pre-specified comparisons per platform, model proposals captured once and reused.

**Problem**
When a tool call crashes or its response is lost, retrying can duplicate an action (two tickets, two payments) and assuming success can hide one that never happened. Most agent evaluations ignore this boundary.

**Results**
- Fail-closed authorisation blocked every injected unauthorised action (0/100 vs 100/100 for fail-open).
- Full runtime: 0/200 repeated effects on crash-and-replay vs 117/200 for each simpler baseline; without the ledger bundle 170/170 effects were orphaned and recovery fell from 300/300 to 200/300.
- Without reconciliation, 100/100 crash-after-effect cases stayed ambiguous although no duplicates occurred; injected evidence-write faults left 75/100 trials unresolved.

**Concepts:** [[Agents]] · [[Agent security]]
**From:** [[2026-11-19]]

# My notes


---
# References
[arXiv 2611.23353](https://arxiv.org/abs/2611.23353)
