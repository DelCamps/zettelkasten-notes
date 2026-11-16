---
date: 2026-11-11
section: AI
importance: High
kind: value
source: "Claude blog"
url: https://claude.com/resources/articles/sheets-whiteboards-data
status: unread
id: 2026-11-11-claude-sheets-whiteboards-data
---
2026-11-11 07:16
Tags: #daily-knowledge #ai

---
# Claude adds Sheets and Whiteboards (beta) and makes Claude Data, its warehouse dashboards,

Anthropic launched Claude Sheets and Claude Whiteboards in beta and made Claude Data (formerly Dashboards) generally available on all paid plans, with certified queries and live sharing in beta. Claude Data queries Snowflake, Databricks, BigQuery, Redshift, ClickHouse or Salesforce through connectors, and turns on by default for Enterprise on November 19, 2026.

## Details

**Availability and price**
Whiteboards, Sheets and Data on all paid plans (Data: Pro, Max, Ultra, Team, Enterprise), web, desktop and mobile; counts toward plan usage limits. Team: on by default. Enterprise: Sheets and Whiteboards off by default; Claude Data on by default from November 19, 2026; certified queries and live sharing are beta and off by default on Enterprise. No separate price stated.

**Caveats**
Sheets is basic for now (Anthropic points to Excel for full features). Live sharing shows viewers results from the sharer's own connections, so dashboards must be checked before sharing. Claude Meetings was announced as coming soon only.

**Client use cases**
- Self-service KPI dashboards over a client's Snowflake or Databricks warehouse, with data-team-certified metrics
- Live-shared management dashboards where viewers see only approved query results without warehouse access
- Workshop facilitation: Whiteboards turning discovery sessions into owners, dates and action items
- Quick planning models in Sheets before moving to Excel

**How we could offer it**
- Claude Data accelerator: connect the client warehouse, define certified queries from their semantic layer (dbt/Looker), set governance with custom roles
- Rollout and governance review for Enterprise tenants before the 19 November default-on change
- Bundle with existing Claude Enterprise deployments as a lightweight BI layer next to Power BI

**Pitch**
Let business users ask the warehouse in plain language and get dashboards built on the metric definitions your data team already certified.

**What it is**
Three shared work surfaces inside Claude. Sheets: Claude builds and edits spreadsheets with tabs, formulas, formatting and drop-downs, with edits outlined and shared co-editing; export to .xlsx/CSV or hand off to Claude for Excel. Whiteboards: a shared board where Claude groups sticky notes by theme, turns a plan into a timeline with owners and drafts action items; export to doc/deck or Lucid/Miro. Claude Data: dashboards and narrated 'data stories' over company data via warehouse/CRM connectors, with certified metric definitions (beta, also from dbt, Looker or Cube via MCP), cached refresh and version history. Interactive connectors (Adobe, Atlassian, Box, Notion) now open full-size beside the chat.

**Concepts:** [[Claude]] · [[Agents]]
**From:** [[2026-11-11]]

# My notes


---
# References
[Claude blog](https://claude.com/resources/articles/sheets-whiteboards-data)
