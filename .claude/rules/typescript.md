---
name: TypeScript Claude Rules # Rule set label.
description: TypeScript-specific guidance for Claude tools. # Purpose of this file.
paths: # Claude path globs for TS/TSX files.
  - "**/*.ts"
  - "**/*.tsx"
---

# TypeScript Rule

- Prefer strict typing and explicit interfaces.
- Validate untrusted input at application boundaries.
