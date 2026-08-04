# AGENTS

This file is always-on guidance for multi-agent workflows in VS Code.

## Shared Rules

- Planner agents should gather context and produce actionable plans.
- Implementer agents should make minimal, testable code changes.
- Reviewer agents should prioritize correctness, security, and regressions.
- All agents should report assumptions and unknowns clearly.

## Handoff Protocol

- Planning output should include scope, risks, and acceptance checks.
- Implementation output should include changed files and verification steps.
- Review output should list findings by severity, then recommendations.
