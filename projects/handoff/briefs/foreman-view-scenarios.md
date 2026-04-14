---
firewall: tester-only
---

# Acceptance Scenarios: Foreman View

> ⚠ **FIREWALL — Writer context boundary.**
> This document is input to the Tester and Coordinator only.
> The Writer (AI coder) must never receive this file or its contents.

**Brief:** [`foreman-view.md`](foreman-view.md)
**Feature:** Foreman View
**Last updated:** 2026-03-13

---

## Tier 1 — Automatable

### S1: Contact list renders all foremen

**Given:** The app loads
**When:** The contact list state is displayed
**Then:** All 4 foremen are visible as tappable rows, each showing name and trade
**Method:** DOM assertion — count contact rows; assert each contains a name and trade label; assert no `<select>` element is present

### S2: Selecting a foreman opens the chat view

**Given:** The contact list is displayed
**When:** The tester clicks the first foreman row
**Then:** The contact list is hidden; the chat view is visible with the correct foreman's name in the header
**Method:** DOM assertion — after click, chat container is visible; contact list is hidden; chat header text contains the foreman name

### S3: Sending a message creates an outgoing bubble

**Given:** The chat view is open for any foreman
**When:** The tester types "Zone 4 electrical conduit is 80% done" and clicks the send button
**Then:** The message appears in the thread as a right-aligned bubble; the input is cleared
**Method:** DOM assertion — message thread contains a bubble with class indicating outgoing/right alignment; bubble text matches sent message; input value is empty after send

### S4: Agent reply appears as an incoming bubble

**Given:** A foreman message has just been sent
**When:** The agent reply renders (may require a short async wait)
**Then:** A left-aligned incoming bubble appears in the thread with reply text containing "Got it" or "logged"
**Method:** DOM assertion — thread contains a bubble with class indicating incoming/left alignment after the outgoing bubble; text contains acknowledgment language

### S5: Zero form elements

**Given:** The app is open in either state (contact list or chat)
**When:** The tester inspects the full DOM
**Then:** There are no `<select>` elements, no `<label>` elements, no `<input type="submit">` elements, and no visible form-style dropdowns
**Method:** DOM assertion — `querySelectorAll('select').length === 0`; `querySelectorAll('label').length === 0`

---

## Tier 2 — Judgment

### S6: UI is visually indistinguishable from a native messaging app

**Given:** The chat view is open with at least one sent message and one agent reply
**When:** The Tester views the rendered output
**Then:** The layout matches native messaging conventions: outgoing bubbles right-aligned with blue/colored background, incoming bubbles left-aligned with neutral background, message input pinned to the bottom of the screen with a send button to its right, contact name in a fixed header
**Rubric:** PASS if the UI would not look out of place as a screenshot in an iOS Messages thread. FAIL if there are visible form elements, if messages are not in a bubble layout, or if the input is not bottom-pinned.

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
      "reason": "4 contact rows present, each with name and trade; no <select> element found"
    }
  ],
  "spec_amendment": "..."
}
```

`spec_amendment` is required when `result` is FAIL. Omit when PASS.
