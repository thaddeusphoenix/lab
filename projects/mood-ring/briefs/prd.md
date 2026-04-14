# AI Product Requirements Document: Mood Ring

> A generative color object that reflects where you are in four human cycles — rendered as a wearable artifact for your profile or phone.

**Status:** Draft
**Owner:** Wintermute (Product Manager)
**Last updated:** 2026-03-03
**Related Feature Briefs:** [In-Prototype Feedback Loop](./feedback-loop.md)

---

## 1. Strategic Context

### Problem Statement

_The digital artifacts people carry on their phones and profiles are almost entirely functional. None of them are personal, generative, beautiful, and derived from something objectively true about the person holding them._

**User:** Design-conscious individuals who want a personal digital object — not a productivity tool.
**Pain:** There is nothing on your phone that is quietly yours in the way a piece of jewelry is yours. Status indicators, avatars, and wallpapers are chosen, not derived. They do not update with you.
**Evidence:** The cultural object already exists and is understood — the mood ring. People have intuited for fifty years that color can carry personal meaning. The market for generative and personalized digital art is established.
**Current workaround:** None. People use stock wallpapers, generic avatars, or leave profile status fields blank.

### User Personas

| Persona | Behaviors | Motivations | Job to be Done |
|---|---|---|---|
| The aesthete | Curates their digital identity carefully; changes wallpapers seasonally | Personal expression, quiet distinction | Find a profile artifact that feels uniquely theirs without looking "designed" |
| The cycle-aware person | Follows moon phases, pays attention to seasons; may use apps like Co-Star or Clue | Connection to natural rhythms; mindfulness | See a visual representation of where they are in time right now |
| The skeptic | Would never self-report a mood; distrusts wellness apps | Authenticity, privacy | Engage with an object derived from objective data, not self-disclosure |

### Strategic Objectives

| Objective | Target | Timeframe |
|---|---|---|
| Visual appeal | At least 3 of 5 people shown it say they'd use it as a wallpaper | First prototype test |
| Concept legibility | Users can describe what each color represents after brief onboarding | Usability test |
| Personal resonance | Users describe the object as feeling "theirs" — not arbitrary | Qualitative interviews |

---

## 2. Data Specifications

> _Not applicable. Mood Ring performs no retrieval and requires no training data. All computation is deterministic math from three user inputs: age, current time, and location._

---

## 3. Reasoning Architecture

> _Not applicable. The color derivation is a pure function — inputs map to outputs through defined astronomical and cyclical formulas. There is no probabilistic model or agentic behavior._

---

## 4. Functional Requirements

### User Stories

> **Note:** These are product-level stories for alignment. Detailed build-loop acceptance scenarios live in a separate `[feature]-scenarios.md` file.

| # | Given | When | Then |
|---|---|---|---|
| 1 | A user opens the prototype | They enter their age and allow location access | The ring renders immediately with a unique color composition derived from their four cycles |
| 2 | The ring is visible | The user holds the ring circle for ~3 seconds | A poetic reading of the four cycles fades in, line by line |
| 3 | The reading has fully settled | The user sees the feedback prompt | They tap yes / somewhat / no; optionally type a sentence; the submission registers silently |
| 4 | The user taps "read again" | — | All state resets; the ring is visible again; cycle values update to current moment |
| 5 | The user wants the ring as a wallpaper | They long-press the rendered image | The image is saveable as a static PNG at wallpaper resolution |

### Interaction States

| State | Trigger | User-visible behavior |
|---|---|---|
| Input | Page load | Age input field visible; location permission prompt |
| Rendering | Age entered + location granted | Ring draws with circular-mean blended color; no delay visible |
| Idle | Ring rendered | Ring is static; "hold to reveal" affordance visible |
| Reveal | Hold gesture (~3s) | Reading lines fade in sequentially |
| Feedback | Reading complete | `yes · somewhat · no` prompt appears at bottom; subdued, non-interruptive |
| Submitted | Choice tapped + Enter pressed | "noted" appears; prompt fades; ring remains visible |

### Out of Scope

- No mood input from the user — color is computed, never self-reported
- No social features — no feeds, follows, or sharing flows (saving to camera roll uses native OS affordance)
- No animation or motion — the ring is a still image that updates per session, not a live animation
- No backend or accounts — all computation is client-side; nothing is stored or transmitted beyond the Google Forms feedback submission
- No additional cycles — four cycles, defined. No v1 customization.

---

## 5. Evaluation & Performance Standards

> _Not applicable. Mood Ring produces deterministic visual output from mathematical inputs. There is no probabilistic model to score._

---

## 6. Non-Functional Requirements & Guardrails

### Latency Targets

| Operation | Target | Worst-case bound |
|---|---|---|
| Ring render after inputs confirmed | <200ms | <500ms on low-end mobile |
| Reading reveal (per line) | Perceptible fade (~300ms each) | No hard bound — this is deliberate pacing |
| Feedback submission | Fire-and-forget; user sees no latency | Timeout silently if Forms POST fails |

### The Escape Hatch

No AI decision-making exists in this product, so no AI override is needed. If location permission is denied, the product must degrade gracefully: prompt the user to enter a timezone or city manually, so the circadian and seasonal cycles can still compute.

### Privacy & Bias Boundaries

- **No PII is stored or transmitted.** Age and location are used only to compute the current cycle position in the browser; neither is sent to a server.
- The feedback submission (yes/somewhat/no + optional free text) is anonymous — no user identifier is attached.
- The Google Forms data sink is the only external call; it receives only the pipe-delimited payload: `response | color_label | rgb_value | free_text`.

---

## 7. Lifecycle & Maintenance

### Degradation Thresholds

No model to degrade. Maintenance is triggered by:
- Browser API deprecation (geolocation, Canvas, Web Crypto)
- Google Forms breaking the no-CORS submission path
- A significant mismatch between the color framework and user feedback patterns (e.g., systematic "no" responses suggesting the color derivation needs recalibration)

### Monitoring Cadence

| Signal | Cadence | Alert threshold |
|---|---|---|
| Feedback submission rate | Weekly (manual Sheets review) | <10% of sessions submitting → prompt is broken or misplaced |
| "yes" vs. "no" distribution | Weekly | >60% "no" sustained over 20+ responses → core premise failing |
| Open text themes | Weekly | Patterns reviewed manually to surface concept confusion or aesthetic concerns |

### Ownership Model

| Phase | Owner |
|---|---|
| Building | Tech Lead |
| Deploying | Delivery Manager (GitHub Pages) |
| Monitoring | Product Manager (feedback analysis) |
| Retiring | Product Manager |

---

## Biggest Unknowns

1. **Does the concept need to be explained, or can the visual carry it?** If every user needs a paragraph of context to appreciate the object, the art isn't working.
2. **What rendering style makes it feel like jewelry rather than a data visualization?** Unified blend, stripes, and fractal blending produce very different aesthetics — this needs prototypes, not debate.
3. **Does the life-arc cycle feel meaningful or morbid?** Including a color for "how far through your life you are" is either quietly profound or quietly unsettling. The tone question may be the thing that makes or breaks the product.
