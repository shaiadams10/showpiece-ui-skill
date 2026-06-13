$ErrorActionPreference = "Stop"

$candidatePaths = @(
  (Join-Path $HOME ".agents/skills/animated-showcase-ui"),
  (Join-Path $HOME ".codex/skills/animated-showcase-ui"),
  (Join-Path $HOME ".gemini/antigravity-cli/skills/animated-showcase-ui")
)

$removed = @()

foreach ($path in $candidatePaths) {
  if (Test-Path -LiteralPath $path) {
    $resolved = Resolve-Path -LiteralPath $path
    $name = Split-Path -Leaf $resolved.Path
    if ($name -ne "animated-showcase-ui") {
      throw "Refusing to remove unexpected path: $resolved"
    }
    Remove-Item -LiteralPath $resolved.Path -Recurse -Force
    $removed += $resolved.Path
  }
}

if ($removed.Count -eq 0) {
  Write-Host "No global animated-showcase-ui installs found."
} else {
  Write-Host "Removed global animated-showcase-ui installs:"
  $removed | ForEach-Object { Write-Host "  $_" }
}

