#!/usr/bin/env bash
set -euo pipefail

# Hook contract: read JSON from stdin, optionally act, then emit JSON to stdout.
payload="$(cat)"

if ! command -v jq >/dev/null 2>&1; then
  echo '{"continue":true}'
  exit 0
fi

# Support both camelCase and snake_case payload variants.
file_path="$(printf '%s' "$payload" | jq -r '.tool_input.filePath // .tool_input.file_path // empty')"

if [ -n "$file_path" ] && [ -f "$file_path" ] && command -v npx >/dev/null 2>&1; then
  case "$file_path" in
    *.js|*.jsx|*.ts|*.tsx|*.json|*.md|*.css|*.scss|*.html|*.yml|*.yaml)
      npx --yes prettier --write "$file_path" >/dev/null 2>&1 || true
      ;;
  esac
fi

echo '{"continue":true}'
