---
date: 2026-11-04
section: AI
importance: Low
kind: value
source: "Databricks blog"
url: https://www.databricks.com/blog/claude-platform-now-supports-native-opentelemetry-observability-databricks-mlflow
status: unread
id: 2026-11-04-databricks-mlflow-claude-otel
---
2026-11-04 07:16
Tags: #daily-knowledge #ai

---
# Databricks MLflow now ingests Claude Platform OpenTelemetry traces natively for agent debu

Databricks says Claude Platform's native OpenTelemetry export can now send traces straight into MLflow, stored in Unity Catalog tables. Messages API, SDK and Claude Managed Agents spans arrive through Zerobus Ingest, and teams can then use trace analysis, MLflow Issues, review queues and LLM-judge evaluations. The OTel export is in public beta.

## Details

**Availability and price**
OpenTelemetry for Claude Platform is in public beta, and MLflow Issues is in beta. No pricing or GA date is given.

**Caveats**
This is a beta integration published by Databricks. Inputs and outputs are captured only with content mode set to 'full', which raises data-handling questions. The post gives no throughput or latency figures.

**Client use cases**
- Clients on Databricks building Claude agents who want traces, debugging and evals in one governed place
- Routing failed agent runs to domain experts through review queues
- Side-by-side evaluation of baseline and revised agents with LLM judges

**How we could offer it**
- Agent observability setup as part of a Claude-on-Databricks build
- Evaluation service: build judges and review queues on top of production traces
- Skills needed: OpenTelemetry, MLflow, Unity Catalog

**Pitch**
For Claude agents on Databricks clients, we can now wire production traces straight into MLflow and Unity Catalog. That gives a governed eval and debugging loop without third-party tooling.

**What it is**
This is an integration between Claude Platform's OTel export and Databricks MLflow. Claude's instrumentation emits spans for model requests and tool calls over the OpenTelemetry Protocol. Databricks ingests them through Zerobus Ingest into Unity Catalog tables linked to MLflow experiments, with Unity Catalog access control and SQL querying. Setup has 3 steps: create an experiment, configure the export (workspace ID, region, spans table, table-scoped OAuth token), then run and inspect. Claude Code and the Claude Agent SDK can send traces to the same destination.

**Concepts:** [[Claude]] · [[Evals and benchmarks]]
**From:** [[2026-11-04]]

# My notes


---
# References
[Databricks blog](https://www.databricks.com/blog/claude-platform-now-supports-native-opentelemetry-observability-databricks-mlflow)
