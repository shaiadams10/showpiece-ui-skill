# Portability

The skill content is intentionally standard Agent Skills format:

- Folder named `demo-ui-craft`.
- Required `SKILL.md`.
- YAML frontmatter with `name` and `description`.
- Markdown instructions in the body.
- Optional `references/` and `assets/`.
- Optional Codex UI metadata in `agents/openai.yaml`; agents that do not read it can ignore it.

## Install Locations

This repository keeps the canonical skill in `.agents/skills/demo-ui-craft`. Use the same `demo-ui-craft` folder in the target skill directory only when intentionally installing elsewhere.

| Tool | Global | Project |
| --- | --- | --- |
| Codex | `~/.agents/skills/demo-ui-craft` | `<project-root>/.agents/skills/demo-ui-craft` |
| Antigravity desktop | `~/.agents/skills/demo-ui-craft` | `<project-root>/.agents/skills/demo-ui-craft` |
| Antigravity CLI | `~/.gemini/antigravity-cli/skills/demo-ui-craft` | `<project-root>/.agent/skills/demo-ui-craft` |

For this repo, do not use the global locations. Run `scripts/install-local-skill.ps1` from the repository root to keep the Antigravity CLI project mirror in sync.

## Compatibility Notes

- Do not rely on `agents/openai.yaml` for core behavior; all operational instructions must stay in `SKILL.md` and `references/`.
- Keep frontmatter limited to `name` and `description` for broad parser compatibility.
- Use relative paths from the skill root when referencing files.
- Treat large references, especially `source-routes.md`, as searchable resources.
