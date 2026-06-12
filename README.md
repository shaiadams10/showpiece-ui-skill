# Demo UI Craft Skill

Repo-local Agent Skill for creating polished animated demo UIs: agent workbenches, terminal-to-browser flows, prompt-to-artifact scenes, cinematic device mockups, workflow canvases, dashboard population, chat choreography, code transformations, knowledge graphs, and other high-end product-demo visuals.

## Install Into A Local Project

From the root of the project where you want the skill installed.

Recommended `npx` install from GitHub:

```bash
npx github:shaiadams10/demo-ui-craft-skill
```

Install into a different target directory:

```bash
npx github:shaiadams10/demo-ui-craft-skill -- --target /path/to/project
```

PowerShell:

```powershell
powershell -ExecutionPolicy Bypass -Command "irm https://raw.githubusercontent.com/shaiadams10/demo-ui-craft-skill/main/scripts/install-from-github.ps1 | iex"
```

Bash:

```bash
curl -fsSL https://raw.githubusercontent.com/shaiadams10/demo-ui-craft-skill/main/scripts/install-from-github.sh | bash
```

This installs:

- `.agents/skills/demo-ui-craft` for Codex and Antigravity desktop project-local discovery.
- `.agent/skills/demo-ui-craft` for Antigravity CLI project-local discovery.

## Clone And Install

```powershell
git clone https://github.com/shaiadams10/demo-ui-craft-skill.git
cd demo-ui-craft-skill
powershell -ExecutionPolicy Bypass -File scripts/install-local-skill.ps1 -TargetProject "C:\path\to\your\project"
```

## Use In This Repo

The canonical skill lives at `.agents/skills/demo-ui-craft`.

Run validation after edits:

```powershell
python "C:/Users/shaib/.codex/skills/.system/skill-creator/scripts/quick_validate.py" ".agents/skills/demo-ui-craft"
```

Package the skill:

```powershell
powershell -ExecutionPolicy Bypass -File scripts/package-skill.ps1
```
