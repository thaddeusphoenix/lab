# AI Product Requirements Document: Camp Planner

> A purpose-built planning tool that helps working parents collect, organize, and track summer programs per child — covering the full arc from discovery to deadline to confirmed enrollment.

**Status:** Draft
**Owner:** Wintermute (Product Manager)
**Last updated:** 2026-03-17
**Related Feature Briefs:** [Core Planning Loop](./feature-brief-core-planning.md)

---

## 1. Strategic Context

### Problem Statement

_Working parents manage summer program enrollment across multiple programs, deadlines, and children using general-purpose tools (Notes, Google Calendar, spreadsheets) that store dates but provide no preparation context. The result: missed spots, surprise cancellation fees, and gap weeks._

**User:** Working parents of school-age children managing summer programs for one or more kids.
**Pain:** The job starts with collection — finding programs and getting them into one place, organized by child. Today that means manually re-entering data from program websites. Then comes the deadline pressure: parents know registration opens March 15, but lack the registration link, correct session, and payment method ready when the window opens. The spot is gone in minutes. Finally, parents have no clear view of whether their summer is covered week by week.
**Evidence:**
- Validated by research session with Sari Gelzer (2026-02-26). Sari sets alarms and prepares specifically to "be ready to click the button." She uses Notes and Google Calendar. She explicitly said she wished the app could "click the button for her."
- Validated by prototype feedback session (2026-03-17, spouse of founder, 40s, mother of 2: 3-year-old girl and 9-year-old boy). First instinct on opening the app was to build a list of classes found and organize them by child. Add-program form felt too laborious — she expected to paste a link or copy program text for auto-fill. Requested calendar view per child to see gaps.

**Current workaround:** Google Sheets, Calendar apps, Notes. Parents rebuild their tracking system every year from scratch.

### User Personas

| Persona | Behaviors | Motivations | Job to be Done |
|---|---|---|---|
| Morgan (Logistics Parent) | Plans 8–10 weeks in advance; overbookings as a hedge strategy; tracks cancellation windows | Full summer coverage, zero surprises | See which weeks are covered per child and get a warning before cancellation windows close |
| Jamie (Independent Planner) | Researches programs extensively; registers solo without a partner's input | Self-sufficiency, acting on her own schedule | Have one place to track all research without needing to re-find things at registration time |
| Priya (Social Coordinator) | Coordinates with other parents; sends and receives program recommendations | Shared information, reducing duplicate research | Know what other parents are doing for their kids; share a program in one action |

### Strategic Objectives

| Objective | Target | Timeframe |
|---|---|---|
| Onboarding success | >80% of test users complete initial setup unassisted | Usability testing before launch |
| Deadline capture rate | 0 registration or cancellation deadlines missed in a planned season | First full summer of use |
| Year-over-year retention | Parents return to plan the following summer | 12 months post-first use |

---

## 2. Data Specifications

### AI Extraction Input

When a parent pastes a URL or raw text from a program website, the app sends that content to a language model to extract structured program data.

| Field | Source | Notes |
|---|---|---|
| Program name | Extracted | Required |
| Start date / End date | Extracted | Required |
| Sign-up deadline | Extracted | Required |
| Refund / cancellation deadline | Extracted | Required |
| Program fee | Extracted | Optional |
| Drop-off location | Extracted | Optional |
| Pick-up location | Extracted | Optional |
| Registration URL | Extracted | Optional — critical for prep card |
| Tax benefit info | Extracted | Optional — research artifact; surface if found (e.g., FSA eligibility) |

All extracted values are presented to the parent for confirmation before saving. No data is auto-committed without review.

### Local Storage

All program data is stored in browser localStorage / IndexedDB. No data leaves the device in v1 except extraction requests (URL or pasted text sent to AI extraction endpoint).

---

## 3. Reasoning Architecture

### AI Extraction

**Task:** Given a URL or pasted text from a program registration page, extract structured fields and return them as JSON for parent review.

