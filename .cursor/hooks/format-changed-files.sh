#!/usr/bin/env bash
set -euo pipefail

# Cursor afterFileEdit hook: format the edited file when Prettier is available.
payload="$(cat)"

if ! command -v jq >/dev/null 2>&1; then
  exit 0
fi

# Support common Cursor / shared payload field names.
file_path="$(printf '%s' "$payload" | jq -r '.file_path // .filePath // .path // .tool_input.file_path // .tool_input.filePath // empty')"

if [ -n "$file_path" ] && [ -f "$file_path" ] && command -v npx >/dev/null 2>&1; then
  case "$file_path" in
    *.js|*.jsx|*.ts|*.tsx|*.json|*.md|*.css|*.scss|*.html|*.yml|*.yaml)
      npx --yes prettier --write "$file_path" >/dev/null 2>&1 || true
      ;;
  esac
fi

exit 0
