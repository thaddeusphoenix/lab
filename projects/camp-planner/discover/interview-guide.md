# User Interview Guide: Camp Planner

**Prepared by:** Neuromancer (User Researcher)
**Project:** Camp Planner
**Created:** 2026-02-25
**Status:** Draft

---

## Purpose

These interviews are designed to answer the three biggest unknowns from the Strategic Initiative Brief before any feature decisions are made:

1. **What is the core value?** Which part of the problem — deadline tracking, schedule visualization, or overbooking decision support — causes the most pain and would deliver the most relief?
2. **When does the pain peak?** At what moment in the planning cycle does a parent feel overwhelmed enough to reach for a new tool?
3. **App or template?** Is this a tool problem or a template problem? What would make a parent adopt something new instead of just improving their existing setup?

Each section below maps to one or more of these unknowns. The goal is to listen for behavior, not preferences — what parents *did*, what broke down, and what it cost them.

---

## Participant Screener

Interview people who meet **all** of the following:

- Has at least one child between ages 5 and 14
- At least one parent in the household works full-time, or the family depends on structured programs for summer childcare coverage
- Has gone through at least **one full summer** of program planning (not a first-timer — we need people who've experienced the friction, not anticipated it)
- Enrolled their child in **two or more separate programs** last summer (we need participants managing complexity, not a single all-summer camp)

**Prioritize participants who also:**

- Have registered for more programs than they ultimately attended (overbooker behavior)
- Have missed a deadline, paid a cancellation fee they didn't expect, or had a gap week catch them off guard

**Interview size:** 5–8 participants is sufficient to identify recurring patterns. Stop sooner if the same themes emerge consistently.

---

## Interview Structure

| Section | Topic | Time |
|---|---|---|
| 1 | Background and context | 5 min |
| 2 | Walk me through last summer | 10 min |
| 3 | Where it broke down | 10 min |
| 4 | What matters most | 10 min |
| 5 | Tools and adoption | 10 min |
| 6 | Wrap-up | 5 min |

**Total:** ~50 minutes. Do not rush Section 3 — that is where the real product signal lives.

---

## Intro Script

> "Thanks for making time. We're exploring a problem a lot of parents describe — managing the logistics of summer planning for kids. I'm not going to show you anything we've built. I'm here to understand how *you* do it today and where it gets hard. There are no right answers. The most useful thing you can do is be honest about what's actually going on, including the messy parts.
>
> I may take notes or ask if I can record — just for my own reference, not shared publicly. Any questions before we start?"

---

## Section 1: Background and Context

*Goal: Establish the participant's household situation and level of experience with summer planning. Set up the rest of the interview.*

1. Tell me about your family — how many kids do you have and what are their ages?
2. What does your work situation look like during the summer? Are both parents working? Do you have any flexibility in your schedule?
3. How many summers have you been navigating this kind of planning? Was there a year it first felt hard to manage?

**Facilitator note:** You're listening for: number of children (especially multiple kids with different needs), employment situation (does coverage actually matter, or is someone home?), and experience level (first-timer vs. veteran who has developed workarounds).

---

## Section 2: Walk Me Through Last Summer

*Goal: Understand the actual planning workflow — what they did, when, and with what tools. Maps to Unknown 2 (when does pain peak) and Unknown 3 (app vs. template).*

4. Walk me through how you planned last summer, starting from the very beginning. Where did it start, and when?
5. What tools or systems did you use to track everything? Can you describe what that looked like — or if you still have it, show me?
6. How did you keep track of which weeks were covered versus still open?
7. Who else was involved in the planning? Did you manage it alone, or did your partner participate? How did you coordinate?
8. When did you feel like the plan was "done"? Or did it stay in flux until summer actually started?

**Facilitator note:** Ask to see their actual spreadsheet, doc, or calendar setup if they're willing. Real artifacts reveal more than descriptions. Pay attention to how they talk about *weeks* vs. *programs* — that distinction matters.

---

## Section 3: Where It Broke Down

*Goal: Find the specific failures, near-misses, and costs. This is the most important section. Maps to Unknown 1 (core value) — whatever caused the most pain is the feature that matters most.*

9. What was the hardest part of managing it all last summer?
10. Tell me about a time something went wrong — a deadline you missed, a program that filled before you registered, a cancellation fee you didn't expect. What happened?
11. How did you track registration deadlines and cancellation windows for each program? Walk me through what that actually looked like.
12. Have you ever registered for more programs than you planned to use — kind of as a hedge — and then had to decide which ones to cancel? How did you manage that?
13. Was there ever a week where you realized too late that your child had no program? What did you do?
14. What did any of these problems actually cost you — in money, time, or stress?

**Facilitator note:** If they say "it was fine" or "I'm pretty organized," probe: *"Was there a moment, even a small one, where you had to scramble or double-check something that almost slipped?"* Almost everyone has one. Listen for: financial losses (missed cancellation windows), time costs (scrambling for backup), and stress costs (anxiety about gaps or deadlines).

---

## Section 4: What Matters Most

*Goal: Understand priorities without asking leading questions about our features. Maps directly to Unknown 1 (core value).*

15. If you could only fix one thing about how you manage summer planning, what would it be?
16. What does it feel like at the end of planning season when everything is sorted? When did you last feel that way?
17. What does it feel like when something goes wrong with the plan? Can you give me an example from your own experience?
18. On a scale from 1 to 10, how confident are you going into each summer that you haven't missed anything important? What would it take to feel like a 10?
19. When you imagine a version of this process that just *works* — what's different from today?

**Facilitator note:** Question 15 is the most important question in this section. Listen carefully: if they say "knowing all the deadlines in one place," that's deadline tracking. If they say "seeing what weeks are still open," that's schedule visualization. If they say "being able to decide which programs to drop," that's overbooking decision support. Tally across participants — the modal answer shapes what we build first.

---

## Section 5: Tools and Adoption

*Goal: Understand what they've already tried, why it worked or failed, and what would make them adopt something new. Maps to Unknown 3 (app vs. template).*

20. Have you ever tried using a new tool or a different system to manage this better — an app, a template, anything?
    - *If yes:* What made you try it? What made you keep using it or abandon it?
    - *If no:* Why not? What would need to be true for you to try something new?
21. What devices do you use when you're doing summer planning? Is this something you do on your phone, your laptop, both?
22. Do you plan in big focused sessions, or in small moments throughout the day when you have a few minutes?
23. If someone built a tool specifically for managing summer programs — tracking deadlines, showing you which weeks are covered, helping you decide what to cancel — where would your skepticism come from? What would make you not trust it or not use it?
24. What would it take for you to actually make the switch from whatever you're doing now?

**Facilitator note:** Question 23 is a useful inversion. Instead of asking "would you want this," ask where the doubt would come from. Responses like "I'd need to trust it won't lose my data" or "I'd need to see that it actually saves time" reveal adoption barriers more honestly than direct preference questions.

---

## Section 6: Wrap-Up

*Goal: Surface anything the interview structure missed. Capture the language participants use naturally — it feeds directly into messaging.*

25. Is there anything about how you manage this that surprised you when you first figured it out — something that isn't obvious until you've been through it?
26. If you were going to complain about summer planning to another parent, what would you say?
27. Is there anything I didn't ask about that feels like an important part of this?

**Facilitator note:** Question 26 is often the most useful question in the entire interview. The way someone complains is how they'd describe the product's value to a friend. Write down the exact words they use.

---

## After Each Interview

Immediately after each session (within 30 minutes), capture:

- **The one failure that mattered most** — the breakdown that cost them something real
- **The one thing they would fix first** — their exact words from question 15
- **The complaint** — their exact words from question 26
- **Any surprises** — anything that contradicts the current persona or brief

File each observation as a report in `reports/` and tag which unknown it addresses. After 5+ interviews, look for the pattern across answers to question 15 — that pattern tells us what to build first.
