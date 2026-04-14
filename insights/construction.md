# Insights: Construction

Atomic claims derived from Handoff project work and field feedback. Each is a falsifiable assertion — not a category, not a summary.

---

**P6/Oracle API access is an industry-wide blocker for scheduling startups — not a technical gap, a procurement and licensing one.**
Source: Willis Clayton-Stankowski (Cahil Construction), confirmed independently at Future Tech Construction Conference. OpenProject as a stand-in understates the severity.

**Daily log aggregation + 3-week look-ahead is more valuable than schedule write-back, because it doesn't require API access to the scheduling system.**
The Superintendent's core need is coordination visibility, not schedule automation. Write-back is the wrong target.

**SMS is the only viable input channel for field workers. Foremen will not open an app.**
Any input model that requires launching a dedicated app fails at adoption. The enrollment behavior doesn't exist.

**The input model is the moat in construction software, not the analytics.**
Tools that accept unstructured input and produce structured output outcompete tools that require structured input — even when the analytics are worse. The barrier to data entry IS the product problem.

**65% of major project delays trace to idle time during trade handoffs, not to individual task failures.**
The coordination gap, not execution failure, is the dominant delay driver on large sites.

**Human-in-the-loop approval flows are not a limitation — they are the product.**
Superintendents do not want AI to make schedule decisions. They want AI to eliminate the data entry burden and surface the right decisions to the right person. Accuracy over automation.

**The Wizard-of-Oz test for SMS prompts should precede any automation build.**
Whether foremen self-report without prompting is the riskiest behavioral assumption in the product. Test with a human sending the SMS before writing the trigger layer.
