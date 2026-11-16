---
date: 2026-10-28
section: AI
importance: Med
kind: news
source: "Cloudflare blog"
url: https://blog.cloudflare.com/kv-cache-exposure-remediation/
status: unread
id: 2026-10-28-cloudflare-kv-cache-leak
---
2026-10-28 07:16
Tags: #daily-knowledge #ai

---
# Cloudflare an SGLang KV-cache bug leaked other users' prompt data in 155 GLM-5.3 responses

Cloudflare disclosed that from 27 Aug to 9 Sep 2026, 155 responses from GLM-5.3 on Workers AI contained data from other customers' recent requests. The cause was a KV pool of 681,280 tokens behind a 1,048,576-token advertised context, plus an SGLang bug in disaggregated prefill/decode mode. The fixes are in SGLang v0.5.22.

## Details

**Caveats**
Only GLM-5.3 on Workers AI was affected. The same bug was reported upstream as SGLang issue #30233 in July, so self-hosted disaggregated SGLang deployments may have had it too.

**For your work**
If you or a client self-host on SGLang with disaggregated prefill/decode, upgrade to v0.5.22 or later and check pool size against context length. Tests that only check status codes miss this.

**Method**
- An over-length prompt was marked rejected and replaced with a one-token placeholder, but the disaggregation admission queue checked 'finished' rather than 'rejected', so the request went through
- Prefill sent 1 KV page while decode reserved 8, so decode attended over 7 stale pages holding earlier users' data
- Reported by Gadi Evron (Knostic) via HackerOne on 8 Sep; the model was made private on 9 Sep at 14:00 UTC
- Operator flags: --disaggregation-enable-kv-checksum and --kv-canary; check that KV pool size is at least the context length

**Problem**
In a multi-tenant LLM server, KV-cache pages are reused across requests. If isolation fails, the model's output can include text from another tenant's prompt, while the API still returns HTTP 200 with fluent output.

**Results**
- 155 affected responses, all to prompts longer than 681,280 tokens; no evidence of deliberate exploitation
- Prefill pool raised to about 2.04M tokens; over-length requests are now rejected at admission
- Page integrity-tag prototype costs under 1% in throughput

**Concepts:** [[Agent security]] · [[Inference efficiency]]
**From:** [[2026-10-28]]

# My notes


---
# References
[Cloudflare blog](https://blog.cloudflare.com/kv-cache-exposure-remediation/)
