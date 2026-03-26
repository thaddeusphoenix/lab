# Product Requirements Document: CivilGrid Layer Picker

> A geography-aware, role-configured layer management panel that lets infrastructure developers and engineering firms control which GIS datasets appear on the map during site due diligence.

**Status:** Draft
**Owner:** Nathan Stankowski
**Last updated:** 2026-03-23
**Related Feature Briefs:** _(to be added as build loop briefs are created)_

---

## 1. Strategic Context

### Why We're Building This

CivilGrid started as a data clearinghouse. Early customers were 1–2 power users per organization who would load all layers, verify that relevant data existed, then export everything to their CAD solution and filter there. Showing everything was sufficient for that model — the value was simply confirming the data was there.

To grow, we need to move beyond that model. We want to sell more licenses, which requires more use cases that deliver value to more users. That means enabling workflows *on top of the data* inside the product — not just piping it out to CAD. To do that, users need the ability to display only the data relevant to their current workflow.

The layer picker is the first move toward in-product value. It serves three converging purposes:

1. **Targeted downloads** — users pre-filter to a smaller, more relevant dataset before exporting to CAD, rather than downloading everything
2. **In-product visual analysis** — users filter to the layers they need for eye-level review: early planning and site discovery, or mid/late-stage Q&A and constraint checking
3. **In-product reporting and analysis** — users configure a focused data context for reporting, analysis, or other in-product workflows

A fourth use case is on the horizon: **Presets as Context Packages** — saved layer configurations that define the data context for AI-assisted processes and structured reporting. This is out of scope for MVP but the data model should not foreclose it.

The strategic pivot: CivilGrid moves from a place users come to *verify data exists* to a place users come to *do work with data*.

---

### Problem Statement

**User:** Infrastructure developers and civil/environmental engineers using CivilGrid for site due diligence
**Pain:** With 150+ GIS datasets available, the current map experience surfaces irrelevant layers (e.g., NY State Parks for a California project), doesn't remember a user's configuration between sessions, and provides no role-based starting point — forcing users to manually configure the map on every project before any real analysis begins.
**Evidence:** _(to be validated)_ Support tickets related to layer discoverability; customer interview signals around repetitive setup; low layer engagement breadth suggesting users don't explore beyond familiar defaults.
**Current workaround:** Users manually toggle layers at the start of each session, often from memory. Layers relevant to their workflow may be missed entirely because they're buried in a long undifferentiated list.

### User Personas

| Persona | Behaviors | Motivations | Job to be Done |
|---|---|---|---|
| **Infrastructure Developer** | Opens CivilGrid at site selection or early pre-dev stage. Evaluates multiple sites in parallel. Cares about big-picture risk: land rights, transmission access, geotechnical hazards. | Reduce budget and schedule surprises before committing capital to a site. | Quickly assess whether a site has deal-breakers — utility conflicts, seismic risk, parcel encumbrances — before spending on detailed engineering. |
| **Civil / Environmental Engineer** | Opens CivilGrid mid-project or during permitting. Works deeply on a single site. Cares about precise utility routing, seismic specifics, and regulatory boundaries. | Produce accurate deliverables and avoid field surprises. | Find and document specific underground and regulatory data that informs design and permitting. |
| **Environmental Consultant** | Focused on risk characterization — geotechnical studies, wetlands, fault lines, park boundaries. | Identify environmental constraints that affect project viability or permitting timeline. | Characterize site-specific environmental and geotechnical risks. |

### Strategic Objectives

**Business goal:** Sell more licenses by expanding the number of use cases that deliver value to more user types — moving CivilGrid beyond single-power-user-per-org adoption.

| Objective | Target | Timeframe |
|---|---|---|
| Reduce time-to-first-meaningful-layer-configuration for new users | Reduce by >40% vs. pre-launch baseline | 90 days post-GA |
| Increase layer engagement depth per session | >20% increase in avg. distinct layers interacted with per session | 90 days post-GA |
| Establish the layer management UI foundation for proprietary layer upload upsell | Layer picker data model supports custom layers without re-architecture | At MVP launch |
| Improve NRR among active layer picker users | Active users show >5pp NRR improvement vs. non-users | 12 months post-GA |

