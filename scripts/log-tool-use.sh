#!/usr/bin/env bash
set -euo pipefail

# Hook contract: read JSON from stdin, log metadata, then allow execution.
payload="$(cat)"
log_file=".github/hooks/audit.log"
mkdir -p "$(dirname "$log_file")"

if command -v jq >/dev/null 2>&1; then
  tool_name="$(printf '%s' "$payload" | jq -r '.tool_name // .toolName // "unknown"')"
  timestamp="$(date -u +"%Y-%m-%dT%H:%M:%SZ")"
  printf '%s | tool=%s\n' "$timestamp" "$tool_name" >> "$log_file"
else
  timestamp="$(date -u +"%Y-%m-%dT%H:%M:%SZ")"
  printf '%s | tool=unknown\n' "$timestamp" >> "$log_file"
fi

echo '{"continue":true}'
