# Vibe + Prompt Coding Template (VS Code + Cursor + Claude)

This repository is a starter scaffold for AI-assisted development workflows across:

- VS Code native chat customizations
- Cursor project rules, commands, skills, agents, and hooks
- Claude-based tools (Claude Code)

It provides always-on instructions, scoped instructions/rules, reusable prompts/commands, custom agents, hook configs, hook scripts, and skill packs in each ecosystem.

## Full Folder Tree

```text
my-vibe-coding-template/
├── .github/
│   ├── copilot-instructions.md
│   ├── agents/
│   │   ├── planner.agent.md
│   │   ├── implementer.agent.md
│   │   ├── reviewer.agent.md
│   │   ├── feature-builder.agent.md
│   │   └── strict-formatter.agent.md
│   ├── instructions/
│   │   ├── general-coding.instructions.md
│   │   ├── typescript.instructions.md
│   │   ├── python.instructions.md
│   │   └── documentation.instructions.md
│   ├── prompts/
│   │   ├── create-component.prompt.md
│   │   ├── security-review.prompt.md
│   │   ├── write-tests.prompt.md
│   │   └── compare-ide-setup.prompt.md
│   ├── hooks/
│   │   ├── formatting.json
│   │   ├── security.json
│   │   └── audit.json
│   └── skills/
│       ├── webapp-testing/SKILL.md
│       └── github-actions-debugging/SKILL.md
├── .cursor/
│   ├── hooks.json
│   ├── rules/
│   │   ├── copilot-instructions.mdc
│   │   ├── general-coding.mdc
│   │   ├── typescript.mdc
│   │   ├── python.mdc
│   │   └── documentation.mdc
│   ├── commands/
│   │   ├── create-component.md
│   │   ├── security-review.md
│   │   ├── write-tests.md
│   │   └── compare-ide-setup.md
│   ├── agents/
│   │   ├── planner.md
│   │   ├── implementer.md
│   │   ├── reviewer.md
│   │   ├── feature-builder.md
│   │   └── strict-formatter.md
│   ├── hooks/
│   │   ├── block-dangerous.sh
│   │   ├── log-tool-use.sh
│   │   └── format-changed-files.sh
│   └── skills/
│       ├── webapp-testing/SKILL.md
│       ├── github-actions-debugging/SKILL.md
│       └── compare-ide-setup/
│           ├── SKILL.md
│           └── scripts/compare-pairs.py
├── .claude/
│   ├── CLAUDE.md
│   ├── settings.json
│   ├── rules/
│   │   ├── general.md
│   │   └── typescript.md
│   ├── agents/
│   │   ├── researcher.md
│   │   └── implementer.md
│   └── skills/
│       └── webapp-testing/SKILL.md
├── scripts/
│   ├── format-changed-files.sh
│   ├── format-changed-files.ps1
│   ├── block-dangerous.sh
│   └── log-tool-use.sh
├── AGENTS.md
├── CLAUDE.md
└── README.md
```

Notes:

- `.github/hooks/audit.log` is created automatically by `scripts/log-tool-use.sh` the first time the VS Code/Claude audit hook runs.
- `.cursor/hooks/audit.log` is created automatically by `.cursor/hooks/log-tool-use.sh` the first time the Cursor audit hook runs.

## Correspondence Map (VS Code → Cursor)

| VS Code                                  | Cursor                                                         |
| ---------------------------------------- | -------------------------------------------------------------- |
| `.github/copilot-instructions.md`        | `.cursor/rules/copilot-instructions.mdc` (`alwaysApply: true`) |
| `.github/instructions/*.instructions.md` | `.cursor/rules/*.mdc` (`globs` / `alwaysApply`)                |
| `.github/prompts/*.prompt.md`            | `.cursor/commands/*.md` (slash commands)                       |
| `.github/agents/*.agent.md`              | `.cursor/agents/*.md`                                          |
| `.github/hooks/*.json` + `scripts/*.sh`  | `.cursor/hooks.json` + `.cursor/hooks/*.sh`                    |
| `.github/skills/<name>/SKILL.md`         | `.cursor/skills/<name>/SKILL.md`                               |
| `AGENTS.md`                              | `AGENTS.md` (shared; Cursor also reads this)                   |

