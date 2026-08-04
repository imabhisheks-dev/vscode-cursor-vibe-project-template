---
description: Compare VS Code, Cursor, and Claude template files for drift and recommend sync updates.
name: Compare IDE Setup
agent: Reviewer
tools:
  - search/codebase
  - read/terminalLastCommand
---

# Compare IDE Setup Prompt

Keep the IDE templates on the same page across VS Code (`.github`), Cursor (`.cursor`), and Claude (`.claude`).

1. Run the inventory script from repo root:

```bash
python3 .cursor/skills/compare-ide-setup/scripts/compare-pairs.py
```

2. Inspect every missing or diverged pair by reading the paired files.
3. Compare shared guidance intent; preserve IDE-specific frontmatter and hook contracts.
4. Report:
   - what is aligned
   - what is missing on which IDE
   - what diverged
   - concrete recommended text/behavior to append or port
5. Do not edit files unless the user explicitly asks to apply the sync.

Follow the report format and sync policy in `.cursor/skills/compare-ide-setup/SKILL.md`.
