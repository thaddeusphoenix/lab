# Insights: AI Product Design

Atomic claims derived from lab builds, client work, and product evaluation. Each is a falsifiable assertion.

---

**Agentic tools create disproportionate value at the scale where the data problem is too large to solve manually.**
Small data volumes don't justify agents. The value threshold is where synthesis exceeds human bandwidth.

**Coming Soon clicks are more honest demand signals than feature request forms.**
Clicks are behavior; feature requests are opinion. Behavior under real product conditions beats surveyed intent.

**Layer activation patterns reveal what users are actually solving for — better than any interview.**
What users turn on tells you what problem they're actually in. What they say they want tells you their theory of the product.

**A role-based defaults pattern gives AI workflows a Trojan horse entry point.**
Ship role defaults first. Replace rule-based defaults with AI inference later. The UX surface is identical; the underlying intelligence upgrades invisibly.

**Too many false positives erode AI agent trust faster than missing features.**
An agent that is wrong 20% of the time will be overridden and ignored. Accuracy is the precondition for adoption — not a nice-to-have.

**Removing the backend doesn't limit the product — it defines it.**
Zero infrastructure means zero onboarding funnel. The constraint becomes the differentiator when the user population resists registration.

**HTML build artifacts must use `<script>` not `<script type="module">` — modules silently fail on file:// URLs.**
A module that works in a dev server will silently fail when the output is opened directly in a browser. The build loop produces file:// artifacts.

**If the Writer sees the acceptance scenarios, it optimizes to pass the test rather than solve the problem.**
The firewall between Writer and Tester is not a process preference — it is the mechanism that makes the loop produce honest signal.

**PDF generation on macOS: write HTML + CSS, render via Playwright headless Chromium. Do not use weasyprint or ReportLab.**
weasyprint fails on macOS (libgobject naming mismatch). ReportLab produces messy table output. Playwright is the only reliable path.

**The people most advantaged by AI are not engineers — they are people who are articulate about how they think.**
Externalizing reasoning to files forces you to examine it. The bottleneck is clarity of thought, not technical skill.
