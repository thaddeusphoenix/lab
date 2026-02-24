# Project Feature Brief: Trust Engine

> Produce a verifiable trust signal on each job entry — one that a General Contractor would actually act on — by combining EXIF metadata, computer vision consistency checks, and peer validation into a composite badge.

**Status:** Draft
**Owner:** Wintermute (Product Manager)
**Last updated:** 2026-02-23
**Parent Initiative:** [`strategic-initiative-brief.md`](strategic-initiative-brief.md)

---

## The Problem

**User:** General Contractor (as the trust consumer) and Worker (as the trust beneficiary).

**Pain:** Without verification, the Workbook portfolio is a photo album. A contractor looking at it cannot distinguish a legitimate verified tradesperson from someone who aggregated construction photos from the internet. The Trust Engine is the feature that separates a reputation marketplace from a photo storage app — it is what justifies the GC paying for access and what gives the worker's portfolio actual value.

**Evidence:** The entire background check industry — Checkr, Sterling, HireRight — exists because employers will pay to reduce hiring risk when their own judgment is insufficient. The informal construction labor market has no equivalent infrastructure, which is why hiring defaults to word-of-mouth. That default isn't a preference; it's a fallback. A verifiable alternative would compete directly with it.

## The Proposed Solution

A layered trust scoring system combining three signal types, applied to every completed job entry:

**Layer 1 — Deterministic (authenticity):** EXIF GPS coordinates and timestamps are extracted from each photo in the Before → Progress → Completed sequence. Checks are binary: coordinates must be consistent across photos in the same job, timestamps must be plausible (hours apart, not seconds), and image fingerprinting must not match known stock or duplicate photos. These checks are pass/fail — the agent reasons about nothing here; either the data is there and consistent or it isn't.

**Layer 2 — AI (consistency):** Computer vision analyzes whether the Before, Progress, and Completed photos are visually consistent with the same physical space — same floor area, same walls, same general environment. This is not an assessment of craftsmanship quality; it is a continuity check. Does the sequence look like one job, or three unrelated photos?

**Layer 3 — Social (peer validation):** The Proximity Protocol (initiated by the ingestion engine) contributes a peer validation signal when a co-present, verified worker vouches for the job. This is the highest-weight signal, because it requires a human with skin in the game to affirm the work.

The output is a composite trust badge on each job entry — visible on the worker's public profile — with plain-language explanation of which signals contributed.

## Why This, Why Now

The Trust Engine is the feasibility blocker for the whole initiative. The Strategic Initiative Brief identifies it as the highest-risk question: *can AI distinguish quality in messy, real-world construction environments?* That question needs an answer before the supply side scales. Building more workers into an unverified system creates a debt — a pool of records we'll eventually have to re-score or disclaim. Testing the Trust Engine early, on a small set of real submissions, is the fastest way to learn whether the core value proposition is technically viable. It also gives the demand-side discovery something concrete to show GCs: not "we'll verify work," but "here is how we verify it — does this change how you'd hire?"

## Out of Scope

- Fine-tuning custom computer vision models — start with commodity APIs (OpenAI Vision, Google Cloud Vision)
- Assessing craftsmanship quality or skill level (is the tile work actually good?) — this is a separate, harder problem
- Dispute resolution or fraud investigation workflows for contested badges
- The GC-facing marketplace interface that surfaces trust signals to buyers

## Success Looks Like

1. **Classification accuracy:** The system correctly distinguishes authentic from fabricated test submissions ≥ 85% of the time on a seeded test set of real and synthetic job sequences
2. **GC signal validity:** At least 3 GCs, shown a trust badge and its explanation, say it would meaningfully influence their decision to contact a worker
3. **Worker false-positive rate:** Fewer than 10% of legitimate submissions from real workers are incorrectly flagged or downgraded by the system

## Biggest Unknowns

1. **Can commodity CV APIs handle real construction photo conditions?** Job site photos have variable lighting, inconsistent angles, cluttered environments, and low resolution from budget phones. Does visual consistency scoring degrade to noise in these conditions — or does it produce a reliable signal? This is testable cheaply with a batch of real photos before any system is built.

2. **What is the minimum trust signal a GC will act on?** EXIF verification alone? EXIF plus visual consistency? Or does nothing short of peer validation move the needle? We don't know the GC's evidence threshold — and different buyers (foreman vs. owner vs. HR) may have different bars entirely. This needs to be asked directly, not assumed.

3. **How do we handle legitimate submissions without EXIF?** WhatsApp strips metadata from forwarded images, and older phones may not embed GPS. A worker who sends genuine job photos through a device or flow that loses EXIF data looks fraudulent under Layer 1. Does peer validation compensate fully — or does a missing EXIF result in a permanently lower-tier badge that penalizes workers for hardware they don't control?
