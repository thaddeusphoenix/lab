# Project Feature Brief: Core Planning Loop

> Working parents lose money and miss spots because they are not prepared to act when registration opens — not because they don't know the deadline.

**Status:** Aligned
**Owner:** Wintermute (Product Manager)
**Last updated:** 2026-03-16
**Platform:** Progressive Web App (PWA) — mobile-first, installable to home screen, no App Store required
**Parent Initiative:** [Camp Planner Strategic Initiative Brief](strategic-initiative-brief.md)

---

## The Problem

**User:** Working parents with school-age children who manage summer program enrollment across multiple programs, deadlines, and children.

**Pain:** The planning failure is not ignorance of deadlines — it is unpreparedness at the moment of action. Parents know registration opens on March 15. What they don't have, when March 15 arrives, is the registration link, the correct session selected, their payment method ready, and their account logged in. The result: missed spots, late registrations, and the stress of a problem that was visible weeks in advance but not acted on in time. Alongside this, parents have no single place to see whether their summer is actually covered week by week, or how their total spending tracks against a household budget.

**Evidence:** Validated by first research session (Sari Gelzer, 2026-02-26). Sari described setting alarms and preparing specifically to "be ready to click the button." She uses Notes and Google Calendar today — tools that store dates but provide no preparation context. She explicitly said she wished the app could "click the button for her."

---

## Output Artifact

**A single self-contained HTML file** — all CSS and JavaScript inline. No external dependencies. Must run correctly when opened directly in a browser and when served over HTTP (GitHub Pages).

This file IS the product. It is a mobile-first Progressive Web App with bottom tab navigation, localStorage persistence, and PWA meta tags that enable home-screen installation on iOS and Android.

---

## Technical Requirements

### PWA Installation (required)

Include all of the following in the `<head>`:

```html
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="theme-color" content="#2563EB">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<meta name="apple-mobile-web-app-title" content="Camp Planner">
```

Include a PWA manifest via a dynamically generated data URI or blob URL. The manifest must specify:
- `name`: "Camp Planner"
- `short_name`: "Camps"
- `display`: "standalone"
- `background_color`: "#ffffff"
- `theme_color`: "#2563EB"
- `start_url`: "."
- `icons`: at minimum one SVG icon (192×192 and 512×512 sizes) generated as inline SVG data URIs — a simple blue circle with a white tent/sun icon or letter "C" is fine

### Mobile Layout

- Base design width: 375px. All elements must work at 375px–430px viewport.
- `box-sizing: border-box` on everything.
- **Bottom tab bar** — fixed at `bottom: 0`, full width, white background with top border. Tabs: Programs, Coverage, Decisions. Icons above labels. Each tab ≥64px tall. Use `padding-bottom: env(safe-area-inset-bottom)` to clear the iOS home indicator.
- **Content area** — `padding-bottom` must account for tab bar height (≥64px) plus safe area so content is not hidden behind the tab bar.
- No horizontal scrolling.
- All touch targets ≥44px tall and ≥44px wide.
- System font: `-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif`

### localStorage Persistence

Store and load all data from localStorage. Keys:
- `campplanner_programs` — JSON array of program objects
- `campplanner_budget` — JSON object `{ total: number }`
- `campplanner_checklist` — JSON object keyed by program ID: `{ [programId]: { item1: bool, item2: bool, item3: bool } }`

On page load, read from localStorage. On every state change (add, edit, delete, budget save, checklist toggle), write back to localStorage immediately.

### Pre-loaded Sample Data

On first load (when `campplanner_programs` is absent from localStorage), seed with these three programs:

```json
[
  {
    "id": "sample-1",
    "name": "Galileo Innovation Camp",
    "startDate": "2026-07-06",
    "endDate": "2026-07-10",
    "registrationDeadline": "2026-03-25",
    "registrationUrl": "https://galileo-camps.com",
    "cancellationDeadline": "2026-04-15",
    "cancellationFee": 75,
    "fee": 650,
    "status": "Considering",
    "notes": ""
  },
  {
    "id": "sample-2",
    "name": "YMCA Summer Day Camp",
    "startDate": "2026-06-15",
    "endDate": "2026-06-26",
    "registrationDeadline": "2026-05-01",
    "registrationUrl": "https://ymca.org/summer",
    "cancellationDeadline": null,
    "cancellationFee": null,
    "fee": 420,
    "status": "Registered",
    "notes": ""
  },
  {
    "id": "sample-3",
    "name": "City Arts Summer Intensive",
    "startDate": "2026-07-27",
    "endDate": "2026-08-07",
    "registrationDeadline": "2026-04-30",
    "registrationUrl": "",
    "cancellationDeadline": null,
    "cancellationFee": null,
    "fee": 890,
    "status": "Considering",
    "notes": ""
  }
]
```

Seed budget: `{ "total": 2500 }`

---

## The Proposed Solution

A three-tab mobile app. Bottom tab bar navigates between Programs, Coverage, and Decisions. A budget tracker lives at the top of the Programs tab.

### Tab 1: Programs

**Budget tracker** — displayed as a card at the top of the Programs tab. Shows:
- Total budget (editable — tap "Edit" to reveal a number input, then "Save")
- A segmented progress bar: green segment = committed spend (Registered programs), amber segment = potential additional spend (Considering programs), gray = remaining
- Three stat labels below: Committed ($X), Potential ($X), Remaining ($X)
- If committed + potential exceeds budget: remaining shows in red

