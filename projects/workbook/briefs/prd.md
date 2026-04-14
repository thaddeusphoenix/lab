# AI Product Requirements Document: Workbook

> A text-message interface for trades workers — agree on job scope, send a text invoice, track what you're owed. Worker texts a phone number; a thin AI server understands the intent and responds with structured output.

**Status:** Draft
**Owner:** Wintermute (Product Manager)
**Last updated:** 2026-03-03
**Related Feature Briefs:** [Scope and Invoice](./scope-and-invoice.md)

---

## 1. Strategic Context

### Problem Statement

_Skilled trades workers start jobs on a handshake and invoice on an informal text. When a client goes quiet, the worker has nothing to point to — no written agreement, no formal invoice, no paper trail._

**User:** Skilled trade workers — handymen, tile setters, plumbers, painters, electricians — who work informally, often without a bank account, email address, or registered business entity.
**Pain:** The only existing invoicing tools (Stripe, QuickBooks, Wave) assume infrastructure the worker doesn't have. The worker already has a phone. The client is already in their contacts. The thread already exists — it just needs better structure.
**Evidence:** Workers already send informal job confirmations and payment requests via WhatsApp. The behavior exists. The tool structures it.
**Current workaround:** "hey can you pay me?" — an informal text with no attached scope, amount, or record.

### User Personas

| Persona | Behaviors | Motivations | Job to be Done |
|---|---|---|---|
| The informal worker | Books jobs verbally or via WhatsApp; invoices casually at job end | Get paid on time; protect themselves from disputes | Send a message that looks professional enough that clients take it seriously |
| The repeat contractor | Has regular clients; tracks multiple open jobs at once | Reduce cognitive load on unpaid jobs | Know what they're owed without having to mentally track every open job |
| The cautious worker | Has been stiffed before; wants a paper trail | Evidence if a dispute escalates | Have something to point to when a client disputes a scope or amount |

### Strategic Objectives

| Objective | Target | Timeframe |
|---|---|---|
| Scope agreement adoption | 20 workers use the scope agreement on at least one real job | 30 days post-launch |
| Invoice adoption | 20 workers send a text invoice on at least one job | 30 days post-launch |
| Second-job return rate | ≥50% of first-job users log a second job | 60 days post-launch |

---

## 2. Data Specifications

### Data Ingredient List

| Data Source | Type | Volume / Window | Owner |
|---|---|---|---|
| Inbound SMS/WhatsApp messages | Unstructured text — worker intents | Per-message, real-time | SMS provider (Twilio) |
| Job records | Structured — scope, fee, status, client name | Current + 90 days active jobs | Worker device (localStorage) |
| Worker session context | Minimal — current active job state | Active session only | Server in-memory (stateless between messages) |

### Quality Thresholds

| Metric | Threshold | Consequence if Unmet |
|---|---|---|
| **SMS delivery rate** | ≥98% messages delivered within 5s | Worker sends a message, hears nothing — product feels broken |
| **Intent classification accuracy** | ≥92% correct intent on golden dataset | Worker's message is misunderstood; wrong action taken; trust erodes |
| **Response completeness** | 100% of classified intents produce a structured response | Silent failures are unacceptable — always respond, even if "I didn't understand that" |

### Data Supply Chain

- **Inbound messages:** Twilio webhook → AI server → intent classification → structured response
- **Job data:** Stored locally on worker device only. Server does not retain job records between messages. Session context reconstructed from client state on each message.
- **Failure mode:** If Twilio fails to deliver, the message is lost — no retry mechanism in v1. If AI classification fails, the system responds with a help message rather than silently dropping the message.

---

## 3. Reasoning Architecture

### Decision Logic

```
Inbound SMS from worker
        ↓
Intent classification (LLM)
        ↓
 ┌──────────────────────────────────────────────────┐
 │  new_job        → prompt for client + scope      │
 │  scope_confirm  → format scope agreement text    │
 │  invoice        → format invoice message         │
 │  mark_paid      → mark job paid, confirm         │
 │  status_check   → list open jobs + amounts owed  │
 │  help           → show command guide             │
 │  unknown        → request clarification          │
 └──────────────────────────────────────────────────┘
        ↓
Format structured response
        ↓
Reply via SMS to worker
```

### Authority Boundaries

| Capability | Disposition |
|---|---|
| Parse and classify worker intent | Must execute autonomously |
| Generate scope agreement text from worker-provided details | Must execute autonomously |
| Format invoice message with line items, total, and payment note | Must execute autonomously |
| Suggest a fee amount based on scope type | May suggest only — worker always confirms |
| Contact the client directly | Prohibited — the worker sends all client-facing messages |
| Store or transmit job data to any server | Prohibited — job data stays on worker device |
| Take any financial action (payment request links, bank transfers) | Prohibited in v1 |

### Memory & State

- **Session context:** The current active job (client name, scope, agreed fee, status). Reconstructed from client-side state passed with each message — the server is stateless between messages.
- **Lookback:** 90 days of job history available for status_check queries.
- **Session timeout:** No session concept in SMS — every message is a fresh request. Context is always supplied by the client.

---

## 4. Functional Requirements

### User Stories

> **Note:** These are product-level stories for alignment. Detailed build-loop acceptance scenarios live in a separate `[feature]-scenarios.md` file.

