# Project Feature Brief: Daily Log + Pull Planning

> Foremen spend time producing actuals and commitments that never make it upstream in a structured form. Superintendents spend time chasing that information to build look-ahead schedules and feed the PM/Scheduler. This replaces the manual collection and aggregation in the middle — accepting foreman updates through whatever channel requires the least effort, and giving the Superintendent a structured artifact they can act on and pass up the chain.

**Status:** Aligned
**Owner:** Wintermute (Product Manager)
**Last updated:** 2026-03-17
**Parent Initiative:** [`strategic-initiative-brief.md`](strategic-initiative-brief.md)

---

## The Problem

**Users:** Three roles in sequence — Foreman → Superintendent → Project Manager / Schedule Controller.

**The flow:**
1. **Foreman** provides actuals (what was completed, men on site, blockers) and planned commitments (upcoming inspections, deliveries, trade handoffs) to the Superintendent.
2. **Superintendent** uses foreman communication to build and maintain the look-ahead schedule and to feed updates to the master schedule. They run the weekly sub coordination meeting off the look-ahead.
3. **Project Manager / Schedule Controller** incorporates Superintendent inputs — alongside other sources — to publish updated master schedules (P6 or equivalent). Published schedules drive planning decisions and financial actions including billing and payment applications.

**Pain:** The information produced by foremen does not reach the Superintendent in structured form. Foremen already fill out daily logs on paper, in their company's system, or via GC-required forms — but the Superintendent still has to chase them to get the same information verbally. The Superintendent then manually consolidates what they collect into a look-ahead and summarizes it for the PM/Scheduler. Information degrades at every handoff. The PM publishes schedules and billing documents based on data that may be days old.

**Evidence:** Willis Clayton-Stankowski (Cahil Construction) reviewed the Handoff prototype and identified daily logs and pull planning as the higher-value, more practical use case — specifically because it avoids the P6/Oracle API integration wall that has blocked every scheduling startup he's encountered. The Superintendent's manual daily log and look-ahead coordination meeting are confirmed industry norms at this level of construction.

---

## The Proposed Solution

Foremen submit updates through whatever channel requires the least additional effort from them — a brief SMS, a forwarded email, or a PDF scan of their paper daily log attached to an SMS or email. There is no single required format. Claude extracts all available fields from each submission: men on site, completed work, blockers, and any forward-looking commitments. PDF attachments are processed via Claude's vision capability — the goal is full extraction of whatever the daily log contains, not just structured fields. When a submission is missing a field, the dashboard surfaces the gap explicitly rather than silently leaving it blank.

The Superintendent sees two views.

The **daily log** is one row per sub, populated as updates arrive throughout the morning — men on site, what they completed, where they're stuck.

The **3-week look-ahead** is a rolling calendar/Gantt view of all activity across the next 21 days. It has two distinct layers:

- **Planned** — activities pulled from the P6 master schedule that fall within the look-ahead window. These represent what the schedule says should happen. P6 is a read source only; no write-back required.
- **Committed** — events that foremen and the Superintendent have explicitly confirmed will happen: inspections, material deliveries, trade handoffs, coordination milestones. Committed entries come from foreman submissions (SMS, email, photo) and Superintendent decisions in the UI.

The gap between planned and committed is the primary signal. A P6 activity appearing in the look-ahead with no corresponding commitment from the responsible foreman is a flag — the Superintendent needs to surface it in the coordination meeting. A committed event with no P6 backing is a field-driven addition that may need to flow back to the scheduler. Every entry in the look-ahead carries a visible source label — **P6** for planned activities, the foreman's name and trade for committed events — so the Superintendent can immediately see what is schedule-derived versus field-confirmed.

The look-ahead is more detailed than P6 at the activity level and is the artifact the Superintendent uses to run their weekly sub coordination meeting.

The Superintendent's approved look-ahead and daily log data also generates a **schedule update report** in a machine-readable format (JSON) — a structured digest of actuals and committed changes the PM/Schedule Controller can import into P6 or any scheduling tool without manual re-entry. This removes the need for any direct P6 write-back: the Superintendent produces a structured output, the PM consumes it and applies it on their end. The system sits between the field and the scheduler, not between the scheduler and P6.

---

