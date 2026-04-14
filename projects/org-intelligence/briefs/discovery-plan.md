# 30-Day Discovery Plan: CivilGrid Intelligence Architecture

**Goal:** Transform the white paper from a vision document into a specific, actionable implementation plan grounded in CivilGrid's actual operations, tools, signal sources, and team.

**Access:** Full business access — all teams, systems, data, and tools.

**Final deliverable:** A revised architecture document with a specific substrate taxonomy, intelligence layer spec, role mapping with named candidates, and a phased implementation plan with milestones and owners.

---

## What We're Trying to Learn

The white paper has three open questions. Everything in this plan traces back to answering them.

| Unknown | Why it matters | How we answer it |
|---|---|---|
| **Where is the honest signal?** | The intelligence layer is only as good as the signal feeding it. If it's in five disconnected tools, we have a consolidation problem before we have an architecture problem. | Tool inventory + data team interview + analytics access |
| **What is the minimum viable world model?** | If it's too thin, the AI can't surface useful context. If it's too thick, the team won't maintain it and it decays into a wiki nobody reads. | Documentation audit + shadowing what people actually reference day-to-day |
| **Will the team run toward this or away from it?** | An architecturally perfect model that nobody adopts is a failure. Cultural readiness shapes the rollout sequence, not just the change management messaging. | Team interviews + observe actual work patterns + understand org structure |

---

## Week 1: Orient + Map the Current State

**Goal:** Understand the tools, structure, and information flows before any interpretation.

### Day 1–2: Orientation + Tool Inventory

**Activities:**
- Kickoff meeting with CTO and Head of Product: what do they most want to change, and what do they most want to preserve
- Full tool inventory: every SaaS product the company pays for, what it's used for, who uses it, and whether it has an API or export capability
- Request access to: product analytics dashboard, support ticket system, CS account notes, sales CRM, engineering project management, internal documentation

**Outputs:**
- `tool-inventory.md` — complete list of tools, owners, and data they hold
- Initial hypothesis on where the honest signal lives

**Key questions:**
- What analytics tool tracks in-product behavior? Is layer activation data in there?
- Where do support tickets live? Are they tagged/categorized?
- Where does CS write account notes? Is it searchable?
- Where does institutional knowledge currently live? (Notion? Confluence? Google Docs? Slack?)
- Is there an existing engineering documentation practice? (ADRs? RFCs? Anything?)

---

### Day 3–4: Leadership Interviews

Five interviews, 45 minutes each. One open question per interview: "Walk me through the last time a decision in your area was slower than it should have been. What information were you waiting for, and where was it?"

| Interview | Focus |
|---|---|
| **CEO** | Strategic context, what "throughput" means specifically, what they're afraid of changing |
| **CTO** | Engineering cycle time, where information slows, current documentation practice, tech debt in the org model |
| **Head of Product** | How signal reaches roadmap decisions, what doesn't reach decisions, how long from "customer need identified" to "feature spec" |
| **Head of Data** | How dataset coverage decisions are made, how demand signals are currently tracked, how engineering learns about coverage changes |
| **Head of CS** | What customer feedback never reaches product, what patterns they see that nobody else sees, how they currently communicate signal upstream |

**Output:**
- `leadership-interviews.md` — key quotes and themes, not summaries
- Identified friction points: the five highest-cost coordination patterns currently in the company

---

### Day 5: Signal Audit Workshop

Two-hour working session with Head of Product + Head of Data + one senior engineer.

**Goal:** Map every meaningful signal the business generates — behavioral, operational, and customer — and track it to where it currently lives and who has access.

**Workshop output (draft `signal-map.md`):**
```
Signal                          | Source         | Tool           | Accessible to  | Freshness
Layer activation patterns       | Product        | [tool]         | [who]          | [lag]
Coming Soon click volume        | Product        | [tool]         | [who]          | [lag]
Project location data           | Product        | [tool]         | [who]          | [lag]
Session return depth            | Product        | [tool]         | [who]          | [lag]
Support ticket patterns         | CS/Support     | [tool]         | [who]          | [lag]
Account health signals          | CS             | [tool]         | [who]          | [lag]
Sales pipeline data             | Sales          | [tool]         | [who]          | [lag]
Dataset coverage requests       | Data           | [tool]         | [who]          | [lag]
```

