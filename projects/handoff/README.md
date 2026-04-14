# Handoff

An offline-first, voice-activated field execution tool that lets subcontractors log progress by talking, while an agent reconciles updates against the master schedule in real time — giving Site Superintendents visibility without the chase.

**Phase: Build**
**Strategic Brief:** [`briefs/strategic-initiative-brief.md`](briefs/strategic-initiative-brief.md)

---

## Problem

On hyperscale construction sites, "gaps between trades" during handoffs account for an estimated 65% of major project delays. Site Superintendents spend a disproportionate amount of their day chasing subcontractors for status updates rather than managing the site. Existing scheduling tools (Procore, Primavera, MS Project) were built for the office — not the field.

## Solution

Foremen text plain-language progress updates from their phones. An NL matching agent maps each message to the right work package in the project schedule and proposes an update. The Superintendent reviews, approves, or corrects in a web UI. Every decision trains the matcher to be more accurate over time.

---

## What's Running

### Live System (`build/`)

| File | What it does |
|---|---|
| `build/server.py` | Flask backend — NL matching, OpenProject API, Twilio webhook, rules engine |
| `build/app.html` | Superintendent web UI — match review, approve/correct, SMS queue |
| `build/match-rules.json` | Accumulated approve/correct decisions — improves matching over time |
| `build/phone-map.json` | Phone number → foreman identity mapping |
| `build/requirements.txt` | `flask`, `requests`, `twilio` |

### How to Start

```bash
# 1. OpenProject (if not already running)
cd /Users/nathanstankowski/lab/infrastructure/openproject
docker compose up -d

# 2. ngrok (new terminal) — expose Flask to Twilio
ngrok http 5001
# paste the https URL to Twilio webhook if it changed

# 3. Flask server (new terminal)
cd /Users/nathanstankowski/lab/projects/handoff/build
python3 server.py

# 4. Open the Superintendent UI
open http://localhost:5001
```

### Twilio
- **Inbound number:** +1 (833) 958-8253 — text this number as a foreman
- **Webhook:** `https://<ngrok-url>/sms` — must be updated in Twilio console if ngrok URL changes
- **Update webhook via API:**
```bash
curl -s -X POST \
  "https://api.twilio.com/2010-04-01/Accounts/${TWILIO_SID}/IncomingPhoneNumbers/${TWILIO_PHONE_SID}.json" \
  -u ${TWILIO_SID}:${TWILIO_TOKEN} \
  --data-urlencode "SmsUrl=https://<NEW-NGROK-URL>/sms"
```

### OpenProject
- **URL:** http://localhost:8080
- **Project:** Handoff — Data Center Build (ID: 3)
- **Work packages:** 125 total — 44 summary activities, 81 field-level (IDs 86–166)
- **Field-level WPs** are what foremen report against and what the matcher queries

---

## Infrastructure

```
infrastructure/openproject/
├── docker-compose.yml        # OpenProject + Postgres
├── import-schedule.py        # Bulk-created the 125 work packages
├── import-relations.py       # Created 91 predecessor relations
└── wp-id-map.json            # Activity_ID → OpenProject WP ID
```

---

## Discovery Artifacts

```
discover/
├── schedule-expanded.csv       # Full 125-activity schedule with field-level detail
├── foreman-message-samples.json # 70 realistic NL test messages across 6 categories:
│                                #   easy (20), fuzzy (20), ambiguous (10),
│                                #   multi-activity (5), pct-variation (10), no-match (5)
```

---

## Feature Briefs (ready for build loop)

```
briefs/
├── foreman-view.md              # Chat UI brief (Writer input)
├── foreman-view-scenarios.md    # Chat UI test scenarios (Tester only)
├── superintendent-view.md       # Dashboard brief (Writer input)
└── superintendent-view-scenarios.md  # Dashboard test scenarios (Tester only)
```

These briefs describe the standalone HTML prototype versions. The live system in `build/` supersedes them for the current pilot phase but they remain valid for a clean production build.

---

## What Works Today

- [x] SMS from foreman's phone → Twilio → Flask `/sms` webhook
- [x] NL matching against 81 live OpenProject work packages
- [x] Superintendent review UI — match card, confidence score, alternatives, % override
- [x] Approve → updates OpenProject (`percentageDone` + status → In Progress + comment)
- [x] Correct → logs correction, penalizes wrong match in future scoring
- [x] No-match → clarification prompt with editable text, sends back to foreman thread
- [x] Rule accumulation — `match-rules.json` grows with each decision
- [x] SMS queue polling — new texts appear in Superintendent UI within 3 seconds

## What's Next

- [ ] **Matching quality** — run the 70 sample messages, measure hit rate, tune alias tables
- [ ] **Rules inspector** — simple UI view of what's in `match-rules.json`
- [ ] **Superintendent UX** — tighten the review interaction based on pilot observations
- [ ] **Multi-foreman pilot** — map more phone numbers, test with real schedule language
- [ ] **Production build loop** — run `foreman-view` and `superintendent-view` briefs for clean HTML artifacts

---

## Four Risks Audit

| Risk | Level | Notes |
|---|---|---|
| **Value** | High | Schedule compression is directly measurable and high-stakes for GCs and owners |
| **Usability** | Medium | SMS input validated; Superintendent UI needs real user feedback |
| **Feasibility** | Medium — de-risked | Core NL matching works end-to-end; OpenProject as P6 stand-in validated |
| **Business Viability** | Unknown | Superintendent is the user; buying motion runs through GC operations leadership |
