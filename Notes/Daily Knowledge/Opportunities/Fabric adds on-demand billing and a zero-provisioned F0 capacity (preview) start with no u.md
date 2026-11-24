---
date: 2026-11-24
section: AI
importance: Med
kind: value
source: "Microsoft Fabric blog"
url: https://community.fabric.microsoft.com/t5/Fabric-Updates-Blog/Fabric-on-demand-billing-and-Zero-provisioned-F0-Capacity/ba-p/5377585
status: unread
id: 2026-11-24-fabric-f0-on-demand-billing
---
2026-11-24 07:16
Tags: #daily-knowledge #ai

---
# Fabric adds on-demand billing and a zero-provisioned F0 capacity (preview) start with no u

Microsoft Fabric now offers on-demand billing per workload category (for example Data Warehouse or Data Factory), metered in unsmoothed CU-hours at 1x to 3x the pay-as-you-go CU price, plus a new F0 SKU with no upfront compute-capacity charge. Admins can set spend limits over a rolling 24-hour window, and the existing F2 to F8192 SKUs remain.

## Details

**Availability and price**
Preview. On-demand usage is billed in CU-hours at 1x to 3x the regional pay-as-you-go CU price depending on the billing category; storage is separate. On-demand billing for Apache Spark (formerly autoscale billing) stays GA with unchanged pricing. The post does not list regions.

**Caveats**
- Preview, and up to 3x the pay-as-you-go rate: steady workloads are still cheaper on a reserved SKU
- Usage is not smoothed, so spikes hit the bill directly
- When the 24-hour limit is reached new operations pause, which needs to be designed for

**Client use cases**
- Start a Fabric pilot or proof of concept with no reserved capacity, so the client pays only for what the pilot uses
- Isolate a seasonal or spiky workload (month-end close, a promotion) from steady reporting without buying a bigger SKU
- Give development and test workspaces cheap capacity while production stays on a reserved F SKU

**How we could offer it**
- Fabric cost and capacity assessment: which workloads are steady vs bursty, and the break-even between reserved and on-demand
- Low-commitment Fabric pilot offer built on F0, with spend limits and a FinOps dashboard from the Capacity Metrics App
- Ongoing FinOps managed service for Fabric; skills: Fabric admin, capacity planning, cost modelling

**Pitch**
Fabric's new F0 capacity removes the upfront capacity cost, so we can start client pilots without a reserved SKU. Paired with a spend-limit setup, it is an easy, low-risk way into Fabric deals.

**What it is**
A new way to consume Fabric. F0 is a zero-provisioned capacity where every workload category runs on on-demand billing only. Existing F2+ capacities can move selected categories onto on-demand billing so bursty workloads stop competing for the shared capacity. Usage is measured in CU-hours without smoothing, priced as a multiplier (1x to 3x, by category) of the regional pay-as-you-go CU price, with storage billed separately. Spend limits pause new operations once reached, and a new 'On-demand compute' tab in the Capacity Metrics App shows usage per category.

**Concepts:** [[Power BI and Fabric]]
**From:** [[2026-11-24]]

# My notes


---
# References
[Microsoft Fabric blog](https://community.fabric.microsoft.com/t5/Fabric-Updates-Blog/Fabric-on-demand-billing-and-Zero-provisioned-F0-Capacity/ba-p/5377585)
