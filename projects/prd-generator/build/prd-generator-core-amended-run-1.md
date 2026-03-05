# Project Feature Brief: PRD Generator Core

> A client-side HTML tool that takes raw discovery inputs and produces a structured PRD draft — with gap detection and targeted follow-up questions — ready to download as markdown.

**Status:** Aligned
**Owner:** Wintermute (Product Manager)
**Last updated:** 2026-03-03
**Parent Initiative:** [PRD Generator PRD](./prd.md)

---

## The Problem

**User:** Wintermute (Product Manager)
**Pain:** Writing a PRD from raw discovery notes takes 60–90 minutes and produces uneven quality. The PM must manually translate heterogeneous inputs into a structured 7-section document while simultaneously detecting what's missing.
**Evidence:** Every PRD in the lab has been drafted by hand with no tooling assistance. The PRD template exists but the work of filling it from raw material is entirely manual.

---

## The Proposed Solution

A single-file HTML application (`prd-generator.html`) that accepts raw text in a textarea, calls the Claude API client-side (user provides their own API key), and returns a structured PRD draft in the 7-section format defined in `templates/prd.md`. The tool scores each section on completion, surfaces targeted follow-up questions for empty or thin critical sections, allows the user to answer inline, and incorporates those answers into the relevant sections before producing a finalized PRD as downloadable markdown.

---

## Why This, Why Now

This project exercises every layer of the lab's development process end-to-end: PRD creation, feature brief, acceptance scenarios, AI Build Loop execution, shipped artifact, and amendment log as process record. The tool is also immediately useful — PRD drafting is a recurring bottleneck in every project. Building it as a client-side HTML file matches the lab's established pattern (Mood Ring, Tiny Tracks) and requires no coordinator modifications.

---

## UX States

The tool has six user-facing states:

1. **Idle** — Page loads. The user sees: an API key input field (with sessionStorage persistence), a textarea labeled "Paste your raw notes, brief, or research here", and a "Generate PRD" button. Brief instructions below the textarea.

2. **Generating** — "Generate PRD" clicked. A spinner or progress indicator is visible. The button is disabled. The textarea is read-only during generation.

3. **Draft with gaps** — Generation complete. The PRD draft renders below the input area in a readable format. Sections with empty or thin content show an inline gap question below the section heading (highlighted distinctly — e.g., a bordered call-out box). A "Finalize" button appears at the bottom, disabled until at least one gap answer is filled.

4. **Draft complete (no gaps)** — Generation complete, no empty/thin critical sections. PRD draft renders. "Copy markdown" and "Download .md" are immediately available. No "Finalize" step needed.

5. **Incorporating** — "Finalize" clicked. Second API call in progress. Spinner visible. Gap question fields are locked.

6. **Finalized** — Incorporation complete. Final PRD renders, replacing the draft. Gap question areas are removed. "Copy markdown" and "Download .md" are both visible and active.

7. **Error** — Any API call fails. A plain error message appears with the error detail. Input is preserved. A "Retry" button is available.

---

## Design Constraints

- **Visual register:** Dark background, minimal layout, monospace font for the PRD output. Matches the lab aesthetic (dark, technical, clean). No decorative elements.
- **No modal overlays.** All interactions happen in the main document flow.
- **API key field:** Present at the top. On first use, blank. After first entry, the key is stored in sessionStorage and auto-filled on return within the same tab session. A small "clear" link resets it.
- **Gap questions:** Rendered inline below the relevant section — not in a separate panel or at the bottom. Each gap question is a labeled textarea with placeholder text indicating what kind of answer to provide.
- **PRD output:** Rendered as formatted markdown in a scrollable region. The raw markdown is also available via "Copy markdown" — this copies the underlying markdown string, not the rendered HTML.

---

## Required Section Headers

The Stage 1 system prompt must instruct the model to produce a PRD using **exactly these 7 section headers**, in this order, verbatim:

```
## 1. Strategic Context
## 2. Data Specifications
## 3. Reasoning Architecture
## 4. Functional Requirements
## 5. Evaluation & Performance Standards
## 6. Non-Functional Requirements & Guardrails
## 7. Lifecycle & Maintenance
```

The final markdown output must begin with `# AI Product Requirements Document: [Product Name]` followed by these 7 headers. No other section naming scheme is acceptable.

The skip-note rule applies to **sections 2, 3, and 5** when the input describes no AI, ML, or model components. Each skipped section must still appear with its exact header, followed by a skip note in the form:
`> _Not applicable. [One sentence reason derived from the input.]_`

