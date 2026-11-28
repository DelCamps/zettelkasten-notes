---
date: 2026-11-27
section: AI
importance: Med
kind: paper
source: "arXiv 2611.30483"
url: https://arxiv.org/abs/2611.30483
status: unread
id: 2026-11-27-agent-database-damage
---
2026-11-27 07:16
Tags: #daily-knowledge #ai

---
# When an agent breaks a production database, the engine's undo features and permissions dec

A preregistered study replays 22 scripted mistakes on four SQL engines and runs a small tool-calling agent on hazardous tasks across PostgreSQL, MySQL, SQLite, ClickHouse, Cassandra, MongoDB, Valkey, Kafka and OpenSearch. Out of the box, engines differ less in what a mistake destroys than in what they let you undo: Cassandra's default auto_snapshot and ClickHouse's UNDROP turned the highest raw losses into the lowest permanent ones, and least-privilege identities cut Kafka's permanent loss from 11.3% to 0%. Tested on: six small open-weight models (4B-12B, plus a 35B MoE), nine engines, 9,468 trials, three seeds; no frontier models.

## Details

**Caveats**
Six small 4-bit models on one machine; frontier models and commercial agents not tested. Only three of seven hypotheses met their rule. Trials are clustered (36 task instances per engine), so several permission effects do not survive instance-level analysis.

**For your work**
A checklist for client agents with database tools: enable the vendor's minimum backup and change log, keep backups outside the agent's identity, use least-privilege roles that withhold destructive operations, diff state instead of trusting the agent's report, and make sure no readable admin credentials exist.

**Method**
- Layer A: a frozen library of 22 canonical mistakes applied by script (no model) to four relational engines under five permission arms and two recovery arms, then an engine-native recovery drill.
- Layer B: a minimal tool-calling agent on tasks containing hazards (injected notes, a planted admin credential, a change freeze) across nine engines, 9,468 trials.
- Seven preregistered hypotheses with decision rules; deviations dated and reported.

**Problem**
Agents now run statements against production databases and several incidents deleted production data. Is the damage decided by the model, a guard layer, or the database engine?

**Results**
- Default setup, permanent canary loss: MySQL 15.3%, SQLite 15.5%, PostgreSQL 13.7%, Cassandra 0% (auto_snapshot before TRUNCATE and DROP), ClickHouse 3.9% (UNDROP within 480 s).
- Least-privilege identity: Kafka 11.3% to 0%, Valkey 13.2% to 0.2%, MongoDB 6.9% to 0.2%; on PostgreSQL and MySQL most original-row loss came from deletes still allowed.
- Vendor minimum backup with change log removed every loss of protected rows on all four relational engines in Layer A.
- More than half of loss trials lost only a backup copy kept in the same namespace and identity the agent used.

**Concepts:** [[Agent security]] · [[AI safety]] · [[Agents]]
**From:** [[2026-11-27]]

# My notes


---
# References
[arXiv 2611.30483](https://arxiv.org/abs/2611.30483)
