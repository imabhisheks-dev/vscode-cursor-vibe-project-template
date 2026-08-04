# Vibe + Prompt Coding Template (VS Code + Claude)

This repository is a starter scaffold for AI-assisted development workflows across:

- VS Code native chat customizations
- Claude-based tools (Cursor / Claude Code)

It provides always-on instructions, scoped instructions/rules, reusable prompts, custom agents, hook configs, hook scripts, and skill packs in both ecosystems.

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
│   │   └── write-tests.prompt.md
│   ├── hooks/
│   │   ├── formatting.json
│   │   ├── security.json
│   │   └── audit.json
│   └── skills/
│       ├── webapp-testing/SKILL.md
│       └── github-actions-debugging/SKILL.md
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

Note: .github/hooks/audit.log is created automatically by scripts/log-tool-use.sh the first time the audit hook runs.

## What Each File Type Does

### Always-on instructions

- .github/copilot-instructions.md
  VS Code auto-detects this as repository-wide coding guidance.
- AGENTS.md
  VS Code can apply this as always-on multi-agent guidance.
- CLAUDE.md (repo root)
  Claude always-on instructions for the repository.
- .claude/CLAUDE.md
  Claude workspace-level instruction overlay.

### Scoped instructions and rules

- .github/instructions/*.instructions.md
  VS Code instruction files using YAML frontmatter with applyTo globs.
- .claude/rules/*.md
  Claude rule files using YAML frontmatter with paths arrays.

### Agents

- .github/agents/*.agent.md
  VS Code custom agents with YAML fields: name, description, tools, agents, model, handoffs, hooks.
- .claude/agents/*.md
  Claude agent definitions with frontmatter fields including comma-separated tools/disallowedTools.

### Prompt files

- .github/prompts/*.prompt.md
  Reusable prompt templates with fields: description, name, agent, model, tools.

### Hooks

- .github/hooks/*.json
  VS Code hook definitions containing PreToolUse/PostToolUse command hooks.
- .claude/settings.json
  Claude hook settings in settings.json format.
- scripts/*.sh and scripts/*.ps1
  Hook command implementations using stdin JSON -> stdout JSON contract.

### Skills

- .github/skills/<name>/SKILL.md
  VS Code skill packs with YAML frontmatter.
- .claude/skills/<name>/SKILL.md
  Claude skill packs in Claude-compatible location.

## When VS Code Loads These

- .github/copilot-instructions.md
  Loaded as repository-level instructions automatically.
- AGENTS.md
  Used when AGENTS support is enabled in settings.
- .github/instructions/*.instructions.md
  Applied when matching file paths are in context.
- .github/agents/*.agent.md
  Available in agent mode / custom agent selection.
- .github/prompts/*.prompt.md
  Available in prompt picker / slash prompt workflows.
- .github/hooks/*.json and agent hooks
  Triggered around tool use when hook support is enabled.
- .github/skills/**/SKILL.md
  Discoverable as skill packs for relevant tasks.

## VS Code vs Claude Differences

- Instruction scope key:
  VS Code uses applyTo; Claude uses paths.
- Tool naming:
  VS Code commonly uses names like create_file / replace_string_in_file.
  Claude commonly uses names like Write / Edit.
- Hook payload casing:
  VS Code payloads commonly use camelCase fields.
  Claude commonly uses snake_case fields such as tool_input.file_path.
- Hook matcher behavior:
  VS Code currently parses matcher-related values but ignores matcher filtering and runs hooks broadly.
  Claude applies hook matching semantics in its own runtime.

## Required Settings

Enable these VS Code settings for full behavior:

- chat.useCustomAgentHooks
  Required for agent-scoped hooks (for example, strict-formatter.agent.md).
- chat.useAgentsMdFile
  Enables AGENTS.md integration.
- chat.useClaudeMdFile
  Enables CLAUDE.md integration in compatible VS Code flows.

## Hook Script Setup

Run this once on macOS/Linux to mark shell scripts executable:

```bash
chmod +x scripts/*.sh
```

## How To Add New Items

### Add a new instruction

1. Create a new .github/instructions/<topic>.instructions.md file.
2. Add frontmatter fields: name, description, applyTo.
3. Write concise rules in Markdown body.

### Add a new VS Code agent

1. Create .github/agents/<agent-name>.agent.md.
2. Add frontmatter fields: name, description, tools, agents, model, handoffs, hooks.
3. Keep tools minimal and role-specific.

### Add a new prompt

1. Create .github/prompts/<prompt-name>.prompt.md.
2. Add frontmatter fields: description, name, agent, model, tools.
3. Include placeholders and clear expected output format.

### Add a new hook

1. Add or update a .github/hooks/*.json file.
2. Reference a command script and timeout.
3. Ensure script reads stdin JSON and writes stdout JSON with continue true/false.

### Add a new skill

1. Create .github/skills/<skill-name>/SKILL.md.
2. Set frontmatter name equal to the folder name.
3. Add short, task-focused guidance in the body.

### Add Claude equivalents

1. Add matching rule files under .claude/rules with paths.
2. Add Claude agents under .claude/agents with comma-separated tools.
3. Add matching skills under .claude/skills when needed.
