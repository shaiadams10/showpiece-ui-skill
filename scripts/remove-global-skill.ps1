$ErrorActionPreference = "Stop"

$candidatePaths = @(
  (Join-Path $HOME ".agents/skills/demo-ui-craft"),
  (Join-Path $HOME ".codex/skills/demo-ui-craft"),
  (Join-Path $HOME ".gemini/antigravity-cli/skills/demo-ui-craft")
)

$removed = @()

foreach ($path in $candidatePaths) {
  if (Test-Path -LiteralPath $path) {
    $resolved = Resolve-Path -LiteralPath $path
    $name = Split-Path -Leaf $resolved.Path
    if ($name -ne "demo-ui-craft") {
      throw "Refusing to remove unexpected path: $resolved"
    }
    Remove-Item -LiteralPath $resolved.Path -Recurse -Force
    $removed += $resolved.Path
  }
}

if ($removed.Count -eq 0) {
  Write-Host "No global demo-ui-craft installs found."
} else {
  Write-Host "Removed global demo-ui-craft installs:"
  $removed | ForEach-Object { Write-Host "  $_" }
}
