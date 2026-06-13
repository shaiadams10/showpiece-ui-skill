# Repository Agent Instructions

## Local Skill Scope

This repository owns the `animated-showcase-ui` skill. Keep it repo-local.

- Canonical skill path: `.agents/skills/animated-showcase-ui`
- Do not install or copy this skill into global user locations such as `~/.agents/skills`, `~/.codex/skills`, or `~/.gemini/antigravity-cli/skills`.
- For Antigravity CLI project-local discovery, sync the canonical skill to `.agent/skills/animated-showcase-ui` with `scripts/install-local-skill.ps1`.

## Editing The Skill

- Edit the canonical copy under `.agents/skills/animated-showcase-ui` only.
- Keep `SKILL.md` concise and put larger guidance in `references/`.
- Treat `references/source-routes.md` as a searchable audit artifact; use `rg` instead of loading it whole.
- After edits, run:

```powershell
python "C:/Users/shaib/.codex/skills/.system/skill-creator/scripts/quick_validate.py" ".agents/skills/animated-showcase-ui"
```

## Visual Direction

When improving the skill, expand reusable visual systems and decision rules rather than adding one-off component examples. The most important references are:

- `.agents/skills/animated-showcase-ui/references/visual-taxonomy.md`
- `.agents/skills/animated-showcase-ui/references/visual-language.md`
- `.agents/skills/animated-showcase-ui/references/component-bank.md`

## Packaging

- `package.json` exposes the public `npx github:shaiadams10/animated-showcase-ui-skill` installer through `scripts/install-npx.cjs`.
- Use `scripts/install-local-skill.ps1` to create/update the Antigravity CLI project-local mirror.
- Use `scripts/install-from-github.ps1` and `scripts/install-from-github.sh` as the public raw-GitHub installer entrypoints documented in `README.md`.
- Use `scripts/package-skill.ps1` to build `dist/animated-showcase-ui-skill.zip` from the canonical skill.
- Use `scripts/remove-global-skill.ps1` to remove accidental global installs of this exact skill name.

