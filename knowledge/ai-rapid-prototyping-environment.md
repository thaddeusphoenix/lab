# AI Rapid Prototyping Environment — Team Reference

**Source:** Original research compiled 2026-02-27
**Relevance:** Directly applicable to how the lab builds, evaluates, and ships AI products

---

## The Core Premise

The 2025–2026 shift is from deterministic, instruction-based software to non-deterministic, agentic AI. The prototyping environment's job is to bridge raw research and production-grade applications — a high-velocity sandbox where teams validate four risks: **value, usability, feasibility, and business viability** before committing to build.

Well-designed prototyping environments reduce the traditional 8-month production timeline by up to 60%.

---

## Team Model: Empowered vs. Feature Factory

| | Traditional Feature Team | Empowered AI Product Team |
|---|---|---|
| **Success metric** | Output (features shipped) | Outcome (problems solved) |
| **Mindset** | Mercenary (follow orders) | Missionary (solve the vision) |
| **Discovery** | Periodic | Continuous — weekly customer touchpoints |
| **Accountability** | Siloed competencies | Shared across the trio |

The Product Trio (PM + Designer + Engineer) is the foundational unit. In the AI era:
- The **engineer** architects problem-solving strategies, not just code
- The **designer** makes non-deterministic AI behavior usable and intuitive
- The **PM** acts as the nervous system — every iteration grounded in a testable hypothesis

Teams must be long-lived and empowered to move on objectives they set themselves, aligned with higher-level OKRs. Autonomy is especially critical for AI, where feasibility constraints emerge only during prototyping.

---

## Upskilling: What AI PMs Must Now Do

The era of pure project management is over. Effective AI PMs must demonstrate **Deep AI Intuition** — which comes only from hands-on building, understanding model limitations, and exploring architectural trade-offs.

The environment should support "vibe coding" — ideas translated into functional prototypes in hours, not weeks. Low-code and no-code tools let non-technical trio members experiment with prompts and agentic workflows without constant engineering intervention.

---

## Technical Stack — Five Essential Layers

### 1. Development Environment (AI-Native IDEs)

| Tool | Strength |
|---|---|
| **Cursor** | Premier for complex codebases. "Composer" modifies multiple files from plain language descriptions |
| **Windsurf** | "Cascade" auto-determines files to examine and executes terminal commands. Best for teams new to a framework |
| **Replit** | Browser-based, zero-installation. Best for instant stakeholder demos |

### 2. Backend Frameworks

- **FastAPI (Python)** — Standard for AI startups. Native async support, Pydantic validation, matches LLM streaming
- **Node.js / Nest.js** — Better when integrating with React/Next.js frontends
- Python remains dominant for AI due to library support (TensorFlow, PyTorch, Hugging Face)

### 3. Agentic Orchestration

| Framework | Strength | Best For |
|---|---|---|
| **LangGraph** | Graph-based, explicit control over decision flows, cyclical/parallel/conditional workflows | Engineering teams that value reproducibility |
| **CrewAI** | Role-based agents ("Analyst", "Researcher") organized into Crews. Low barrier to entry | Early-stage conceptual validation |
| **LlamaIndex** | Designed for data-heavy RAG workflows | Structured extraction from complex files |

### 4. LLM Gateways (Prevent Vendor Lock-In)

Gateways provide a unified, OpenAI-compatible API across hundreds of models.

| Gateway | Core Strength | Ideal Use Case |
|---|---|---|
| **Bifrost (Maxim AI)** | 54x faster than Python gateways, <11µs at 5k req/s | Latency-sensitive production apps |
| **LiteLLM** | 100+ model providers | Prototyping across niche/emerging models |
| **Portkey** | Strong observability and budget guardrails | Managing costs across multiple teams |
| **Helicone** | Rust-based, extremely low overhead | High-traffic APIs |

Bifrost's semantic caching reduces API costs by up to 60% — critical during high-iteration prototyping.

### 5. Evaluation Framework

See "The Evaluation Loop" section below.

---

## The Model Context Protocol (MCP)

MCP solves the "N × M" integration problem — where every model requires a custom integration for every tool. It is the "USB-C for AI": standardized, secure, auditable.

**How it works:**
1. **Discovery** — the agent queries the MCP server for available capabilities
2. **Invocation** — the agent reads tool descriptions and invokes with structured parameters
3. **Response** — the server executes and returns machine-readable results the agent uses for its next step

