# Hook contract: read JSON from stdin, optionally act, then emit JSON to stdout.
$raw = [Console]::In.ReadToEnd()

if ([string]::IsNullOrWhiteSpace($raw)) {
  Write-Output '{"continue":true}'
  exit 0
}

try {
  $payload = $raw | ConvertFrom-Json -Depth 20
} catch {
  Write-Output '{"continue":true}'
  exit 0
}

$filePath = $null
if ($payload.tool_input.filePath) { $filePath = $payload.tool_input.filePath }
elseif ($payload.tool_input.file_path) { $filePath = $payload.tool_input.file_path }

if ($filePath -and (Test-Path -LiteralPath $filePath)) {
  $ext = [System.IO.Path]::GetExtension($filePath).ToLowerInvariant()
  $supported = @('.js', '.jsx', '.ts', '.tsx', '.json', '.md', '.css', '.scss', '.html', '.yml', '.yaml')
  if ($supported -contains $ext) {
    $npx = Get-Command npx -ErrorAction SilentlyContinue
    if ($npx) {
      try {
        & $npx.Source --yes prettier --write $filePath *> $null
      } catch {
        # Ignore formatter failures so the hook never hard-blocks work.
      }
    }
  }
}

Write-Output '{"continue":true}'
