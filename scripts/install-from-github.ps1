param(
  [string]$TargetProject = (Get-Location).Path,
  [string]$Repo = "shaiadams10/showpiece-ui-skill",
  [string]$Ref = "main",
  [switch]$SkipAntigravityCliMirror
)

$ErrorActionPreference = "Stop"

$target = Resolve-Path -LiteralPath $TargetProject
$tempRoot = Join-Path ([System.IO.Path]::GetTempPath()) ("showpiece-ui-" + [System.Guid]::NewGuid().ToString("N"))
$zipPath = Join-Path $tempRoot "repo.zip"
$extractPath = Join-Path $tempRoot "extract"
$archiveUrl = "https://github.com/$Repo/archive/refs/heads/$Ref.zip"

New-Item -ItemType Directory -Force -Path $tempRoot | Out-Null

try {
  Invoke-WebRequest -UseBasicParsing -Uri $archiveUrl -OutFile $zipPath
  Expand-Archive -LiteralPath $zipPath -DestinationPath $extractPath

  $sourceSkill = Get-ChildItem -LiteralPath $extractPath -Directory |
    Select-Object -First 1 |
    ForEach-Object { Join-Path $_.FullName ".agents/skills/showpiece-ui" }

  if (-not (Test-Path -LiteralPath (Join-Path $sourceSkill "SKILL.md"))) {
    throw "Downloaded archive did not contain .agents/skills/showpiece-ui/SKILL.md"
  }

  $codexDest = Join-Path $target ".agents/skills/showpiece-ui"
  $codexParent = Split-Path -Parent $codexDest
  New-Item -ItemType Directory -Force -Path $codexParent | Out-Null
  if (Test-Path -LiteralPath $codexDest) {
    Remove-Item -LiteralPath $codexDest -Recurse -Force
  }
  Copy-Item -LiteralPath $sourceSkill -Destination $codexParent -Recurse
  Write-Host "Installed repo-local skill:"
  Write-Host "  $codexDest"

  if (-not $SkipAntigravityCliMirror) {
    $cliDest = Join-Path $target ".agent/skills/showpiece-ui"
    $cliParent = Split-Path -Parent $cliDest
    New-Item -ItemType Directory -Force -Path $cliParent | Out-Null
    if (Test-Path -LiteralPath $cliDest) {
      Remove-Item -LiteralPath $cliDest -Recurse -Force
    }
    Copy-Item -LiteralPath $sourceSkill -Destination $cliParent -Recurse
    Write-Host "Installed Antigravity CLI project mirror:"
    Write-Host "  $cliDest"
  }
} finally {
  if (Test-Path -LiteralPath $tempRoot) {
    Remove-Item -LiteralPath $tempRoot -Recurse -Force
  }
}

