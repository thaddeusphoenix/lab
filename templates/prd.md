# AI Product Requirements Document: [Product Name]

> One sentence: What does this product do and for whom?

**Status:** Draft | Aligned | Active | Shipped | Closed
**Owner:**
**Last updated:** YYYY-MM-DD
**Related Feature Briefs:** _(links to child feature briefs as they are created)_

---

## 1. Strategic Context

### Problem Statement

_Focus on user friction, not on the absence of AI. Name the specific pain, who experiences it, and the evidence that it is real._

**User:**
**Pain:**
**Evidence:**
**Current workaround:**

### User Personas

_Target segments — their behaviors, motivations, and Jobs to be Done._

| Persona | Behaviors | Motivations | Job to be Done |
|---|---|---|---|
| | | | |

### Strategic Objectives

_What success looks like in business terms. Not features shipped — impact achieved._

| Objective | Target | Timeframe |
|---|---|---|
| | | |

---

## 2. Data Specifications

> _AI-specific section. Skip if this product has no retrieval pipeline, training data, or model-serving infrastructure._

### Data Ingredient List

_Be precise — data types, volumes, time windows, and identifiers. Avoid vague terms like "user data"._

| Data Source | Type | Volume / Window | Owner |
|---|---|---|---|
| | | | |

### Quality Thresholds

| Metric | Threshold | Consequence if Unmet |
|---|---|---|
| **Completeness** | e.g., 95% fields populated | |
| **Freshness** | e.g., <24 hours old | |
| **Accuracy** | | |

### Data Supply Chain

_Who owns the data, where it originates, what happens if a source fails._

---

## 3. Reasoning Architecture

> _AI-specific section. Skip if this product has no agentic behavior, decision logic, or model memory._

### Decision Logic

_Map how the system reasons through information to reach a decision. Use flowcharts, logic trees, or written if/then rules._

### Authority Boundaries

| Capability | Disposition |
|---|---|
| **Must execute autonomously** | |
| **May suggest only** | |
| **Prohibited without human review** | |

### Memory & State

_How much history the model can access. What constitutes a session. Session timeout rules. State persistence requirements._

---

## 4. Functional Requirements

### User Stories

_Product-level behavioral scenarios. Use Given-When-Then format._

> **Note:** These are product-level stories for alignment — they describe intent, not test rubrics. Detailed build-loop acceptance scenarios live in a separate `[feature]-scenarios.md` file and are never included here.

| # | Given | When | Then |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |

### Interaction States

_Define the user-visible behavior for each UI state._

| State | Trigger | User-visible behavior |
|---|---|---|
| Idle | | |
| Loading | | |
| Error | | |
| Success | | |

### Out of Scope

_What related problems or capabilities are explicitly excluded from this product._

---

## 5. Evaluation & Performance Standards

> _AI-specific section. Skip if this product has no probabilistic or model-scored outputs._

### Golden Dataset

_Curated set of must-pass scenarios validated by domain experts. Required before launch._

**Size:**
**Owner:**
**Validation method:**

### Scored Metrics

| Metric | Target | Minimum to Ship |
|---|---|---|
| **Faithfulness** (grounded in source context) | | |
| **Relevancy** | | |
| **Hallucination rate** | | |

### Baseline at Launch

_Minimum acceptable performance required to ship. Below this threshold, the build does not deploy._

---

## 6. Non-Functional Requirements & Guardrails

### Latency Targets

| Operation | Target | Worst-case bound |
|---|---|---|
| | | |

### The Escape Hatch

_How every AI interaction provides a human-readable exit. One-click overrides, clear paths to human support, or graceful degradation._

### Privacy & Bias Boundaries

_Acceptable variance across user groups. PII handling requirements. Data retention rules._

---

## 7. Lifecycle & Maintenance

### Degradation Thresholds

_At what point does model performance decay trigger an automatic rollback or retraining request._

### Monitoring Cadence

| Feature / Signal | Cadence | Alert threshold |
|---|---|---|
| | | |

### Ownership Model

| Phase | Owner |
|---|---|
| Building | |
| Deploying | |
| Monitoring | |
| Retiring | |

---

## Biggest Unknowns

_The open questions whose answers would most change the architecture, scope, or go/no-go decision. These drive Discover phase work._

1.
2.
3.
