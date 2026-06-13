# Implementation Recipes

## React/Tailwind Scene Skeleton

Use this structure for most in-app demos:

```tsx
export function DemoScene() {
  return (
    <section className="relative min-h-screen overflow-hidden bg-neutral-950 text-white">
      <BackgroundLayer />
      <main className="relative mx-auto grid min-h-screen w-full max-w-7xl grid-cols-1 items-center gap-8 px-6 py-12 lg:grid-cols-[0.95fr_1.05fr]">
        <NarrativePanel />
        <ProductSurface />
      </main>
    </section>
  );
}
```

Rules:

- Put decorative backgrounds behind `main`.
- Keep one main surface larger than all other elements.
- Use `max-w`, `aspect-ratio`, and explicit min heights to prevent layout shifts.
- Keep real data arrays near the scene so copy, labels, and timing are easy to change.

## Browser/Terminal Demo

Use when showing a dev or agent workflow.

Pieces:

- Terminal panel: command prompt, streaming logs, success line.
- Browser shell: address bar, tabs, app content.
- Status rail: steps such as "Plan", "Edit", "Run", "Verify", "Ship".
- Motion: terminal lines stagger in; browser fades/scales in after success; cursor clicks primary controls.

Implementation hints:

- Drive the scene from a `steps` array with timestamps or active index.
- Use `motion.div` layout transitions for active panels.
- Use monospace only inside terminal/code; keep the rest in the app font.
- Add final proof: green check, deployed URL, visual diff, passing tests, or metric.

## Chat Bubble Flow

Use for AI copilots, support agents, browser-use demos, assistants, or workflow automation.

Pieces:

- User prompt bubble.
- Agent response bubble.
- Tool-call cards with icons and statuses.
- Live result preview: browser, table, chart, document, or canvas.
- Optional cursor path or arrows linking tool calls to the result.

Implementation hints:

- Keep bubbles compact; long text kills demo polish.
- Use tool-call cards with short labels like `read_page`, `edit_file`, `run_tests`, `open_browser`.
- Animate status from queued to running to complete.
- Never leave the result surface blank; even skeletons should resolve.

## Bento Product Reveal

Use for feature breadth or SaaS launch pages.

Pieces:

- One hero tile with actual product surface.
- Two to four supporting tiles: metrics, integrations, activity, chart, workflow.
- Text reveal for headline; marquee or logo loop for proof.

Implementation hints:

- Use a strict grid with stable row heights.
- Give every tile a different content type.
- Animate tile entrance with staggered opacity/translate, not random transforms.
- Avoid nesting cards inside cards.

## Remotion Scene

Use for exportable videos or tightly timed animations.

Pattern:

```tsx
import { Composition } from "remotion";

export const RemotionRoot = () => (
  <Composition
    id="ProductDemo"
    component={ProductDemoScene}
    durationInFrames={150}
    fps={30}
    width={1280}
    height={720}
  />
);
```

Rules:

- Use frame-based timing, not wall-clock timers.
- Keep font sizes larger than normal web UI.
- Test the first, middle, and final frames.
- Prefer remocn compositions and transitions for device/browser/terminal scenes.

## Install And Adapt Checklist

1. Confirm package manager.
2. Confirm Tailwind and shadcn setup before running registry commands.
3. Install one component at a time.
4. Read the generated files and remove unused demo data.
5. Rename components to fit local conventions if the project uses a naming pattern.
6. Replace placeholder copy and media.
7. Verify import aliases such as `@/components`.
8. Run lint/build if available.

## Visual QA Checklist

- Desktop screenshot: no overlap, blank canvas, or unreadable labels.
- Mobile screenshot: primary story still visible or intentionally simplified.
- Motion: no jarring loops, excessive blur, or seizure-risk flashing.
- Contrast: text over images/canvas is readable.
- Performance: no heavy WebGL/canvas background behind already complex UI unless needed.
- Reduced motion: core information remains visible.
