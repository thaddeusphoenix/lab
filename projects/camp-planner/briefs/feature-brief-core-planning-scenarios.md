---
firewall: tester-only
---

# Acceptance Scenarios: Core Planning Loop (Mobile PWA)

> ⚠ **FIREWALL — Writer context boundary.**
> This document is input to the Tester and Coordinator only.
> The Writer (AI coder) must never receive this file or its contents.
> Keep it in a separate file from the brief at all times.

**Brief:** [`feature-brief-core-planning.md`](feature-brief-core-planning.md)
**Feature:** Core Planning Loop — Mobile PWA
**Last updated:** 2026-03-16

---

## Tier 1 — Automatable

_Deterministic. Verified by DOM inspection or code reading. No judgment required._

### S1: PWA mobile meta tags are present

**Given:** The HTML file is opened
**When:** The Tester inspects the `<head>`
**Then:** The following meta tags are present with correct values:
- `<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">`
- `<meta name="apple-mobile-web-app-capable" content="yes">`
- `<meta name="apple-mobile-web-app-status-bar-style" ...>`
- `<meta name="apple-mobile-web-app-title" content="Camp Planner">`
- `<meta name="theme-color" content="#2563EB">`
- A `<link rel="manifest" ...>` element is present
**Method:** Read the HTML source — assert each meta tag exists with a matching value.

### S2: Bottom tab bar renders with three tabs

**Given:** The page loads
**When:** The Tester inspects the bottom navigation
**Then:** A fixed bottom tab bar is visible with exactly three tabs labeled Programs, Coverage, and Decisions. Each tab has a label. The bar uses `position: fixed` and `bottom: 0`. The CSS includes `env(safe-area-inset-bottom)` for bottom padding.
**Method:** DOM/CSS inspection — assert three tab elements exist with the correct labels. Assert `position: fixed` and `bottom: 0` on the tab bar element. Assert `env(safe-area-inset-bottom)` appears in the CSS for the tab bar or its padding.

### S3: Programs tab is the default active tab on load

**Given:** The page loads fresh
**When:** No tab has been tapped
**Then:** The Programs tab content is visible. Coverage and Decisions tab content are hidden. The Programs tab button is styled as active (e.g., blue color or active class).
**Method:** DOM inspection — assert Programs tab content container has `display` not `none`; assert other tab content containers are hidden.

### S4: Three sample programs are present on first load

**Given:** localStorage is empty (or absent) for `campplanner_programs`
**When:** The page loads
**Then:** Three program cards are rendered: "Galileo Innovation Camp", "YMCA Summer Day Camp", and "City Arts Summer Intensive".
**Method:** DOM inspection — assert three program name elements are present and contain the expected strings.

### S5: Add program FAB is present and opens an add form

**Given:** The Programs tab is active
**When:** The Tester taps/clicks the FAB (floating action button)
**Then:** A form or modal opens containing at minimum inputs labeled Name, Start Date, End Date, and Registration Deadline.
**Method:** DOM interaction — click the FAB element; assert a form/modal becomes visible with at least 4 input fields including required fields.

### S6: Coverage grid shows 11 weeks

**Given:** The Coverage tab is tapped
**When:** The coverage view renders
**Then:** Exactly 11 week rows or cells are displayed, spanning Jun 8 through Aug 21, 2026. A summary line shows "X of 11 weeks covered" or similar wording.
**Method:** DOM inspection on Coverage tab — count week row/cell elements; assert count equals 11; assert week labels include "Jun 8" and "Aug 17" (or "Aug 21").

### S7: Decisions tab renders at least one card for a near-deadline program

**Given:** The sample data is loaded (Galileo Innovation Camp has registrationDeadline 2026-03-25, which is within 14 days of 2026-03-16)
**When:** The Decisions tab is tapped
**Then:** An Enrollment Prep Card is visible for Galileo Innovation Camp. The card shows the registration deadline and a registration link element (either a functional link or a disabled/placeholder link). Three checklist items are visible with checkboxes.
**Method:** DOM inspection on Decisions tab — assert a card containing "Galileo" is present; assert a link/button referencing the registration URL is present; assert three checkbox-style elements are present within that card.

### S8: Budget tracker renders on Programs tab with correct values

**Given:** The sample budget is seeded at $2,500 and sample programs include YMCA ($420 Registered) and Galileo ($650 Considering) and City Arts ($890 Considering)
**When:** The Programs tab is active and the budget tracker is visible
**Then:** A budget display is visible showing:
- A total/budget value of $2,500
- A committed value of $420 (registered programs only)
- A potential value of at minimum $420 (or combined committed + considering)
- The values are labeled so the parent understands what each number means
**Method:** DOM inspection — assert dollar amounts matching the above values appear in the budget section. Exact labels may vary; assert numeric values are correct.

---

## Tier 2 — Judgment

_Requires LLM evaluation against intent. Each must yield a machine-readable PASS or FAIL._

