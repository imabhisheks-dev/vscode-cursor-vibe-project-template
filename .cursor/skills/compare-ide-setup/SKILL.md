---
name: compare-ide-setup
description: Compares VS Code, Cursor, and Claude IDE template files for drift and recommends sync edits. Use when the user runs /compare-ide-setup, asks to keep IDEs aligned, or mentions template parity across .github, .cursor, and .claude.
---

# Compare IDE Setup

Keep VS Code (`.github`), Cursor (`.cursor`), and Claude (`.claude`) template surfaces on the same page.

## Workflow

1. Run the inventory script from repo root:

```bash
python3 .cursor/skills/compare-ide-setup/scripts/compare-pairs.py
```

2. For every row with `missing` or `body_sync=diverged`, read the paired files.
3. Compare **guidance intent** (bullets, policies, role purpose), not IDE-specific syntax.
4. Produce a report for the user. Do **not** edit files unless the user explicitly asks to apply syncs.

## Sync policy

- Shared guidance body should stay semantically aligned across IDEs.
- Keep IDE-specific wrappers local:
  - VS Code instructions: `applyTo`
  - Cursor rules: `globs` / `alwaysApply`
  - Claude rules: `paths`
  - VS Code prompts vs Cursor commands: different frontmatter shapes
  - Hooks: different event names and JSON contracts (`continue`/`permissionDecision` vs `permission`)
- Prefer the newest meaningful guidance (`NEWEST` column / git history / richer bullet set).
- When Cursor-only mechanics exist (for example Cursor permission JSON), keep those Cursor-side and port the **behavior** to VS Code/Claude equivalents.
- When one IDE has a new command/agent/skill/rule and counterparts are missing, recommend creating the counterparts.

## Expected pairing map

| Concern             | VS Code                                               | Cursor                                   | Claude                           |
| ------------------- | ----------------------------------------------------- | ---------------------------------------- | -------------------------------- |
| Repo instructions   | `.github/copilot-instructions.md`                     | `.cursor/rules/copilot-instructions.mdc` | `CLAUDE.md`                      |
| General rules       | `.github/instructions/general-coding.instructions.md` | `.cursor/rules/general-coding.mdc`       | `.claude/rules/general.md`       |
| TypeScript rules    | `.github/instructions/typescript.instructions.md`     | `.cursor/rules/typescript.mdc`           | `.claude/rules/typescript.md`    |
| Python rules        | `.github/instructions/python.instructions.md`         | `.cursor/rules/python.mdc`               | (optional)                       |
| Docs rules          | `.github/instructions/documentation.instructions.md`  | `.cursor/rules/documentation.mdc`        | (optional)                       |
| Agents              | `.github/agents/<name>.agent.md`                      | `.cursor/agents/<name>.md`               | `.claude/agents/<name>.md`       |
| Prompts/commands    | `.github/prompts/<name>.prompt.md`                    | `.cursor/commands/<name>.md`             | (optional)                       |
| Skills              | `.github/skills/<name>/SKILL.md`                      | `.cursor/skills/<name>/SKILL.md`         | `.claude/skills/<name>/SKILL.md` |
| Hooks config        | `.github/hooks/*.json`                                | `.cursor/hooks.json`                     | `.claude/settings.json`          |
| Hook scripts        | `scripts/*.sh`                                        | `.cursor/hooks/*.sh`                     | `scripts/*.sh`                   |
| Shared agents guide | `AGENTS.md`                                           | `AGENTS.md`                              | `AGENTS.md`                      |

## Report format

Use this structure:

```markdown
# IDE setup comparison

## Summary

- Aligned pairs: N
- Missing counterparts: N
- Diverged guidance: N

## Missing counterparts

- [pair] missing on <ide>: recommend create `<path>` from `<source>`

## Diverged guidance

### <pair>

- Newer/richer source: <ide> (`<path>`)
- Drift: <1-3 bullets>
- Recommended append/port:
  - To `<target-path>`: add/update "<exact guidance text or close paraphrase>"
  - Keep local frontmatter/hook contract unchanged

## Hook behavior check

- Security block patterns: aligned/diverged
- Audit logging: aligned/diverged
- Format-on-edit: aligned/diverged

## Recommended next actions

1. ...
```

## Conversion reminders

When recommending ports:

- VS Code `applyTo: "**/*.ts,**/*.tsx"` → Cursor `globs: "**/*.ts,**/*.tsx"` / Claude `paths: ["**/*.ts","**/*.tsx"]`
- VS Code prompt → Cursor command: keep description + body; drop VS Code-only `agent`/`model`/`tools` unless useful as comments
- VS Code/Claude hook deny (`continue:false`, `permissionDecision:deny`) → Cursor `{ "permission": "deny", ... }`
- Do not recommend pasting `.github/hooks/*.json` into `.cursor/hooks.json` unchanged
