# Strategic Initiative Brief: Workbook

> A Dynamic Reputation Marketplace that turns a skilled worker's daily job site photos into a verified, portable proof-of-work record — giving labor career mobility and giving contractors a trusted, verified-only hiring pool.

**Status:** Draft
**Owner:** Wintermute (Product Manager)
**Last updated:** 2026-02-23
**Related Feature Briefs:** [`whatsapp-ingestion.md`](whatsapp-ingestion.md)

---

## The Opportunity

Skilled trade and construction labor — a workforce in the tens of millions globally, heavily immigrant — has no portable, digital record of its work. Reputation travels by word of mouth, locked inside a single employer or foreman relationship. When a worker moves to a new city, contractor, or trade, that history disappears. From the contractor side, General Contractors face a documented global labor shortage and hire largely blind: no verified skill record, no work history, no accountability layer beyond a phone call to a reference who may or may not pick up.

This is a two-sided data vacuum. On the supply side, workers have no way to build equity from their daily labor. On the demand side, GCs carry hiring risk on every new crew member with no systemic way to reduce it.

## Why Now

Three forces are converging:

1. **The labor shortage is structural, not cyclical.** The construction industry faces a persistent skilled labor gap driven by aging workforce retirement and underinvestment in trade training. GCs are actively looking for better ways to source and vet labor — the demand-side pain is acute.

2. **WhatsApp is already the infrastructure.** The smartphone is already in the worker's pocket. WhatsApp has deep penetration in the communities that make up much of the US and global construction labor force. The distribution channel exists — the product just needs to show up inside it.

3. **Computer vision and AI are now capable at the edge.** Assessing construction photo quality, mapping visual consistency across a job sequence, and extracting metadata from images (GPS, timestamps) are now tractable problems with commodity API access. The "Truth Engine" that makes the verification meaningful is buildable by a small team.

## Why Us

The moat is not the interface — it's the data and the network. Every verified photo record created by a worker is behavioral data that cannot be purchased, licensed, or synthesized. Competitive entrants face the same cold-start problem we do, but we can get there first by meeting workers on WhatsApp rather than asking them to change their behavior. Traditional workforce platforms (LinkedIn, Indeed, staffing agencies) are structurally unable to reach this population — their acquisition models assume email addresses, résumés, and internet-native behavior. We enter where those tools cannot.

## What We're Building

A two-sided marketplace anchored in Proof of Work. Workers interact exclusively via WhatsApp: they send Before, Progress, and Completed photos tagged to a job. An AI Trust Engine analyzes visual consistency, validates EXIF metadata, and enables peer verification from co-workers on the same site. This builds a verified portfolio — a Reference Book — attached to the worker's phone number. General Contractors access a verified-only labor pool and, as a secondary benefit, receive automated daily logs and compliance-ready photo records as a byproduct of the same worker behavior.

## What We're Not Doing

- Not building a scheduling, dispatch, or payroll tool
- Not targeting white-collar, office, or remote workers
- Not replacing HR systems or integrating with ATS platforms in this phase
- Not building a native mobile app — the interface is WhatsApp, full stop

## Success Looks Like

| Metric | Target | Timeframe |
|---|---|---|
| Verified workers with 10+ records in their Reference Book | 500 | 6 months post-launch |
| Monthly worker retention (active photo submissions) | ≥ 40% | 6 months post-launch |
| Paying GC accounts accessing the verified labor pool | 10 | 12 months post-launch |

## Biggest Unknowns

1. **Can the AI Trust Engine work in the real world?** Construction sites are messy, lighting is poor, and fraud is motivated. Does computer vision produce reliable quality signals in these conditions — or does it produce noise that erodes trust in the verification?

2. **Will workers send photos consistently after onboarding?** The value to the worker (career mobility, new opportunities) is deferred. The behavior required (tagging and sending photos daily) is ongoing. What is the retention mechanism strong enough to sustain participation without a direct, immediate reward?

3. **What is the GC's actual evidence threshold?** Before a contractor pays for or acts on a Workbook verification, what level of proof do they need to trust it? And who inside the GC organization is the actual buyer — the foreman, the HR team, the owner?
