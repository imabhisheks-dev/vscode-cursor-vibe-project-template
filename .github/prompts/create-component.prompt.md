---
description: Scaffold a new UI component with tests and docs. # What this reusable prompt does.
name: Create Component # Prompt label shown in prompt picker.
agent: Implementer # Agent mode target that should execute the prompt.
model: GPT-5.3-Codex # Preferred model for this prompt.
tools: # Optional tool constraints for this prompt.
  - edit
  - search/codebase
---

# Create Component Prompt

Create a new component using project conventions.

- Ask for component name and destination path if missing.
- Generate source, test, and minimal usage docs.
- Keep accessibility and typing requirements in scope.
