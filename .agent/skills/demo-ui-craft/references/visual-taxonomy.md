# Visual Taxonomy

Use this when the request is vague and the agent needs to invent a compelling demo visual. Pick one primary visual system, then combine it with one supporting motion layer and one proof layer.

## Highest-Impact Demo Visuals

### AI Operating A Computer

Show a cursor moving through a browser, selecting fields, opening menus, reading content, and completing a task. Pair with a compact chat/tool-call rail.

Use for browser-use demos, research agents, QA agents, web automation, support agents, and data-entry workflows.

Smoothness cues: cursor easing with intentional pauses, click ripples, focus rings, small scroll momentum, UI panels that react immediately to each action.

### Terminal To Live Product

Show a terminal command, streaming logs, build/test/deploy success, then transition to a live browser or app shell.

Use for coding agents, deployment tools, local devtools, CI/CD, API platforms, and infra automation.

Smoothness cues: typewriter logs, active line glow, status badges changing in sequence, browser window scaling in after success, final URL or success toast.

### Prompt To Artifact

Show a prompt entering an AI surface, intermediate tool calls, then a generated artifact: slide, image, website, report, chart, video, or document.

Use for generative AI products, creative tools, research/reporting, design automation, and multimodal workflows.

Smoothness cues: token stream, skeleton-to-final morph, progress phases, final artifact snap-to-grid, before/after comparison.

### Workflow Canvas

Show nodes, pipes, arrows, labels, and data packets moving through a process. Use layers for triggers, models, tools, databases, and outputs.

Use for automation platforms, agent orchestration, data pipelines, ETL, RAG, observability, and workflow builders.

Smoothness cues: moving particles along paths, node glow on activation, edge drawing, staggered node entrance, animated success state.

### Dashboard Populating

Start from empty state or loading skeletons and progressively fill metrics, charts, tables, maps, and activity feeds.

Use for analytics, finance, CRM, ops, observability, security, and admin tools.

Smoothness cues: count-up numbers, line draw charts, bar growth, table row streaming, subtle map marker pulses.

### Device Or Browser Theater

Put the product inside a MacBook, phone, browser, IDE, or floating device stack. Animate camera-like zooms, scrolls, pans, and reveals.

Use for SaaS heroes, product launches, mobile apps, devtools, and anything where the UI itself is the object of desire.

Smoothness cues: parallax layers, realistic shadows, consistent perspective, no skewed text, gentle depth movement.

### Chat Bubble Choreography

Use messages, reactions, avatars, typing indicators, file cards, voice bars, and tool-call cards to show collaboration.

Use for AI assistants, team chat, customer support, sales agents, onboarding, and copilots.

Smoothness cues: bubbles enter from their speaker side, typing indicator resolves into content, cards expand only after the relevant message.

### Code Transformation

Show a diff, inline suggestions, file tree changes, test results, and preview output. Avoid walls of code; focus on one meaningful change.

Use for coding agents, refactoring tools, test generators, SDKs, docs generators, and code review products.

Smoothness cues: syntax-highlighted line reveal, deletion/insertion wipe, active file tab, test rows flipping from pending to pass.

### Data Object Journey

Animate a file, document, image, row, lead, ticket, or event moving through stages until it becomes an enriched output.

Use for document AI, CRM enrichment, email agents, support routing, security triage, logistics, and healthcare workflows.

Smoothness cues: object cards transform between states, metadata chips attach, confidence score appears, final destination highlights.

### Map And Globe Intelligence

Show locations, arcs, routes, clusters, heatmaps, or global activity pulses.

Use for logistics, cybersecurity, sales territories, travel, network tools, supply chain, and social proof.

Smoothness cues: arcs draw sequentially, clusters pulse softly, route lines follow real geography, avoid excessive particle noise.

### Bento System Overview

Show one large product tile surrounded by smaller proof tiles: metric, integration, user quote, workflow step, alert, chart.

Use for landing pages and investor demos when breadth matters.

Smoothness cues: staggered tile entrance, hover glow on active tile, internal micro-animation per tile, strict grid alignment.

### Before And After Reveal

Show raw input on one side and polished output on the other. Use a slider, wipe, flip, or layered reveal.

Use for design tools, cleanup/enhancement, optimization, migrations, AI editing, transformations, and performance products.

Smoothness cues: draggable compare handle, masked wipe, synced labels, final result held long enough to inspect.

### Timeline Or Mission Control

Show chronological steps, active runs, queued tasks, completed checks, artifacts, and alerts.

Use for autonomous agents, monitoring, CI, long-running tasks, background jobs, and audit trails.

