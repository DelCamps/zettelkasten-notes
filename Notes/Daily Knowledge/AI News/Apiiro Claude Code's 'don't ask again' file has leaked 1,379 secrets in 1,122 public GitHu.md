---
date: 2026-11-08
section: AI
importance: High
kind: news
source: "Apiiro (via The Hacker News)"
url: https://apiiro.com/blog/coding-agents-leaking-secrets-github-dont-ask-again
status: unread
id: 2026-11-08-claude-code-dont-ask-again-secrets
---
2026-11-08 07:16
Tags: #daily-knowledge #ai

---
# Apiiro Claude Code's 'don't ask again' file has leaked 1,379 secrets in 1,122 public GitHu

When a user picks 'Yes, and don't ask again', Claude Code saves the approved command word for word, passwords included, in .claude/settings.local.json, a file that often gets committed. Apiiro found 104,185 public copies of the file, 1,122 of them with at least one secret, and common scanners missed many of them.

## Details

**Caveats**
Apiiro did not test whether the secrets still work. A 2025 bug report about this behaviour (issue #5544) was closed by a bot as 'not planned'. Apiiro's page blocks bots, so these figures were checked against The Hacker News' write-up (7 Nov), which dates Apiiro's research to 6 Nov. One company Apiiro notified confirmed its leaked key was live.

**For your work**
Add .claude/settings.local.json to every repo's .gitignore template, scan .claude/, .cursor/ and .gemini/ folders (and their history) like .env files, approve command patterns such as Bash(npm run:*) rather than single commands, and keep secrets in variables.

**Method**
- GitHub-wide search for .claude/settings.local.json and .claude/settings.json, plus git history and forks
- Traced which commits changed the file: in 539 of 1,105 traced repos, a commit co-authored by Claude did
- Ran gitleaks and TruffleHog (without verification) over the files with secrets
- Compared 16 coding agents; reproduced with Opus 5.5 and Fable 5.1

**Problem**
Permission allow-rules are stored as the literal approved command. Claude Code ignores the file only in the user's global git excludes, not in the project's .gitignore, so the protection does not travel with the repo.

**Results**
- 1,379 distinct secrets in 1,122 of 104,185 copies (about 1.1%): 379 database passwords, 43 SSH logins, 42 GitHub/GitLab/npm tokens, 23 AWS keys
- Including shared settings.json, older versions and chat logs: 2,539 secrets across 1,994 repos; half had been exposed for at least 217 days
- gitleaks flagged 564 of the files and TruffleHog 643; neither flagged 215, mostly passwords inside commands like PGPASSWORD= or sshpass -p
- Claude Code was the only one of the 16 agents confirmed to save the full approved command in a project file by default

**Concepts:** [[Agent security]] · [[Coding agents]] · [[Claude]]
**From:** [[2026-11-08]]

# My notes


---
# References
[Apiiro (via The Hacker News)](https://apiiro.com/blog/coding-agents-leaking-secrets-github-dont-ask-again)