### Keep IDEs aligned

Use `/compare-ide-setup` in Cursor (or the VS Code prompt `Compare IDE Setup`) to:

1. Inventory paired files across `.github`, `.cursor`, and `.claude`
2. Flag missing counterparts and diverged guidance
3. Recommend concrete text/behavior to append or port

Supporting files:

- `.cursor/commands/compare-ide-setup.md`
- `.cursor/skills/compare-ide-setup/SKILL.md`
- `.cursor/skills/compare-ide-setup/scripts/compare-pairs.py`
- `.github/prompts/compare-ide-setup.prompt.md`

## What Each File Type Does

### Always-on instructions

- `.github/copilot-instructions.md`
  VS Code auto-detects this as repository-wide coding guidance.
- `.cursor/rules/copilot-instructions.mdc` and `.cursor/rules/general-coding.mdc`
  Cursor always-apply project rules.
- `AGENTS.md`
  Shared always-on multi-agent guidance (VS Code + Cursor).
- `CLAUDE.md` (repo root)
  Claude always-on instructions for the repository.
- `.claude/CLAUDE.md`
  Claude workspace-level instruction overlay.

### Scoped instructions and rules

- `.github/instructions/*.instructions.md`
  VS Code instruction files using YAML frontmatter with `applyTo` globs.
- `.cursor/rules/*.mdc`
  Cursor rules using YAML frontmatter with `globs` and/or `alwaysApply`.
- `.claude/rules/*.md`
  Claude rule files using YAML frontmatter with `paths` arrays.

### Agents

- `.github/agents/*.agent.md`
  VS Code custom agents with YAML fields: name, description, tools, agents, model, handoffs, hooks.
- `.cursor/agents/*.md`
  Cursor agent role prompts with name/description frontmatter and preferred-tool guidance.
- `.claude/agents/*.md`
  Claude agent definitions with frontmatter fields including comma-separated tools/disallowedTools.

### Prompt / command files

- `.github/prompts/*.prompt.md`
  Reusable prompt templates with fields: description, name, agent, model, tools.
- `.cursor/commands/*.md`
  Cursor slash-command prompts (description frontmatter + markdown body).

### Hooks

- `.github/hooks/*.json`
  VS Code hook definitions containing PreToolUse/PostToolUse command hooks.
- `.cursor/hooks.json`
  Cursor hook definitions (`beforeShellExecution`, `preToolUse`, `afterFileEdit`).
- `.cursor/hooks/*.sh`
  Cursor-native hook scripts (permission allow/deny JSON contract).
- `.claude/settings.json`
  Claude hook settings in settings.json format.
- `scripts/*.sh` and `scripts/*.ps1`
  Shared VS Code/Claude hook command implementations using stdin JSON -> stdout JSON (`continue` true/false).

### Skills

- `.github/skills/<name>/SKILL.md`
  VS Code skill packs with YAML frontmatter.
- `.cursor/skills/<name>/SKILL.md`
  Cursor project skills with YAML frontmatter.
- `.claude/skills/<name>/SKILL.md`
  Claude skill packs in Claude-compatible location.

## When Cursor Loads These

- `.cursor/rules/*.mdc`
  Applied always or when matching file globs are in context.
- `AGENTS.md`
  Used as shared agent guidance.
- `.cursor/commands/*.md`
  Available as project slash commands.
- `.cursor/agents/*.md`
  Reusable agent role definitions for multi-agent workflows.
- `.cursor/hooks.json` and `.cursor/hooks/*.sh`
  Triggered around shell, tool use, and file-edit events.
- `.cursor/skills/**/SKILL.md`
  Discoverable project skills for relevant tasks.

## When VS Code Loads These

- `.github/copilot-instructions.md`
  Loaded as repository-level instructions automatically.
- `AGENTS.md`
  Used when AGENTS support is enabled in settings.
- `.github/instructions/*.instructions.md`
  Applied when matching file paths are in context.
- `.github/agents/*.agent.md`
  Available in agent mode / custom agent selection.
