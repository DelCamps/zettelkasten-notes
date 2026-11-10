---
date: 2026-11-10
section: AI
importance: Med
kind: value
source: "AWS What's New"
url: https://aws.amazon.com/about-aws/whats-new/2026/11/nitro-sandboxes-eks-ecs-ec2/
status: unread
id: 2026-11-10-aws-nitro-sandboxes
---
2026-11-10 07:16
Tags: #daily-knowledge #ai

---
# AWS Nitro Sandboxes hardware-isolated VMs for each pod, task or VM to run agents and AI-ge

AWS launched Nitro Sandboxes, lightweight VMs managed by the Nitro Hypervisor that give each EKS pod, ECS task or EC2 VM its own hardware-isolated environment. EKS and ECS need a one-line change. AWS pitches it for running agents and AI-generated code in isolation while sharing one instance across many agentic workloads.

## Details

**Availability and price**
Announced 9 Nov 2026 as 'available today' in all commercial AWS Regions, at no additional charge. The announcement does not use the term GA.

**Caveats**
Infrastructure building block, not a turnkey agent product. Check supported instance types and how it fits with the client's existing container security tooling.

**Client use cases**
- Sandboxed execution for coding agents and code-interpreter tools in client agent platforms
- Multi-tenant agent hosting where each customer's or user's agent runs in its own isolated VM
- Releasing API keys and credentials to an agent only after attestation

**How we could offer it**
- Reference architecture for secure agent runtimes on EKS/ECS, with Nitro Sandboxes plus least-privilege identity and egress controls
- Agent-security hardening reviews: move existing container-based code execution to hardware-isolated sandboxes

**Pitch**
Agents that run code are a security risk. Nitro Sandboxes gives each one its own hardware-isolated VM at no extra charge, and we can retrofit it into the client's existing Kubernetes or ECS setup.

**What it is**
Per-workload hardware isolation on most Nitro-based EC2 instances. Native support for Pod Identity, VPC CNI, EBS/EFS/S3 and CloudWatch. Can also run directly on EC2 with your own AMI, orchestration and VMMs (Amazon Linux and Firecracker supported natively). Cryptographic attestation can verify a sandbox's integrity before secrets are released to it.

**Concepts:** [[AWS]] · [[Agent security]]
**From:** [[2026-11-10]]

# My notes


---
# References
[AWS What's New](https://aws.amazon.com/about-aws/whats-new/2026/11/nitro-sandboxes-eks-ecs-ec2/)
