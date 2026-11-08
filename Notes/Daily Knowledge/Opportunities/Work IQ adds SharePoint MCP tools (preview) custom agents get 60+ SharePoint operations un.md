---
date: 2026-11-08
section: AI
importance: Med
kind: value
source: "Microsoft 365 Developer Blog"
url: https://devblogs.microsoft.com/microsoft365dev/work-iq-sharepoint-mcp-tools/
status: unread
id: 2026-11-08-work-iq-sharepoint-mcp
---
2026-11-08 07:16
Tags: #daily-knowledge #ai

---
# Work IQ adds SharePoint MCP tools (preview) custom agents get 60+ SharePoint operations un

Microsoft has added SharePoint tools to the Work IQ API, the layer that powers Microsoft Copilot, so custom apps and agents can find files, manage lists and libraries and handle approvals. The catalog holds more than 60 SharePoint operations. Agents discover them at runtime through four generic tools rather than registering one tool per operation.

## Details

**Availability and price**
Preview. The post gives no GA date and no licensing or pricing.

**Caveats**
Writes use SharePoint internal field names, so people, lookup and taxonomy values must be resolved from the schema. Site keys are scoped to one site. Some arguments are JSON-encoded strings. More roadmap news is expected at Ignite (November 17-20, 2026).

**Client use cases**
- Document-control agents that file, version and route contracts or deliverables in SharePoint libraries
- Approval agents that start and track SharePoint approvals from a chat or business process
- List-driven trackers (risks, issues, RFIs) that an agent keeps up to date
- Read-only knowledge agents that can't write, scoped with WorkIQ.Read

**How we could offer it**
- Build SharePoint process agents in Copilot Studio, Foundry or our own harness over one MCP endpoint
- A permissions and scope review (Read vs. Act) as part of an agent governance engagement
- Migrate custom Graph or SharePoint REST integrations to Work IQ for a smaller tool surface

**Pitch**
Your agents can now work inside SharePoint the way your people do, with the same permissions and without a custom integration for every list and library.

**What it is**
A SharePoint MCP surface in the Work IQ API, now in preview. It covers lists and libraries, list items, files and folders, search, approvals, rules, Quick Steps, the recycle bin and versioning. The tools are search_paths, get_schema, do_action and get_site_key. Access needs the new delegated scopes WorkIQ.Read and WorkIQ.Act, and read-only agents get a reduced tool set.

**Concepts:** [[Microsoft 365 Copilot]] · [[Agents]]
**From:** [[2026-11-08]]

# My notes


---
# References
[Microsoft 365 Developer Blog](https://devblogs.microsoft.com/microsoft365dev/work-iq-sharepoint-mcp-tools/)
