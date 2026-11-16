---
date: 2026-11-03
section: AI
importance: High
kind: news
source: "Claude API docs / release notes"
url: https://platform.claude.com/docs/en/build-with-claude/message-threads
status: unread
id: 2026-11-03-claude-message-threads
---
2026-11-03 07:16
Tags: #daily-knowledge #ai

---
# Claude API message threads (beta) agent loops send only the new turn, so time to first tok

Anthropic released message threads in beta on the Messages API. You send the full conversation once with "thread": {"type": "create"}, then each later turn sends only the new messages plus the previous response id. A thread expires 5 minutes after its last request and is deleted no more than 1 hour after its last use. It works on the Claude API, Claude Platform on AWS, Google Cloud and Microsoft Foundry.

## Details

**Caveats**
- Not ZDR-eligible: the thread is held in memory, encrypted, for up to 1 hour.
- Threads do not cache for you. You still set cache_control yourself, with at most 4 breakpoints.
- Batches, token counting and on-demand compaction are not supported.
- MCP URLs and tokens are not stored, so you send them every turn.
- On the 5.5 models, changing system or tools invalidates earlier thinking blocks.

**For your work**
For long tool-using agents on Foundry or the direct API this is a nearly free latency gain. Use the SDK helper so it handles replay on a 404. Check the ZDR point before using it with client data that has zero-retention terms.

**Method**
- Create: send the first request as usual (full messages, system, tools) with "thread": {"type": "create"} and the beta header message-threads-2026-08-12. The API stores the conversation under the response id.
- Continue: send only the new messages (usually the tool_result blocks) with "thread": {"type": "continue", "previous_message_id": ...}. Do not send system or tools. Model, thinking, tool_choice, mcp_servers and the top-level cache_control must stay the same, or you get a 400 thread_fingerprint_mismatch.
- Threads are append-only and best-effort. Each response id can be continued once. If the thread is gone you get a 404 thread_not_found and must replay the full conversation in a new create request. The SDK helper does this for you and also offers fork().

**Problem**
In long agent loops every turn re-uploads the whole conversation, which the API then validates and tokenizes again. Requests keep growing, and so does time to first token.

**Results**
- The docs promise smaller requests and a lower, steadier time to first token as the conversation grows. They give no benchmark figures.
- Supported on Opus 5.5, Sonnet 5.5, Haiku 5.5, Fable/Mythos 5.1 and older 4.x models, on all four platforms (beta).

**Concepts:** [[Claude]] · [[Inference efficiency]] · [[Agents]]
**From:** [[2026-11-03]]

# My notes


---
# References
[Claude API docs / release notes](https://platform.claude.com/docs/en/build-with-claude/message-threads)
