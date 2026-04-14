# Project Feature Brief: Foreman View

> The Foreman's daily input surface: a native messaging app UI where foremen submit plain-language progress updates, exactly like texting a colleague.

**Status:** Aligned
**Owner:** Wintermute (Product Manager)
**Last updated:** 2026-03-13
**Parent Initiative:** [`strategic-initiative-brief.md`](strategic-initiative-brief.md)

---

## The Problem

**User:** Trade foreman on a hyperscale construction site

**Pain:** Foremen are asked to log progress daily, but every existing tool forces them to navigate form fields, dropdowns, and labeled inputs. On a job site, foremen are moving — they won't stop to fill out a form. The reporting never gets done, which creates the data gap that costs the Superintendent hours every morning.

---

## The Proposed Solution

A single self-contained HTML file that renders a native messaging app UI — modeled exactly on iOS Messages or Android Messages. The screen has two states:

**Contact List state:** A scrollable list of foreman contact rows. Each row shows a foreman name and trade. Tapping a row opens the chat.

**Chat state:** A full-screen message thread with a header showing the selected foreman's name and trade, a scrollable thread of chat bubbles, a text input pinned to the bottom, and a circular send button adjacent to the input. Tapping a back arrow returns to the contact list.

When the foreman types a message and hits send:
1. The message appears as a right-aligned outgoing bubble (blue, rounded).
2. A stub agent reply appears as a left-aligned incoming bubble (gray, rounded) after a short delay. Reply text: "Got it — update logged."
3. The input clears and the thread scrolls to the bottom.

There is no connection to the Superintendent View in this file. This is the Foreman's standalone input surface.

---

## Output Constraints

- **The complete HTML file must not exceed 10,000 characters total.** Hard limit. If over, cut CSS verbosity first — trim transition declarations, collapse shorthand properties. Never truncate JavaScript.
- No JSDoc. No inline comments. Short variable names. No polyfills.
- Use `<script>` not `<script type="module">` — the file opens on `file://` URLs.

---

## Design Constraints

- **Zero form elements.** No `<select>`, no `<label>`, no `<input type="text">` styled as a form field, no structured inputs. The message composer must be a `<textarea>` or `<input>` used as a chat composer — not a labeled form field.
- Contact rows must be tappable `<div>` or `<button>` elements — not a `<select>` dropdown.
- Outgoing bubbles: right-aligned, blue background, white text, border-radius ≥ 16px.
- Incoming bubbles: left-aligned, light gray background, dark text, border-radius ≥ 16px.
- Message input pinned to the bottom of the screen with the send button to its right.
- Chat header shows the foreman name and trade. A back arrow/chevron returns to the contact list.
- No timestamps required. No read receipts. No typing indicators.

---

## Stub Data

Hardcode exactly 4 foremen in a `FOREMEN` array:

```
{ id: 'f1', name: 'Marcus T.', trade: 'Electrical' }
{ id: 'f2', name: 'Rosa V.', trade: 'Mechanical' }
{ id: 'f3', name: 'Devon K.', trade: 'Concrete' }
{ id: 'f4', name: 'Priya S.', trade: 'Steel Framing' }
```

---

## Out of Scope

- Real voice transcription
- Live P6 or backend integration
- Multi-foreman simultaneous sessions
- Message persistence across page loads
- Actual agent NL mapping (stub reply only)
- The Superintendent View (separate brief)

---

## Acceptance Scenarios

Defined in `foreman-view-scenarios.md`.

**⚠ Firewall rule:** The brief is the Writer's input. The scenarios are the Tester's rubric. The Writer never receives the scenarios file.
