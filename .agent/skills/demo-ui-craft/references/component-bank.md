# Component Bank

This audit covers the libraries the user supplied. Use `source-routes.md` for the complete route snapshot, especially when searching for a specific component name.

## Source Roles

| Source | Use For | Avoid When |
| --- | --- | --- |
| 21st.dev | Community component discovery, AI chat/input surfaces, registry installs, inspiration across many design systems, Magic-generated variations. | You need a stable closed catalog; it is a live community registry with thousands of routes. |
| Aceternity UI | React/Next/Tailwind/Motion hero sections, scroll effects, backgrounds, cards, nav, forms, device mockups, production-ready shadcn-style installs. | You need video-frame timing or Remotion-native composition. |
| React Bits | Highly animated React effects, text animation, backgrounds, cursor effects, creative UI cards, variant-based copy/install. | You need restrained enterprise UI or accessibility-first primitives without adaptation. |
| remocn | Cinematic Remotion components, video-ready UI scenes, terminal/browser flows, transitions, typography, timed compositions. | You need generic app primitives only, unless using remocn UI components directly. |

## 21st.dev

21st.dev provides:

- Public community components with Featured, Newest, Popular, Best of Week, Themes, and Top Authors views.
- Marketing block categories: Announcements, Backgrounds, Borders, Calls to Action, Clients, Comparisons, Docks, Features, Footers, Heroes, Hooks, Images, Maps, Navigation Menus, Pricing Sections, Scroll Areas, Shaders, Testimonials, Texts, Videos.
- UI component categories: Accordions, AI Chats, Alerts, Avatars, Badges, Buttons, Calendars, Cards, Carousels, Checkboxes, Date Pickers, Dialogs/Modals, Dropdowns, Empty States, File Trees, File Uploads, Forms, Icons, Inputs, Links, Menus, Notifications, Numbers, Paginations, Popovers, Radio Groups, Selects, Sidebars, Sign Ins, Sign Ups, Sliders, Spinner Loaders, Tables, Tabs, Tags, Text Areas, Toasts, Toggles, Tooltips.
- Magic: prompt-to-UI variations, web or MCP usage, enhancement of existing UI, logo/icon lookup through SVGL, community-component inspiration, and ownership of generated code.
- 21st registry libraries: publish with `npx @21st-dev/registry publish`, install with `npx @21st-dev/registry add @scope/component`, with public, unlisted, private, and team-scoped visibility.

Demo use:

- Use AI Chats, Inputs, Cards, Buttons, Dialogs, Sidebars, Tables, Forms, and Numbers for agent workbench screens.
- Use Heroes, Backgrounds, Shaders, Pricing, Testimonials, CTA, and Texts for launch pages.
- Use Magic when the user wants multiple stylistic variations or when the existing project has no strong visual direction.

Audit note: the route snapshot contained 7,635 community component routes. Search `source-routes.md` for names such as `ai-chat`, `animated-ai-input`, `browser`, `terminal`, `dashboard`, `button`, `shader`, `hero`, or author/library names.

## Aceternity UI

Installation pattern:

```bash
npx shadcn@latest add @aceternity/<component>
```

Demo pages often expose a demo install command:

```bash
npx shadcn@latest add @aceternity/<component>-demo
```

Audited categories and useful components:

