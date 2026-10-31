---
date: 2026-10-31
section: AI
importance: Med
kind: value
source: "Microsoft Fabric blog"
url: https://community.fabric.microsoft.com/t5/Fabric-Updates-Blog/Introducing-the-data-engineering-agent-for-Fabric-Project-Osmos/ba-p/5377944
status: unread
id: 2026-10-31-fabric-project-osmos
---
2026-10-31 07:16
Tags: #daily-knowledge #ai

---
# Microsoft Fabric previews Project Osmos a data-engineering agent that builds, runs and val

On 29 October Microsoft introduced Project Osmos, a data-engineering agent for Fabric built from its January 2026 acquisition of Osmos. You describe the outcome and the validation rules, and specialised agents write PySpark, run it in Fabric Spark, check the results and report back, as a persistent team task that consumes Fabric capacity. It gives our data practice a way to speed up Fabric migrations and pipeline fixes, with human review still built in.

## Details

**What it is**
A multi-agent orchestrator (knowledge, Spark worker and validation agents) that works on persistent tasks hosted in Fabric. It submits PySpark through the Fabric Livy API, so it tests on real data instead of only generating code. Before a task starts, you review guardrails: which resources it may use, where outputs go, staged versus in-place writes, rerun behaviour, whether schema changes are allowed, and the reasoning effort. You launch and steer it from GitHub Copilot CLI, Claude Code or Codex through the Skills for Fabric plugin, and you can disconnect while it keeps running. Teammates can join the same task, and it keeps state and history across new data drops. In the same week Microsoft also released the Fabric Notebook Toolkit (FNTK, preview), a CLI that lets coding agents run and debug single notebook cells.

**Client use cases**
- Insurance or post-merger data consolidation: reconcile policy and claims data from SAP, Guidewire and Oracle into a validated view
- Converting existing pipelines to incremental loads and checking rerun behaviour
- Optimising Spark notebooks and Delta tables in an existing lakehouse
- Migrating data-engineering workloads from another platform to Fabric while preserving business rules

**How we could offer it**
- Accelerated Fabric migration: our engineers set the outcomes, guardrails and validation rules, and Osmos does the bulk of the implementation
- Data-agent governance: permission design, staging-only write patterns, evidence review, and capacity (CU) cost control
- A pilot on one messy domain (claims, finance) to measure speed and quality against a manual baseline

**Pitch**
Microsoft's new Fabric agent, Project Osmos, builds and actually validates Spark pipelines against the client's own lakehouse data, and we steer it from Copilot CLI or Claude Code. I think we could package it as a faster, cheaper Fabric migration and data-quality offer and try it on one client domain first.

**Availability and price**
Preview (the post points to preview limitations in the quickstart). It needs Contributor or higher workspace permissions, the required tenant settings and an eligible Fabric capacity; trial capacities are not supported. Tasks consume Fabric capacity units (CUs), and the post gives no separate price.

**Caveats**
Preview only, so check the quickstart for limits and region availability. The guardrail instructions are not a substitute for access controls: the agent runs with the user's permissions. Compute and reasoning effort burn capacity, and the team still owns acceptance of results. Competitors: Databricks Genie Code, Snowflake Cortex agents.

**Concepts:** [[Power BI and Fabric]] · [[Multi-agent systems]] · [[Coding agents]]
**From:** [[2026-10-31]]

# My notes


---
# References
[Microsoft Fabric blog](https://community.fabric.microsoft.com/t5/Fabric-Updates-Blog/Introducing-the-data-engineering-agent-for-Fabric-Project-Osmos/ba-p/5377944)
