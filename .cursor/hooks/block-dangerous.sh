#!/usr/bin/env bash
set -euo pipefail

# Cursor beforeShellExecution hook: allow or deny dangerous shell commands.
payload="$(cat)"

if ! command -v jq >/dev/null 2>&1; then
  echo '{ "permission": "allow" }'
  exit 0
fi

candidate="$(printf '%s' "$payload" | jq -r '.command // .tool_input.command // .tool_input.query // .tool_input.sql // ""')"
lower="$(printf '%s' "$candidate" | tr '[:upper:]' '[:lower:]')"

if printf '%s' "$lower" | grep -Eq 'rm[[:space:]]+-rf|drop[[:space:]]+table|truncate[[:space:]]+table'; then
  cat <<'EOF'
{
  "permission": "deny",
  "user_message": "Blocked a dangerous command pattern (rm -rf / DROP TABLE / TRUNCATE TABLE).",
  "agent_message": "A project safety hook denied this command because it matched a dangerous pattern."
}
EOF
  exit 0
fi

echo '{ "permission": "allow" }'
exit 0
