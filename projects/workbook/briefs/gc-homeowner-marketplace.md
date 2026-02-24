# Project Feature Brief: GC & Homeowner Marketplace

> General Contractors have no reliable way to source and vet verified skilled labor; this feature gives them a searchable, trust-scored directory of workers who have proven their skills with photo evidence.

**Status:** Draft
**Owner:** Wintermute (Product Manager)
**Last updated:** 2026-02-23
**Parent Initiative:** [`strategic-initiative-brief.md`](strategic-initiative-brief.md)

---

## The Problem

**User:** General Contractors (primary), homeowners (secondary)
**Pain:** GCs hire labor with almost no verified information — a phone call to a reference, a handshake, and a gamble. There is no portable, cross-employer record of what a worker has actually done. The result is hiring risk on every new crew member and a slow, word-of-mouth sourcing process that fails under volume or time pressure. Homeowners face a version of the same problem: they rely on star ratings that measure satisfaction, not skill, and have no way to see documented proof that a worker completed a comparable job successfully.
**Evidence:** The construction labor shortage is structural — the industry has documented difficulty filling skilled trade roles even when workers are available. GCs are an established B2B buyer category with demonstrated willingness to pay for staffing and compliance tools. Existing platforms (Angi, HomeAdvisor, staffing agencies) compete on convenience, not verification quality, which signals that real proof of skill is an unsolved and differentiated problem.

## The Proposed Solution

The Marketplace begins as a manual, concierge operation targeting GCs only. Before any self-serve product is built, we curate a filtered list of verified workers — by trade, location, and trust score — and deliver it directly to GC contacts as a PDF, spreadsheet, or formatted message. This validates demand, surfaces what information GCs actually act on, and generates early revenue or intent signals without engineering investment. As supply grows and GC behavior is understood, the concierge operation graduates to a self-serve web directory where GCs can search, filter by trade and trust level, and initiate contact through the platform. GCs pay for access — a subscription or per-hire fee — while workers remain free. Homeowners are a second phase, served only after the GC workflow is proven and supply is sufficient to support a consumer-grade discovery experience.

## Why This, Why Now

The supply side — worker portfolios, the Trust Engine, verified photo records — exists to power this feature. Without a marketplace, those portfolios produce no demand-side value and no revenue. Workbook's unit economics only work if the platform captures demand-side monetization; the supply side is the moat, but the marketplace is where the business model closes. Starting with GCs before homeowners is the right sequence for two reasons. First, GCs have acute, recurring hiring needs and are willing to pay for a better sourcing tool — the revenue case is stronger and faster to close. Second, GC feedback is more signal-dense: a single GC who hires through the marketplace and returns is stronger validation than many one-off homeowner searches. Homeowners are a larger eventual market but require more supply density, a more polished experience, and a different acquisition motion — none of which should be built until the GC case is proven.

## Out of Scope

- Homeowner marketplace in this phase — no consumer-facing search, no homeowner acquisition
- Job posting or inbound job board (workers are not browsing for work here; buyers are browsing for workers)
- Payroll, W-2/1099 classification, or compliance documentation beyond the Trust Engine's existing verification
- Integration with ATS or HR systems at GCs
- Reviews, ratings, or feedback loops from GCs back to worker profiles (a future iteration)
- Mobile app — any self-serve product is web-based

## Success Looks Like

1. At least 5 GCs receive a concierge worker list and at least 2 make contact with a worker from that list within the first 60 days of operating the concierge.
2. At least 1 GC converts to a paying account (subscription or per-hire fee) before the self-serve product is built, validating willingness to pay.
3. When the self-serve directory launches, at least 3 of the initial concierge GCs migrate to it and use it without hand-holding, confirming the product can replace the manual operation.

## Biggest Unknowns

1. **Are GC and homeowner needs too different to serve with one product?** GCs care about compliance documentation, reliability across multiple hires, and volume; homeowners care about price, availability, and a single job going well. These may require fundamentally different interfaces, acquisition channels, and pricing models — or a single product may be unable to serve both without compromising for each. This needs to be answered before any homeowner investment is made.
2. **What is the GC's actual activation trigger?** We do not yet know what moves a GC from reviewing a worker list to making contact. Is it the trust score? A specific trade credential? The volume of completed jobs? The presence of a recognizable project type? The concierge phase exists in part to observe this behavior directly before designing a self-serve experience around it.
3. **How many verified workers need to exist before the marketplace is credible?** A directory with 12 workers in two trades and one metro is not a marketplace — it is a list. There is a threshold below which GCs will not take the product seriously. We do not know where that threshold is, and building the marketplace prematurely risks a first impression we cannot recover from.
