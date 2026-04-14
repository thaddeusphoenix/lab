---
firewall: tester-only
---

# Acceptance Scenarios: Daily Log + Pull Planning

> ⚠ **FIREWALL — Writer context boundary.**
> This document is input to the Tester and Coordinator only.
> The Writer (AI coder) must never receive this file or its contents.
> Keep it in a separate file from the brief at all times. Never paste scenarios into the brief.

**Brief:** [daily-log.md](daily-log.md)
**Feature:** Daily Log + Pull Planning
**Last updated:** 2026-03-17

---

## Tier 1 — Automatable

### S1: PDF daily log — fields extracted and displayed

**Given:** A foreman has sent an SMS with a PDF daily log attached. The PDF contains: foreman name, trade, date, men on site (count), list of completed work items, and one blocker.
**When:** The daily log dashboard loads.
**Then:** The foreman's row shows all extracted fields — men on site count matches the PDF value, at least one completed work item is displayed, the blocker is present, and no field reads "missing" or blank for a field that was present in the PDF.
**Method:** DOM assertion — check that the foreman row contains the correct men-on-site value, a non-empty completed work section, and a non-empty blocker section.

---

### S2: Missing field surfaced explicitly

**Given:** A foreman has sent a brief SMS that contains completed work and a blocker but no manpower count.
**When:** The daily log dashboard loads.
**Then:** The foreman's row displays the completed work and blocker correctly, and the men-on-site field is explicitly flagged as missing — a visible indicator (e.g., "—" or "No count") rather than an empty cell.
**Method:** DOM assertion — men-on-site cell contains a non-blank gap indicator, not an empty string.

---

### S3: Look-ahead source labels present on all entries

**Given:** The look-ahead has been populated with at least one planned activity (sourced from P6) and at least one committed event (sourced from a foreman submission).
**When:** The look-ahead view renders.
**Then:** Every entry carries a visible source label. P6-sourced entries display "P6" or equivalent. Foreman-committed entries display the foreman's name and trade. No entry is present without a source label.
**Method:** DOM assertion — every look-ahead entry element contains a child node with source text; no entry has an empty source field.

---

### S4: Schedule update report is valid JSON

**Given:** The Superintendent has approved at least one daily log entry and at least one look-ahead commitment.
**When:** The schedule update report is generated and downloaded.
**Then:** The output file is valid JSON, contains at least one `actuals` entry and one `commitments` entry, and each entry includes `trade`, `date`, and `description` fields at minimum.
**Method:** Parse the output with `JSON.parse()` — no exception thrown. Assert presence of `actuals` and `commitments` arrays with at least one item each containing the required fields.

---

### S5: Planned/committed gap flagged

**Given:** The look-ahead contains a P6 planned activity for a trade within the next 7 days with no corresponding foreman commitment from that trade.
**When:** The look-ahead view renders.
**Then:** The planned activity is visually flagged as uncovered — a distinct visual treatment (e.g., warning color, icon, or label) differentiates it from activities that have a corresponding commitment.
**Method:** DOM assertion — planned activity element without a matching commitment has a CSS class or attribute indicating gap state; a planned activity with a matching commitment does not.

---

## Tier 2 — Judgment

### S6: PDF extraction quality — unstructured daily log

**Given:** A PDF daily log in a non-standard format — handwritten or a GC-specific template with labeled fields in an unexpected layout. The PDF contains men on site, at least two completed work items with location references, and one blocker.
**When:** Claude processes the attachment and the daily log row renders.
**Then:** The extracted data is accurate and complete enough for the Superintendent to act on — correct manpower count, work items that reflect what the PDF actually says (not paraphrased beyond recognition), and a blocker that captures the actual constraint described.
**Rubric:** Evaluate whether: (1) the manpower count is numerically correct, (2) each completed work item references the same trade and location as the PDF source, (3) the blocker describes the actual constraint and not a generic placeholder. Minor rewording is acceptable; omissions or factual errors are not.
**Pass signal:** PASS if all three field types are present and accurate. FAIL if any field is omitted, numerically wrong, or describes a different activity than what the PDF contains.

---

### S7: Look-ahead renders planned vs. committed coherently

**Given:** The look-ahead contains a mix of P6 planned activities and foreman-committed events across at least three trades over a 3-week window. Some planned activities have matching commitments; some do not. Some committed events have no P6 backing.
**When:** A Superintendent reviews the look-ahead.
**Then:** The visual distinction between planned and committed is immediately clear without reading source labels. The gap between planned and committed activities is scannable — a Superintendent can identify uncovered activities at a glance. Field-driven committed events with no P6 backing are distinguishable from covered planned activities.
**Rubric:** Evaluate whether: (1) planned and committed entries are visually distinct at first glance, (2) uncovered planned activities stand out without requiring the user to compare rows manually, (3) the layout supports scanning by trade or by date, not just a flat list.
**Pass signal:** PASS if all three visual distinction criteria are met. FAIL if planned and committed look identical, if gaps require manual row-by-row comparison to identify, or if the layout does not support scanning.

---

### S8: Schedule update report is usable by a PM/Scheduler

**Given:** The Superintendent has approved a mix of daily log entries and look-ahead commitments across multiple trades over two days.
**When:** The PM/Schedule Controller receives the JSON schedule update report.
**Then:** The report contains enough structured information to update a master schedule without requiring the PM to contact the Superintendent for clarification — trade, area, date, type of entry (actual vs. commitment), and a description field are present and unambiguous.
**Rubric:** Evaluate whether: (1) each entry is unambiguously attributable to a trade and area, (2) the distinction between actuals (what happened) and commitments (what will happen) is clear in the data structure, (3) a scheduler reading the JSON could identify which P6 activities need updating without additional context.
**Pass signal:** PASS if all three criteria are met. FAIL if trade or area is missing from any entry, if actuals and commitments are not structurally distinguished, or if the report requires verbal clarification to interpret.

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
      "reason": "Foreman row shows 14 men on site matching PDF value; two completed work items present; blocker 'rebar delivery delayed' present."
    },
    {
      "id": "S7",
      "tier": 2,
      "result": "FAIL",
      "reason": "Planned and committed entries use identical visual styling; uncovered planned activities are not distinguishable without reading source labels individually."
    }
  ],
  "spec_amendment": "Add to Design Constraints: planned and committed look-ahead entries must use visually distinct treatments — different background color, border, or icon — such that uncovered planned activities are identifiable without reading source labels. A Superintendent scanning the look-ahead must be able to spot gaps in under 10 seconds."
}
```

**Rules for `spec_amendment`:**
- Required when `result` is `FAIL`. Omit when `PASS`.
- Must name the specific constraint that was violated.
- Must be written as a direct addition to the brief — the Coordinator pastes it in verbatim.
- One amendment per failed scenario. If multiple scenarios fail, list them separately.