| # | Given | When | Then |
|---|---|---|---|
| 1 | A worker has agreed verbally to do a job | They text the Workbook number with the client name and what they're doing | The system creates a new job and responds with a formatted scope agreement the worker can forward to the client |
| 2 | The worker has sent a scope agreement and the client replied "yes" | The worker texts "confirmed" to Workbook | The job status updates to scope-confirmed; system acknowledges |
| 3 | The job is complete | The worker texts "invoice [client name]" | The system responds with a formatted invoice message (scope, amount, payment note) the worker forwards directly to the client |
| 4 | The client pays | The worker texts "paid [client name]" | The job is marked paid; system confirms and shows outstanding balance |
| 5 | The worker wants to know what they're owed | They text "what do I have open?" | The system lists open jobs with amounts and days outstanding |
| 6 | The worker is confused about how to use the product | They text "help" | The system responds with a plain-language guide to available commands |

### Interaction States

| State | Trigger | User-visible behavior |
|---|---|---|
| Onboarding | First message to the number | Enrollment message: confirms number is active, shows first command to try |
| Active job | new_job classified | System prompts for any missing details (client name, scope, fee) one field at a time |
| Awaiting client confirmation | scope_confirm sent | Job in "pending" state; system confirms it will wait |
| Invoiced | invoice command | System sends invoice text; job moves to "invoiced" status |
| Paid | mark_paid command | Job closes; outstanding balance updates |
| Error / unknown | Unrecognized intent | System sends: "I didn't catch that. Text HELP for a list of commands." |

### Out of Scope

- No photos, portfolio building, or proof-of-work documentation
- No persistent server-side storage of worker data
- No account creation or third-party service registration
- No automated outbound reminders or scheduled messaging
- No payment processing, payment links, or bank account integration
- No marketplace or hiring features

---

## 5. Evaluation & Performance Standards

### Golden Dataset

_A curated set of 150+ real and synthetic worker SMS messages covering the full range of intents, phrasing styles, spelling variations, and code-switching (English/Spanish). Validated by domain review before launch._

**Size:** 150 messages minimum (25+ per intent class)
**Owner:** Product Manager + Tech Lead
**Validation method:** Hand-labeled by PM, cross-checked by a second reviewer. Minimum 92% classification agreement required.

### Scored Metrics

| Metric | Target | Minimum to Ship |
|---|---|---|
| Intent classification accuracy (golden dataset) | 95% | 92% |
| Response format correctness | 100% (scope/invoice output must be parseable and forwarding-ready) | 100% |
| Unknown-intent catch rate | <8% of valid commands misclassified as unknown | <10% |

### Baseline at Launch

Intent classification must reach 92% on the golden dataset before the product is shared with real workers. Below this threshold, workers will experience misunderstood messages often enough to abandon the product.

---

## 6. Non-Functional Requirements & Guardrails

### Latency Targets

| Operation | Target | Worst-case bound |
|---|---|---|
| SMS response (worker texts → receives reply) | <5s | <10s |
| Intent classification (LLM inference) | <2s | <4s |
| Job status query | <1s | <2s |

### The Escape Hatch

Every interaction must have a clear path out:
- `HELP` always works, regardless of session state. Always responds with the command guide.
- `STOP` unsubscribes the worker immediately (required by SMS compliance law).
- Unknown intents never drop silently — always respond with a clarification prompt.
- The system never takes an irreversible action (like marking a job paid) without explicit confirmation from the worker.

### Privacy & Bias Boundaries

- **No job data is stored server-side.** The AI server processes messages and responds. It does not retain records between calls.
- Worker phone numbers are the only persistent identifier. No name, location, or financial data is stored server-side.
- The AI must never infer or assume a fee amount and present it as confirmed — fee is always worker-entered or worker-confirmed.
- SMS compliance: STOP/HELP/CANCEL keywords must be handled per TCPA requirements.

---

## 7. Lifecycle & Maintenance

### Degradation Thresholds

| Signal | Rollback trigger |
|---|---|
| Intent classification accuracy drops below 88% on weekly spot-check | Pause new user onboarding; investigate model or prompt drift |
| SMS delivery failure rate exceeds 2% | Alert + switch SMS provider if sustained |
| Worker error/unknown response rate exceeds 15% | Review recent messages for new phrasing patterns; update golden dataset and prompt |

### Monitoring Cadence

| Signal | Cadence | Alert threshold |
|---|---|---|
| Intent classification accuracy (spot-check sample) | Weekly | <92% → address before next week |
| Worker error message rate | Daily (first 30 days), weekly after | >15% of responses are clarification prompts |
| Job completion rate (invoiced → paid) | Weekly | Tracked as business metric, not technical alert |

### Ownership Model

| Phase | Owner |
|---|---|
| Building | Tech Lead |
| Deploying | Delivery Manager |
| Monitoring | Tech Lead (classification accuracy) + PM (business metrics) |
| Retiring | Product Manager |

---

## Biggest Unknowns

1. **Does a formal text invoice change client payment behavior?** The hypothesis is that a structured, professional-looking invoice creates a social obligation that "hey can you pay me?" does not. This is the core assumption — needs testing on real jobs with real clients.
2. **Will workers install even a zero-friction PWA?** Saving a web page to a home screen is not downloading an app, but it is still a new behavior. The product needs to work completely from SMS before requiring any app installation.
3. **Does a written scope agreement prevent disputes, or just document them?** A written "yes" from the client may not change the outcome of a dispute — but it may change whether workers feel more protected and whether clients honor their commitments.
