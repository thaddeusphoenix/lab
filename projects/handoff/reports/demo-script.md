# Handoff — Demo Script
**Audience:** Product Manager
**Duration:** 3 minutes

---

## Before You Start

- Flask server running: `python3 server.py` (in `build/`)
- ngrok tunnel active, Twilio webhook pointed at it
- Superintendent UI open at `http://localhost:5001`
- Your phone ready to text **+1 (833) 958-8253**

---

## 1. What This Is (60 sec)

> "This is a working prototype I built to test a specific hypothesis about field execution on hyperscale data center sites. Not a mockup — it's a live system end to end."

**Tools and techniques:**

> "The stack is deliberately minimal. Twilio handles SMS inbound — foremen text a number, no app required. A Flask server calls Claude via the Anthropic API — the foreman's message, the full work package list, and a log of past decisions go in as a single prompt. Claude returns the best-matching activity, a confidence score, and an extracted completion percentage. OpenProject is standing in for Primavera P6 and gets updated in real time. The whole thing is about 600 lines of Python and one HTML file."

> "The interesting part isn't the stack — it's the learning loop. Every decision the Superintendent makes gets logged and fed back into the next Claude prompt as a few-shot example. The model starts with general construction vocabulary and learns this site's specific language over time."

---

## 2. Workflow Walkthrough (75 sec)

Text **+1 (833) 958-8253**:
> "north side electrical rough-in is about 80 percent done"

While it processes:
> "Foreman sends a text. That's it. No login, no app, no form."

When the card appears in the UI:
> "Claude matched it to the right work package and extracted 80% from plain language. It's queued for the Superintendent."

Click the amber pill to expand:
> "Raw message, proposed percentage, confidence score. One tap to approve — OpenProject updates immediately."

Now show a wrong match or send a second message, then click Reassign:
> "When Claude gets it wrong, the Superintendent corrects it. That correction goes back into the prompt. The system earns accuracy through use."

Point to a gray card:
> "Gray means no update received. On a real site, that's the Superintendent's first conversation of the morning — not data entry."

---

## 3. Discovery Potential (45 sec)

> "What I find interesting about this as a discovery tool is what you'd learn from running it on a real site for two weeks."

- **Matching accuracy** — we have 70 test messages ready to evaluate. That baseline tells you whether the model is good enough to trust without the Superintendent reviewing every single card.
- **Message patterns** — the corpus of foreman texts is itself a dataset. What language do crews actually use? What's ambiguous? That shapes both the product and the training data.
- **Superintendent behavior** — how often do they override versus approve? Where do they correct? That's a signal about where the model needs work and where the Superintendent's expertise is hardest to encode.

> "The hypothesis this prototype is testing: can you replace the morning phone tree with a two-minute review? The data to answer that is available the day you go live."
