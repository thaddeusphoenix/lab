# Project Feature Brief: Admin & Trust Operations

> When the Trust Engine makes wrong decisions at scale, Workbook staff need tools to catch, correct, and learn from those errors before they destroy worker confidence in the platform.

**Status:** Draft
**Owner:** Wintermute (Product Manager)
**Last updated:** 2026-02-23
**Parent Initiative:** [`strategic-initiative-brief.md`](strategic-initiative-brief.md)

---

## The Problem

**Users:** Workbook staff (the trust operators) and workers (the harmed party).

**Pain:** The Trust Engine is a probabilistic system. At any meaningful scale, it will produce false positives — legitimate workers incorrectly flagged as fraudulent, valid badge applications denied, scores that do not reflect reality. For Workbook staff, there is currently no tooling to act on these failures: no queue to review flagged submissions, no interface to override a score, no way to reinstate a suspended account without direct database access. For workers, the consequence is worse: a real tradesperson who built an honest portfolio and gets incorrectly branded a fraud has no recourse. They cannot appeal. They cannot escalate. They leave the platform and they tell their network to avoid it. Unlike a wrong hire or a missed notification, an incorrect fraud flag carries a reputational charge — it is not a neutral inconvenience.

**Evidence:** The Trust Engine's own success criteria acknowledge a false-positive tolerance: the current brief targets fewer than 10% of legitimate submissions being incorrectly flagged. At 500 verified workers, that is up to 50 workers incorrectly treated as bad actors. Without a correction mechanism, each of those is a permanent error.

## The Proposed Solution

An internal admin interface giving Workbook staff a structured workflow to review Trust Engine flags, adjudicate badge disputes, override scores, and suspend or reinstate worker accounts. The interface surfaces the raw Trust Engine reasoning — which signals fired, which thresholds were crossed — so that reviewers are adjudicating with evidence, not guessing. Dispute outcomes and manual overrides are logged, and patterns in those outcomes feed back into the Trust Engine as training signal. The goal is a tight loop: the automated system flags, humans correct it where it is wrong, and the corrections make the automated system better over time.

## Why This, Why Now

Admin & Trust Operations is a post-MVP feature — the operational overhead of building and maintaining a review queue only makes sense once there are enough workers to generate flags worth triaging. In the early rollout, Workbook staff can handle exceptions manually and directly. What cannot wait until post-MVP is the architecture: the Trust Engine must be built from day one with override hooks, score mutability, and a flag state model that an admin layer can eventually act on. If the Trust Engine is shipped as a sealed black box — scores written once and never correctable, account states toggled by automated logic with no manual path — retrofitting correction capability later means rebuilding core data models under a live system. The right move is to stub the override capability at build time and defer the UI until the queue justifies it.

## Out of Scope

- Public-facing appeal flows visible to workers (the initial version is internal-only; workers contact support through WhatsApp)
- Fraud analytics dashboards or trend visualization beyond basic queue filtering
- Integration with external identity verification providers
- Automated retraining pipelines — manual pattern reports feed into Trust Engine updates, but model retraining is a separate engineering workstream
- Role-based access control beyond a basic admin vs. read-only distinction in the first version

## Success Looks Like

1. Every Trust Engine flag and badge dispute is reviewed and resolved within a defined SLA, with no flag sitting unactioned indefinitely
2. Worker false-positive rate decreases quarter-over-quarter as manual override patterns surface Trust Engine weaknesses and feed back into scoring logic
3. Workers who submit a dispute receive a clear outcome — confirmed or overturned — with a plain-language explanation, and the percentage who re-engage with the platform after a successful overturn is tracked as a retention signal

## Biggest Unknowns

1. **What is the right escalation policy when a worker is flagged?** Immediate account suspension protects against active fraud but punishes legitimate workers for the duration of review. Queuing the account for human review before any action preserves worker experience but leaves a potentially fraudulent actor active. The answer likely depends on signal severity — a single ambiguous EXIF anomaly warrants a different response than a match against a known stock photo database — but the thresholds for each tier need to be defined and tested against real flag distributions before the policy is locked.

2. **How do we prevent the dispute process from being gamed by fraudulent workers?** A clear, accessible appeals path is essential for legitimate workers. The same path is an attack surface for bad actors who learn to dispute every flag and drain reviewer bandwidth. The design needs friction mechanisms — dispute rate limiting, required supporting evidence, reviewer-visible dispute history — that deter gaming without making legitimate appeals unreasonably difficult. The right calibration is unknown until we see real dispute behavior.
