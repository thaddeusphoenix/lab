# Project Feature Brief: Superintendent View

> The Superintendent's daily reconciliation screen: agent-mapped foreman updates, three-state activity list, and one-tap approve/override — no data entry required.

**Status:** Aligned
**Owner:** Wintermute (Product Manager)
**Last updated:** 2026-03-13
**Parent Initiative:** [`strategic-initiative-brief.md`](strategic-initiative-brief.md)

---

## The Problem

**User:** Site Superintendent on a hyperscale construction site

**Pain:** Every morning the Superintendent calls or walks to each trade foreman to collect status updates, then manually translates what they hear into schedule fields in P6. This turns a site management role into a data entry role. On a site with dozens of active trades, this consumes hours and introduces a reporting lag that makes schedule risk invisible until it becomes slippage.

---

## The Proposed Solution

A single self-contained HTML file that renders the Superintendent's reconciliation dashboard. The page loads with a stubbed P6 schedule and a set of pre-loaded foreman messages. An in-browser agent maps those messages to schedule activities using keyword extraction. The Superintendent sees every activity's current state and approves or overrides the agent's proposals.

### Activity States

Every activity has one of three states:
- **gap** — no foreman message has been received for this activity
- **pending** — the agent has mapped a foreman message to this activity and proposed an update; awaiting Superintendent approval
- **approved** — the Superintendent has approved the agent's proposed update

### Required JavaScript Functions

Write these functions in order, completing each before starting the next:

1. **`tokenize(str)`** — lowercases the string, splits on non-word characters, returns an array of tokens.

2. **`extractPercentage(text)`** — returns a number (0–100) extracted from the text. Handle: "80%", "80 percent", "eighty percent", "halfway" (50), "almost done" (90), "done" / "complete" / "finished" (100), "just started" (10). Return `null` if no percentage signal found.

3. **`mapMessageToActivity(text, foremanId)`** — scores each activity in `P6_SCHEDULE` against the message tokens using the activity's `zoneAliases` and `tradeAliases` arrays. A zone alias match adds 5 points; a trade alias match adds 4 points; a foreman match (activity's `foremanId` equals the sender) adds 3 points. Returns the activity object with the highest score above 0, or `null` if no activity scores above 0.

4. **`renderActivityList()`** — iterates `P6_SCHEDULE`, creates a card element for each activity, applies the correct CSS class (`status-gap`, `status-pending`, or `status-approved`) based on `activity.status`, and writes them into `#activity-list`. Pending cards include an Approve button (`onclick="approveActivity('activityId')"`) and an Override button. Gap cards show a "No update" badge. Approved cards show a green badge. Called on load and after every state change.

5. **`approveActivity(id)`** — finds the activity in `P6_SCHEDULE` by id, sets `status` to `'approved'`, calls `renderActivityList()`.

6. **`bulkApprove()`** — sets `status` to `'approved'` on all activities with `status === 'pending'`, calls `renderActivityList()`.

7. **`handleSimulatedMessages()`** — iterates `SIMULATED_MESSAGES`, calls `mapMessageToActivity` for each, and for matched activities: sets `status` to `'pending'` and sets `proposedPct` to the result of `extractPercentage(message.text)`. Called once on load after `renderActivityList()`.

8. **DOMContentLoaded init block** — wires the Bulk Approve button click to `bulkApprove()`, calls `renderActivityList()`, calls `handleSimulatedMessages()`, calls `renderActivityList()` again after messages are processed.

### Stub Data

Hardcode `P6_SCHEDULE` with exactly 6 activities across 3 trades:

```
{ id:'A1', name:'Electrical Conduit Zone 4', trade:'Electrical', zone:'Zone 4',
  foremanId:'f1', zoneAliases:['zone 4','zone4','north','z4'],
  tradeAliases:['electrical','conduit','rough-in','wire'], status:'gap', proposedPct:null }

{ id:'A2', name:'Electrical Panel Level 2', trade:'Electrical', zone:'Level 2',
  foremanId:'f1', zoneAliases:['level 2','level2','lvl2','l2'],
  tradeAliases:['electrical','panel','switchgear'], status:'gap', proposedPct:null }

{ id:'A3', name:'Mechanical Ductwork Zone 2', trade:'Mechanical', zone:'Zone 2',
  foremanId:'f2', zoneAliases:['zone 2','zone2','south','z2'],
  tradeAliases:['mechanical','duct','ductwork','hvac','mep'], status:'gap', proposedPct:null }

{ id:'A4', name:'Mechanical Piping Level 3', trade:'Mechanical', zone:'Level 3',
  foremanId:'f2', zoneAliases:['level 3','level3','lvl3','l3'],
  tradeAliases:['mechanical','pipe','piping','plumbing'], status:'gap', proposedPct:null }

{ id:'A5', name:'Concrete Pour Zone 1', trade:'Concrete', zone:'Zone 1',
  foremanId:'f3', zoneAliases:['zone 1','zone1','east','z1'],
  tradeAliases:['concrete','pour','slab','foundation'], status:'gap', proposedPct:null }

{ id:'A6', name:'Concrete Formwork Level 1', trade:'Concrete', zone:'Level 1',
  foremanId:'f3', zoneAliases:['level 1','level1','lvl1','l1'],
  tradeAliases:['concrete','formwork','form','shoring'], status:'gap', proposedPct:null }
```

Hardcode `SIMULATED_MESSAGES` with exactly 4 entries — these represent foreman messages already received before the Superintendent opens the dashboard:

```
{ foremanId:'f1', text:'north side electrical rough-in is about 80 percent done' }
{ foremanId:'f2', text:'MEP on level two is about halfway' }
{ foremanId:'f3', text:'we finished the concrete pour in zone 1' }
{ foremanId:'f1', text:'panel work on level 2 is just started' }
```

After `handleSimulatedMessages()` runs, activities A1, A2, A3, and A5 should have `status:'pending'`; A4 and A6 should remain `status:'gap'`.

---

## Output Constraints

- **The complete HTML file must not exceed 12,000 characters total.** Hard limit. If over: remove all CSS `transition` declarations, remove all CSS comments, collapse padding/margin shorthands, shorten activity names to under 20 characters. Never truncate a JavaScript function body.
- No JSDoc. No inline code comments. Short variable names.
- Use `<script>` not `<script type="module">` — file opens on `file://` URLs.

---

## Visual Design

- Three states must be visually distinct by color alone — no legend required:
  - **gap**: red left border, red "No update" badge
  - **pending**: amber/orange left border, amber badge, prominent green Approve button + blue Override button
  - **approved**: green left border, green badge, no action buttons
- A stats bar or summary row at the top showing counts: X pending, Y gap, Z approved.
- Bulk Approve button visible when any activities are in pending state.

---

## Out of Scope

- Real P6 API integration
- Live foreman message receiving
- The Foreman View messaging UI (separate brief: `foreman-view.md`)
- User authentication
- Offline sync

---

## Acceptance Scenarios

Defined in `superintendent-view-scenarios.md`.

**⚠ Firewall rule:** The brief is the Writer's input. The scenarios are the Tester's rubric. The Writer never receives the scenarios file.