## Why This, Why Now

The schedule write-back approach (P6/Oracle API integration) is confirmed as a near-term blocker by a domain expert with direct GC relationships. Daily logs and pull planning deliver comparable value to the Superintendent — daily visibility, a coordination artifact, fewer manual hours — without requiring API access to any scheduling system. The SMS input mechanism and Claude NL parsing from the existing Handoff prototype are directly reusable. This is the path to a real pilot.

---

## Out of Scope

- **Writing back to P6** — P6 is a read source for planned activities only; no update or sync
- Automated outbound prompts to subs (manual follow-up for now)
- Full OCR of arbitrary daily log formats from day one — start with common fields, expand as patterns emerge
- Time and attendance or payroll use of men-on-site data
- Safety, incident, or compliance reporting
- Earned value calculation or schedule forecasting
- Integration with Procore or other project management platforms

---

## Success Looks Like

1. A Superintendent can open the dashboard in the morning and see a populated daily log for every sub who has submitted — no manual collection or data entry required on their end.
2. The 3-week look-ahead — with planned activities from P6 and committed events from foremen — is the artifact the Superintendent uses to run their weekly sub coordination meeting, without supplementing it from another source.
3. The PM/Schedule Controller receives a structured schedule update report from the Superintendent's approved data that they can use to update the master schedule and support billing — without having to chase the Superintendent for a verbal summary.

---

## Biggest Unknowns

1. **How complete is the data across channels, and can gaps be surfaced usefully?** No single submission will reliably contain all three fields. The question is whether Claude can extract enough from the combination of SMS, email, and photo submissions across a morning to give the Superintendent a daily log they trust — and whether surfacing explicit gaps (e.g., "no manpower count from Electrical") is actionable or just noise.

2. **What daily log formats do foremen actually use?** Paper daily logs vary by GC, sub, and region. Before building photo extraction, we need to understand the range of formats in the field — whether there are 3 common templates or 30. This determines whether a Claude vision extraction approach is viable or whether we need a more structured intake path first.

3. **Is P6 read access obtainable in practice?** Write-back to P6 is confirmed as nearly impossible. Read access to pull planned activities into the look-ahead window is a lower bar — but still requires GC IT cooperation and possibly Oracle licensing. The planned/committed model only works if we can populate the planned layer from P6. If read access is also blocked, the planned layer would need to be seeded manually or from an exported schedule file (CSV/XER), which changes the workflow.

4. **What constitutes a meaningful planned/committed gap?** The gap between a P6 planned activity and a foreman commitment is the core signal. But not every gap is a problem — some activities have long lead times, some are owned by trades not yet on site. The Superintendent needs to be able to distinguish a gap that requires a coordination conversation from one that is expected. The rules for that distinction are site-specific and need to be grounded in real look-ahead data before the UI can surface them usefully.

---

## Acceptance Scenarios

Defined in a separate document — [`daily-log-scenarios.md`](daily-log-scenarios.md).

**⚠ Firewall rule:** The brief is the Writer's input. The acceptance scenarios are the Tester's rubric. These must live in separate files. The Writer never receives the scenarios document. The Tester receives both. This separation is non-negotiable — if the Writer sees the scenarios, it optimizes for passing the test rather than solving the problem.

The brief is not ready to trigger a build loop until its companion scenarios document exists and is complete.


## Amendments — Run 1 (2026-03-17)

Add to Schedule Update Report requirements: every entry in the actuals and commitments arrays of the JSON output must include an explicit 'area' field (e.g., floor, grid reference, zone) as a discrete structured field — not embedded in the description string. Entries where area is not determinable from the submission must set 'area' to null with an explicit null value rather than omitting the field. A scheduler must be able to filter or sort entries by area without parsing free-text.


## Amendments — Run 2 (2026-03-17)

Add to Build Constraints: the output must be a complete, self-contained HTML file with no truncated JavaScript. All rendering functions (daily log table population, gantt/list look-ahead render, report JSON generation, PDF simulation, SMS parse preview) must be fully present and syntactically valid such that the page loads and populates without errors in a browser. The seed data, rendering logic, and all event handlers must be included in a single deliverable file. If output length is a concern, reduce seed data volume rather than truncating rendering logic.
