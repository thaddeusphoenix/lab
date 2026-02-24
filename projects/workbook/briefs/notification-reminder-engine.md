# Project Feature Brief: Notification & Reminder Engine

> Workers and clients fall through the cracks when the platform goes silent — this is the outbound messaging system that closes those gaps.

**Status:** Draft
**Owner:** Wintermute (Product Manager)
**Last updated:** 2026-02-23
**Parent Initiative:** [`strategic-initiative-brief.md`](strategic-initiative-brief.md)

---

## The Problem

**User:** Skilled trades workers and their clients
**Pain:** The platform depends on time-sensitive actions — a client paying an invoice, a co-worker confirming a peer validation, a worker responding to a job inquiry — but none of those actions happen if the person doesn't know they're needed. Workers have no native reason to re-open a WhatsApp conversation with Workbook once they've stopped using it. Clients, especially, have no relationship with the platform at all — they receive a payment link and are expected to act on it without any follow-up.
**Evidence:** This is structural, not anecdotal. The Worker Payments, Trust Engine, Proximity Protocol, and Marketplace features all depend on outbound prompts to function. A payment that goes unpaid for seven days without a reminder is a payment that may never arrive. A peer validation request that is never sent means a verified co-worker's Trust Score never updates. The absence of this engine does not just slow the platform down — it breaks the core loops that make Workbook worth using.

## The Proposed Solution

Build a rules-based outbound messaging service that fires WhatsApp messages on platform events. The engine handles five notification types: a payment overdue reminder to the client when an invoice is unpaid after seven days; a peer validation request to a co-worker when the Proximity Protocol detects co-presence and triggers a vouching event; a badge update to the worker when their Trust Engine score changes or a peer validation arrives; a job inquiry alert to the worker when a GC or homeowner contacts them through the marketplace; and a payment received confirmation to the worker when a client pays. Each message is written to read like it came from a real person, not a system — short, direct, and in the register of the platform, not corporate software. No "Your invoice #1042 requires action." Instead: "Hey — just a reminder that Carlos still hasn't paid the $1,200 invoice from last Thursday. Want us to send him another nudge?" The engine tracks delivery status and suppresses duplicate messages. It does not attempt to be a conversation — it prompts a specific action and stops.

## Why This, Why Now

The Notification & Reminder Engine ships in Phase 2 alongside Worker Payments because Worker Payments cannot function without it. A payment link sent once, with no follow-up, has a low collection rate in any channel — in an informal labor market where cash is the default, it has a near-zero rate. The same dependency exists for Proximity Protocol: a peer validation that is never requested is a signal that never enters the Trust Engine. This feature has no user-visible surface of its own, but it is the connective tissue that makes every other feature close the loop. Building Worker Payments without this engine is building a car with no ignition.

## Out of Scope

- Inbound message parsing or response handling (owned by WhatsApp Ingestion Engine)
- User-configurable notification preferences or opt-down controls (post-MVP)
- Rich media notifications (images, PDFs) delivered via the engine (plain text only in this phase)
- Multi-channel delivery (email, SMS) — WhatsApp is the only channel
- Escalation paths if the client never pays (collections, dispute flow) — out of scope for this feature
- Real-time push delivery SLA guarantees — best-effort delivery in this phase

## Success Looks Like

1. Invoice collection rate increases measurably when overdue reminders are sent — baseline is no reminder; target is a statistically significant lift in payments within 14 days of invoice creation.
2. Peer validation requests triggered by Proximity Protocol result in a response (accept or decline) from the co-worker within 48 hours in at least 60% of cases, measured against requests sent with no follow-up.
3. Zero workers or clients report the Workbook number as spam or block it in the first 90 days of operation — tracked via WhatsApp Business API delivery failure signals and any direct inbound complaints.

## Biggest Unknowns

1. What is the optimal message timing and frequency before users block the number? WhatsApp is a personal channel. One too many reminders — or a message at 10pm — and the worker or client blocks the Workbook number permanently. We do not know whether one reminder at day 7 is right, or whether day 3 plus day 7 converts better without causing blocks. We need to test this carefully and err toward fewer messages until we have data.
2. What happens when a user blocks the number, and how do we recover? If a client blocks Workbook's WhatsApp number, we have no delivery path and no way to detect the block proactively — WhatsApp's API returns a delivery failure, but we cannot distinguish a block from a technical failure. There is no recovery path: we cannot re-engage a user who has blocked us, and we cannot reach them through an alternative channel (no email, no app). A blocked client means an unpaid invoice with no resolution mechanism. A blocked worker means they are invisible to the platform they signed up for. We need a detection strategy and a contingency — even if the contingency is a manual outreach fallback by a human operator.