**Decision criteria:** If more than half the signal is siloed in tools with no API or export, the first phase of the implementation plan is a consolidation sprint before anything else.

---

## Week 2: Deep Dives by Function

**Goal:** Understand how work actually flows — not how it's supposed to flow.

### Engineering (Days 6–8)

**Activities:**
- Observe one full engineering standup/sync — don't participate, just watch what information gets shared and what questions get asked
- Interview three engineers (IC level): what context do you wish you had before starting a ticket? what do you spend time reconstructing that should already be documented?
- Review the last 10 engineering decisions — where was the decision recorded? who was in the room? how long did it take from "question raised" to "decision made"?
- Audit current engineering documentation: what exists, where, how current

**Key questions:**
- What is the current average time from ticket created to ticket shipped?
- What percentage of engineering time goes to coordination (meetings, Slack, waiting for answers) vs. building?
- What's the single most expensive recurring coordination pattern? (e.g., "explaining product context to engineers before they start a feature")
- Does the team write ADRs? RFCs? Anything that captures reasoning, not just decisions?

**Output:** `engineering-baseline.md` — current cycle time, coordination overhead estimate, documentation state

---

### Product (Days 8–9)

**Activities:**
- Review the current roadmap document — format, location, who maintains it, how often it changes
- Trace one recent feature from "idea" to "spec": how many meetings, how many people, how long
- Interview the PM: where does signal get lost between customer behavior and roadmap decision?

**Key questions:**
- How does a Coming Soon click currently reach a roadmap prioritization meeting? (How many hops? How much lag?)
- What product decisions in the last 6 months were made on gut vs. data? Why?
- What is the PM function's current biggest time sink?

**Output:** `product-signal-flow.md` — the current path from signal to decision, with lag measured at each step

---

### Data Team (Day 9)

**Activities:**
- Understand the coverage matrix: how it's maintained, where it lives, who can edit it, how engineering learns about changes
- Understand how new dataset requests are triaged — is there a formal queue? informal? driven by CS?
- Assess whether Coming Soon clicks are being reviewed at all, and by whom

**Key questions:**
- When a new state goes live, what is the notification chain? How does CS find out? How does engineering find out?
- What data does the team produce that nobody seems to use?
- What questions does the rest of the company regularly ask that the data team has to manually answer?

**Output:** `data-team-flows.md` — coverage matrix maintenance process, demand signal capture state

---

### Customer Success (Days 10–11)

**Activities:**
- Read the last 30 CS account notes — look for patterns, recurring requests, themes that haven't reached the product team
- Interview two CSMs: what do you know about customers that the product team doesn't act on?
- Observe one CS customer call if possible — watch how product capability comes up

**Key questions:**
- What customer feedback do you give repeatedly that never seems to reach the roadmap?
- Which accounts are most at risk right now, and does engineering know why?
- How do you currently communicate "this customer desperately needs X dataset in Y state" to the data team?

**Output:** `cs-signal-gaps.md` — list of signals currently known to CS that are not reaching engineering or product decisions

---

## Week 3: Shadowing + Team Interviews

**Goal:** Understand what people actually do vs. what they say they do, and identify the human elements of the org model.

### Observe These Meetings (Don't Participate)

| Meeting | What to watch for |
|---|---|
| Engineering planning/sprint meeting | How is context provided? How long does it take for engineers to get up to speed on what they're building? |
| Product-Engineering sync | What information is being relayed that should already be documented? What decisions are made in real-time that could have been async? |
| CS-Product feedback loop (if it exists) | How much signal is compressed, distorted, or lost in the relay? |
| Any all-hands or company-wide sync | What does leadership communicate that would be better in a substrate file? |

---

### IC Interviews (Days 12–15)

Six to eight interviews with individual contributors across engineering, data, and CS. One open question: "Tell me about a time you needed information to do your job and it took longer than it should have to get it."

