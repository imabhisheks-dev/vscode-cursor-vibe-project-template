#!/usr/bin/env bash
set -euo pipefail

# Hook contract: read JSON from stdin and return allow/deny decision JSON.
payload="$(cat)"

if ! command -v jq >/dev/null 2>&1; then
  echo '{"continue":true}'
  exit 0
fi

candidate="$(printf '%s' "$payload" | jq -r '.tool_input.command // .tool_input.query // .tool_input.sql // ""')"
lower="$(printf '%s' "$candidate" | tr '[:upper:]' '[:lower:]')"

if printf '%s' "$lower" | grep -Eq 'rm[[:space:]]+-rf|drop[[:space:]]+table|truncate[[:space:]]+table'; then
  echo '{"continue":false,"permissionDecision":"deny","reason":"Blocked dangerous command pattern."}'
  exit 0
fi

echo '{"continue":true}'
