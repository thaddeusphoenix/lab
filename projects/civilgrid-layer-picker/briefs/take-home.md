# CivilGrid Layer Picker — PM Take-Home Response

**Date:** 2026-03-23

---

## Overview

The layer picker is not a cosmetic feature. It is the first time CivilGrid gives customers explicit control over what they see and why — moving the product from "here is your data" to "here is your workspace." Done well, it becomes the foundation for every high-value capability that follows: saved configurations, team sharing, and proprietary layer management.

---

## 1. Potential Solutions, Required Data, and Assumptions

### Three Solution Options

**Option A — Simple Checkbox Panel**

A static sidebar listing all 150+ layers, grouped by category (Electric, Gas, Geotechnical, etc.), with toggle switches. Users turn layers on and off manually. No persistence between sessions. No intelligence.

- **Pros:** Low engineering lift, ships fast, unblocks the immediate UX problem
- **Cons:** 150+ items is a long list. No geography filtering means irrelevant layers (NY State Parks for a CA project) clutter the UI. No memory means users repeat the same setup on every session. Teaches nothing about how customers actually use the product.

**Option B — Filtered Panel with Project-Aware Persistence (Recommended for MVP)**

A structured panel with three improvements over Option A:

1. **Geography-aware filtering** — surface only layers with coverage in the project's state(s). Layers not yet loaded in a state are shown as "Coming Soon" rather than removed entirely, so customers understand the roadmap and sales can set expectations.
2. **User role defaults** — on first load, pre-select a sensible default layer set based on the user's role (developer, civil engineer, environmental consultant). Defaults are editable; the goal is to reduce time-to-value, not to constrain.
3. **Per-project persistence** — layer state saves per project, not per session. When a user returns to a project, their configuration is intact.

- **Pros:** Solves the core UX problems. Respects geography constraints. Builds the data infrastructure (layer state per project) needed for future presets and sharing.
- **Cons:** Requires role data at the user level (may need a one-time migration or onboarding prompt). Geography filtering requires a maintained layer-coverage matrix.

**Option C — Smart Layer Picker with Presets, Search, and Sharing**

All of Option B plus: saved named presets ("My Transmission Line Due Diligence"), team-level preset sharing, full-text search across layer names and descriptions, and a preview of what data density looks like per layer before enabling it.

- **Pros:** Highest long-term value. Presets are the direct precursor to the proprietary layer upload upsell.
- **Cons:** Significantly higher build cost. Sharing requires team/org data model work that may not exist yet. Risk of over-building before validating that customers want presets at all.

### Recommendation: Option B for MVP

Option B solves the real problem — disorganized, irrelevant layers slowing down due diligence workflows — without betting on usage patterns we haven't confirmed. It also builds the technical substrate (layer state per project, coverage matrix, role-based defaults) that makes Option C a natural iteration rather than a re-architecture.

Option A is too thin — it ships a UI component but doesn't improve the actual workflow. Option C ships features that belong in iteration 2.

---

### Data Needed Before Committing

- **Layer activation analytics** — which layers are currently enabled by default, which get turned off, and which are never interacted with. If 80% of sessions use the same 12 layers, that shapes the default set dramatically.
- **Support ticket analysis** — are customers filing tickets about map clutter, missing layers, or layer state resetting between sessions?
- **5–8 customer interviews** — structured around one question: *walk me through your last due diligence session, from opening the map to completing your analysis.* Do not ask "what would you like in a layer picker?" — behavior data is more reliable than feature requests.
- **Sales call recordings** — how does the current map experience come up in demos and trials?
- **Role distribution in the customer base** — what percentage of users are developers vs. engineers vs. consultants?
- **Layer coverage data** — a current, maintained record of which layers are live in which states.

---

### Explicit Assumptions

