# Quality Loop

Use this when generating any visual showcase, README demo, hero, animated UI scene, or video-ready composition.

## Minimum Bar

- Text must fit inside its containers at every checked viewport or rendered frame.
- UI controls, badges, chips, and cards must have stable dimensions; animation must not resize the layout.
- The palette must feel intentional: one neutral surface system, one primary accent, one secondary accent, and restrained success/warning colors.
- Foreground product UI must be more important than decorative background motion.
- Motion must communicate progress, cause/effect, or focus. Remove motion that only adds noise.
- The first frame must read clearly without needing animation.
- The final frame must hold a satisfying proof state.

## Iteration Process

1. Generate or implement the first candidate.
2. Capture a screenshot or rendered frame.
3. Self-review against the visual failure checklist below.
4. Fix the highest-impact issue first.
5. Re-render and compare against the prior version.
6. Keep iterating until there are no obvious fit, hierarchy, spacing, color, or motion defects.

## Visual Failure Checklist

- Text clipped, cramped, or escaping rounded boxes.
- Text too large for compact panels.
- Background contrast competing with foreground UI.
- Decorative glow, grid, or particles crossing important labels.
- Too many accent colors with no hierarchy.
- Cards use inconsistent radius, border, shadow, or padding.
- Cursor, arrows, or particles point at nothing meaningful.
- Animation makes every element move at once.
- Important proof state is missing or too small.
- Mobile or narrow layout collapses into overlap.

## Automation Expectations

- For browser UI, use screenshot checks with desktop and mobile viewport sizes.
- For canvas/WebGL/Three.js, check nonblank pixels and framing.
- For generated GIF/video, check dimensions, frame count, file size, and first/final frame readability.
- For README demo assets in this repository, run:

```powershell
python scripts/generate-readme-demo.py
python scripts/check-readme-demo.py
```

The automated check is not a substitute for taste. It catches basic regressions; the agent must still visually inspect the result and improve weak composition.
