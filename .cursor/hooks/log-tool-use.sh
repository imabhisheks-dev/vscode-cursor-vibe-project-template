#!/usr/bin/env bash
set -euo pipefail

# Cursor preToolUse hook: append tool activity to a repository audit log.
payload="$(cat)"
log_file=".cursor/hooks/audit.log"
mkdir -p "$(dirname "$log_file")"

if command -v jq >/dev/null 2>&1; then
  tool_name="$(printf '%s' "$payload" | jq -r '.tool_name // .toolName // .tool // "unknown"')"
  timestamp="$(date -u +"%Y-%m-%dT%H:%M:%SZ")"
  printf '%s | tool=%s\n' "$timestamp" "$tool_name" >> "$log_file"
else
  timestamp="$(date -u +"%Y-%m-%dT%H:%M:%SZ")"
  printf '%s | tool=unknown\n' "$timestamp" >> "$log_file"
fi

echo '{ "permission": "allow" }'
exit 0
