# Project Feature Brief: Worker Discoverability

> Buyers in the GC & Homeowner Marketplace cannot reliably find the right worker for a job — this feature solves that by giving verified workers a presence in search results anchored to where they actually work, ranked by the signals that matter to the people hiring.

**Status:** Draft
**Owner:** Wintermute (Product Manager)
**Last updated:** 2026-02-23
**Parent Initiative:** [`strategic-initiative-brief.md`](strategic-initiative-brief.md)

---

## The Problem

**User:** General Contractors and homeowners searching the marketplace for a verified worker; and skilled trades workers trying to get hired through it.

**Pain:** A marketplace without a discoverability system is a directory — a flat list that rewards whoever appears first and buries everyone else arbitrarily. GCs need to surface workers who are credible, available, geographically relevant, and skilled for the specific trade at hand. Workers need the platform to surface them fairly, or there is no reason to keep contributing photos. Both problems are real: poor search produces bad matches on the demand side, and an opaque or unfair ranking system produces churn on the supply side.

**Evidence:** The Trust Engine produces a composite score per worker, but that score has no effect on discoverability until this system is built. The Worker Profile & Reference Book creates a shareable artifact, but a buyer has to already know about a worker to find it. The marketplace has no mechanism for a GC who needs a tiler in a specific neighborhood to find one — and no mechanism for a tiler in that neighborhood to know whether the platform is working for them.

## The Proposed Solution

Worker Discoverability is the ranking and retrieval layer that sits beneath the GC & Homeowner Marketplace. When a buyer searches, results are scoped by trade category and sub-specialty using a structured skill taxonomy (tile, framing, plumbing, electrical, painting, drywall, concrete, and their sub-specialties), then filtered by a location radius derived from the worker's verified GPS job history rather than a declared home address. Using job-site GPS as the location anchor is privacy-respecting by design: no worker is required to disclose where they live, and location authority comes from the verified record of where they have worked — a signal the Trust Engine has already validated. Within that filtered pool, results are ranked by a combination of Trust Engine composite score, profile completeness (number of verified jobs, number of active trade categories, peer validation count), and an availability signal derived from photo submission recency and inquiry response rate. Workers who have been active in the past 30 days and have responded to previous inquiries rank higher; inactive accounts do not surface at the top. To address the cold-start problem for new workers — the core tension of any ranking system — the discoverability layer reserves a fixed allocation of results for workers with fewer than five verified jobs, surfacing them in a labeled "New to Workbook" slot that is visible to buyers and explained honestly. This prevents a two-tier system where experienced workers monopolize results and new entrants never gain enough exposure to build the history that would move them up. The allocation shrinks as a worker's record grows, creating a fair ramp rather than a permanent ceiling.

## Why This, Why Now

The marketplace without discoverability is a half-built product. Supply-side work in Phases 1 and 2 produces verified workers with portfolios, trust scores, and payment history — but none of that creates hiring outcomes unless buyers can find the right worker for their job. Discoverability is the connective tissue between the supply side and the demand side. It must ship with the marketplace rather than after it, because a marketplace that cannot surface relevant results damages buyer trust immediately and produces no data on whether the ranking signals are working. Building it now also forces the product to answer the cold-start question before the worker base grows large enough to make inequity structural.

## Out of Scope

- Paid placement or sponsored listings — ranking is merit-based, not purchased
- Manual curation or editorial selection of featured workers
- Buyer-side saved searches, alerts, or recommendation emails
- Worker-facing analytics showing where they rank or how their position has changed
- Craftsmanship quality scoring beyond what the Trust Engine already produces
- Geographic filtering outside the GPS job history model (declared address, service area self-reporting)

## Success Looks Like

1. At least 60% of marketplace searches by GCs and homeowners result in the buyer viewing at least one worker profile, within 90 days of marketplace launch.
2. Workers with fewer than five verified jobs receive at least 15% of total search result impressions across the platform, confirming that the cold-start allocation is functioning and not being suppressed by system behavior.
3. Workers who receive at least one inquiry within their first 60 days on the platform retain at an equal or higher rate than the overall worker cohort, demonstrating that early discoverability drives continued supply-side engagement.

## Biggest Unknowns

1. **What signals do GCs and homeowners actually use to decide who to contact?** Trust score, photo quality, proximity, recency, trade category specificity — we do not know which of these drives click-through and contact in practice. A buyer might scan photos before reading a trust badge, or weight recent activity over total job count. Until we observe real buyer behavior in the marketplace, our ranking formula is a hypothesis. This should be tested with a small cohort of GCs before the ranking logic is hardened.

2. **Does a ranking system discourage new worker adoption?** If workers learn quickly that their profile is buried because they have fewer jobs than established workers on the platform, they may stop submitting photos before they build the record needed to climb. The cold-start allocation mitigates this — but whether it mitigates it enough to prevent churn among new entrants is unknown. The retention rate of workers in their first 60 days, before and after the allocation is tuned, is the metric that will answer this.
