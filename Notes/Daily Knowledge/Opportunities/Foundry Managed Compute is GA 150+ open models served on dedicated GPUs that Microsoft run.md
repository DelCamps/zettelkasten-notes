---
date: 2026-11-22
section: AI
importance: High
kind: value
source: "Microsoft Foundry blog"
url: https://devblogs.microsoft.com/foundry/managed-compute-ga/
status: unread
id: 2026-11-22-foundry-managed-compute-ga
---
2026-11-22 07:16
Tags: #daily-knowledge #ai

---
# Foundry Managed Compute is GA 150+ open models served on dedicated GPUs that Microsoft run

Microsoft Foundry's Managed Compute is now generally available. Clients pick an open model and Microsoft provisions the GPUs, maintains the containers and runs the serving stack. The catalog has 150+ open models on NVIDIA A100, H100 or H200 or AMD MI300X GPUs, with US and EU Data Zones. LoRA adapter serving is in preview, and Bring Your Own Weights is in limited preview.

## Details

**Availability and price**
Generally available. You pay hourly for each accelerator, and the deployment wizard shows the hourly cost. US and EU Data Zones are available. It needs Managed Compute GPU quota. LoRA adapter serving is in preview, and Bring Your Own Weights is in limited public preview (sign-up).

**Caveats**
You pay for dedicated GPUs whether or not they are busy, so low or spiky traffic may cost more than pay-per-token APIs. The performance result (one DeepSeek V4.1 Flash instance on four MI300X GPUs supported 128 concurrent agents, matching Signal65's tuned self-hosted setup) comes from a vendor-commissioned study.

**Client use cases**
- Sovereign or EU-resident workloads that need open models instead of hosted frontier APIs
- High-volume batch extraction or classification where a dedicated open model costs less per token
- Serving client fine-tunes (LoRA adapters from Foundry post-training) next to the base model
- Search pipelines using the NVIDIA Nemotron 3.5 Embed, Rerank and Parse models

**How we could offer it**
- Model-selection and TCO assessment: an open model on Managed Compute versus GPT or Claude per use case, sized with a representative load test
- Pilot: deploy one open model in the client's Foundry project with Azure Monitor dashboards for throughput, 429 errors and latency
- Managed service: model lifecycle, adapter deployment and GPU quota and cost governance

**Pitch**
Microsoft now runs open models for clients on dedicated GPUs inside Foundry, with EU Data Zones and a vetted supply chain. We can offer an 'open-model landing zone' for clients who want control or lower unit cost without running Kubernetes themselves.

**What it is**
A managed way to serve open-weight models in Foundry. You choose a model and a deployment template (context length, runtime, GPU configuration), and Foundry runs it behind an OpenAI-compatible endpoint. To scale, you add instances behind the same endpoint. Prompt-aware routing sends requests that share a prefix to the same instance, so the prompt cache is reused. Speculative decoding is turned on for leading models. Microsoft reviews each model's licence, screens it for untrusted code, validates the SafeTensors weights, and signs and patches the serving images.

**Concepts:** [[Open-weight models]] · [[Inference efficiency]]
**From:** [[2026-11-22]]

# My notes


---
# References
[Microsoft Foundry blog](https://devblogs.microsoft.com/foundry/managed-compute-ga/)
