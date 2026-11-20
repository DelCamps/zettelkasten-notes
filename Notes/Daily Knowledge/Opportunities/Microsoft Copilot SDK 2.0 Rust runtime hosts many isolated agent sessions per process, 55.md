---
date: 2026-11-20
section: AI
importance: Med
kind: value
source: "Microsoft Command Line blog"
url: https://commandline.microsoft.com/microsoft-copilot-sdk-2-0-github/
status: unread
id: 2026-11-20-microsoft-copilot-sdk-2
---
2026-11-20 07:16
Tags: #daily-knowledge #ai

---
# Microsoft Copilot SDK 2.0 Rust runtime hosts many isolated agent sessions per process, 55

The former GitHub Copilot SDK ships as Microsoft Copilot SDK 2.0, giving programmatic access to the Copilot agent harness in TypeScript, Python, Go, .NET, Java and Rust. One rebuilt Rust runtime hosts many sessions with their own identity, tools and history; Microsoft reports 120 versus 7.55 sessions per second and 126 MB versus 1,383 MB for 10 clients.

## Details

**Availability and price**
Released at Ignite on 17 November 2026; the post does not label 2.0 as GA (the SDK itself was GA in June 2026). No licensing or pricing details; today the architectures run on your own infrastructure, with GitHub Copilot cloud sandboxes and Foundry managed agents as managed options.

**Caveats**
Promotion to a sandbox cannot be reversed. Each delegated worker costs an agent plus a container. Sessions now act as the requesting user, a change from the process identity. Billing and inference terms are not stated.

**Client use cases**
- Embedding a coding or operations agent inside a client's internal platform
- Multi-user agent services where each session acts as the requesting user
- Coordinator-and-worker agents with sandboxed shell and file access

**How we could offer it**
- Architecture assessment: choose the session and sandbox topology per client workload
- Implementation of client-branded agents on the Copilot harness, hosted on client infrastructure
- Skills needed: TypeScript or .NET engineers, identity (GitHub tokens) and sandbox design

**Pitch**
Clients can now build their own agents on the same harness as GitHub Copilot, in six languages, with per-user identity and much lower runtime cost. It is a natural build offer alongside Copilot Studio.

**What it is**
An SDK to embed the Copilot agent harness in your own apps and services. 2.0 adds a shared multi-tenant runtime, per-session user identity, an 'empty' mode with no shell, files or default tools, durable sessions that resume from any instance, in-process embedding via a C ABI, and five sandbox topologies from shared runtime to coordinator-and-workers.

**Concepts:** [[Agents]] · [[GitHub Copilot]]
**From:** [[2026-11-20]]

# My notes


---
# References
[Microsoft Command Line blog](https://commandline.microsoft.com/microsoft-copilot-sdk-2-0-github/)
