---
description: Compare VS Code, Cursor, and Claude template files for drift and recommend sync updates.
---

# Compare IDE Setup

Keep the IDE templates on the same page.

Use the **compare-ide-setup** skill and follow it exactly.

1. Run:

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
5. Do not edit files unless I explicitly ask you to apply the sync.
