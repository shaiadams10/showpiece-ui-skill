---
name: animated-showcase-ui
description: Create stunning animated showcase UIs, animated product-demo visuals, modern launch scenes, agent demos, SaaS hero demos, browser/terminal walkthroughs, chat bubble flows, MacBook/device mockups, cursor-driven interactions, data-flow diagrams, cinematic Remotion scenes, and polished React/Tailwind/Framer Motion interfaces. Use when the user asks for vague or specific visual direction such as "modern cool animated visuals", "make this look impressive", "create an animated product demo", "build a showcase UI", "make a beautiful animated landing demo", or help choosing/generating visual patterns from libraries such as 21st.dev, Aceternity UI, React Bits, and remocn.
---

# Animated Showcase UI

## Goal

Produce demo UIs that feel like high-end product launches: clear narrative, premium motion, believable product surfaces, dense but legible UI detail, and visuals selected for the product context rather than generic decoration.

The skill should be especially useful when the user is not visually specific. Treat vague asks like "make it modern", "make cool animated visuals", "make it look like a premium demo", or "make this more impressive" as a request to choose the creative direction for them.

## First Move

1. Identify the demo story in one sentence: actor, product, transformation, proof.
2. If the user is vague, do not stall for detailed visual instructions; choose a strong visual direction from `references/visual-taxonomy.md`.
3. Pick a primary visual metaphor from `references/visual-language.md`.
4. Choose implementation sources from `references/component-bank.md`.
5. Build or adapt code in the host project using the existing stack first.
6. Apply the quality loop from `references/quality-loop.md`.
7. Verify visually in a browser or renderer, including desktop and mobile when applicable.

If the user asks for a complete source audit, search `references/source-routes.md` with `rg`; do not load the whole file into context unless the user explicitly asks for the full route list.

## Visual Direction Rules

- Lead with the product surface: browser window, chat, terminal, workflow canvas, dashboard, device mockup, or generated contextual media.
- When the user is not creative or not exact, be creative on their behalf: propose and implement the strongest fitting scene rather than asking for a component list.
- Combine at most one large scene, one motion accent system, and one text reveal system. Too many effects makes a demo look noisy.
- Prefer meaningful motion: cursor paths show intent, arrows show causality, panels reveal progress, terminal lines prove work, charts populate with outcome.
- Design for capture: keep important action inside a 16:9 safe area, avoid tiny text, and make motion readable at 1x playback.
- Build real UI where possible. Use generated bitmap assets for hero backdrops, contextual product imagery, avatars, thumbnails, or cards when they communicate the domain better than abstract gradients.
- Use reduced-motion fallbacks for interaction-heavy or background-heavy effects.
- Reject first drafts with obvious visual defects. Fix text containment, spacing, hierarchy, palette, and motion purpose before calling the work done.

## Decision Guide

- **Agent or AI product demo**: Use chat bubbles, tool-call cards, terminal-to-browser flow, cursor path, progress steps, browser flow, code diff, and AI generation canvas.
- **Developer tool demo**: Use MacBook/browser shells, terminal simulator, live code compilation, code accordion, glass code block, command menu, and deploy success states.
- **SaaS landing or investor demo**: Use hero device assemble, bento grids, infinite marquee, dashboard populate, pricing tier focus, testimonials, stats, and scroll/parallax reveals.
- **Creative or frontier tech demo**: Use React Bits backgrounds, WebGL/canvas shaders, 3D marquee/globe, cursor effects, chromatic transitions, and masked typography.
- **Workflow or automation demo**: Use data-flow pipes, drag-and-drop flow, arrows, checkpoints, timeline, toast notifications, and browser-flow scenes.
- **Video/exportable scene**: Prefer remocn and Remotion-style compositions. Use React UI components inside Remotion only when timing and dimensions are controlled.

## Implementation Workflow

1. Audit the project stack:
   - React/Next/Vite, Tailwind version, shadcn setup, Framer Motion or Motion, Remotion, Three.js/WebGL, icon library.
   - Existing colors, typography, spacing, component conventions.
2. Select a composition:
   - Use `references/visual-language.md` for narrative patterns.
   - Use `references/component-bank.md` for source library selection and audited components.
   - Use `references/implementation-recipes.md` for concrete build patterns.
3. Install or copy components:
   - Aceternity: generally `npx shadcn@latest add @aceternity/<component>`.
   - React Bits: use the component page CLI or shadcn/jsrepo variant, often with TS/Tailwind choices.
   - remocn: generally `pnpm dlx shadcn@latest add @remocn/<component>`.
   - 21st.dev: use public component pages, Magic, MCP, or registry commands when available.
4. Adapt aggressively:
   - Replace demo copy, dummy images, colors, and placeholder data.
   - Keep the source component's core animation logic unless it conflicts with the product story.
   - Remove unused effects and dependencies.
5. Verify:
   - Run the app.
   - Inspect screenshots or rendered frames.
   - Check text fit, responsive layout, animation timing, contrast, and no blank canvases.

## Quality Bar

The output should have:

- A clear first-frame read within 2 seconds.
- One obvious focal path for the viewer's eye.
- Realistic UI states: loading, progress, completion, selection, hover, or active step.
- Consistent shadows, radii, borders, font scale, and icon style.
- No decorative element that competes with the main product surface.
- No one-note palette. Use accents and neutrals intentionally.

## References

- `references/visual-language.md`: demo patterns, storyboards, generated-image guidance.
- `references/visual-taxonomy.md`: expanded bank of high-impact animated visual systems and motion pairings.
- `references/component-bank.md`: audited libraries, categories, when to use each source.
- `references/implementation-recipes.md`: React/Tailwind/Motion/Remotion recipes and validation checks.
- `references/quality-loop.md`: visual QA process, failure checklist, and automated demo-asset checks.
- `references/portability.md`: Codex and Antigravity skill compatibility and install locations.
- `references/source-routes.md`: exhaustive route snapshot from the audited public sitemaps; search with `rg`.