---

## 2. Data Specifications

> _Skipped — this product has no AI retrieval pipeline, training data, or model-serving infrastructure. The layer picker is a UI configuration layer over existing GIS data._

---

## 3. Reasoning Architecture

> _Skipped — this product has no agentic behavior or model decision logic. Geography filtering and role defaults are deterministic rule-based logic, not ML._

---

## 4. Functional Requirements

### User Stories

| # | Given | When | Then |
|---|---|---|---|
| 1 | A developer opens a project with a Phoenix, AZ location | They open the layer picker | They see only layers with Arizona coverage; NY State Parks and other state-specific layers are absent or clearly labeled "Not available in AZ" |
| 2 | A new user identifies as a Civil Engineer during onboarding | They open the layer picker on their first project | A curated default set is pre-enabled: Distribution Lines, Service Lines, Transmission Lines, Fault Lines, Parcels, Roads — their most likely due diligence stack |
| 3 | A user enables Transmission Lines, disables Roads, and enables Fault Lines | They close the project and return the next day | Their layer configuration is exactly as they left it |
| 4 | A layer (e.g., Parcels) exists in CivilGrid but is not yet loaded for Nevada | A Nevada project user opens the layer picker | Parcels appears in the panel with a "Coming Soon in NV" label and is non-interactive; user can click to signal interest |
| 5 | CivilGrid has not launched in Montana | A Montana project user opens the layer picker | A banner explains CivilGrid data is not yet available in this state; no layers are shown as interactive |
| 6 | A user types "fault" in the layer picker search bar | — | The panel filters to show Fault Lines and any other layers matching the query; categories collapse except those with matches |
| 7 | A user hovers over a layer name | — | A tooltip shows: dataset name, data source/provider, last updated date, and geographic coverage note |

### Interaction States

| State | Trigger | User-visible behavior |
|---|---|---|
| **Layer: Active** | User has toggled layer on | Layer visible on map; indicator in picker shows active state (colored icon or filled toggle) |
| **Layer: Available** | Layer has coverage in project geography; user has not enabled it | Shown in panel with off toggle; can be enabled |
| **Layer: Coming Soon** | Layer exists in CivilGrid catalog but not yet loaded for this state | Shown in panel, grayed out, with "Coming Soon in [State]" label; non-interactive; click logs interest signal |
| **Layer: Not in area** | CivilGrid has not launched in the project's state | Layer hidden entirely OR shown only in an "Unavailable in your area" collapsed section |
| **No data in state** | CivilGrid has not launched at all in the project's state | Panel shows informational banner: "CivilGrid data is not yet available in [State]." No interactive layers shown. |
| **Search active** | User has typed in search bar | Panel filters to matching layers only; non-matching categories collapse |
| **Loading** | Panel is fetching layer availability for project geography | Skeleton loader within panel; map remains interactive |

### Category Hierarchy (MVP)

The panel is organized hierarchically. Categories expand/collapse. Default state: top-level categories collapsed, user's role-default layers pre-enabled.

```
Electric
  Transmission Lines
  Distribution Lines
  Service Lines
  Vaults
Gas
  Transmission Lines
  Distribution Main Lines
  Service Lines
  Points
Water
  (subcategories)
Sewer
  (subcategories)
Land Rights
  Parcels
  Easements
Geotechnical
  Geotechnical Studies
  Seismic
    Fault Lines
    Landslide Areas
Transportation
  Roads
    National Highway Network
  State DOT
    State Highway Network
    Transportation District Boundaries
Boundaries
  Cities
  Counties
  State Parks (state-specific; shown only for project state)
  City Parks (city-specific; shown only for relevant city)
```

