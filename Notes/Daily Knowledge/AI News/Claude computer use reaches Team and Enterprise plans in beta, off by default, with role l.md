---
date: 2026-11-22
section: AI
importance: Med
kind: news
source: "Claude release notes"
url: https://support.claude.com/en/articles/12138966-release-notes
status: unread
id: 2026-11-22-claude-computer-use-team
---
2026-11-22 07:16
Tags: #daily-knowledge #ai

---
# Claude computer use reaches Team and Enterprise plans in beta, off by default, with role l

Anthropic's 20 November release notes say computer use, which lets Claude see a user's screen and work in the desktop apps they allow, is now in beta on Team and Enterprise plans and rolling out gradually. Admins turn it on in Organization settings, can limit it to custom roles on Enterprise, restrict it to specific apps and manage it with MDM. Organizations with HIPAA-ready configuration, ZDR for Claude Code, customer-managed keys or FERPA settings cannot turn it on.

## Details

**Caveats**
Anthropic warns there is no sandbox between Claude and the user's apps, that on-screen content such as web pages or emails could cause unintended actions, and that folder limits and read-only settings do not apply. Screenshots are saved with the chat, and Anthropic may keep the latest one in its record of the automated action check.

**For your work**
For clients on Claude Team or Enterprise this is the first admin-governed way to automate desktop apps. Treat it as a prompt-injection surface: start with an allow list of apps, block password managers, and pilot with a custom role before turning it on for everyone.

**Method**
- Works in the new unified Chat and Cowork experience in Claude Desktop (macOS 14 or later and Windows), and from web and mobile when Computer access is on.
- Only an Owner or Primary Owner can enable it or edit the app lists; App access offers 'Block these apps' or 'Allow only these apps'.
- Enterprise admins choose which custom roles get it; to exclude a user, set their role first and wait 15 minutes.

**Problem**
Enterprises want Claude to work in desktop apps that have no API, but need admin control over who can use it and which apps it can touch.

**Results**
- Off by default and rolling out gradually; turning it off can take about an hour, sometimes longer, to reach each user's Claude Desktop.
- Not available in Claude Code or in tasks started with the separate Cowork option.
- A refreshed Claude Mobile design is rolling out the same day, starting on iOS 26 or later.

**Concepts:** [[Claude]] · [[Computer-use agents]] · [[Agent security]]
**From:** [[2026-11-22]]

# My notes


---
# References
[Claude release notes](https://support.claude.com/en/articles/12138966-release-notes)