### S9: Mobile-native visual quality

**Given:** The HTML file is rendered
**When:** The Tester reads the full CSS and evaluates the visual design at 375px width
**Then:** The app looks and feels like a native mobile app — not a desktop web page squeezed onto a phone. Specifically:
- Bottom tab navigation follows the iOS/Android native tab bar convention (icons + labels, fixed bottom)
- Cards use white backgrounds with soft shadows or subtle borders — not flat divs
- Typography is sized for mobile (body text ≥14px, headings ≥16px)
- Program status badges use color-coded pill styling
- The overall composition would not look out of place on the App Store
**Rubric:** Evaluate whether the CSS bottom tab bar, card design, typography scale, and color usage collectively produce a native-app-like visual quality. A page that is just a scrolling list of divs with browser-default styling FAILS. A page with a fixed bottom nav, card-based layout, color-coded badges, and mobile-appropriate spacing PASSES.
**Pass signal:** PASS if bottom tab navigation is fixed and styled natively, cards have distinct visual treatment, and text sizes are appropriate for mobile. FAIL if the layout looks like a desktop webpage, uses default browser element styling for navigation, or has no visual hierarchy.

### S10: Enrollment Prep Card serves its purpose

**Given:** The Decisions tab is active and Galileo Innovation Camp appears as an Enrollment Prep Card (deadline ≤14 days)
**When:** The Tester reads the card
**Then:** The card clearly communicates urgency and gives the parent everything they need to register in one place: the deadline date, the fee, a way to reach the registration page, and a readiness checklist that prompts the three preparation actions.
**Rubric:** The card must include: (1) a visual urgency signal (color, icon, or label indicating this needs immediate attention), (2) the specific deadline date, (3) the fee amount, (4) a registration link or clear indication that no link is saved, (5) three checkable items for readiness. The checklist items must be about preparation actions, not generic text.
**Pass signal:** PASS if all five elements are present and the card is visually distinct from non-urgent program cards. FAIL if the card lacks a registration link element, lacks a checklist, or is visually indistinguishable from a regular program card.

### S11: Coverage grid communicates summer coverage at a glance

**Given:** The Coverage tab is active with the sample data (YMCA covers Jun 15–26; Galileo covers Jul 6–10 if registered; City Arts covers Jul 27–Aug 7)
**When:** The Tester reads the coverage grid
**Then:** The grid makes it immediately obvious which weeks are covered and which are gaps. Green/amber weeks are visually distinct from empty weeks. A parent could scan this in 3 seconds and know their coverage situation.
**Rubric:** Evaluate whether the week-by-week layout uses clear color differentiation (not just text), whether gap weeks look visually alarming (empty, red, or visually "missing"), and whether the summary count is prominent enough to be seen immediately. The grid should not require reading every cell label to understand the summer picture.
**Pass signal:** PASS if covered and gap weeks use color-coded visual treatment, gap weeks are clearly distinct from covered weeks, and a summary is visible. FAIL if all weeks look the same regardless of coverage status, or if the coverage state can only be determined by reading individual text labels.

### S12: Add program form is complete and usable on mobile

**Given:** The FAB is tapped and the add program form/sheet opens
**When:** The Tester reads the form structure and evaluates usability
**Then:** The form contains all required fields (Name, Start Date, End Date, Registration Deadline) plus the key optional fields (Registration URL, Fee, Status, Cancellation Deadline). The form is presented as a bottom sheet (not a new page or inline section). Input fields are large enough for thumb use. A Save button and a way to dismiss/cancel are present.
**Rubric:** Evaluate whether the form slides up as a bottom sheet (not a full page navigation), whether fields are vertically stacked with adequate spacing, whether the Save button is prominent and full-width, and whether the Registration URL field is present (this field is critical to the Enrollment Prep Card feature).
**Pass signal:** PASS if all required fields are present, the form appears as a modal/sheet rather than a page, and a Registration URL field exists. FAIL if Registration URL is absent, if the form is inline rather than modal, or if required fields are missing.

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
      "reason": "All five PWA meta tags present with correct values; manifest link element found."
    },
    {
      "id": "S9",
      "tier": 2,
      "result": "FAIL",
      "reason": "Tab bar uses horizontal links with no icons and no fixed positioning — looks like a desktop navbar, not a native tab bar."
    }
  ],
  "spec_amendment": "Add to Technical Requirements: the bottom tab bar must use position:fixed, bottom:0, and each tab must include both an icon (SVG or emoji) above and a text label below. The tab bar must not use a standard horizontal nav/link pattern."
}
```

**Rules for `spec_amendment`:**
- Required when `result` is `FAIL`. Omit when `PASS`.
- Must name the specific constraint that was violated.
- Must be written as a direct addition to the brief — the Coordinator pastes it in verbatim.
- One amendment per run. Combine failures into a single actionable amendment.
