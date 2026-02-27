# Research Observation — Camp Planner — 2026-02-26

**Filed by:** Neuromancer (User Researcher)
**Session type:** Prototype feedback session
**Participant:** Sari Gelzer — mother of two (ages 8 and 3)
**Prototype shown:** Cardboard prototype v1 (`discover/prototype-v1.html`)
**Session length:** Not recorded
**Notes quality:** Raw / unstructured

---

## What Was Observed

Sari is a working parent managing summer programs for two children at different life stages — an 8-year-old who is actively in the camp market and a 3-year-old who is aging toward it. She currently uses Notes and Google Calendar to manage summer planning. Her session surfaced significant signal against all three of the brief's biggest unknowns, and introduced several themes not anticipated in the brief.

---

## Against the Three Biggest Unknowns

### Unknown 1 — What is the core value?

The prototype offers three candidates: deadline tracking, schedule visualization, and overbooking decision support. Sari's most emphatic moments pointed toward **none of the three as primary**. The themes she returned to most often were:

**The enrollment moment.** She described a specific, high-stress ritual around registration opening: setting alarms, making sure she's logged in, has the correct link, and knows exactly what she's signing up for — all before the moment hits. This is not deadline tracking in the passive sense (knowing a date). It is active preparation for a precise, time-sensitive action. She said she'd want the app to "click the button for her." The Decisions tab in the prototype is the closest analog, but it does not capture the preparation dimension at all.

**Social coordination.** Sari mentioned coordinating with other parents four times across different contexts: sharing the sign-up moment with a friend, making sure kids can attend programs together, aligning schedules with other moms, and sharing the overall plan. This is a primary behavior in her planning workflow, not a secondary feature. She described the ideal as being able to send a friend "the signup moment, a short description, and a button that will set them to sign up on time." We had explicitly placed social features out of scope in the brief. This observation directly challenges that decision.

**Balanced schedule building.** She described wanting a schedule that is "tuned" — balancing active camps with intellectual camps with performing arts camps, and also accounting for within-day logistics like travel time between programs. This is more sophisticated than our coverage view implies. We designed the coverage grid to answer "is this week filled?" Sari is asking "is this week *well-composed*?"

**Verdict on Unknown 1:** The core value question cannot be resolved with a single tab. The enrollment moment and social coordination are the two behaviors Sari returned to most. Neither is prominently represented in the current prototype.

---

### Unknown 2 — When does the pain peak?

Several distinct pain moments emerged:

- **The enrollment open moment** — time-compressed, high-stakes, requires advance preparation to execute successfully
- **Weekly coverage anxiety** — not just camps but any structured program; the question is whether every week has *something*
- **Budget accumulation** — tracking total spend across all programs and checking it against an overall household budget; she mentioned coordinating this with her spouse
- **Waitlist limbo** — she distinguished between waitlisting and enrolling; managing the uncertainty of waitlist positions has its own tracking complexity distinct from confirmed registrations

**Verdict on Unknown 2:** Pain is distributed across the planning cycle rather than concentrated at a single point. The enrollment open moment is the sharpest, most time-sensitive peak. Budget anxiety appears to be chronic.

---

### Unknown 3 — App or template?

Sari uses Notes and Google Calendar — both flexible, general-purpose tools. Her desire for the app to "click the button" is an explicit signal that she wants automation or at least active preparation support, not just better organization. A spreadsheet template cannot do that.

However, she also said a Google Sheet of all local camps "is a big deal for new parents." This is a direct endorsement of program discovery — a capability we placed explicitly out of scope in the brief.

**Verdict on Unknown 3:** It is a tool problem. But the tool she described is more capable than what we designed: it has social sharing, enrollment-moment preparation, program discovery, and budget tracking, in addition to deadline management and coverage visualization.

---

## Surprises That Challenge the Current Brief

### 1. Social coordination is a first-class feature, not a nice-to-have

The brief's "What We're Not Doing" section explicitly excludes "social features (sharing schedules with other parents, coordinating carpools)." Sari mentioned coordinating with other parents four times. This is not an edge case — it appears to be a core part of how she plans. Before removing it from scope again, the PM needs to decide: is this a feature we are deliberately not building (and why), or did we exclude it prematurely because we didn't know it was this important?

### 2. Program discovery matters to new parents

The brief excludes program discovery on the grounds that we are not a directory or marketplace. Sari validated this for new parents specifically: knowing what camps exist and which ones her children qualify for by age is a real need. We may be designing for the experienced parent (who already knows the camps) while new parents have a different and earlier problem. This may be a segmentation issue, not a scope issue.

### 3. Age-based qualification is a distinct need

The 3-year-old is aging into camps. Sari needs to know what programs her younger child will qualify for as they grow. This is not captured anywhere in the prototype or brief. It may be out of scope for v1, but it should be named as a deferred feature rather than ignored.

### 4. The enrollment moment is a distinct interaction, not just a deadline

We designed deadline tracking as a display problem — show the parent what's coming. Sari described it as an execution problem — she needs to be *ready* to act, not just informed that action is needed. These require different design responses. A notification is not enough; a preparation checklist or a direct link to the registration page at the right moment might be.

### 5. Budget tracking needs a spouse

Sari mentioned needing to coordinate with her spouse about budget. Budget is not a solo decision. This implies the tool may need a basic multi-user or sharing model — not just for coordinating with other parents, but within the household itself.

---

## What This Does Not Mean

- It does not mean the prototype is wrong. The three tabs produced useful reactions and confirmed that these problem dimensions are real. They just are not weighted correctly for Sari's priorities.
- It does not mean we should add all of these features before building anything. It means the brief's "Out of Scope" section needs to be revisited with this evidence in hand before we commit to a first feature.
- It does not mean Sari's profile represents all users. She is a social coordinator with two children at different stages. A parent of one child who plans independently may have a very different priority set. One session is not enough to change direction — it is enough to flag the gaps.

---

## Routed to Wintermute — Decisions Needed

1. **Revisit the social features exclusion.** Sari mentioned parent coordination four times. Before the next session, the PM should decide whether social sharing (sending a friend a registration link + deadline) is in or out of scope for v1, and why. If out, name the reason explicitly so the team can hold the line.

2. **Is program discovery in scope for a "new parent" entry point?** Sari's comment about a Google Sheet of local camps suggests we may be designing only for experienced parents. Is there a lightweight discovery layer (not a full directory) that serves new parents without bloating scope?

3. **How should we handle the enrollment moment?** The brief treats deadline tracking as an informational feature. Sari wants a preparation + execution feature. These are different. The PM and designer should decide what "helping a parent be ready to register" looks like at the lowest viable fidelity.

4. **Budget tracking — is it a feature or a view?** Sari wants to track total spend and check it against a household budget. We have a "$1,450 paid" stat in the prototype. Is that enough, or does the tool need budget-setting and spend tracking?
