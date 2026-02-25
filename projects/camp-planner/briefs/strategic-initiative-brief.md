# Strategic Initiative Brief: Camp Planner

> A purpose-built planning tool that helps working parents track candidate programs, stay ahead of registration and cancellation deadlines, and ensure their children's summer is covered week by week.

**Status:** Draft
**Owner:** Wintermute (Product Manager)
**Last updated:** 2026-02-25
**Related Feature Briefs:** _(links once created)_

---

## The Opportunity

Parents of school-age children face a recurring, high-stakes planning problem every year: filling their children's summers with programs that keep kids engaged and supervised while they work. The challenge is multi-layered and time-sensitive. Popular programs open registration months in advance and fill fast. Parents hedge by registering for more programs than they need — overbooking as a strategy — which requires tracking cancellation windows so they can back out before fees become non-refundable. Fees and payment deadlines vary by program and are easy to miss. The goal is continuous coverage across 8–10 weeks, which means thinking in weekly blocks, not individual program registrations.

No purpose-built tool exists for this. Parents cobble together Google Sheets, calendar apps, and memory. The result is a planning system that leaks: missed deadlines, surprise cancellation fees, and gap weeks that leave a working parent scrambling for coverage.

The addressable market is large: any household with school-age children where both parents work, or a single parent working full-time. In the US alone, that is tens of millions of families with this problem recurring every year.

## Why Now

- Competition for spots at popular programs has intensified, making deadline awareness higher-stakes than it was even five years ago
- Post-pandemic, parents have become more deliberate planners — improvising childcare coverage is no longer acceptable to most
- Purpose-built tools for specific life workflows (travel planning, home buying, event coordination) have trained consumers to expect better than a spreadsheet
- No clear market leader exists in this space — the category is open

## Why Us

The problem is well-defined, domain-specific, and repeatable. It does not require solving a hard technical problem — it is a data management and visualization problem wrapped in a well-understood user need. The build complexity is low relative to the value delivered. Early success creates strong word-of-mouth: parents in the same social networks share tools that solve shared pain. If we become the thing parents send each other in April ("what are you using for camp this summer?"), distribution compounds.

## What We're Building

A lightweight web tool for working parents to manage their children's summer program planning from first-look to locked schedule. Parents can add candidate programs with key dates, fees, and status. A week-by-week calendar view shows which weeks are covered and which have gaps. The tool surfaces approaching registration and cancellation deadlines before they become problems. Parents can track overbooking positions and make cancel vs. commit decisions with full financial context visible.

## What We're Not Doing

- **Program discovery or search** — we are not a directory, marketplace, or recommendation engine
- **Direct registration or payment** — no integrations with program registration systems
- **Social or coordination features** — no sharing schedules with other parents, no carpool coordination
- **Year-round activity management** — we are starting with summer; after-school and other seasons are out of scope
- **Childcare or nanny scheduling** — this is about structured programs, not in-home care

## Success Looks Like

| Metric | Target | Timeframe |
|---|---|---|
| Parents build a full summer plan without help | >80% of test users complete initial setup unassisted | Usability testing before launch |
| Deadline capture rate | Parents using the tool miss 0 registration or cancellation deadlines in a planned season | First full summer of use |
| Year-over-year retention | Parents return to plan the following summer | 12 months post-first use |

## Biggest Unknowns

1. **What is the core value — deadline tracking, schedule visualization, or overbooking decision support?** The answer changes what we build first. We cannot treat all three as equal priority in the first version without building too much.

2. **At what point in the planning cycle do parents feel the most acute pain — and is that when they would reach for a new tool?** If the pain peak is in March (when registration chaos begins) but the desire to plan is in January, the tool's activation moment shifts.

3. **Would a dedicated app solve this better than a well-designed shareable spreadsheet template?** Before committing to a web build, we should test whether a polished spreadsheet delivers 80% of the value at 10% of the cost. If it does, we learn something important about whether this is a tool problem or a template problem.
