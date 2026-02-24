# Project Feature Brief: Building Experience Validation

> Validate that the act of designing a model train layout is satisfying and intuitive before adding any feature that lets users skip or shortcut the building process.

**Status:** Draft
**Owner:** Wintermute (Product Manager)
**Last updated:** 2026-02-24
**Parent Initiative:** [`strategic-initiative-brief.md`](strategic-initiative-brief.md)

---

## The Problem

**User:** Someone drawn to the idea of building a miniature train layout — placing track, painting terrain, adding trees and houses, watching a train run the loop they designed.

**Pain:** Unknown. The building experience has not been tested with real users under real conditions. We have a working prototype, but the interactions were designed in Gemini — they were not designed from observed user behavior.

**The core assumption we're testing:** The act of building a layout from scratch is engaging and satisfying. That placing a curve piece, connecting it to a straight, watching the locomotive navigate the join — that this loop is intrinsically rewarding, not just functional.

If that assumption is wrong, no amount of visual polish or feature depth fixes it. The building mechanic is the product.

## The Deliberate Constraint: No Save/Load

Save/load is intentionally withheld during this validation phase. This is not an oversight — it is a research tool.

**Why:** Users who can save their progress will build toward a comfortable state and stay there. They will optimize around friction rather than feel it. The pain of rebuilding from scratch on every session means every friction point gets encountered again and again, at full intensity, before the user can learn to avoid it.

**What this surfaces:** The moments that feel tedious to redo reveal what is most important to make effortless. If a user rebuilds their loop three times and every time they find track rotation confusing, that confusion matters. If they sail through it, it does not.

**When this constraint ends:** When we have a clear picture of the friction points in the building loop and have addressed the ones that matter, save/load becomes the next milestone — both as a feature and as the signal that the building experience is worth preserving.

## What We're Validating

**Primary question:** Is building a layout from scratch engaging enough that a user wants to do it?

**Secondary questions:**
- Can a user successfully close a loop of track (a necessary condition for running a train) without help or instruction?
- Which track piece interactions cause confusion or repeated attempts?
- Does the user understand the rotation mechanic (R key / FAB button) without being told?
- At what point does the user place a locomotive — early (eager to see it move) or late (after the layout feels complete)?
- What is the emotional state when the train first runs a loop they built?

## Known Friction Hypotheses

These are guesses at what the building experience will expose. Each one is a testable assumption:

| Hypothesis | What it looks like | Why it might matter |
|---|---|---|
| Track rotation is invisible | Users place wrong-facing pieces and delete + retry instead of rotating | R key is keyboard-only until the FAB; not discoverable |
| Track connection has no feedback | Users can't tell if two pieces actually connect until they run the train and it stops | No visual snap indicator or connection state |
| No undo creates anxiety | Users avoid experimenting because a mistake means deleting and replacing | Permanence discourages creative placement |
| The grid is too small to build interesting layouts | Users run out of room before the layout feels complete | 20×20 at current tile size may feel cramped |
| Piece selection is friction | Switching between track types requires scanning the sidebar | Tool palette organization may not match the building mental model |
| Camera fights the placement | Users lose sight of where they are placing pieces while orbiting | Orbit and place share the same mouse/touch interaction space |

## Out of Scope

- Save/load (deliberately withheld — see above)
- New track pieces, scenery, or rolling stock
- Visual fidelity improvements
- Mobile app or distribution
- Any feature that adds to the building palette before the existing palette is validated

## Success Looks Like

1. A user with no instruction can lay a closed loop of track and run a locomotive on it within a single session
2. At least one clear friction point identified that, if removed, would make the building experience meaningfully faster or more satisfying
3. The user voluntarily tries to build a second or more complex layout after completing the first — evidence that the loop is intrinsically rewarding, not just completable

## Biggest Unknowns

1. **Is track rotation the primary confusion point, or is it track connection?** These are different problems. Rotation is a discoverability problem — the mechanic exists but users don't know about it. Connection is a feedback problem — the mechanic works but users can't tell. We need to observe which one causes more abandonment.

2. **Does the building process feel like play or like puzzle-solving?** If users approach track placement as a creative act — "I want to see what this looks like" — that is play. If they approach it as solving for a correct answer — "I need to figure out which piece goes here" — that is puzzle-solving. Play retains users; puzzle-solving frustrates them when they fail. The emotional register matters.

3. **What is the minimum viable loop that feels satisfying?** Is four straight pieces and four curves enough, or does a loop need to feel substantial to trigger the reward of running the train? This determines what the baseline interaction target should be.