## Technical Constraints

- **Client-side only.** No server, no backend, no build step. A single `.html` file that opens in a browser.
- **Claude API call — Stage 1:** One `messages.create` call using the `claude-sonnet-4-6` model. The system prompt embeds the exact 7-section structure above and instructs the model to produce a PRD draft as plain markdown.
- **Claude API call — Stage 2:** One `messages.create` call when gap answers exist. The system prompt instructs incorporation of gap answers into the correct sections. The user message includes the current draft and the gap Q&A pairs. The model returns the finalized PRD markdown with answers placed inside the relevant sections.
- **No streaming.** Full response before rendering.
- **Gap question HTML placement:** Gap questions must be injected **inside the rendered section**, immediately below the section heading, as a visually distinct element (e.g., a bordered callout `div`). They must not be collected into a separate `#gap-questions-area` div outside the PRD content area. Each gap block stays with its section when the PRD scrolls.
- **API key storage:** sessionStorage only. Never localStorage. Never transmitted to any server other than the Claude API endpoint.
- **No external dependencies** beyond the Anthropic JS SDK loaded from a CDN (unpkg or jsDelivr).

---

## System Prompt — Stage 1 (Draft Generation)

The Stage 1 system prompt must:
1. Instruct the model to act as a PRD writer for an internal lab tool.
2. Embed the full 7-section PRD structure (section headers, field names, brief descriptions of each).
3. Instruct the model: for sections 2, 3, and 5 — if the input contains no reference to AI models, retrieval pipelines, training data, or agentic behavior — output the section header followed by: `> _Not applicable. [One sentence explaining why, derived from the input.]_`
4. Instruct the model: never invent personas, metrics, targets, or technical constraints not present in the input. If a critical section has no source material, output the header and a clearly marked placeholder: `> _[Gap: describe what's missing and why it matters]_`
5. Instruct the model to output only the PRD markdown — no preamble, no explanation, no closing remarks.

## System Prompt — Stage 2 (Gap Incorporation)

The Stage 2 system prompt must:
1. Instruct the model to update the PRD draft by incorporating the gap answers provided.
2. Each gap answer must be placed in the correct section — not appended at the bottom or listed as a separate section.
3. If an answer resolves a gap placeholder, replace the placeholder with the incorporated content.
4. Output only the updated PRD markdown — no explanation, no commentary.

---

## Out of Scope

- Multiple simultaneous inputs or file upload UI
- History, versioning, or session persistence across page reloads
- Streaming output
- Collaborative editing or shared links
- Integration with GitHub, Notion, or any external tool
- PRD review, critique, or scoring UI (tool drafts only — quality assessment is manual)
- Non-PRD output formats (feature briefs, acceptance scenarios)

---

## Success Looks Like

1. A user can paste raw notes and receive a full 7-section PRD draft within 30 seconds, with AI sections correctly skipped or populated.
2. Empty or thin sections trigger targeted gap questions — not generic "tell me more" prompts.
3. Gap answers are incorporated into the correct sections in the final output, not appended at the bottom.

---

## Biggest Unknowns

1. **How reliably does the model detect AI components from raw text?** The skip/include decision for sections 2, 3, and 5 is the hardest judgment call. Prompt engineering for this needs explicit examples.
2. **What makes a gap question "targeted" vs. generic?** The Stage 1 prompt needs to instruct the model to produce specific, contextual gap questions — not boilerplate. This is the hardest part of the prompt to get right.

---

## Acceptance Scenarios

_Defined in a separate document — `prd-generator-core-scenarios.md` in the same `briefs/` directory._

**⚠ Firewall rule:** The brief is the Writer's input. The acceptance scenarios are the Tester's rubric. These must live in separate files. The Writer never receives the scenarios document. The Tester receives both. This separation is non-negotiable — if the Writer sees the scenarios, it optimizes for passing the test rather than solving the problem.

The brief is not ready to trigger a build loop until its companion scenarios document exists and is complete.


## Amendments — Run 1 (2026-03-04)

The artifact must be a complete, syntactically valid single HTML file with no truncation. The JavaScript must be fully present and parseable — the file must load in a browser without errors. The model identifier must be exactly 'claude-sonnet-4-6' as specified in Technical Constraints; 'claude-sonnet-4-5' is not acceptable. Deliver the entire file in one response; do not truncate.
