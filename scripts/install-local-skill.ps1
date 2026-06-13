param(
  [string]$TargetProject,
  [switch]$SkipAntigravityCliMirror
)

$ErrorActionPreference = "Stop"

$repoRoot = Resolve-Path -LiteralPath (Join-Path $PSScriptRoot "..")
$canonical = Join-Path $repoRoot ".agents/skills/animated-showcase-ui"
$targetRoot = if ($TargetProject) {
  Resolve-Path -LiteralPath $TargetProject
} else {
  $repoRoot
}
$skillDest = Join-Path $targetRoot ".agents/skills/animated-showcase-ui"
$cliMirror = Join-Path $targetRoot ".agent/skills/animated-showcase-ui"

if (-not (Test-Path -LiteralPath (Join-Path $canonical "SKILL.md"))) {
  throw "Canonical skill is missing: $canonical"
}

$skillParent = Split-Path -Parent $skillDest
New-Item -ItemType Directory -Force -Path $skillParent | Out-Null

if ($skillDest -ne $canonical) {
  if (Test-Path -LiteralPath $skillDest) {
    $resolvedDest = Resolve-Path -LiteralPath $skillDest
    if (-not $resolvedDest.Path.StartsWith($targetRoot.Path, [System.StringComparison]::OrdinalIgnoreCase)) {
      throw "Refusing to remove skill outside target project: $resolvedDest"
    }
    Remove-Item -LiteralPath $skillDest -Recurse -Force
  }
  Copy-Item -LiteralPath $canonical -Destination $skillParent -Recurse
}

Write-Host "Repo-local skill:"
Write-Host "  $skillDest"

if (-not $SkipAntigravityCliMirror) {
  $mirrorParent = Split-Path -Parent $cliMirror
  New-Item -ItemType Directory -Force -Path $mirrorParent | Out-Null

  if (Test-Path -LiteralPath $cliMirror) {
    $resolvedMirror = Resolve-Path -LiteralPath $cliMirror
    if (-not $resolvedMirror.Path.StartsWith($targetRoot.Path, [System.StringComparison]::OrdinalIgnoreCase)) {
      throw "Refusing to remove mirror outside repo: $resolvedMirror"
    }
    Remove-Item -LiteralPath $cliMirror -Recurse -Force
  }

  Copy-Item -LiteralPath $canonical -Destination $mirrorParent -Recurse
  Write-Host "Synced Antigravity CLI project mirror:"
  Write-Host "  $cliMirror"
}

Write-Host "No global skill locations were modified."

