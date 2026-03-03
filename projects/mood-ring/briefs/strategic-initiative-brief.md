# Strategic Initiative Brief: Mood Ring

> A piece of digital jewelry — a generative color object that reflects where you are in four overlapping human cycles, rendered as a wearable artifact for your profile or phone.

**Status:** Draft
**Owner:** Wintermute (Product Manager)
**Last updated:** 2026-03-02
**Related Feature Briefs:** _(none yet)_

---

## The Opportunity

Every human is simultaneously moving through multiple cycles — the arc of a life, the rhythm of a year, the turn of the moon, the passage of a day. None of these are felt consciously most of the time. A mood ring is a cultural object people have understood for fifty years: it tells you something about your inner state through color. This project reframes that object. Instead of skin temperature, the color reflects your position in four objective, universal cycles. The result is not a measurement tool — it is a mirror. A quiet reminder that you are located somewhere in time, in ways that most people never visualize.

The surface this lives on is already crowded with utility — calendars, notifications, metrics. There is very little digital art that is personal, always current, and derived from something true about the person displaying it. That is the gap.

## Why Now

- Generative and personalized digital art is a recognized aesthetic category — people understand what it means for a visual to be "yours" in a way that is computed, not chosen
- Profile customization and status expression (avatars, status indicators, wallpapers) are mature, understood behaviors on every platform
- The inputs are minimal — age and location — which means the barrier to a working prototype is almost nothing
- Browser APIs for geolocation, time, and canvas rendering make a single-file implementation viable today

## Why Us

- The concept requires no backend, no accounts, no infrastructure — this is a pure computation from inputs to color output, which compresses the prototype cycle to hours
- The four-cycle model is a defined, coherent artistic idea — not a vague "generative art" brief. That specificity makes design decisions easier to evaluate
- A working prototype is the fastest way to know if the thing is beautiful, and beauty is the only thing that matters here

## What We're Building

A generative color object — the Mood Ring — that takes three inputs (age, current time, current location) and produces a visual: a blended or patterned composition of four colors, one per cycle. The four cycles are:

1. **Life arc** — position from birth to a statistically average death for someone of the entered age
2. **Moon phase** — current lunar phase based on date and location
3. **Solar season** — position in the annual solar cycle (solstices and equinoxes) based on date and location
4. **Circadian** — position in the 24-hour solar day based on local time and location (sunrise/sunset as anchors)

Each cycle maps to a color at a given moment. The four colors compose a single visual — unified blend, stripes, or fractal-style blending are all candidates for the rendering mode. The artifact is sized and shaped to live as a profile status icon or a phone wallpaper. It updates in real time.

## What We're Not Doing

- **No mood input from the user** — the name is metaphorical. The ring derives from external cycles, not self-reported emotional state. No journaling, no check-ins, no mood tracking.
- **No social features** — no sharing flows, no feeds, no follows. If the object ends up somewhere public (a profile), it got there because the user put it there through existing platform affordances.
- **No additional cycles or customization** — four cycles, defined. No user-configurable cycle selection in v1.
- **No animation or motion** — the object is a still image that updates. It is not a screensaver or a looping animation.
- **No backend or accounts** — all computation is client-side. Nothing is stored or transmitted.

## Success Looks Like

| Metric | Target | Timeframe |
|---|---|---|
| The object is visually compelling enough to want on your phone | Qualitative — at least 3 of 5 people shown it say they'd use it as a wallpaper | First prototype test |
| The four-cycle concept is legible without explanation | Users can describe what each color represents after a brief onboarding | Usability test |
| Personal resonance | Users describe the object as feeling "theirs" — distinct, meaningful, not arbitrary | Qualitative interviews |

## Biggest Unknowns

1. **Does the concept need to be explained, or can the visual carry it?** The four-cycle model is intellectually interesting but not immediately obvious from the color alone. If every user needs a paragraph of context to appreciate the object, the art isn't working. The prototype needs to test whether the visual is compelling first, explanation second — or whether explanation is load-bearing.

2. **What rendering style makes it feel like jewelry rather than a data visualization?** Unified blend, stripes, and fractal blending produce very different aesthetics. A unified blend risks feeling arbitrary. Stripes risk feeling like a chart. Fractal blending risks feeling busy. The right choice determines whether this reads as art or as a status widget. This is the most important design question and needs to be answered with prototypes, not debate.

3. **Does the life-arc cycle feel meaningful or morbid?** Including a color that represents "how far through your life you are" is either quietly profound or quietly unsettling, depending on the person. This is a tone question as much as a design question — and it may be the thing that makes the object interesting rather than the thing that makes people decline to display it.
