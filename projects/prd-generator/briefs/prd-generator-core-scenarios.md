---
firewall: tester-only
---

# Acceptance Scenarios: PRD Generator Core

> ⚠ **FIREWALL — Writer context boundary.**
> This document is input to the Tester and Coordinator only.
> The Writer (AI coder) must never receive this file or its contents.
> Keep it in a separate file from the brief at all times. Never paste scenarios into the brief.

**Brief:** [prd-generator-core.md](./prd-generator-core.md)
**Feature:** PRD Generator Core
**Last updated:** 2026-03-03

---

## Tier 1 — Automatable

_Deterministic. Verified by DOM assertions, output structure checks, or string matching. No judgment required — the outcome is objectively true or false._

### S1: All 7 section headers present after generation

**Given:** The textarea contains a product description of at least 100 words describing a non-trivial product (e.g., a web app for managing freelance invoices).
**When:** The user clicks "Generate PRD" and the generation completes without error.
**Then:** The rendered output contains all 7 of the following section headers, in order: `## 1. Strategic Context`, `## 2. Data Specifications`, `## 3. Reasoning Architecture`, `## 4. Functional Requirements`, `## 5. Evaluation & Performance Standards`, `## 6. Non-Functional Requirements & Guardrails`, `## 7. Lifecycle & Maintenance`. At least 5 of the 7 sections contain substantive content (more than a single placeholder line).
**Method:** DOM text assertion — check that all 7 header strings are present in the output container; count sections with >50 characters of non-header content.

### S4: Finalized output contains gap answers in correct sections

**Given:** A textarea with sparse input (~80 words, no user persona described). Generation has completed and a gap question for the "User Personas" section is visible inline below section 1.
**When:** The user types an answer into the gap question textarea (e.g., "The primary user is a freelance graphic designer who invoices 3–5 clients per month") and clicks "Finalize".
**Then:** The downloaded or copied markdown contains the persona description within the `## 1. Strategic Context` section — not appended at the end of the document or in a separate "Gap Answers" section.
**Method:** String search in the copied/downloaded markdown output — verify the persona text appears between the `## 1. Strategic Context` header and the `## 2. Data Specifications` header. Verify no "Gap Answers" or "Addendum" section exists.

### S5: Downloaded markdown has correct heading and all 7 section headers

**Given:** A finalized PRD (either via the "Finalize" flow or directly after generation with no gaps).
**When:** The user clicks "Copy markdown" or "Download .md".
**Then:** The markdown string begins with `# AI Product Requirements Document:` (followed by the product name), and contains all 7 `## [N].` section headers. The file, if downloaded, has a `.md` extension.
**Method:** String assertion on the clipboard contents or downloaded file contents. Check for the exact heading prefix and all 7 section header prefixes.

---

## Tier 2 — Judgment

_Requires evaluation against intent. An LLM-as-judge reads this document and the brief as its rubric, then evaluates the output. Each scenario must yield a machine-readable PASS or FAIL._

### S2: AI sections correctly skipped for non-AI input

**Given:** The textarea contains a product description that makes no reference to AI models, LLMs, retrieval pipelines, training data, fine-tuning, or agentic behavior (e.g., a description of a static recipe website or a simple CRUD task tracker).
**When:** The draft appears.
**Then:** Sections 2 (Data Specifications), 3 (Reasoning Architecture), and 5 (Evaluation & Performance Standards) each display a skip note rather than placeholder fields or fabricated content. The skip note must be a brief sentence explaining why the section doesn't apply — derived from what the input describes — not a generic "N/A".
**Rubric:** The judge should look for: (a) the section header is present, (b) the content immediately following the header is a skip note in the form `> _Not applicable. [Reason.]_` or equivalent, (c) the reason is specific to the described product (e.g., "This product performs no model inference" not just "Not applicable"), (d) the section contains no fabricated architecture, data source tables, or metric rows.
**Pass signal:** PASS if all three sections (2, 3, 5) contain a specific, contextual skip note and no fabricated content. FAIL if any of the three sections contains fabricated AI-specific content, or if any section is simply blank with no note.

### S3: Sparse input triggers targeted gap questions

**Given:** The textarea contains fewer than 50 words that describe a product concept without naming a user persona, user segment, or target customer (e.g., "An app that helps you track what you eat. You log meals and it shows you patterns over time.").
**When:** The draft appears.
**Then:** At least one gap question appears inline below Section 1 (Strategic Context) specifically asking about the target user, user segment, or persona — not a generic "tell us more" prompt. The gap question must reference the missing content specifically (e.g., "Who is the primary user of this app? Describe their behaviors, goals, and context.").
**Rubric:** The judge should look for: (a) a visible gap question UI element below Section 1, (b) the question text specifically names the missing content (user/persona), (c) the question is not generic boilerplate that could apply to any product, (d) the question contains enough context that the user knows exactly what to provide.
**Pass signal:** PASS if at least one gap question below Section 1 specifically targets the missing user/persona information with a contextual prompt. FAIL if no gap questions appear, or if all gap questions are generic (e.g., "Please provide more detail about this section").

---

## Tester Output Format

Every run must produce a structured result the Coordinator can parse. No prose summaries — structured JSON only.

```json
{
  "run": 1,
  "result": "PASS",
  "scenarios": [
    {
      "id": "S1",
      "tier": 1,
      "result": "PASS",
      "reason": "All 7 section headers present. 6 of 7 sections contain substantive content (>50 chars). Section 2 contains a valid skip note."
    },
    {
      "id": "S2",
      "tier": 2,
      "result": "FAIL",
      "reason": "Section 3 (Reasoning Architecture) contained a fabricated decision logic flowchart despite the input describing a static recipe site with no AI components."
    },
    {
      "id": "S3",
      "tier": 2,
      "result": "PASS",
      "reason": "Gap question below Section 1 read: 'Who is the primary user of this food tracking app? Describe their age range, context, and what problem they are trying to solve.' Specific and contextual."
    },
    {
      "id": "S4",
      "tier": 1,
      "result": "PASS",
      "reason": "Persona answer found between ## 1. Strategic Context and ## 2. Data Specifications headers. No 'Gap Answers' section in output."
    },
    {
      "id": "S5",
      "tier": 1,
      "result": "PASS",
      "reason": "Markdown begins with '# AI Product Requirements Document: Food Tracker'. All 7 ## section headers present. Download file extension is .md."
    }
  ],
  "spec_amendment": "Add to System Prompt — Stage 1: The model must not produce any content in sections 2, 3, or 5 if the input makes no reference to AI, ML, or model components. If uncertain, output a skip note and ask a gap question rather than fabricating content."
}
```

**Rules for `spec_amendment`:**
- Required when `result` is `FAIL`. Omit when `PASS`.
- Must name the specific constraint that was violated.
- Must be written as a direct addition to the brief — the Coordinator pastes it in verbatim.
- One amendment per failed scenario. If multiple scenarios fail, list them separately.
