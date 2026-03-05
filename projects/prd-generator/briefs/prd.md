# AI Product Requirements Document: PRD Generator

> A client-side HTML tool that transforms raw inputs — notes, existing briefs, research transcripts — into a structured PRD draft, surfaces gaps, and exports clean markdown.

**Status:** Active
**Owner:** Wintermute (Product Manager)
**Last updated:** 2026-03-03
**Related Feature Briefs:** [PRD Generator Core](./prd-generator-core.md)

---

## 1. Strategic Context

### Problem Statement

_Writing a PRD from scattered discovery materials is slow and produces inconsistent quality. The PM must manually translate heterogeneous inputs — brain dumps, research notes, existing briefs — into a structured document that follows the 7-section format. The quality of the result depends entirely on how well the PM holds the template in mind while writing._

**User:** Wintermute (Product Manager) — the person who runs discovery and creates PRDs before any feature enters the build loop.
**Pain:** PRD drafting from raw inputs takes 60–90 minutes and produces uneven quality. AI-specific sections are often skipped when they shouldn't be, or included with generic filler when they should be skipped. Gap detection is manual — the PM must notice what's missing.
**Evidence:** Every PRD in the lab has been written from scratch with no tooling assistance. The pattern is consistent: raw notes → open document → manually work through 7 sections → re-read → patch gaps. The template exists but doesn't accelerate the work.
**Current workaround:** PM opens the PRD template, reads raw notes alongside it, and writes sections manually. Second pass for gap detection.

### User Personas

| Persona | Behaviors | Motivations | Job to be Done |
|---|---|---|---|
| Wintermute (PM) | Runs discovery, holds the template in mind, writes PRDs before anything enters build | Move fast without sacrificing document quality | Turn a pile of notes into a structured, ready-to-align PRD in under 10 minutes |

### Strategic Objectives

| Objective | Target | Timeframe |
|---|---|---|
| PRD drafting time | Under 10 minutes from paste to downloadable draft | At launch |
| Gap coverage | All empty or thin critical sections surface a targeted follow-up question | At launch |
| Process demonstration | Exercise every layer of the lab's development process end-to-end | This build |

---

## 2. Data Specifications

### Data Ingredient List

| Data Source | Type | Volume / Window | Owner |
|---|---|---|---|
| User-pasted raw input | Unstructured text — notes, existing brief, research transcript, brain dump | Up to ~8,000 tokens per session | User (PM) |
| PRD template structure | Reference schema — 7-section format with field descriptions | Static, embedded in prompt | PM / repo |

### Quality Thresholds

| Metric | Threshold | Consequence if Unmet |
|---|---|---|
| **Input completeness** | No minimum — tool must handle sparse input gracefully | Sparse input triggers gap questions rather than silent filler |
| **Section presence** | All 7 headers must appear in every output | Sections 2, 3, 5 display a skip note when AI components are absent |
| **Gap question relevance** | Questions must target missing content specifically, not ask generic "tell me more" prompts | Irrelevant questions waste the user's time and undermine trust |

### Data Supply Chain

- **Input path:** User pastes raw text into a textarea → single Claude API call → structured draft returned as markdown
- **Gap path:** System scores each section (empty / partial / complete) → generates targeted follow-up questions for empty/partial critical sections → user answers inline → second Claude API call incorporates answers
- **No persistence:** Nothing is stored server-side. API key in sessionStorage only. Input text and output draft live in the browser session.
- **Failure mode:** If the Claude API call fails, surface a plain error message with the raw error. Never silently produce an empty or partial draft.

---

## 3. Reasoning Architecture

### Decision Logic

```
User pastes raw input
        ↓
Stage 1: Synthesize input → draft all 7 PRD sections
        ↓
Stage 2: Score each section (empty / partial / complete)
        ↓
Stage 3: For empty or partial critical sections → generate targeted gap questions
        ↓
[User answers gap questions inline]
        ↓
Stage 4: Incorporate answers into the relevant sections → finalized PRD
        ↓
Export as downloadable markdown
```

**AI skip detection:** If the input contains no reference to models, AI components, retrieval pipelines, training data, or agentic behavior, sections 2, 3, and 5 must display:
> _Not applicable. [Short reason derived from input]._

### Authority Boundaries

| Capability | Disposition |
|---|---|
| Synthesize input into PRD section drafts | Must execute autonomously |
| Detect presence or absence of AI/model components | Must execute autonomously |
| Score section completeness (empty / partial / complete) | Must execute autonomously |
| Generate follow-up questions for empty/partial sections | Must execute autonomously |
| Incorporate gap answers into the correct sections | Must execute autonomously |
| Invent personas not mentioned in the input | Prohibited — must ask instead |
| Invent metrics or targets not mentioned in the input | Prohibited — must ask instead |
| Invent technical constraints not mentioned in the input | Prohibited — must ask instead |
| Produce filler content in sections with no source material | Prohibited — mark as partial and generate a gap question |

### Memory & State

- **Session scope:** One PRD per session. No history across sessions.
- **State:** Three states — draft (after Stage 1–3), gap Q&A (while user answers), finalized (after Stage 4).
- **Persistence:** None. Closing the tab loses all state. Intentional — this is a drafting tool, not a document store.

---

## 4. Functional Requirements

### User Stories

> **Note:** These are product-level stories for alignment. Detailed build-loop acceptance scenarios live in a separate `prd-generator-core-scenarios.md` file.