- **Users are project-centric, not exploratory.** They open CivilGrid with a specific site and objective. This justifies per-project persistence over global preferences.
- **Two primary user segments exist with meaningfully different layer needs.** Developers (budget/schedule risk focus) prioritize land rights, utilities, and geotechnical. Engineers (technical due diligence focus) go deeper into utility specifics, seismic, and transportation.
- **Geography-aware filtering is table stakes, not a nice-to-have.** A California engineer seeing NY State Parks layers in their panel erodes trust in the product's relevance.
- **"Coming Soon" is preferable to hiding.** For states where CivilGrid hasn't launched a layer, showing it as coming soon is a retention and expectation-setting tool.
- **Layer state persistence is the single highest-value improvement.** Users resetting their layer configuration on every session is likely the most friction-heavy current behavior.
- **The proprietary layer upload feature is not MVP scope** — it requires a separate infrastructure build. MVP must only avoid architecturally blocking it.

---

## 2. Business KPIs

### Feature-Level KPIs

**Time to First Meaningful Layer Configuration**
How long it takes a new user to reach a layer state that reflects their actual use case — operationalized as the first session where a user deviates from defaults and the session exceeds a productive session length threshold.

*Why it matters:* If users spend the first 10 minutes of every session hunting for layers, that's 10 minutes not spent on the analysis they're paying for.

**Layer Engagement Depth per Session**
The number of distinct layers a user interacts with per session, segmented by role.

*Why it matters:* Increased depth signals users are exploring the full value of the data catalog — CivilGrid's core product moat. Flat depth after launch suggests defaults are too sticky.

**Layer Configuration Retention Rate**
Percentage of returning users whose saved layer state is present and intact on next project open.

**Coming Soon Layer Click Rate**
How often users interact with a "Coming Soon" layer. Leading indicator of demand for specific datasets; feeds directly into roadmap prioritization.

---

### Business-Level KPIs and Causal Chains

**Net Revenue Retention (NRR)**

*Causal chain:* A confusing, cluttered map experience increases time-to-value on every project → users complete fewer due diligence tasks per session → the product feels less capable than it is → renewal conversations start from a weaker perceived value position. A layer picker that reduces friction compresses time-to-value and gives CS a concrete improvement to reference in renewal QBRs.

*Measurement:* Track NRR for cohorts who have actively used the layer picker vs. those who haven't. Expect 6–12 month lag.

**Sales Cycle Velocity / Trial-to-Paid Conversion**

*Causal chain:* The layer picker makes demos more compelling — sales can show a geography-aware panel that immediately reflects the prospect's project type and location. This shortens the "convince me the tool is relevant to my use case" phase.

*Measurement:* Average days from demo to contract for deals where the layer picker was featured vs. not.

**Expansion Revenue from Proprietary Layer Upsell (Future)**

*Causal chain:* Once users are actively managing layer configurations, proprietary layer upload slots in cleanly — customers already know exactly where to go. The learning curve is near zero.

*Measurement:* Proprietary layer adoption rate as a percentage of accounts that were active layer picker users at time of upsell.

---

## 3. MVP vs. Future Iterations

### MVP: What's In

- **Structured layer panel** organized by category, with clear visual hierarchy
- **Geography-aware filtering** — layers labeled "Coming Soon" or hidden based on project location
- **Role-based default layer sets** — pre-configured on account creation (developer / civil engineer / environmental consultant)
- **Per-project layer state persistence** — saves automatically, restores on return
- **Layer metadata on hover/expand** — dataset name, source, last updated, coverage notes
- **Basic keyword search** within the panel

### MVP: What's Explicitly Out

- **Saved named presets** — defer until usage data confirms cross-project reuse intent
- **Team/org sharing** — requires org data model work, significant additional scope
- **Proprietary layer upload** — separate product capability, own build cycle
- **Layer ordering / z-index control** — power-user feature, defer until post-MVP feedback

### Iteration 1: Presets and Cross-Project Efficiency

Ship named presets — users save their current layer configuration and reload it on any future project. Converts the layer picker from a per-project utility into a repeatable workflow accelerator. Presets are the direct UI precedent for proprietary layers.

