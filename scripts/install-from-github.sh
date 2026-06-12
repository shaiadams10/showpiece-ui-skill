#!/usr/bin/env bash
set -euo pipefail

TARGET_PROJECT="${TARGET_PROJECT:-$(pwd)}"
REPO="${REPO:-shaiadams10/showpiece-ui-skill}"
REF="${REF:-main}"
SKIP_ANTIGRAVITY_CLI_MIRROR="${SKIP_ANTIGRAVITY_CLI_MIRROR:-0}"

TMP_ROOT="$(mktemp -d)"
ZIP_PATH="$TMP_ROOT/repo.zip"
EXTRACT_PATH="$TMP_ROOT/extract"
ARCHIVE_URL="https://github.com/$REPO/archive/refs/heads/$REF.zip"

cleanup() {
  rm -rf "$TMP_ROOT"
}
trap cleanup EXIT

mkdir -p "$EXTRACT_PATH"

if command -v curl >/dev/null 2>&1; then
  curl -fsSL "$ARCHIVE_URL" -o "$ZIP_PATH"
elif command -v wget >/dev/null 2>&1; then
  wget -q "$ARCHIVE_URL" -O "$ZIP_PATH"
else
  echo "curl or wget is required" >&2
  exit 1
fi

if ! command -v unzip >/dev/null 2>&1; then
  echo "unzip is required" >&2
  exit 1
fi

unzip -q "$ZIP_PATH" -d "$EXTRACT_PATH"
SOURCE_ROOT="$(find "$EXTRACT_PATH" -mindepth 1 -maxdepth 1 -type d | head -n 1)"
SOURCE_SKILL="$SOURCE_ROOT/.agents/skills/showpiece-ui"

if [[ ! -f "$SOURCE_SKILL/SKILL.md" ]]; then
  echo "Downloaded archive did not contain .agents/skills/showpiece-ui/SKILL.md" >&2
  exit 1
fi

CODEX_DEST="$TARGET_PROJECT/.agents/skills/showpiece-ui"
mkdir -p "$(dirname "$CODEX_DEST")"
rm -rf "$CODEX_DEST"
cp -R "$SOURCE_SKILL" "$(dirname "$CODEX_DEST")/"
echo "Installed repo-local skill:"
echo "  $CODEX_DEST"

if [[ "$SKIP_ANTIGRAVITY_CLI_MIRROR" != "1" ]]; then
  CLI_DEST="$TARGET_PROJECT/.agent/skills/showpiece-ui"
  mkdir -p "$(dirname "$CLI_DEST")"
  rm -rf "$CLI_DEST"
  cp -R "$SOURCE_SKILL" "$(dirname "$CLI_DEST")/"
  echo "Installed Antigravity CLI project mirror:"
  echo "  $CLI_DEST"
fi