- Backgrounds and effects: Webcam Pixel Grid, Images Badge, Parallax Hero Images, Scales, Dotted Glow Background, Background Ripple Effect, Sparkles, Background Gradient, Background Gradient Animation, Wavy Background, Background Boxes, Background Beams, Background Beams With Collision, Background Lines, Aurora Background, Meteors, Glowing Stars, Shooting Stars, Vortex, Spotlight, Spotlight New, Canvas Reveal Effect, SVG Mask Effect, Tracing Beam, Lamp Effect, Grid and Dot Backgrounds, Glowing Effect, Google Gemini Effect.
- Cards: Keyboard, Terminal, Tooltip Card, ASCII Art, Pixelated Canvas, 3D Card Effect, Evervault Card, Card Stack, Card Hover Effect, Wobble Card, Expandable Card, Card Spotlight, Focus Cards, Infinite Moving Cards, Draggable Card, Comet Card, Glare Card, Direction Aware Hover.
- Scroll and parallax: Parallax Scroll, Sticky Scroll Reveal, Macbook Scroll, Container Scroll Animation, Hero Parallax.
- Text: Canvas Text, Encrypted Text, Layout Text Flip, Colourful Text, Squiggly Text, Text Generate Effect, Typewriter Effect, Flip Words, Text Hover Effect, Container Text Flip, Hero Highlight, Text Reveal Card, Text Flipping Board.
- Buttons: Magnetic Button, Noise Background, Tailwind CSS Buttons, Hover Border Gradient, Moving Border, Stateful Button.
- Loaders: Multi Step Loader, Loader.
- Navigation: Notch, Floating Navbar, Navbar Menu, Sidebar, Floating Dock, Tabs, Resizable Navbar, Sticky Banner.
- Inputs and forms: Signup Form, Placeholders And Vanish Input, File Upload, Gooey Input.
- Overlays and popovers: Dither Shader, Animated Modal, Animated Tooltip, Link Preview.
- Carousels and sliders: Images Slider, Carousel, Apple Cards Carousel, Animated Testimonials.
- Layout and grid: Layout Grid, Bento Grid, Container Cover.
- Data and visualization: GitHub Globe, World Map, Timeline, Compare, Code Block.
- Cursor and pointer: Following Pointer, Pointer Highlight, Lens.
- 3D: 3D Globe, 3D Pin, 3D Marquee.
- Free sections: Feature Sections Free, Cards Sections Free, Hero Sections Free.
- Pro blocks/templates surfaced by the site: Hero Sections, Shaders, Illustrations, Logo Clouds, Bento Grids, CTA Sections, Testimonials, Team Sections, Empty States, Feature Sections, Pricing Sections, Cards, Navbars, Footers, Login and Signup, Contact Sections, Blog Sections, Blog Content Sections, FAQs, Sidebars, Stats Sections, Backgrounds, Text Animations, plus multiple marketing/portfolio templates.

Best demo matches:

- MacBook/device hero: Macbook Scroll, Container Scroll Animation, 3D Card Effect.
- AI/devtools: Terminal, Code Block, Sidebar, Placeholders And Vanish Input, Multi Step Loader.
- Premium launch: Hero Parallax, Lamp Effect, Spotlight, Bento Grid, Infinite Moving Cards, Text Generate Effect.

## React Bits

React Bits provides animated, interactive React components with CSS/Tailwind and JavaScript/TypeScript variants. It supports shadcn and jsrepo style installs; component pages provide copy-ready commands. A common shadcn example is:

```bash
npx shadcn@latest add @react-bits/BlurText-TS-TW
```

Audited groups:

- Text animations: Split Text, Blur Text, Circular Text, Text Type, Shuffle, Shiny Text, Text Pressure, Curved Loop, Fuzzy Text, Gradient Text, Falling Text, Text Cursor, Decrypted Text, True Focus, Scroll Float, Scroll Reveal, ASCII Text, Scrambled Text, Rotating Text, Glitch Text, Scroll Velocity, Variable Proximity, Count Up.
- Animations and effects: Animated Content, Fade Content, Electric Border, Orbit Images, Pixel Transition, Glare Hover, Antigravity, Logo Loop, Target Cursor, Magic Rings, Laser Flow, Magnet Lines, Ghost Cursor, Gradual Blur, Click Spark, Magnet, Strands, Sticker Peel, Pixel Trail, Cubes, Metallic Paint, Noise, Shape Blur, Crosshair, Image Trail, Ribbons, Splash Cursor, Meta Balls, Blob Cursor, Star Border.
- UI components: Animated List, Scroll Stack, Bubble Menu, Magic Bento, Circular Gallery, Reflective Card, Card Nav, Stack, Fluid Glass, Pill Nav, Tilted Card, Masonry, Glass Surface, Dome Gallery, Chroma Grid, Folder, Staggered Menu, Model Viewer, Lanyard, Profile Card, Dock, Gooey Nav, Pixel Card, Carousel, Spotlight Card, Border Glow, Flying Posters, Card Swap, Glass Icons, Decay Card, Flowing Menu, Elastic Slider, Counter, Infinite Menu, Stepper, Bounce Cards.
- Backgrounds: Ferrofluid, Lightfall, Liquid Ether, Prism, Dark Veil, Light Pillar, Silk, Floating Lines, Side Rays, Light Rays, Pixel Blast, Color Bends, Evil Eye, Line Waves, Radar, Soft Aurora, Aurora, Plasma, Plasma Wave, Particles, Gradient Blinds, Grainient, Grid Scan, Beams, Pixel Snow, Lightning, Prismatic Burst, Galaxy, Dither, Faulty Terminal, Ripple Grid, Dot Field, Dot Grid, Threads, Hyperspeed, Iridescence, Waves, Grid Distortion, Ballpit, Orb, Letter Glitch, Grid Motion, Shape Grid, Liquid Chrome, Balatro.