**Strategic value for PMs:** As new models (GPT-5, Claude 5, etc.) are released, they immediately work with the existing enterprise MCP layer — no new integrations. The lab's current Claude Code setup already uses MCP servers; this is the same pattern at the enterprise scale.

---

## Prototyping Lifecycle

### Phase 1: Problem Definition
- Define clear success metrics before picking tools
- Build semi-fictional personas grounded in user research
- No prototyping without user understanding — "designing in the dark"

### Phase 2: Match Fidelity to Risk (Marty Cagan)

> "The level of fidelity should match the level of risk."

| Risk Type | Question | Prototype Approach |
|---|---|---|
| **Value** | Will they use it? | Wizard of Oz, low-fi mockup with simulated AI responses |
| **Usability** | Can they use it? | High-fi mockup with realistic UI (v0, Uizard) |
| **Feasibility** | Can we build it? | Code-first spike in Cursor/Claude Code with real APIs and data |
| **Business Viability** | Does it work for the business? | Cost modeling and strategic analysis, not a prototype |

*Note: This maps to the lab's Paper/Cardboard/Plastic/Metal fidelity levels. The main addition here is explicitly tying each fidelity level to the type of risk it's designed to retire.*

### Phase 3: Avoid the Zombie Doc
Static PRDs become outdated immediately. The modern alternative: AI-generated specs that update automatically from the interactive prototype. Tools like Supernova can sync prototype state to developer tools and project management systems via MCP.

---

## The Evaluation Loop

Because AI is non-deterministic, the evaluation loop is the most critical tool for a PM building trustworthy AI products. Treat Evals as a continuous process across build, test, and observe — not a one-time QA step.

### Core Metrics

| Metric | Description | Target |
|---|---|---|
| **Task Accuracy** | Proportion of responses meeting correctness criteria | 85–90% for enterprise knowledge bots |
| **Faithfulness** | For RAG: is the answer supported by retrieved context? | 85–95%, hallucinations <15% |
| **Contextual Relevance** | Are retrieved documents actually relevant? | 90–95% |
| **Tool Correctness** | For agents: correct tool called with correct parameters? | >95% |

### PM's Role in Evals

Engineers provide the testing infrastructure. The PM provides the **judgment layer**:
1. Define what failures are "unforgivable" (safety, legal, factual errors)
2. Establish a rubric (e.g., 1–5 scale with explicit definitions per level)
3. Review 50–100 production interactions to identify where the AI currently breaks
4. For high-stakes decisions: Human-in-the-Loop (HITL) expert evaluators set the gold standard

---

## Enterprise Readiness (Build From Day Zero)

Retrofitting identity infrastructure is the primary reason AI pilots fail to reach production.

- **Tenant Isolation** — every query includes a `tenant_id` predicate. No cross-tenant reads/writes
- **Least Privilege RBAC** — minimum permissions per role per tenant
- **Zero-Trust** — authenticate and authorize every API call, even from internal systems
- **SAML 2.0** — authentication / SSO with SHA-256+ signatures
- **SCIM 2.0** — automated user provisioning/deprovisioning via Identity Provider (Azure AD, Okta)
- **OAuth 2.0** — API authorization with secure bearer tokens

---

## AI-Assisted Engineering Metrics

| Metric | Description |
|---|---|
| **Prompt-to-Commit Success Rate** | % of AI-generated code that ships without human rewrite |
| **Defect Density** | Confirmed defects per KLOC, split AI-assisted vs. manual |
| **AI Revert Percentage** | How often AI-generated code is reverted — signals hallucinations or safety failures |
| **Time-to-Market Reduction** | Cycle time delta before vs. after AI rollout |

---

## Key Takeaways for the Lab

1. **MCP is the right connective tissue.** The lab's current Claude Code setup already uses MCP. As projects scale to production, this is the pattern to standardize on.

2. **Fidelity discipline prevents over-building.** The lab's Paper/Cardboard/Plastic/Metal framework is aligned with Cagan's principle. The discipline to call fidelity explicitly before starting a prototype is the habit that prevents wasted effort.

3. **Evals need to become a practice, not an afterthought.** Research Scout and Deep Dispatch have no evaluation loop yet. As agents get used in real workflows, defining what a "correct" output looks like becomes critical.

4. **The PM must build hands-on.** The lab's model of building prototypes alongside the team (rather than handing off specs) is exactly what the 2025 AI PM Evaluation Framework calls for.

5. **LLM gateways become important at scale.** For now, direct SDK calls (Anthropic, Gemini) are fine. When the lab's agents hit production, a gateway like LiteLLM prevents lock-in and adds observability.