*Trigger:* Layer configuration retention rate is high and session depth is up, but customers are still reconfiguring layers when starting similar new projects.

### Iteration 2: Team Sharing and Org-Level Standards

Allow admins to publish a default preset for the org. Allow users to share presets with teammates. Makes CivilGrid sticky at the team level and increases switching cost.

*Trigger:* Preset creation rate is high. Customer interviews surface requests for consistency across team members.

### Proprietary Layer Upload as the Natural Capstone

Once presets exist, proprietary layer upload slots in cleanly: customers upload their own data (survey results, internal asset records, environmental studies), and it appears in the same panel, toggleable alongside CivilGrid's layers. The workflow is identical to what they already know. This is the premium tier unlock.

---

## 4. Launch Plan

### Existing Customers: Phased Beta to GA

**Phase 1 — Private Beta (Weeks 1–4)**

Recruit 8–12 power users from top accounts — prioritize customers who use the map heavily and who have previously flagged layer confusion in support tickets or CS notes. Provide access with a Loom walkthrough and a 30-minute onboarding call per account.

Goal: find obvious UX failures before broad rollout — geography filtering misclassifications, wrong role defaults, layer state that doesn't persist correctly.

**Phase 2 — Expanded Beta (Weeks 5–8)**

Open to all accounts above a usage threshold (e.g., 5+ sessions in the last 90 days). Email from CS, not marketing — this should feel like a trusted early-access signal. Include a short in-app tooltip sequence introducing the three key behaviors: role defaults, geography filtering, and saved state.

**Phase 3 — General Availability (Week 9+)**

Roll to all customers. In-app announcement modal on next login: two sentences — what changed and why it matters. Update the default map experience to reflect the layer picker being active.

---

### Sales Enablement

**Updated Demo Script**

At the start of a demo, the sales rep inputs the prospect's actual project location and job title. The panel loads with geography-filtered layers and role-appropriate defaults. This turns a generic product tour into a "here is what CivilGrid looks like for *your* project in *your* state" moment.

**One-Liner Value Proposition**

> "CivilGrid now surfaces only the data that's relevant to your project — filtered by geography and configured for your role — so your team spends time on analysis, not managing the map."

**Battle Card Angle**

If competitors show a flat list of all layers with no geography awareness, the CivilGrid layer picker is a direct differentiator. The framing: *they give you data; we give you a configured workspace.*

---

### Marketing

This audience — infrastructure developers, civil engineers, project managers — responds to specificity and credibility, not generic SaaS marketing copy.

- **LinkedIn post with before/after UI** — show the actual product change. Infrastructure professionals are visual.
- **Plain-text email to existing customers** — from the CEO or Head of Product, not a designed newsletter. "We fixed something that was bothering you."
- **Partner channel communication** — a brief note to engineering consultancies or developer associations positions the feature as a product maturity signal.

---

## 5. Post-Launch Measurement

### Week 1–2: Stability and Initial Adoption Signals

- Error rate on layer state saves (alert threshold: >1% of save operations)
- Geography filtering accuracy — QA check on sample projects
- Beta user return sessions — are beta users coming back?
- Support ticket volume — any new category emerging around the layer picker

### Month 1: Adoption Rate and Engagement Depth

- **Layer picker activation rate** — target: >60% of active users within 30 days of GA
- **Default modification rate** — target range: 30–60% (too low = defaults too sticky; too high = defaults wrong)
- **Coming Soon click rate by layer** — feed into data roadmap prioritization

### Month 2–3: Value Indicators

- Session depth vs. pre-launch baseline
- Per-project return rate with saved layer state intact
- Support ticket deflection on layer-related issues
- Qualitative CS signals — is the feature coming up in renewal conversations?

### Month 3+: Business Impact

- NRR cohort split — active layer picker users vs. non-users
- Expansion signals — are heavy layer picker users more likely to expand seats?
- Sales cycle velocity delta for deals where layer picker was demoed
- Trial-to-paid conversion rate (expect movement within 60–90 days of GA)
