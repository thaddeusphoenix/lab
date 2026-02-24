# Project Feature Brief: Proximity Protocol

> Workers completing jobs in isolation get lower-weight trust signals; the Proximity Protocol closes that gap by surfacing co-present peers as on-the-ground vouchers — but it only works if a nearby verified user exists and agrees to respond.

**Status:** Draft
**Owner:** Wintermute (Product Manager)
**Last updated:** 2026-02-23
**Parent Initiative:** [`strategic-initiative-brief.md`](strategic-initiative-brief.md)

---

## The Problem

**User:** Two users are involved. First: the worker being validated — someone like Marco, a verified Workbook user who has submitted a completed job photo sequence and needs the highest-weight trust signal available to make his portfolio credible to a contractor. Second: the peer being asked to vouch — someone like Carlos, a verified Workbook user who was logged at the same GPS location on the same day, has no prior relationship with Workbook as a validator, and receives an unsolicited WhatsApp message asking him to confirm someone else's work.

**Pain:** Marco's Trust Engine score is built from metadata and AI — signals that are real but gameable and impersonal. A General Contractor deciding whether to hire based on a Workbook badge wants to know that a human being who was actually there can stand behind the record. Without peer validation, the highest-quality signal in the Trust Engine is missing from most job entries. Carlos's situation is also a product problem: a cold-ask from an automated system, with no established relationship and no clear incentive, is the kind of message people ignore.

**Evidence:** The entire weight of human accountability research points in the same direction — people behave differently when they know someone with direct knowledge is watching. The Trust Engine brief identifies peer validation as the highest-weight signal precisely because it is the only one that requires a real human to make an active affirmation. The problem is that acquiring that affirmation from a stranger, via WhatsApp, with no warm introduction, is a conversion problem as much as a technical one.

## The Proposed Solution

When a worker submits a Completed photo, the ingestion engine checks whether any other verified Workbook user has GPS-tagged photos from the same coordinates within the same calendar day. If a match exists, the system sends that matched user — Carlos — a WhatsApp message explaining the situation plainly: a fellow tradesperson logged photos at the same site today, and the system is asking whether Carlos can confirm he was there and saw the work. The message includes a brief, one-sentence description of Marco's trade and job type, and two reply options: "Yes, I can vouch" or "No / I didn't see the work." Carlos's response is logged as a peer validation event and fed into the Trust Engine as its highest-weight signal. Marco receives a WhatsApp notification when the vouch is confirmed, with an updated badge on his Reference Book entry. If Carlos does not respond within 48 hours, the job entry is scored without peer validation and the badge reflects the gap — but the system does not re-ping Carlos for the same job.

## Why This, Why Now

The Trust Engine brief identifies peer validation as the signal that separates a credible verification system from metadata-plus-AI alone. Without it, the best badges Workbook can issue are built entirely on technical checks a sufficiently motivated person could game. The Proximity Protocol is the mechanism that makes the social layer possible — and it is only worth building once there are enough verified workers on the platform to generate co-location matches at a meaningful rate. Phase 1 builds that supply. The Proximity Protocol is the first feature that tests whether the supply side can generate network effects: as more workers join, validation coverage improves, badge quality rises, and the value of the portfolio increases for everyone. Getting the cold-ask message right — honest, brief, low-friction, and respectful of Carlos's time — is the design problem that determines whether this feature works at all.

## Out of Scope

- Reciprocal validation tracking or any formal reputation system for validators (Carlos does not get scored or badged for vouching)
- Multi-worker validation (one vouch per job, first match wins)
- Positive framing of no-response as implicit validation — silence is not a vouch
- Any in-app or web-based validation interface — the interaction is WhatsApp-only
- Dispute resolution for contested vouches or retracted validations

## Success Looks Like

1. At least 30% of completed job entries that trigger a Proximity Protocol match result in a confirmed vouch within 48 hours, measured across the first 90 days of the feature in production.
2. Peer-validated job entries produce meaningfully higher GC engagement — measured as profile clicks or contact actions — compared to entries with no peer validation signal, validating the signal's weight in the Trust Engine.
3. The cold-ask message achieves a response rate (yes or no) of at least 50% among matched users, confirming that Carlos is reading and engaging with the request rather than ignoring it entirely.

## Biggest Unknowns

1. **Peer response rate.** Will Carlos respond at all? The message is unsolicited, the ask is a favor for a stranger, and there is no immediate benefit to Carlos. The response rate of a cold WhatsApp ask from an automated system — even a well-crafted one — is unknown. Message framing, length, timing, and the one-tap reply mechanic all affect this, and the right combination needs to be tested before the feature is built at scale.

2. **Gaming and collusion risk.** Two workers on the same crew could agree in advance to vouch for each other regardless of what was actually done. Co-location is a necessary condition for a valid vouch, but it is not sufficient — it confirms presence, not observation. The Trust Engine must treat a peer vouch as a strong signal, not an unfalsifiable one. The system needs a policy for how repeated mutual-vouching patterns are flagged or discounted, and that policy does not yet exist.

3. **The cold-start problem for the social layer.** Many skilled trade jobs — specialty subcontractors, one-person crews, first-call-on-a-new-site situations — have no other Workbook user within GPS range. In those cases, the Proximity Protocol produces no match, and the worker gets no peer validation signal through no fault of their own. If high-trust badges become a competitive differentiator in the marketplace, workers on isolated job sites are structurally disadvantaged. The product needs a clear answer for what a fair trust ceiling looks like for jobs where peer validation is structurally unavailable.