**Program list** — below the budget tracker. Group programs into two sections:
- **Action required** (header label) — programs with status Considering or Waitlisted that have a registration deadline in the future
- **Registered** (header label) — programs with status Registered
- Each program card shows: program name (bold), date range, status badge, and days until registration deadline (color-coded: red ≤7 days, amber ≤14 days, gray >14 days)
- Tapping a card opens the edit sheet

**Add program** — floating action button (FAB) bottom-right, above the tab bar. Blue circle with + icon.

**Add / Edit program sheet** — slides up from bottom as a bottom sheet modal (dark overlay behind, white sheet with rounded top corners). Contains:
- Required fields: Name (text), Start Date (date), End Date (date), Registration Deadline (date)
- Optional fields: Registration URL (url input), Fee ($), Status (segmented control or select: Considering / Registered / Waitlisted / Cancelled), Cancellation Deadline (date), Cancellation Fee ($)
- "Save" button (blue, full width) and "Cancel" link
- Edit sheet also shows a red "Delete program" link at the bottom
- Sheet can be dismissed by tapping the overlay

### Tab 2: Coverage

**Summer 2026 weekly grid.** Display 11 weeks:
- Week 1: Jun 8–12
- Week 2: Jun 15–19
- Week 3: Jun 22–26
- Week 4: Jun 29–Jul 3
- Week 5: Jul 6–10
- Week 6: Jul 13–17
- Week 7: Jul 20–24
- Week 8: Jul 27–31
- Week 9: Aug 3–7
- Week 10: Aug 10–14
- Week 11: Aug 17–21

Coverage logic: a program covers a week if its start date ≤ the week's Friday and its end date ≥ the week's Monday.

Each week cell shows:
- Week label: "Jun 8" style
- Status color: **green** = at least one Registered program covers this week; **amber** = at least one Considering/Waitlisted program but no Registered; **gray/empty** = no coverage
- A small program name label if covered (truncated to 18 chars if needed; if multiple programs, show count)

Layout: vertical stack of week rows, each row full width with the week label on the left and a colored coverage pill on the right. Or a two-column grid — whatever fits better on 375px.

A summary at the top: "X of 11 weeks covered" (count weeks with at least amber coverage).

### Tab 3: Decisions

**Enrollment Prep Cards** — when a program has status = Considering AND registration deadline ≤ 14 days from today's date, display it as an Enrollment Prep Card. This is the highest-priority item.

Enrollment Prep Card design:
- Visually distinct: blue left border (4px), light blue background tint
- Header: "⚡ Register by [date]" in red/urgent styling
- Program name (large, bold)
- Date range
- Fee (if present)
- Registration link button: "Open Registration Page →" — an `<a>` tag that opens `registrationUrl` in a new tab. If no URL: gray disabled-style button labeled "No link saved — add one"
- Three-item readiness checklist (checkboxes, stored in localStorage):
  1. "Account logged in"
  2. "Payment method ready"
  3. "Dates and session confirmed"

**Upcoming deadlines** — programs with registration deadline > 14 days from today (but still in the future) and status = Considering. Displayed as standard cards with deadline and days remaining.

**Cancellation warnings** — programs with status = Registered that have a cancellationDeadline ≤ 14 days from today. Show as amber-bordered warning cards: "Cancel by [date] or pay $[fee]" with a link to the registration URL.

If no action items: show a tidy empty state — "You're all caught up. Nothing needs attention right now."

---

## Color Palette

```
--blue:     #2563EB   (primary action, tab active state, prep card accent)
--blue-50:  #EFF6FF   (prep card background tint)
--green:    #16A34A   (registered, covered, committed spend)
--green-50: #F0FDF4
--amber:    #D97706   (considering, potential spend, cancellation warnings)
--amber-50: #FFFBEB
--red:      #DC2626   (urgent deadlines, overage, gap weeks)
--red-50:   #FEF2F2
--gray-50:  #F9FAFB   (page background)
--gray-100: #F3F4F6
--gray-200: #E5E7EB   (borders)
--gray-400: #9CA3AF   (placeholder text)
--gray-500: #6B7280   (secondary text)
--gray-700: #374151   (primary text secondary)
--gray-900: #111827   (primary text)
```

---

## Out of Scope

- Program sharing — separate feature brief, not part of this build
- URL auto-extraction — useful but not required
- Waitlist management — status label only, no waitlist position tracking
- Multi-child views — one child only in this version; child-switching UI is out of scope
- Multi-user or household sharing
- Program discovery
- Push notifications — out of scope for the HTML file build; noted as a future enhancement
- Service worker / offline caching — the manifest is sufficient for home-screen installation without a service worker

---

## Success Looks Like

1. A parent installs the PWA to their home screen, opens it, and sees sample programs already loaded. The app looks and behaves like a native mobile app — no browser chrome, native fonts, bottom tab navigation.
2. A parent can add a new program via the FAB in under 30 seconds. The coverage grid and budget tracker update immediately.
3. When a registration deadline is within 14 days, the Decisions tab shows an Enrollment Prep Card with the registration link and a checkable readiness list.
4. A parent can see at a glance which weeks of Summer 2026 are covered and which have gaps.

---

## Biggest Unknowns

1. **Will parents add the registration URL when logging a program?** The Enrollment Prep Card loses its core value if parents skip this field. We need to observe whether parents think to add the URL at program-entry time.

2. **Does the three-item readiness checklist match how parents actually prepare?** The checklist (logged in, payment ready, session confirmed) is hypothetical. We should validate whether these are the right items, whether parents find them patronizing or genuinely useful, and whether they check them off or ignore them.
