---
name: Feature Builder # Agent display name.
description: Orchestrator agent that delegates research and implementation. # Agent purpose.
tools: # Tool set includes agent delegation.
  - agent
agents: # Delegation targets available to this orchestrator.
  - Researcher
  - Implementer
model: GPT-5.3-Codex # Preferred model for orchestration.
handoffs: # Optional routing guidance.
  - agent: Researcher
    when: Early discovery, requirements gathering, and architecture exploration.
  - agent: Implementer
    when: After scope is validated and build tasks are ready.
hooks: # Optional hooks around tool use.
  PreToolUse: []
  PostToolUse: []
---

# Feature Builder Agent

Use this agent as a coordinator for multi-step feature delivery.