Best demo matches:

- Cursor/browser-use: Splash Cursor, Target Cursor, Ghost Cursor, Blob Cursor, Click Spark.
- Animated text hero: Split Text, Blur Text, Text Type, Decrypted Text, Glitch Text, Scroll Reveal.
- Memorable visual field: Hyperspeed, Galaxy, Aurora, Liquid Chrome, Dot Grid, Faulty Terminal.
- Interactive card wall: Magic Bento, Chroma Grid, Scroll Stack, Card Swap, Tilted Card.

## remocn

Installation pattern:

```bash
pnpm dlx shadcn@latest add @remocn/<component>
```

remocn is especially useful for Remotion scenes and cinematic UI. Components expose props and Remotion usage examples.

Audited groups:

- Typography: Blur Reveal, Staggered Fade Up, Masked Slide Reveal, Tracking In, Inline Highlight, Marker Highlight, Shimmer Sweep, Typewriter, Slot Machine Roll, Infinite Marquee, Perspective Marquee, Matrix Decode, RGB Glitch Text.
- Core primitives: Spring Pop In, Success Confetti, Bounding Box Selector, Toast Notification.
- Environment and lighting: Mesh Gradient Background, Dynamic Grid, Spotlight Card.
- UI blocks: Glass Code Block, Terminal Simulator, Code Accordion, Code Diff Wipe, Tool Menu Slide In, Animated Line Chart, Animated Bar Chart, Drag And Drop Flow, Data Flow Pipes, Progress Steps.
- Transitions: Zoom Through Transition, Device Mockup Zoom, Image Expand To Fullscreen, Directional Wipe, Spatial Push, Frosted Glass Wipe, Grid Pixelate Wipe, Chromatic Aberration Wipe, Kinetic Type Mask.
- Social: GitHub Stars.
- Compositions: Hero Device Assemble, Ecosystem Constellation, Infinite Bento Pan, Browser Flow, AI Generation Canvas, Live Code Compilation, Terminal To Browser Deploy, Dashboard Populate, Pricing Tier Focus.
- UI primitives: Accordion, Alert Dialog, Blur In, Button, Checkbox, Combobox, Command Menu, Context Menu, Cursor, Dialog, Drawer, Dropdown Menu, Input, Popover, Progress, Radio, Resizable, Select, Sheet, Skeleton, Slider, Spinner, Stepper, Switch, Tabs, Toast, Toggle Group, Tooltip.
- UI blocks: Checkout Flow, Settings Toggle Flow, Signup Flow.

Best demo matches:

- Video-ready agent demo: Browser Flow, Terminal To Browser Deploy, AI Generation Canvas.
- Product launch motion: Hero Device Assemble, Infinite Bento Pan, Pricing Tier Focus.
- Developer proof: Live Code Compilation, Code Diff Wipe, Terminal Simulator, Glass Code Block.
- Timed scene transitions: Device Mockup Zoom, Zoom Through Transition, Image Expand To Fullscreen, Directional Wipe.
