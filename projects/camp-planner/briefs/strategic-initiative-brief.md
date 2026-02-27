# Strategic Initiative Brief: Camp Planner

> A purpose-built planning tool that helps working parents track candidate programs, prepare for high-stakes enrollment moments, and ensure their children's summer is covered week by week — without missing a deadline or blowing the budget.

**Status:** Draft
**Owner:** Wintermute (Product Manager)
**Last updated:** 2026-02-26
**Related Feature Briefs:** [Core Planning Loop](feature-brief-core-planning.md)

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

A lightweight web tool for working parents to manage their children's summer program planning from first-look to locked schedule. Parents add candidate programs with key dates, fees, registration links, and cancellation policies. A week-by-week view shows which weeks are covered and which have gaps. As registration deadlines approach, the tool shifts from passive tracking to active preparation — surfacing the registration link, fee, and a readiness checklist so the parent arrives at the enrollment moment ready to act. Parents set a total summer budget and track committed spend against it as decisions are made. And when they find a program worth sharing, they can send a friend the name, dates, and registration link in one tap.

## What We're Not Doing

- **Program discovery or search** — we are not a directory or marketplace. Parents add programs they already know about. If a parent pastes a registration URL when adding a program, the tool may attempt to extract the name and dates — that is input assistance, not discovery. A curated local program directory is a v2 candidate targeting new parents who do not yet know the landscape.
- **Direct registration or payment** — no integrations with program registration systems. The Enrollment Prep Card surfaces the registration link; the parent still clicks it and registers themselves.
- **Schedule coordination platforms** — no shared editing, no carpool coordination, no family group features. Sharing an individual program (name, dates, registration link, deadline) via a native share sheet is in scope. Shared planning sessions are not.
- **Multi-user or household accounts** — the tool is single-user in v1. Budget is set and managed by one person. Spouse or co-parent sharing requires multi-user infrastructure that is out of scope.
- **Year-round activity management** — starting with summer. After-school programs, recurring activities, and other seasons are out of scope.
- **Childcare or nanny scheduling** — this is about structured programs, not in-home care.
- **Age-based program qualification** — knowing which programs a child will age into is a real need (especially for parents of younger children) but requires program data we do not have. Named as a deferred feature, not ignored.

## Success Looks Like

| Metric | Target | Timeframe |
|---|---|---|
| Parents build a full summer plan without help | >80% of test users complete initial setup unassisted | Usability testing before launch |
| Deadline capture rate | Parents using the tool miss 0 registration or cancellation deadlines in a planned season | First full summer of use |
| Year-over-year retention | Parents return to plan the following summer | 12 months post-first use |

## Biggest Unknowns

1. **Does the Enrollment Prep Card actually change behavior?** Research identified the enrollment moment as the sharpest pain. But we have not yet validated that a preparation card — rather than a simple reminder — is what closes the gap. The riskiest assumption in v1 is that surfacing a link and a checklist makes a parent more likely to register successfully and on time.

2. **Will parents add the registration URL when logging a program?** The Enrollment Prep Card only works if parents store the link up front, potentially months before the deadline arrives. If parents skip this field (because the URL doesn't exist yet, or they don't think to add it), the feature loses its core value. We need to observe this behavior in testing.

3. **Is one session of program sharing enough to drive word-of-mouth, or does it require the recipient to have their own account?** The share button sends a friend a link and deadline. If the recipient needs to sign up to do anything with it, friction may kill the behavior. If the shared link is a readable summary (no account needed), it may spread more naturally.
