param(
  [string]$OutputPath = "dist/showpiece-ui-skill.zip"
)

$ErrorActionPreference = "Stop"

$repoRoot = Resolve-Path -LiteralPath (Join-Path $PSScriptRoot "..")
$skillPath = Join-Path $repoRoot ".agents/skills/showpiece-ui"
$output = Join-Path $repoRoot $OutputPath
$outputParent = Split-Path -Parent $output

if (-not (Test-Path -LiteralPath (Join-Path $skillPath "SKILL.md"))) {
  throw "Canonical skill is missing: $skillPath"
}

New-Item -ItemType Directory -Force -Path $outputParent | Out-Null
if (Test-Path -LiteralPath $output) {
  Remove-Item -LiteralPath $output -Force
}

Compress-Archive -LiteralPath $skillPath -DestinationPath $output
Write-Host "Packaged skill:"
Write-Host "  $output"

