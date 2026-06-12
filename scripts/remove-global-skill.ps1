$ErrorActionPreference = "Stop"

$candidatePaths = @(
  (Join-Path $HOME ".agents/skills/showpiece-ui"),
  (Join-Path $HOME ".codex/skills/showpiece-ui"),
  (Join-Path $HOME ".gemini/antigravity-cli/skills/showpiece-ui")
)

$removed = @()

foreach ($path in $candidatePaths) {
  if (Test-Path -LiteralPath $path) {
    $resolved = Resolve-Path -LiteralPath $path
    $name = Split-Path -Leaf $resolved.Path
    if ($name -ne "showpiece-ui") {
      throw "Refusing to remove unexpected path: $resolved"
    }
    Remove-Item -LiteralPath $resolved.Path -Recurse -Force
    $removed += $resolved.Path
  }
}

if ($removed.Count -eq 0) {
  Write-Host "No global showpiece-ui installs found."
} else {
  Write-Host "Removed global showpiece-ui installs:"
  $removed | ForEach-Object { Write-Host "  $_" }
}

