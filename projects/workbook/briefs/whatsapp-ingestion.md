# Project Feature Brief: WhatsApp Ingestion Engine

> Skilled workers build a verified job portfolio by sending Before, Progress, and Completed photos via WhatsApp — no app, no login, no new behavior required.

**Status:** Draft
**Owner:** Wintermute (Product Manager)
**Last updated:** 2026-02-23
**Parent Initiative:** [`strategic-initiative-brief.md`](strategic-initiative-brief.md)

---

## The Problem

**User:** Skilled trade worker — tile, framing, plumbing, drywall, electrical. Predominantly immigrant. Smartphone native via WhatsApp, not app-download native.

**Pain:** A worker's reputation is trapped in word-of-mouth. When they move to a new contractor, city, or trade, their history disappears. They have no portable, verifiable record of what they've built — only references that may or may not pick up the phone. They do skilled work every day and accumulate no durable proof of it.

**Evidence:** The industry hires on referral and foreman relationships because no alternative infrastructure exists. General Contractors bear the same information gap from the other side — they hire largely blind. This isn't a niche edge case; it is how the entire informal and semi-formal labor market in construction operates.

## The Proposed Solution

A WhatsApp-based ingestion engine that turns daily job site behavior into a verified portfolio. A worker's phone number is their account — no registration form, no password. They send a photo; the bot asks if it's a Before, Progress, or Completed shot. That's the entire interaction. Behind the scenes: EXIF metadata (GPS coordinates, timestamp) is extracted silently to anchor each photo to a real time and place. When a Completed photo arrives, the bot bundles the sequence into a job entry and adds it to the worker's Reference Book. If another verified Workbook user was logged at the same GPS coordinates on the same day, the bot initiates a peer validation request via the Proximity Protocol. The worker can say "my workbook" at any time to see their portfolio summary and generate a shareable public profile link.

## Why This, Why Now

This is the supply-side foundation. Without workers accumulating verified records, there is no marketplace to sell to contractors. The WhatsApp channel is the only acquisition path that doesn't require workers to change their behavior — they already have the app, they already share job site photos in group chats, and they already trust the medium. Every other onboarding model (native app, web form, SMS) introduces friction that kills conversion in this population before the value is established. This feature has to exist — and work — before any other part of Workbook can be validated.

## Out of Scope

- The GC-facing marketplace and hiring interface
- AI visual quality scoring (the Trust Engine — separate feature)
- Multi-language support (English-first)
- Web or native app interfaces
- Payments, monetization, or premium tiers

## Success Looks Like

1. **Core loop completion:** ≥ 60% of workers who onboard (complete name + trade) submit at least one full Before → Progress → Completed sequence within 7 days
2. **Week-2 return rate:** ≥ 30% of workers who complete their first job submit photos from a second job within 14 days
3. **Onboarding completion:** ≥ 70% of workers who send a first message complete the name and trade flow

## Biggest Unknowns

1. **Does the tagging UX work in the real world?** The flow assumes workers can reliably self-tag photos as Before, Progress, or Completed. In the prototype this works cleanly with quick reply buttons — but quick replies behave differently across WhatsApp clients and devices. Can workers in the field, in variable conditions, tag correctly and consistently without confusion or friction?

2. **What sustains the behavior after the first job?** The value to the worker — new job opportunities, contractor access — is deferred by weeks or months. The cost — sending and tagging photos — is daily. What is the immediate reward loop strong enough to keep a worker submitting on job two, job five, job ten? The peer validation badge is a candidate, but its motivating power is unvalidated.