**Model:** Claude (claude-sonnet-4-6 or equivalent capable model)
**Trigger:** Parent taps "Add from link" or "Paste program info" — content is sent immediately
**Output:** Structured JSON matching the field schema in Section 2; confidence is implicit (missing fields return null, not guesses)
**Failure behavior:** If extraction returns no usable fields, fall back to the manual entry form with a toast: "Couldn't read that page — fill in what you know."

**Prompt design principles:**
- Extract only what is explicitly stated; never infer or estimate dates
- Return null for missing fields rather than hallucinating values
- Prioritize registration/sign-up deadline accuracy — this is the highest-stakes field

### Rule-Based Logic (no model required)

- **Coverage calculation:** Week-by-week coverage is derived from program start/end dates per child
- **Conflict detection:** Overlapping date ranges for the same child surface as a conflict flag
- **Deadline proximity:** Notification triggers and prep card activation are time-based rules (1 week / 1 day / 1 hour)
- **Budget calculation:** Committed + potential spend vs. budget ceiling

---

## 4. Functional Requirements

### User Stories

> **Note:** These are product-level stories for alignment. Detailed build-loop acceptance scenarios live in a separate `[feature]-scenarios.md` file.

| # | Given | When | Then |
|---|---|---|---|
| 1 | A parent opens the app for the first time | They see the home screen | The view is organized by child; each child has their own program list; prompt to add first program |
| 2 | A parent has found a program online | They paste the URL or copy-paste program text | The app extracts name, dates, deadlines, fee, locations, and tax info; parent confirms or edits before saving |
| 3 | A parent adds a program manually | They fill in the required fields | Program saves under the selected child with all entered data |
| 4 | A parent wants a time view for one child | They open the calendar view for that child | A week-by-week calendar shows all programs for that child; gap weeks are highlighted; conflict weeks are flagged |
| 5 | A registration deadline is within 14 days | The parent opens the Decisions view | The program displays as an Enrollment Prep Card: registration link, fee, session, and a three-item readiness checklist |
| 6 | A cancellation deadline is within 14 days | The parent views the Decisions list | A cancellation warning card surfaces the deadline, the fee at stake, and a direct link to the cancellation page |
| 7 | A parent has set a summer budget | They look at the budget tracker | They see committed spend, potential spend, and remaining budget |
| 8 | A deadline is approaching | The system triggers a notification | Parent receives a push notification at 1 week, 1 day, and 1 hour before the deadline |

### Program Data Model

Required fields (must be present to save):
- Program name
- Child (which kid this is for)
- Start date, End date
- Sign-up deadline

Optional fields:
- Refund / cancellation deadline
- Program fee
- Drop-off location
- Pick-up location
- Registration URL
- Status (Considering / Registered / Cancelled)
- Notes
- Tax benefit info _(research artifact — visible in form to observe if users notice or ask)_

### Interaction States

| State | Trigger | User-visible behavior |
|---|---|---|
| Empty state | No programs added | Per-child list shows empty; prompt to add first program |
| Add from link | Parent taps "Add from link" | URL input → extraction → review form pre-filled; parent confirms |
| Add from text | Parent taps "Paste program info" | Text paste area → extraction → review form pre-filled; parent confirms |
| Manual add | Extraction fails or parent prefers | Standard form; required fields marked |
| Calendar view | Parent selects a child's calendar | Week grid for that child; gaps highlighted; conflicts flagged |
| Prep card (active) | Deadline ≤14 days, status = Considering | Card shows link, fee, session, checklist |
| Gap alert | Calendar has empty weeks in summer horizon | Gap weeks highlighted visually; no push alert |
| Conflict flag | Two programs overlap for the same child | Overlap weeks flagged in calendar |
| Budget exceeded | Committed + potential spend > budget | Budget tracker shows overage |
| Notification | Deadline - 7 days, - 1 day, - 1 hour | Push notification with deadline name and action link |

### Out of Scope (v1)

- Program discovery or browse — parents add programs they already know about _(noted as future direction)_
- Direct registration or payment integration
- Multi-user or household accounts (v1 is single-user)
- Social sharing / "what other parents are doing" _(noted as future direction — Priya persona)_
- Confirmation email detection / auto-status update _(noted as future direction)_
- Multi-child combined calendar views (per-child toggle is in scope; side-by-side is not)
- Year-round activity management — summer only

