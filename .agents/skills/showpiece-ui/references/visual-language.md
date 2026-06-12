# Visual Language

Use this file to define the demo before choosing components.

## Demo Archetypes

### Terminal to Browser

Show a command running, logs streaming, a build/deploy step completing, then a browser surface opening with the result. Use for devtools, AI coding agents, infrastructure, API demos, and "from prompt to shipped" stories.

Best pieces: remocn Terminal To Browser Deploy, Terminal Simulator, Live Code Compilation; Aceternity Macbook Scroll, Terminal, Code Block; React Bits Faulty Terminal for stylized backgrounds.

### Agent Workbench

Show chat on one side, tool calls or files in the middle, and a live app/browser/dashboard on the other side. Animate cursor movements, status pills, and line-by-line reasoning artifacts.

Best pieces: 21st AI Chat/Input components, remocn Browser Flow, Data Flow Pipes, Progress Steps, Tool Menu Slide In; Aceternity Sidebar, Animated Modal, Placeholders and Vanish Input.

### Product Surface Reveal

Open with masked typography, then reveal a polished dashboard, app shell, or feature card stack. Use subtle parallax and bento panels to communicate breadth without a wall of text.

Best pieces: Aceternity Hero Parallax, Container Scroll Animation, Bento Grid, Layout Grid, Sticky Scroll Reveal; React Bits Magic Bento, Scroll Stack, Chroma Grid; remocn Hero Device Assemble.

### Flow Map

Use nodes, arrows, pipes, progress steps, and cards to show a process moving from input to output. Good for automation, data pipelines, security scans, onboarding, and multi-step AI workflows.

Best pieces: remocn Data Flow Pipes, Drag And Drop Flow, Progress Steps, Bounding Box Selector; Aceternity Timeline, Tracing Beam, Google Gemini Effect, World Map.

### Cinematic Device Scene

Use a laptop, browser, phone, or floating panels as the hero object. Animate assembly, zoom-through, swipe, or scroll.

Best pieces: remocn Hero Device Assemble, Device Mockup Zoom, Image Expand To Fullscreen; Aceternity Macbook Scroll, 3D Card Effect, 3D Pin, 3D Marquee, Images Slider.

### Cursor-Led Interaction

Animate a pointer performing real UI actions: select text, click a button, drag a node, open a menu, run a search. Use when the demo needs "browser-use" or "agent operating UI" energy.

Best pieces: remocn Cursor, Browser Flow, Drag And Drop Flow; React Bits Target Cursor, Ghost Cursor, Splash Cursor, Blob Cursor, Click Spark; Aceternity Following Pointer, Pointer Highlight, Lens.

### Data Comes Alive

Start with empty states, then populate charts, rows, metrics, and cards. Use for analytics, finance, observability, CRM, and dashboards.

Best pieces: remocn Dashboard Populate, Animated Line Chart, Animated Bar Chart; Aceternity Timeline, Compare, GitHub Globe, World Map; 21st tables, charts, cards, numbers.

## Scene Formula

Use this five-beat structure for rich demos:

1. Context: headline or app shell says what domain this is.
2. Input: prompt, command, file upload, search, or selected object.
3. Process: tool calls, cursor path, data-flow pipes, terminal logs, progress steps.
4. Reveal: browser/device/dashboard transitions into final state.
5. Proof: metric, success toast, diff, chart, completed checklist, or generated artifact.

## Generated Visuals

Generate bitmap visuals when the demo needs domain-specific atmosphere or concrete objects that a component library will not provide:

- Product screenshots or mock thumbnails for cards.
- Industry-specific dashboard imagery: logistics maps, healthcare records, fintech charts, design canvases.
- Avatars, customer logos, document thumbnails, or app icons.
- Hero background photography only when it directly supports the product context.

Avoid purely abstract gradient backdrops unless the product itself is abstract or creative tooling. Generated images should not replace the actual product UI surface.

## Timing

- Microinteractions: 120-250ms.
- Panel transitions: 300-600ms.
- Text reveals: 500-1200ms.
- Story beats in video: 1.5-3.0s each.
- Background loops: slow enough to be perceived but not distract from foreground UI.

## Accessibility And Resilience

- Respect `prefers-reduced-motion`.
- Do not rely on animation to explain required information.
- Keep text contrast readable over video, canvas, and gradient surfaces.
- Disable or simplify cursor effects on touch/mobile if they add no value.
