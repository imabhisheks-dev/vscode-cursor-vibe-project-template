---
description: Perform a focused REST API security review. # Purpose of this ask-mode prompt.
name: Security Review # Prompt label shown in prompt picker.
agent: Reviewer # Recommended reviewing agent.
model: GPT-5.3-Codex # Preferred model for security analysis.
tools: # Read-only tooling for safe review workflows.
  - search/codebase
  - search/usages
  - web/fetch
---

# Security Review Prompt

Review REST API code paths for common vulnerabilities.

- Check authN/authZ enforcement.
- Validate input handling and output encoding.
- Highlight secrets exposure and logging risks.
- List findings by severity with concrete fixes.