**What we're listening for:**
- Recurring information gaps (these become substrate files)
- Repeated questions to the same people (these become intelligence layer queries)
- Decisions made without full context (these reveal where the world model is thin)
- The informal coordination network — who does everyone go to when they need context? (These are DRI and player-coach candidates)

---

### Org Structure Mapping (Days 14–15)

**Activities:**
- Get the full org chart with reporting lines, tenure, and self-described expertise
- Identify: who has the most institutional knowledge? who is currently doing informal coordination work that should be systematized? who is most likely to thrive in a DRI model?
- Assess change readiness honestly: who is excited? who is skeptical? whose buy-in is critical?

**Output:** `org-map.md` — structure, tenure, informal influence network, DRI candidates, player-coach candidates

---

## Week 4: Synthesis + Validation

**Goal:** Turn raw discovery into a specific, validated architecture.

### Days 16–18: Draft the Architecture

Using everything gathered, produce the first version of the implementation plan:

1. **Substrate taxonomy** — exact file list with owner, update cadence, and "what current means" for each file
2. **Signal consolidation plan** — which signals need to be moved from siloed tools into the substrate, and how
3. **Intelligence layer spec** — the ten most important queries the system should answer, based on the actual friction patterns observed
4. **Role mapping** — specific names for first DRI assignments, specific names for player-coach transitions
5. **Phase 1 pilot spec** — the exact team, the exact outcome owned by the first DRI, the baseline metrics we'll measure against

---

### Days 19–20: Validation Sessions

Two sessions to pressure-test the draft:

**Session 1: CTO + one senior engineer**
Focus on the substrate taxonomy and intelligence layer spec. Is the file taxonomy realistic to maintain? Are the intelligence layer queries the right ones? What are we missing from the engineering perspective?

**Session 2: CEO + Head of Product**
Focus on the role model and transition plan. Is the DRI model calibrated correctly for their culture? Is the timeline realistic? What would cause them to slow down or stop?

**Output:** Revised architecture with specific pushback incorporated

---

### Days 21–25: Final Deliverable Production

Produce the updated white paper — now a specific implementation plan — with:

- Revised architecture (all three layers, now CivilGrid-specific)
- Substrate file taxonomy with named owners
- Signal consolidation roadmap
- Role model with named candidates for Phase 1
- 24-week implementation plan with milestones
- Baseline metrics and measurement plan

---

### Days 26–30: Buffer + Stakeholder Review

Present the final deliverable to CivilGrid leadership. Address remaining questions. Leave with explicit alignment on:
1. Which team runs the pilot
2. Who the first DRI is and what outcome they own
3. When Phase 1 begins

---

## Artifacts to Produce During Discovery

These files become the first entries in CivilGrid's world model substrate — a self-demonstrating artifact of the architecture we're proposing.

| File | Produced in | Owner |
|---|---|---|
| `tool-inventory.md` | Week 1 | Nathan |
| `signal-map.md` | Week 1 | Nathan |
| `leadership-interviews.md` | Week 1 | Nathan |
| `engineering-baseline.md` | Week 2 | Nathan |
| `product-signal-flow.md` | Week 2 | Nathan |
| `data-team-flows.md` | Week 2 | Nathan |
| `cs-signal-gaps.md` | Week 2 | Nathan |
| `org-map.md` | Week 3 | Nathan |
| `substrate-taxonomy-draft.md` | Week 4 | Nathan |
| `implementation-plan.md` | Week 4 | Nathan |

---

## Decision Gates

Three moments where what we find changes the plan:

**Gate 1 (End of Week 1):** If the honest signal is massively fragmented across tools with no programmatic access, Phase 1 of the implementation becomes a signal consolidation sprint before anything else. The white paper gets a new section on data infrastructure.

**Gate 2 (End of Week 2):** If cycle time data shows the bottleneck is not coordination overhead but something else (e.g., unclear requirements, technical debt, hiring gaps), the architecture may need to address those root causes first. An intelligence layer on top of a broken engineering process speeds up the wrong thing.

**Gate 3 (End of Week 3):** If cultural readiness is low — if there is significant resistance to the DRI model or the reduction of the management layer — the transition plan gets resequenced. We may need to run a longer pilot with a softer rollout before restructuring roles company-wide.
