---
date: 2026-11-21
section: AI
importance: Med
kind: value
source: "Microsoft Fabric blog"
url: https://community.fabric.microsoft.com/t5/Fabric-Updates-Blog/Run-proactive-operations-with-Real-Time-Intelligence-in/ba-p/5414256
status: unread
id: 2026-11-21-fabric-rti-operations-agents
---
2026-11-21 07:16
Tags: #daily-knowledge #ai

---
# Fabric Real-Time Intelligence Operations Agent observability is GA, and agents can now rea

Microsoft's Real-Time Intelligence update makes Operations Agent observability generally available. It shows what an agent observed, decided and did, in Activity screens or a Workspace Monitoring eventhouse. Operations Agents can now use Fabric IQ ontologies as context (preview), and Activator can publish business events that other agents and flows subscribe to (GA).

## Details

**Availability and price**
Operations Agent observability, Activator business events, the IoT Hub endpoint, and Eventhouse CMK and outbound protection: GA. Ontology context, Event Hubs shortcuts and the AI custom visual builder: preview. Real-Time Intelligence itself is generally available. No pricing given.

**Caveats**
The ontology grounding is preview. Actions still rely on human approval by design.

**Client use cases**
- Supply chain: flag late shipments and start the response workflow before customers notice
- Data-centre or plant telemetry: predict failures and recommend actions, with every recommendation auditable
- Contact centre or IT ops: agents monitor service health and route approved actions
- Turn a detected condition into a business event that kicks off flows across teams

**How we could offer it**
- Proactive-operations pilot: stream existing Kafka, Event Hubs or IoT Hub data into Fabric and add an Operations Agent with approval steps
- Agent assurance: set up observability and audit reviews so clients can safely expand what agents do
- Ontology modelling so agents reason over business entities, not raw tables

**Pitch**
Move clients from reacting to alerts to agents that spot problems early and propose fixes, with a full audit trail of every decision.

**What it is**
Operations Agents in Fabric watch live event data against your goals, investigate changes and recommend next steps for human approval, for example in Teams. The update adds audit trails, ontology grounding, AI-generated custom dashboard visuals, Event Hubs shortcuts and a native IoT Hub routing endpoint.

**Concepts:** [[Power BI and Fabric]] · [[Agents]]
**From:** [[2026-11-21]]

# My notes


---
# References
[Microsoft Fabric blog](https://community.fabric.microsoft.com/t5/Fabric-Updates-Blog/Run-proactive-operations-with-Real-Time-Intelligence-in/ba-p/5414256)
