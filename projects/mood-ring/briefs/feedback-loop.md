# Project Feature Brief: In-Prototype Feedback Loop

> Capture whether the core premise is landing — without breaking the experience.

**Status:** Shipped
**Owner:** Wintermute (PM)
**Last updated:** 2026-03-03
**Parent Initiative:** [Mood Ring — Strategic Initiative Brief](./strategic-initiative-brief.md)

---

## The Problem

**User:** The product team, during the Discover phase.
**Pain:** We have a deployed cardboard prototype and no signal on whether the central bet is true — that a generated color derived from four human cycles feels personal and meaningful to the person holding it. Every session shared without feedback capture is signal permanently lost.
**Evidence:** The prototype is live at GitHub Pages and being shared broadly. The core experience terminates at a poetic reading. There is no return path for the user's reaction, and no way for the team to know whether to keep building or change course.

## The Proposed Solution

A two-step feedback prompt built directly into the prototype, appearing after the reading settles. Step one: a quiet tap prompt — `yes · somewhat · no` — that answers the core research question ("did this feel like yours?"). Step two: after a choice is made, a single-line text input fades in, inviting one optional sentence. Tapping a choice locks it and reveals the input; Enter or a small `→` sends both together. The submission posts silently to Google Sheets via Google Forms, with no visible loading state or confirmation beyond the word "noted." The prompt resets cleanly on "read again."

## Why This, Why Now

We are in Discover. The core bet — that this color feels like *yours*, not just *a* color — has not been tested with a single real user. The prototype exists. The distribution channel exists. What is missing is the return loop that turns usage into evidence. Building this now costs two hours and makes every future share count. Not building it means extending the period in which we are guessing about the most important question in the project.

The infrastructure choice matters too: Google Forms routes submissions into Google Sheets, which is queryable via the Sheets API. This means the feedback data is immediately accessible to a future agent that can surface patterns across responses — color labels, reaction types, and open text — without adding a paid dependency or a custom backend.

## Out of Scope

- User accounts or persistent identity of any kind
- A reporting UI or dashboard (Google Sheets serves this at this stage)
- Forcing completion — the text input is always optional
- A/B testing different prompt phrasings
- Feedback on individual lines of the reading (aggregate signal only for now)

## Success Looks Like

1. Every hold-to-reveal session has a clear, low-friction path to submit a response without leaving the prototype or navigating to an external form.
2. Submissions arrive in Google Sheets with enough structure for programmatic analysis: `response | color_label | rgb_value | free_text` in a single parseable field.
3. The prompt does not diminish the primary experience — it appears only after the reading has fully settled, matches the prototype's visual register exactly, and disappears cleanly.

## Biggest Unknowns

1. Will users submit at all, or will the prompt be ignored? Submission rate is itself a signal — low rate may mean the experience is too personal to comment on, or that the prompt appears at the wrong moment.
2. Is "did this feel like yours?" the right question? Responses may cluster at "somewhat," making the structured choice low-signal. The open text field exists partly to compensate for this.
3. Does the open text generate qualitative insight, or mostly silence? If most submissions are choice-only with no text, we should move toward different qualitative methods (personal outreach, recorded sessions).

---

## Design Constraints

These are not negotiable — they define whether the feature belongs in this prototype or breaks it.

- The prompt appears **after** all reading lines have settled (~2.4 seconds post-completion). Never during the reveal.
- Visual register must match exactly: dark background, small uppercase labels, bottom-border text inputs, low-contrast colors. No bright CTAs, no modal overlays, no navigation changes.
- The choice confirmation should feel **observational**, not interrogatory. The selected option brightens; others dim. The tone is the ring watching you, not a form asking you.
- Submission is fire-and-forget. No loading spinner, no error state, no retry. "noted" is the only confirmation the user sees.

## Technical Constraints

- Client-side only. No backend, no build step.
- Google Forms as data sink — `no-cors` fetch to avoid CORS issues. Data lands in Google Sheets automatically.
- Structured payload for future agent use: pipe-delimited string `response | color_label | rgb_value | free_text`.
- All state resets on "read again" — choice, input value, CSS classes.