Smoothness cues: active beam following the timeline, steps locking into completion, artifacts appearing as proof.

### Spatial Stack Of Screens

Show multiple screens floating in a controlled 3D-like stack. Each screen should represent a different workflow stage or product module.

Use for multi-feature products, OS-like tools, design/dev platforms, and broad SaaS demos.

Smoothness cues: shallow depth, stable perspective, blur only on background layers, foreground text remains readable.

### Command Palette Magic

Use a command menu as the central interaction: search, select action, run, result appears.

Use for productivity tools, devtools, admin apps, AI shortcuts, and power-user workflows.

Smoothness cues: keyboard shortcut hint, search suggestions filtering, selected item glow, result surface updates after command.

### Live Collaboration

Show cursors, comments, avatars, presence indicators, approvals, and edits landing in shared UI.

Use for team workflows, docs, design, project management, reviews, and multiplayer apps.

Smoothness cues: colored cursors move naturally, comment pins pop in, avatar stack updates, edit highlight fades slowly.

### Security Scan Reveal

Show files, endpoints, dependencies, or alerts being scanned; risks cluster by severity; fixes apply and risk drops.

Use for security, compliance, code scanning, cloud posture, and privacy tooling.

Smoothness cues: scan beam, severity chips, collapsing issue groups, before/after risk score.

### Knowledge Graph

Show documents, entities, citations, and relationships forming a graph or constellation.

Use for RAG, research agents, legal, healthcare, intelligence, enterprise search, and knowledge bases.

Smoothness cues: nodes settle with spring motion, selected path lights up, citations slide into side panel.

### Media Generation Studio

Show prompt controls, style chips, timeline, generation queue, previews, and final media grid.

Use for image/video/audio generation, creative studios, ad tools, content operations, and design systems.

Smoothness cues: seed thumbnails shimmer then resolve, selected output enlarges, controls update with tactile feedback.

### Financial Or Operations Command Center

Show dense but calm tables, KPIs, anomaly markers, forecasts, and approval flows.

Use for fintech, ops dashboards, internal tools, logistics, procurement, and enterprise demos.

Smoothness cues: numbers count up, anomaly row expands, forecast band draws in, approval button resolves to ledger entry.

## Motion Pairings

- Cursor-led action pairs with browser shells, command palettes, and chat/tool rails.
- Text reveals pair with product-surface reveals, not dense dashboards.
- Flow particles pair with workflow canvases and knowledge graphs.
- Count-ups pair with dashboards, stats, and proof tiles.
- Wipes pair with before/after, image expansion, and code diff.
- Parallax pairs with device theater and bento overviews.
- Confetti/success bursts pair only with true completion states.

## Smooth Animation Standards

- Use easing that feels intentional: spring for pop-in, ease-out for entrance, linear only for constant background loops.
- Keep animation hierarchy clear: primary story motion first, ambient motion second, hover/cursor details third.
- Avoid simultaneous movement of every object. Hold some elements still to make the moving element feel expensive.
- Use stagger in 40-120ms intervals for lists, cards, and steps.
- Preserve readable text during transforms; scale and rotate containers sparingly.
- Prefer opacity + translate + clip-mask for polished reveals.
- Keep loops slow and seamless; hide loop seams behind masks or offscreen travel.
- Add reduced-motion fallback that shows final states without losing meaning.

## Domain-Specific Visual Seeds

- Devtools: IDE tabs, terminal, file tree, tests, browser preview, deploy URL.
- AI agents: chat rail, tool-call cards, cursor path, artifact preview, run timeline.
- Design tools: canvas, layers panel, property inspector, generated thumbnails, before/after.
- Data products: pipeline graph, schema cards, query editor, charts, lineage map.
- Security: attack path, alert queue, risk score, diffed policy, remediation checklist.
- Healthcare: patient timeline, document extraction, triage cards, audit-safe redactions.
- Finance: transaction table, forecast chart, approvals, anomaly explainers, ledger proof.
- Sales/CRM: lead cards, enrichment chips, email sequence, pipeline board, meeting notes.
- Support: ticket inbox, conversation summary, suggested reply, knowledge citation.
- Logistics: route map, vehicle cards, ETA bands, exception alert, warehouse flow.
- Education: lesson plan, progress rings, concept graph, quiz generation, feedback cards.
- Legal: document stack, clauses highlighted, citation graph, redline diff, review status.
- Ecommerce: product grid, inventory sync, checkout flow, recommendation carousel.
- Social/community: activity stream, moderation queue, creator dashboard, growth metrics.