### Role-Based Default Layer Sets

| Role | Default Layers Enabled |
|---|---|
| **Infrastructure Developer** | Transmission Lines (Electric), Parcels, Fault Lines, Landslide Areas, National Highway Network, Counties |
| **Civil / Environmental Engineer** | Distribution Lines, Service Lines, Transmission Lines (Gas), Distribution Main Lines, Fault Lines, Parcels, State Highway Network |
| **Environmental Consultant** | Fault Lines, Landslide Areas, Geotechnical Studies, Parcels, Counties, State Parks (if in state) |

_Note: Role defaults are validated during beta and adjusted based on activation data before GA._

### Out of Scope (MVP)

- **Named presets / Context Packages** — save/load configurations across projects; longer-term, presets are the mechanism for defining data context for AI-assisted workflows and structured reporting. The MVP data model must not foreclose this.
- **Team / org-level shared presets**
- **Proprietary / custom layer upload**
- **Layer z-index / ordering controls**
- **Layer opacity sliders**
- **Data density previews** before enabling a layer
- **Layer comparison mode**
- **Automated layer recommendations** based on project type or past usage

---

## 5. Evaluation & Performance Standards

> _Skipped — this product has no probabilistic or model-scored outputs._

---

## 6. Non-Functional Requirements & Guardrails

### Latency Targets

| Operation | Target | Worst-case bound |
|---|---|---|
| Layer picker panel open (initial load) | <500ms | <1.5s |
| Layer toggle (map layer on/off) | <300ms to visual confirmation | <800ms |
| Layer state save (auto-save on change) | <200ms, non-blocking | <500ms |
| Search filter response | <100ms (client-side filtering) | — |

### Data Integrity

- Layer state must be saved server-side per project, not in localStorage — localStorage loss on browser clear would break the persistence value prop
- Layer coverage matrix (which layers are available in which states) must be versioned and maintainable by the data team without a code deploy
- "Coming Soon" interest clicks must be logged to a demand signal queue; this data feeds roadmap prioritization

### Privacy & Access

- Layer configuration is per-user, per-project — not shared across org members (until team preset feature ships)
- No PII is involved in layer state data
- Custom/proprietary layer metadata (future): must be scoped to the uploading org only; never visible to other orgs

---

## 7. Lifecycle & Maintenance

### Layer Coverage Matrix

The layer coverage matrix (which layers are live in which states) is owned by the Data team and must be updated as new states are loaded. The UI reads from this matrix at project open time — stale matrix = incorrect panel states. Freshness SLA: updated within 24 hours of any new state going live.

### Monitoring Cadence

| Feature / Signal | Cadence | Alert threshold |
|---|---|---|
| Layer state save error rate | Real-time | >1% of save operations |
| Panel load time | Real-time | P95 >1.5s |
| Geography filtering accuracy (QA sample) | Weekly for first 30 days post-GA | Any miscategorized layers |
| "Coming Soon" interest click volume | Weekly | Used for roadmap input, not alerts |

### Ownership Model

| Phase | Owner |
|---|---|
| Building (MVP) | Engineering + PM |
| Beta rollout | Customer Success + PM |
| GA and monitoring | Engineering (ops) + PM |
| Layer coverage matrix maintenance | Data team |
| Retiring / deprecating MVP → Iteration 1 | PM + Engineering |

---

## Biggest Unknowns

1. **Are role-based defaults actually right?** We are assuming developer/engineer/consultant maps cleanly to distinct layer sets. Customer interviews and beta data will validate or invalidate this — wrong defaults are worse than no defaults (they teach users to ignore the feature).
2. **What is the current baseline for layer engagement depth?** Without pre-launch analytics, we cannot set a meaningful improvement target or know if the feature moved the needle. Instrument before GA.
3. **Does per-project persistence require a meaningful data model change?** If layer state is currently session-only with no project-scoped storage, this is an infrastructure decision that could affect timeline. Needs eng scoping early.
