# Project Feature Brief: Worker Profile & Reference Book

> Skilled trades workers have no portable professional identity, and the contractors evaluating them have no reliable way to assess a stranger's skill — this feature solves both problems with a public, verified portfolio page generated from a worker's WhatsApp activity.

**Status:** Draft
**Owner:** Wintermute (Product Manager)
**Last updated:** 2026-02-23
**Parent Initiative:** [`strategic-initiative-brief.md`](strategic-initiative-brief.md)

---

## The Problem

**User:** Skilled trades workers (tile, plumbing, electrical, framing) and the General Contractors or homeowners evaluating them before making contact.

**Pain:** Workers earn reputation entirely through word of mouth — a foreman's phone call, a referral from a friend. That reputation does not travel. When a worker moves to a new city, takes on a direct client, or approaches an unfamiliar GC, they have nothing concrete to show for years of verified work. On the other side, GCs and homeowners are asked to hire a stranger based on a conversation and a verbal reference. There is no standardized, trustworthy artifact that bridges the gap between "someone vouched for this person" and "I have seen their actual work."

**Evidence:** The Cardboard prototype (workbook-profile.html) has been built and demonstrates the concept visually. The strategic initiative brief documents the structural labor shortage and the hiring-blind problem GCs face. The WhatsApp ingestion and Trust Engine features exist precisely because the underlying data — verified photo records — is accumulating with nowhere to go. Without a shareable output, the verification work has no leverage for the worker and no utility for the evaluator.

## The Proposed Solution

Build a production-quality, public-facing portfolio page for each worker, accessible via a unique shareable link (e.g., workbook.co/marco-tile-5a3f) that the worker generates through a simple WhatsApp command. The page requires no login to view and displays the worker's name, trade, verified job entries with Before/Progress/Completed photos, Trust Engine badges, and peer validation count. A contact or hire button gives the evaluator a direct path to reach the worker. The page is generated automatically from verified data already in the system — no manual entry by the worker. This is the shareable output of the entire Phase 1 supply foundation: the thing a worker sends to a contractor instead of a phone number and a prayer.

## Why This, Why Now

The WhatsApp Ingestion Engine and Trust Engine together produce a verified record of a worker's output. Without this feature, that record is internal — useful to the system but invisible to the market. The Worker Profile & Reference Book is what converts verified data into professional equity the worker can actually use. It is the reason a worker continues logging photos: not for a badge they never see, but for a link they can send. It also completes the supply-side value proposition needed before the Phase 3 marketplace is credible — GCs cannot evaluate workers at scale without a standard artifact to review. Building this now closes the loop on Phase 1 and creates the demand-side pull that motivates continued worker engagement.

## Out of Scope

- Authenticated worker login or profile editing via the web — the worker manages their profile through WhatsApp only
- Search or discovery of workers by evaluators — that is the Phase 3 marketplace
- Client or GC reviews, ratings, or written testimonials
- Resume-style fields (employment history, certifications, education)
- Privacy controls or fine-grained content visibility settings — all verified records are shown, or the profile is not shared
- PDF export or print formatting

## Success Looks Like

1. Within 60 days of launch, at least 40% of workers with 5 or more verified job entries have generated and shared a profile link at least once.
2. The profile page loads in under 2 seconds on a mobile connection and renders correctly on WhatsApp's in-app browser on Android and iOS.
3. At least one documented instance of a GC or homeowner making contact through the hire button within the first 30 days of a worker sharing their link — establishing proof that the artifact produces real-world hiring outcomes.

## Biggest Unknowns

1. **What does a GC actually need to make contact?** Photos and trust badges may satisfy a homeowner evaluating a tiler, but a General Contractor hiring for a large site may require trade certifications, union status, or OSHA card information before they pick up the phone. We do not know yet whether the current profile content crosses the GC's decision threshold or whether there is a missing data layer that renders the page insufficient for the higher-stakes hire.

2. **Does a public profile create privacy risk for workers?** Job photos contain GPS metadata and implicitly reveal where a worker has been and when. A public, indexable page with that information attached to a person's name and phone number may create exposure workers did not intend when they logged a photo. Workers in vulnerable immigration situations may face specific risk. We need to understand this before launch — either by stripping or abstracting location data on the public page, or by making shareability opt-in in a way that workers genuinely understand.