- `.github/prompts/*.prompt.md`
  Available in prompt picker / slash prompt workflows.
- `.github/hooks/*.json` and agent hooks
  Triggered around tool use when hook support is enabled.
- `.github/skills/**/SKILL.md`
  Discoverable as skill packs for relevant tasks.

## VS Code vs Cursor vs Claude Differences

- Instruction scope key:
  VS Code uses `applyTo`; Cursor uses `globs` / `alwaysApply`; Claude uses `paths`.
- Prompt surfaces:
  VS Code uses `.github/prompts`; Cursor uses `.cursor/commands`.
- Tool naming:
  VS Code commonly uses names like `create_file` / `replace_string_in_file`.
  Cursor commonly uses names like `Write` / `StrReplace` / `Shell`.
  Claude commonly uses names like `Write` / `Edit`.
- Hook events and payloads:
  VS Code/Claude commonly use PreToolUse/PostToolUse with `continue` / `permissionDecision`.
  Cursor uses events like `beforeShellExecution`, `preToolUse`, and `afterFileEdit` with `permission` allow/deny/ask.
- Hook matcher behavior:
  VS Code currently parses matcher-related values but ignores matcher filtering and runs hooks broadly.
  Cursor and Claude apply matcher semantics in their own runtimes.

## Required Settings

Enable these VS Code settings for full behavior:

- `chat.useCustomAgentHooks`
  Required for agent-scoped hooks (for example, `strict-formatter.agent.md`).
- `chat.useAgentsMdFile`
  Enables `AGENTS.md` integration.
- `chat.useClaudeMdFile`
  Enables `CLAUDE.md` integration in compatible VS Code flows.

For Cursor, project rules/commands/skills/hooks under `.cursor/` are loaded from the repository; review Hooks in Cursor Settings if a hook fails to load.

## Hook Script Setup

Run this once on macOS/Linux to mark shell scripts executable:

```bash
chmod +x scripts/*.sh .cursor/hooks/*.sh
```

## How To Add New Items

### Add a new instruction

1. Create a new `.github/instructions/<topic>.instructions.md` file.
2. Add frontmatter fields: name, description, applyTo.
3. Write concise rules in Markdown body.
4. Add the Cursor equivalent under `.cursor/rules/<topic>.mdc` with `globs` or `alwaysApply`.

### Add a new VS Code agent

1. Create `.github/agents/<agent-name>.agent.md`.
2. Add frontmatter fields: name, description, tools, agents, model, handoffs, hooks.
3. Keep tools minimal and role-specific.
4. Add the Cursor equivalent under `.cursor/agents/<agent-name>.md`.

### Add a new prompt / command

1. Create `.github/prompts/<prompt-name>.prompt.md`.
2. Add frontmatter fields: description, name, agent, model, tools.
3. Include placeholders and clear expected output format.
4. Add the Cursor equivalent under `.cursor/commands/<prompt-name>.md`.
5. If the pairing map changes, update `.cursor/skills/compare-ide-setup/scripts/compare-pairs.py`.

### Compare IDE setup

1. In Cursor, run `/compare-ide-setup`.
2. Or run `python3 .cursor/skills/compare-ide-setup/scripts/compare-pairs.py` and ask the agent to interpret the report.
3. Apply recommended sync edits only after review.

### Add a new hook

1. Add or update a `.github/hooks/*.json` file for VS Code/Claude shared scripts.
2. Reference a command script and timeout.
3. Ensure shared scripts read stdin JSON and write stdout JSON with `continue` true/false.
4. For Cursor, update `.cursor/hooks.json` and add/adapt scripts under `.cursor/hooks/` using Cursor's permission JSON contract.

### Add a new skill

1. Create `.github/skills/<skill-name>/SKILL.md`.
2. Set frontmatter `name` equal to the folder name.
3. Add short, task-focused guidance in the body.
4. Mirror under `.cursor/skills/<skill-name>/SKILL.md` (and `.claude/skills` when needed).

### Add Claude equivalents

1. Add matching rule files under `.claude/rules` with `paths`.
2. Add Claude agents under `.claude/agents` with comma-separated tools.
3. Add matching skills under `.claude/skills` when needed.
