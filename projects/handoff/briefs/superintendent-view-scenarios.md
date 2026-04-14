---
firewall: tester-only
---

# Acceptance Scenarios: Superintendent View

> ⚠ **FIREWALL — Writer context boundary.**
> This document is input to the Tester and Coordinator only.
> The Writer (AI coder) must never receive this file or its contents.

**Brief:** [`superintendent-view.md`](superintendent-view.md)
**Feature:** Superintendent View
**Last updated:** 2026-03-13

---

## Tier 1 — Automatable

### S1: Activity list renders all 6 activities on load

**Given:** The page loads with the stubbed `P6_SCHEDULE` data
**When:** The activity list is rendered
**Then:** All 6 activities are visible, each showing trade name, activity name, zone, and a status indicator
**Method:** DOM assertion — count activity cards in `#activity-list`; assert count is 6; assert each card contains trade, activity name, zone, and a status badge element

### S2: Simulated foreman messages map to pending activities

**Given:** The page has loaded and `handleSimulatedMessages()` has run
**When:** The activity list is rendered
**Then:** Activities A1, A2, A3, and A5 have `status-pending` class/indicator; their cards show the proposed completion percentage and an Approve button
**Method:** DOM assertion — find activity cards for A1, A2, A3, A5; assert each has `status-pending` CSS class; assert each contains an approve button; assert proposed percentage is displayed (80 for A1, 50 for A3, 100 for A5, 10 for A2)

### S3: Gap detection — unlogged activities are visually distinct

**Given:** `handleSimulatedMessages()` has run; A4 and A6 received no messages
**When:** The activity list is rendered
**Then:** A4 and A6 have a visually distinct gap state (different CSS class from pending/approved) and a "No update" or gap label
**Method:** DOM assertion — activity cards for A4 and A6 have `status-gap` CSS class; cards for A1/A2/A3/A5 do not have `status-gap`

### S4: Approve action resolves a pending activity

**Given:** Activity A1 is in pending state with an Approve button visible
**When:** The tester clicks the Approve button for A1
**Then:** A1's status changes to approved; the Approve button is no longer present on A1's card; A1 has `status-approved` CSS class
**Method:** DOM assertion — after click, A1's card has `status-approved` class; `querySelectorAll` on A1's card returns no approve button element

---

## Tier 2 — Judgment

### S5: Agent mapping handles natural language variation

**Given:** The `SIMULATED_MESSAGES` array contains 4 natural language messages as specified in the brief
**When:** The Tester reads the JavaScript source and evaluates `mapMessageToActivity` against the 3 test inputs:
  1. "north side electrical rough-in is about 80 percent done"
  2. "MEP on level two is about halfway"
  3. "we finished the concrete pour in zone 1"
**Then:** The mapping logic resolves at least 2 of 3 inputs to the correct activity through alias/keyword matching — not exact string match
**Rubric:** Look for: zone alias array matching (e.g., 'north' maps to Zone 4), trade alias matching (e.g., 'rough-in', 'mep', 'ductwork'), scoring system that favors multi-token matches. Hardcoded exact-match lookup fails.
**Pass signal:** PASS if mapMessageToActivity returns the correct activity object for at least 2 of the 3 inputs. FAIL if mapping requires exact field names or does not use alias arrays.

### S6: Three states are immediately distinguishable without instructions

**Given:** The activity list contains a mix of approved, pending, and gap activities
**When:** The Tester views the rendered output as a first-time user
**Then:** The three states are distinguishable by visual treatment alone — color, iconography, or badge text — without reading a legend; pending and gap items are more visually prominent than approved items
**Rubric:** Look for: distinct color per state (red/amber/green convention or equivalent); pending items have a clear primary CTA (Approve button) that draws the eye; gap items feel like a call to action, not just absence of data; approved items recede visually.
**Pass signal:** PASS if three states are visually distinct and the pending/gap items are more prominent than approved. FAIL if all states look similar or the view requires reading labels to understand what action is needed.

---

## Tester Output Format

```json
{
  "run": 1,
  "result": "PASS",
  "scenarios": [
    {
      "id": "S1",
      "tier": 1,
      "result": "PASS",
      "reason": "6 activity cards present in #activity-list; each contains trade, name, zone, and status badge"
    }
  ],
  "spec_amendment": "..."
}
```

`spec_amendment` is required when `result` is FAIL. Omit when PASS.
