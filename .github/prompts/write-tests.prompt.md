---
description: Generate unit tests for changed behavior. # Purpose of this prompt template.
name: Write Tests # Prompt label shown in prompt picker.
agent: Implementer # Agent expected to create or update tests.
model: GPT-5.3-Codex # Preferred model for test generation.
tools: # Tools useful for searching and editing tests.
  - search/codebase
  - edit
---

# Write Tests Prompt

Generate unit tests for the selected module.

- Cover happy path and error cases.
- Mock external dependencies as needed.
- Keep test names behavior-oriented.
- Ensure tests are deterministic and isolated.
