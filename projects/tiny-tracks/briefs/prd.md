# AI Product Requirements Document: Tiny Tracks

> A browser-based 3D simulator for designing and running model train layouts — the satisfaction of the hobby without the physical cost, space, or setup.

**Status:** Draft
**Owner:** Wintermute (Product Manager)
**Last updated:** 2026-03-03
**Related Feature Briefs:** [Building Experience Validation](./building-experience-validation.md)

---

## 1. Strategic Context

### Problem Statement

_Model railroading — the act of designing, building, and running a miniature layout — has high barriers to entry: space, cost, and months of patient construction. Many people who want to experience the craft never get to._

**User:** People drawn to the model railroading hobby — the creative satisfaction of building a miniature landscape and watching a train run through it — who cannot or will not invest in the physical version.
**Pain:** The experience (designing a layout, making creative decisions, watching a train complete the loop you designed) is inaccessible unless you have the space, budget, and patience. There is no low-cost version that replicates the *building* experience, as opposed to a driving simulator.
**Evidence:** Working Cardboard prototype demonstrates the core mechanic — grid-based layout builder with terrain, track, scenery, and animated locomotive — is viable in a single HTML file. The interaction loop works.
**Current workaround:** Model railroad driving simulators exist (Trainz, MSTS) but simulate operating trains, not constructing layouts. Nothing captures the builder's experience in a browser.

### User Personas

| Persona | Behaviors | Motivations | Job to be Done |
|---|---|---|---|
| The aspiring builder | Reads about the hobby; watches YouTube videos of layouts; never started | Creative satisfaction, low stakes | Experience building without committing to space or money |
| The lapsed hobbyist | Had a layout as a child or young adult; no longer has the space | Nostalgia; the same satisfaction in a smaller form | Return to the feeling of building without the physical commitment |
| The casual gamer | Plays building/simulation games (Cities Skylines, Minecraft); drawn to tactile building mechanics | Creative control, visible results | Build something in a session, see it work, share it |

### Strategic Objectives

| Objective | Target | Timeframe |
|---|---|---|
| Session engagement | Average session length >10 minutes in first cohort | First 30 days post-launch |
| Return rate | >30% of first-time users return within 7 days | First 30 days |
| Core loop completion | Users who lay a connected loop run the train on it | Observed in usability testing |
| Qualitative | Users describe the building experience as satisfying, not frustrating | Usability interviews |

---

## 2. Data Specifications

> _Not applicable. Tiny Tracks performs no data retrieval or model inference. All logic is client-side simulation: geometric track pathfinding, WebGL rendering, and localStorage persistence._

---

## 3. Reasoning Architecture

> _Not applicable. All "intelligence" is deterministic: the locomotive follows connected track segments using a graph traversal algorithm. There is no probabilistic model or AI reasoning._

---

## 4. Functional Requirements

### User Stories

> **Note:** These are product-level stories for alignment. Detailed build-loop acceptance scenarios live in a separate `[feature]-scenarios.md` file.

| # | Given | When | Then |
|---|---|---|---|
| 1 | The user opens the simulator | — | A blank 20×20 grid terrain is visible with the building toolbar and camera controls |
| 2 | The user selects a track piece from the toolbar | They hover over the grid | A ghost preview of the track piece shows at the cursor position, rotatable with R |
| 3 | The user has laid a connected loop of track | They press the Run button | The locomotive appears and begins pathfinding along the track; it completes laps continuously |
| 4 | The user wants to change the terrain | They select a terrain paint tool and click a grid cell | The cell updates to the selected terrain type (grass, dirt, ballast, water) |
| 5 | The user places scenery | They select a scenery object and click a cell | The object appears on the grid in 3D |
| 6 | The user wants to save their layout | They press Save | The layout is serialized to localStorage and survives a page refresh |
| 7 | The user wants to share or revisit | They copy a URL or bookmark | The layout loads from localStorage on return |

### Interaction States

| State | Trigger | User-visible behavior |
|---|---|---|
| Empty grid | Page load | Blank terrain grid; toolbar visible; camera at default isometric angle |
| Placing track | Track piece selected | Ghost preview follows cursor; click to place; R rotates piece |
| Invalid placement | Track placed on incompatible cell | Piece dims or snaps to nearest valid position; no hard error |
| Train running | Run pressed with valid connected loop | Locomotive animates along track; speed is constant |
| No valid loop | Run pressed with no connected loop | Visual indicator on disconnected track segments; train does not run |
| Saved | Save action | Subtle confirmation; no modal; layout persists across refreshes |

### Out of Scope

- Multiplayer or shared layouts
- Train physics simulation (acceleration, derailment, grades)
- Backend, accounts, or server-side persistence
- Monetization
- Train driving / operating mode (building simulator only in v1)

---

## 5. Evaluation & Performance Standards

> _Not applicable. No probabilistic model outputs to score._

---

## 6. Non-Functional Requirements & Guardrails

### Latency Targets

| Operation | Target | Worst-case bound |
|---|---|---|
| Initial page load | <2s on broadband | <4s on 4G |
| Grid render and interaction | 60fps at 20×20 grid on mid-range hardware | 30fps minimum acceptable |
| Train pathfinding (loop detection) | <100ms | <300ms on large layouts |
| Save to localStorage | <50ms | <200ms |

### The Escape Hatch

No AI decision-making. The relevant "escape hatch" is undo/reset:
- **Undo** (Ctrl/Cmd+Z) must be available for any placement action.
- **Clear layout** must be available with a confirmation step — not a single accidental tap.
- **Export layout** as a JSON string must be available so users are never locked into the browser's localStorage.

### Privacy & Bias Boundaries

- **No PII is collected or transmitted.** The product is entirely client-side.
- Layout data is stored in localStorage — it is not sent to any server.
- No analytics, no tracking, no external calls in v1.

---

## 7. Lifecycle & Maintenance

### Degradation Thresholds

No model to degrade. Maintenance triggers:
- Three.js or WebGL API breaking changes in a major browser update
- localStorage API changes or storage limit reductions
- Performance regression on new mobile hardware profiles (rendering must stay above 30fps minimum)

### Monitoring Cadence

| Signal | Cadence | Alert threshold |
|---|---|---|
| Session length (analytics if added) | Monthly | <5 min average → core building loop is frustrating |
| Return rate (analytics if added) | Monthly | <15% 7-day return → no save/load is killing retention |
| Browser compatibility issues | Per release | Any reported crash on a >5% market share browser |

### Ownership Model

| Phase | Owner |
|---|---|
| Building | Tech Lead |
| Deploying | Delivery Manager (GitHub Pages) |
| Monitoring | Product Manager |
| Retiring | Product Manager |

---

## Biggest Unknowns

1. **Does the "building simulator" framing resonate, or do users want to drive the train?** The core bet is that the satisfaction is in constructing the layout. If users primarily want to control the locomotive, the product direction shifts significantly.
2. **How much visual fidelity is needed before it feels compelling enough to share?** There is a threshold of visual quality below which the experience feels like a toy rather than a simulation. We do not yet know where that threshold is.
3. **Is localStorage enough for retention, or does the lack of save/load kill return visits?** Without save/load, every session starts blank. This is the most likely cause of poor retention and should be validated quickly.
