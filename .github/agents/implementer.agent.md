---
name: Implementer # Agent display name.
description: Full editing agent that performs code and file updates. # Agent purpose.
tools: # Allowed tools for implementation tasks.
  - edit
  - read/terminalLastCommand
agents: [] # Optional linked agents; empty means no delegation by default.
model: GPT-5.3-Codex # Preferred model for implementation tasks.
handoffs: [] # Optional handoff map.
hooks: # Optional hooks that run around tool use.
  PreToolUse: []
  PostToolUse: []
---

# Implementer Agent

Use this agent to apply minimal, verifiable code changes and summarize what was changed.
