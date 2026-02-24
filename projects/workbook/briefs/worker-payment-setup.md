# Project Feature Brief: Worker Payment Setup

> Before a worker can receive a payout through Workbook, they must connect a bank account and pass identity verification — a one-time prerequisite that determines whether the Worker Payments feature works at all for a given user.

**Status:** Draft
**Owner:** Wintermute (Product Manager)
**Last updated:** 2026-02-23
**Parent Initiative:** [`strategic-initiative-brief.md`](strategic-initiative-brief.md)

---

## The Problem

**User:** Skilled trade worker — handyman, tile setter, plumber, electrician, painter — who wants to receive payouts through Workbook's invoicing flow.

**Pain:** Worker Payments cannot disburse funds without a verified destination account. A worker can agree on scope, complete a job, and send an invoice — but if they have never completed payment setup, the money has nowhere to go. The feature is fully blocked until this one-time step is done. At the same time, the population Workbook serves has unusually high rates of being unbanked, underbanked, or undocumented. Standard identity verification processes were designed for workers with Social Security numbers, US bank accounts, and established credit history. A meaningful share of the target user base may not meet those requirements, and the current scope has no answer for them.

**Evidence:** Federal Reserve data consistently shows unbanked and underbanked rates in immigrant and lower-income households running 10–25%, well above the general population. KYC requirements under US financial regulation are not optional — any payment processor collecting and disbursing funds on behalf of workers is obligated to verify identity. Stripe Connect is the practical path for a small team, but it enforces those requirements without exception.

## The Proposed Solution

When a worker first triggers the invoicing flow — or at the point where Workbook would need to disburse funds — the bot sends a single WhatsApp message: "Before I can send you payouts, I need to connect your bank account. Tap the link to set it up: [link]." The link opens a short web-based onboarding flow hosted on a Workbook-branded page, powered by Stripe Connect. The worker provides their legal name, date of birth, last four digits of SSN (or ITIN), and bank account details. Stripe handles identity verification and bank account linking directly. On successful completion, Stripe confirms to Workbook's backend and the worker receives a WhatsApp confirmation: "You're set up. Payouts will go to your account within 2 business days of payment." From that point forward, the setup step is invisible — every subsequent invoice disburses automatically. The web view is the exception, not the experience; the worker returns to WhatsApp as soon as it is done.

## Why This, Why Now

Worker Payments is the feature that makes Workbook sticky — it turns a portfolio tool into something a worker reaches for on every job. But Worker Payments cannot function without payment setup, which makes this feature a hard dependency, not an optional enhancement. It needs to ship with or before the invoice flow. Building it now also forces the hardest strategic question early: how many workers in the target population can actually pass KYC? Answering that question — before the invoicing feature is live — determines whether the payment feature works for the majority of users or only for a subset.

## Out of Scope

- A fully WhatsApp-native identity verification flow (KYC requirements make this impractical without a web view)
- Ongoing bank account management or the ability to change payout accounts post-setup (v1 assumes a single account)
- Business entity verification or contractor company accounts
- International bank accounts or non-USD payout rails
- Building a proprietary identity verification system — Stripe Connect handles this entirely in v1

## Success Looks Like

1. **Setup completion rate:** >= 70% of workers who tap the setup link complete the full Stripe Connect onboarding in a single session
2. **KYC pass rate:** >= 60% of workers who attempt setup pass Stripe's identity verification without manual review or rejection
3. **Time-to-payout:** Workers who complete setup receive their first payout within 3 business days of invoice payment, with no manual intervention required

## Biggest Unknowns

1. **What percentage of the target user population can pass standard KYC?** Stripe Connect requires SSN or ITIN and a US bank account. Immigrant trades workers — particularly those who are undocumented or recently arrived — may not have either. If the KYC failure rate is 30% or higher, the payment feature is structurally broken for a large part of the audience we are trying to serve, and the product strategy needs to account for that before launch.

2. **What alternatives exist for workers who cannot pass standard KYC?** If a meaningful share of users are excluded by Stripe Connect's requirements, what is the fallback? Options potentially include prepaid debit card disbursement (which has looser identity requirements), a partner bank with a different KYC threshold designed for underserved populations, or a tiered verification model that allows limited payouts at lower verification levels. None of these are simple to implement, and some may require separate licensing or bank partnerships. This needs to be scoped before launch, not treated as a future problem.

3. **What will the completion rate be for a web-based flow in a WhatsApp-native product?** Every context switch out of WhatsApp creates drop-off. Workers who receive a link, open a browser, are asked for sensitive financial and identity information, and are expected to return to the conversation face multiple points of abandonment — each of which directly blocks their ability to receive payment. Whether this is a minor friction problem or a significant adoption ceiling depends on the user population and the quality of the web flow, and it cannot be assumed away.