| # | Given | When | Then |
|---|---|---|---|
| 1 | The user has raw notes about a new product | They paste the notes into the textarea and click "Generate PRD" | A structured PRD draft appears with all 7 section headers and substantive content in populated sections |
| 2 | The input describes no AI or model components | The draft appears | Sections 2, 3, and 5 display a skip note derived from the input — not a placeholder and not fabricated content |
| 3 | The draft has empty or thin critical sections | The draft appears | Gap questions appear inline, targeted to the specific missing content |
| 4 | The user has answered the gap questions | They click "Finalize" | The answers are incorporated into the relevant sections — not appended as a list at the bottom |
| 5 | The PRD is finalized | The user clicks "Copy markdown" or "Download" | The output is valid markdown with the correct heading and all 7 section headers, ready to save as `prd.md` |

### Interaction States

| State | Trigger | User-visible behavior |
|---|---|---|
| Idle | Page load | API key field, textarea, "Generate PRD" button. Instructions visible. |
| Generating | "Generate PRD" clicked | Spinner/progress indicator. Button disabled. |
| Draft with gaps | Generation complete | PRD draft visible. Gap questions highlighted inline below thin/empty sections. |
| Draft complete | Generation complete, no gaps | PRD draft visible. "Finalize" or "Copy / Download" immediately available. |
| Incorporating | "Finalize" clicked after gap answers | Second API call in progress. Spinner visible. |
| Finalized | Incorporation complete | Final PRD visible. "Copy markdown" and "Download .md" available. Gap question fields hidden. |
| Error | API call fails | Plain error message with details. Input preserved. Retry available. |

### Out of Scope

- Multiple simultaneous inputs or file upload UI
- History, versioning, or session persistence across page reloads
- Collaborative editing or shared output links
- Integration with GitHub, Notion, or any external tool
- PRD review or feedback features (this tool drafts, not critiques)
- Any non-PRD output format (e.g., feature briefs, acceptance scenarios)

---

## 5. Evaluation & Performance Standards

### Golden Dataset

_A set of 10+ diverse raw inputs — varying in length, specificity, and AI content — with hand-evaluated PRD outputs assessed by PM against the section quality rubric._

**Size:** 10 inputs minimum (mix of AI products, non-AI products, sparse inputs, dense inputs)
**Owner:** Product Manager
**Validation method:** PM reviews each output section-by-section against the rubric. Pass requires ≥90% of sections scoring "complete" or correctly "skipped" on valid inputs.

### Scored Metrics

| Metric | Target | Minimum to Ship |
|---|---|---|
| **Section presence** (all 7 headers appear) | 100% of runs | 100% |
| **AI skip detection accuracy** (sections 2/3/5 correctly skipped or included) | 95% | 90% |
| **Gap question relevance** (questions target the specific missing content) | 80% of gap questions are directly actionable | 70% |
| **Incorporation fidelity** (gap answers appear in correct sections, not appended) | 90% of answers in correct location | 85% |

### Baseline at Launch

All 7 section headers must be present on every run. AI skip detection must be correct on 90% of inputs. Below these thresholds, the output is worse than the PM writing from the template manually.

---

## 6. Non-Functional Requirements & Guardrails

### Latency Targets

| Operation | Target | Worst-case bound |
|---|---|---|
| PRD draft generation (Stage 1–3) | <30s | <60s |
| Gap incorporation (Stage 4) | <20s | <40s |

### The Escape Hatch

- User can edit any section of the draft manually before finalizing — the tool produces a draft, not a locked document.
- "Copy markdown" is always available after draft generation — the user can take the draft and finish it themselves without running the gap incorporation step.
- If the API call fails, the input is preserved and the user can retry or copy their input to use elsewhere.
- The tool never submits, publishes, or acts on the PRD — it produces a file for the user to place themselves.

### Privacy & Bias Boundaries

- **API key:** Stored in sessionStorage only. Never written to localStorage. Cleared on tab close.
- **No external analytics:** No tracking scripts, no usage telemetry, no third-party calls except the Claude API.
- **Input text:** Sent to the Claude API (Anthropic) only. No other destination. User is responsible for ensuring their input does not contain sensitive data they wouldn't send to an AI API.
- **No output storage:** The finalized PRD lives in the browser only until the user downloads or copies it.

---

## 7. Lifecycle & Maintenance

### Degradation Thresholds

- If Claude's output format changes and section parsing breaks, the tool must fail visibly rather than produce silently malformed output.
- If sessionStorage behavior changes in a target browser, the API key field must still function — the tool can prompt for the key on each use.

### Monitoring Cadence

| Signal | Cadence | Alert threshold |
|---|---|---|
| PRD draft quality (PM spot-check on new runs) | Per use | Any run where AI sections are fabricated rather than skipped → prompt review needed |
| Gap question relevance | Per use | Any run where gap questions are generic rather than specific → prompt review needed |

### Ownership Model

| Phase | Owner |
|---|---|
| Building | Tech Lead (AI Build Loop) |
| Deploying | PM (local file or GitHub Pages) |
| Monitoring | PM (per-use quality review) |
| Retiring | PM |

---

## Biggest Unknowns

1. **How much raw input is enough?** The tool's quality depends entirely on the richness of the input. If a user pastes 30 words, the draft will be thin — is that a failure of the tool or expected behavior? The gap detection mechanism is the answer, but it needs to be validated.
2. **Can the AI reliably detect AI components in raw input?** The skip-or-include decision for sections 2, 3, and 5 is the most consequential judgment the tool makes. False positives (fabricating AI architecture content) are worse than false negatives (asking the user to confirm).
3. **Will the two-call pattern feel slow?** Stage 1 (draft) + Stage 4 (incorporate gaps) means two API round-trips. If Stage 1 takes 20s and Stage 4 takes 15s, the total session is ~35s of waiting. That may be acceptable for a drafting tool, but needs to be tested against PM patience.
