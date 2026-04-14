# Insights: Lab Process

Atomic claims derived from operating the build loop, managing briefs, and running projects through phases.

---

**The Brief and the Acceptance Scenarios must describe the same thing — or the loop will not converge.**
The most common escalation cause is not poor execution but a contradiction between the Proposed Solution in the brief and the Pass signals in the scenarios. Fix the contradiction at the source.

**Briefs must embed section headers verbatim from templates.**
The Writer has no access to template files. Referencing `templates/prd.md` without quoting the headers causes the Writer to invent its own structure.

**The "Use Case of 1" principle: you win if one person finds it more useful than the alternative.**
That proof point is what drives the pilot, not the TAM. Build for the person in front of you before scaling the theory.

**A monolithic brief that fails 5 runs should be split, not amended further.**
When the loop escalates, the spec has a structural problem. Splitting the brief into smaller, more coherent scopes is usually the right move — not writing a 6th amendment.

**Prototypes should be labeled by fidelity: Paper / Cardboard / Plastic / Metal.**
Paper = concept sketch. Cardboard = testable flow, no real data. Plastic = close to real, real data. Metal = production-ready. Fidelity drives what questions you can answer.

**Gemini constraint: custom function calling and Google Search grounding cannot be combined in one call.**
Requires two sequential calls. Combining them silently fails or errors, not a clear error message.

**gemini-2.0-flash is unavailable for this account — use gemini-2.5-flash.**

**Python command on this machine is `python3`, not `python`.**

**rmapi: always use the ddvk fork — the juruen fork returns 410.**
