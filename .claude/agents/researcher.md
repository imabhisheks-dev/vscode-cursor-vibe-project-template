---
name: Researcher # Required Claude agent name field.
description: Read-only research agent for discovery and planning. # Agent purpose.
tools: Read, Grep, Glob # Comma-separated tool list in Claude format.
disallowedTools: Edit, Write, Bash # Comma-separated tools this agent must not use.
---

# Researcher Agent

Use for codebase exploration, requirements gathering, and implementation planning.
