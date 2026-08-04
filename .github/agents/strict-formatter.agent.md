---
name: Strict Formatter # Agent display name.
description: Editing agent that enforces formatting with post-tool hooks. # Agent purpose.
tools: # Edit-capable tools.
  - edit
  - search/codebase
agents: [] # Optional linked agents.
model: GPT-5.3-Codex # Preferred model for formatting-focused edits.
handoffs: [] # Optional handoffs.
hooks: # Agent-scoped hooks.
  PostToolUse:
    - type: command
      command: ./scripts/format-changed-files.sh
      timeout: 30
      windows:
        command: powershell -ExecutionPolicy Bypass -File scripts/format-changed-files.ps1
      linux:
        command: ./scripts/format-changed-files.sh
      osx:
        command: ./scripts/format-changed-files.sh
---

# Strict Formatter Agent

Enable the VS Code setting `chat.useCustomAgentHooks` for this agent-scoped hook to run.
This profile is useful when you want formatting enforced automatically after edit-like tools.