---

## 5. Evaluation & Performance Standards

### AI Extraction Quality

| Metric | Target | Alert threshold |
|---|---|---|
| Sign-up deadline extraction accuracy | >90% correct on test set of real program pages | <80% → prompt revision required |
| Field coverage (at least 3 fields extracted) | >85% of URL submissions | <70% → extraction is not saving meaningful time |
| False date extraction rate | <5% (date returned when none exists on page) | >10% → hallucination risk, tighten prompt |

Evaluation method: periodic manual audit of 20 sampled extractions per sprint during build phase.

---

## 6. Non-Functional Requirements & Guardrails

### Latency Targets

| Operation | Target | Worst-case bound |
|---|---|---|
| AI extraction (URL or paste) | <4s | <8s |
| Coverage calendar render after program add/edit | <100ms | <300ms |
| App load from cold start | <1.5s on 4G | <3s |
| Push notification delivery | <60s from scheduled time | — |

### The Escape Hatch

Parents must never feel locked in. A CSV export of all programs (name, dates, fees, links, status, per child) is required before launch.

### Privacy & Guardrails

- **Program data is stored locally** (localStorage / IndexedDB). No user data is sent to a server in v1 except extraction requests.
- Extraction requests send only the URL or pasted text — no child names, no PII from the parent's profile.
- Push notifications require explicit permission, requested only after a parent has added their first program with a deadline.
- No demographic data collected.
- AI extraction: model must not infer or fill in dates that are not present. Missing = null, not a guess.

---

## 7. Lifecycle & Maintenance

### Degradation Thresholds

- **Extraction quality:** if sign-up deadline accuracy drops below 80% on audit, pause AI extraction and default to manual form
- **localStorage limits:** possible on devices with many programs across multiple children — monitor and surface a warning if approaching limits
- **Push notification API changes:** browser API varies; test across Safari iOS (primary surface) and Chrome
- **Seasonal usage pattern:** high demand Jan–May (planning season), low Jun–Aug (summer), repeat

### Monitoring Cadence

| Signal | Cadence | Alert threshold |
|---|---|---|
| Extraction field coverage rate | Weekly during build | <70% → extraction not useful |
| Enrollment Prep Card tap-through rate | Post-launch weekly | <20% → card visible but not trusted |
| Session length on first use | First month post-launch | <3 min → onboarding friction too high |
| Registration URL completion rate | First month | <40% of programs have URL → core prep card feature at risk |
| Tax benefit field interaction rate | First month | Track only — research signal |

### Ownership Model

| Phase | Owner |
|---|---|
| Building | Tech Lead |
| Deploying | Delivery Manager |
| Monitoring | Product Manager + Customer Success |
| Retiring | Product Manager |

---

## Biggest Unknowns

1. **Does paste-to-extract actually eliminate friction?** The add-program form felt too laborious in prototype testing. AI extraction is the proposed fix — but if extraction accuracy is low or the review step feels like the same work, we've solved nothing.
2. **Will parents add the registration URL?** The Enrollment Prep Card loses its core value if parents skip this field. Extraction may solve this passively — if the URL is on the page, we capture it automatically.
3. **Does the calendar view per child actually surface gaps clearly enough?** The coverage grid concept is validated in intent; the visual design needs to make gap weeks immediately obvious without explanation.
4. **What does "tax benefit info" mean to parents?** The field is intentionally vague in v1 — it is a research instrument. We want to observe whether parents notice it, ask about it, or ignore it before defining its scope.
5. **Is social/sharing a growth lever or a nice-to-have?** Two separate users have signaled it (Priya persona + prototype session). The question is whether it drives acquisition or is just a feature request.

---

## Future Directions (not in scope for v1)

These items surfaced in research and are tracked here to inform roadmap decisions — not to be built now.

- **Program discovery / browse** — a curated or searchable index of local programs
- **Social layer** — see what other parents are enrolling their kids in; share a program in one tap
- **Confirmation email detection** — automatically update program status when a booking confirmation lands in the parent's inbox
- **Tax benefit detail** — FSA eligibility flags, dependent care deduction guidance
