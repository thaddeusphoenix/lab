# 10 Years Building Vertical Software: My Perspective on the Selloff

Source: [@nicbstme on X](https://x.com/nicbstme/status/2023501562480644501) — Nicolas Bustamante, founder of Doctrine (Europe's largest legal information platform) and Fintool (AI equity research platform)

## Context

Nearly $1 trillion was wiped from software and services stocks. FactSet dropped from a $20B peak to under $8B. S&P Global lost 30% in weeks. Thomson Reuters shed almost half its market cap in a year.

The author has built on both sides: Doctrine competed with LexisNexis and Westlaw. Fintool competes with Bloomberg, FactSet, and S&P Global today using AI.

> "I built the kind of software that LLMs are now threatening. And I'm now building the kind of software that's doing the threatening."

---

## The Ten Moats of Vertical Software — and What LLMs Do to Each

### Destroyed or Severely Weakened

**1. Learned Interfaces → Destroyed**

Bloomberg Terminal users spend years learning keyboard shortcuts and function codes. That muscle memory was a switching cost. When the interface is natural language chat, years of investment become worthless.

At Doctrine: the interface was the product. Designers, CSMs, user research, careful rollouts — all to manage UI muscle memory. At Fintool: no onboarding, no CSMs, no interface to learn. That entire cost center doesn't exist.

LLMs collapse all proprietary interfaces into one: Chat.

**2. Custom Workflows and Business Logic → Vaporized**

Vertical software encodes how an industry actually works — citational networks, compliance checks, approval workflows. This took years of domain-expert engineers to build.

At Doctrine: a legal research workflow took a team of engineers and legal experts several years. Thousands of lines of Python, custom ranking algorithms, hand-tuned relevance models.

At Fintool: the equivalent is a DCF valuation skill — a markdown file. Writing it took a week. Updating it takes minutes. A portfolio manager can encode their entire methodology without writing a single line of code.

> "Business logic is migrating from code written by specialized engineers to markdown files that anyone with domain expertise can write."

**3. Public Data Access → Commoditized**

Making hard-to-access public data searchable was a genuine moat. FactSet built thousands of parsers for SEC filings. Doctrine built NLP pipelines, named entity recognition, and custom parsers for every court.

At Fintool: none of that was built. Frontier models already know how to navigate a 10-K. The model IS the parser.

**4. Talent Scarcity → Inverted**

Building vertical software required engineers who understood both the domain and the technology — an extremely rare combination. At Doctrine, internal lectures taught engineers how the legal system worked for months before they were productive.

At Fintool: domain experts write their methodology directly into markdown skill files in plain English. The LLM handles the engineering. The scarce resource (domain expertise) can now become software directly, without the engineering bottleneck.

**5. Bundling → Weakened**

Vertical software expanded by bundling adjacent capabilities — each module increasing switching costs. Bloomberg: market data, then messaging, news, analytics, trading, compliance.

LLM agents break bundling because the agent IS the bundle. At Fintool, alerts, watchlists, and portfolio screening are all prompts — no separate modules, no UI to maintain. The agent orchestrates across ten different tools in a single workflow.

When the integration layer moves from the software vendor to the AI agent, the incentive to buy a bundle evaporates.

---

### Holding or Strengthened

**6. Private and Proprietary Data → Stronger**

If data genuinely cannot be replicated, LLMs make it MORE valuable. Bloomberg's real-time pricing from trading desks can't be scraped or synthesized. S&P Global's credit ratings are regulated opinions backed by decades of default data.

The test: *Can this data be obtained, licensed, or synthesized by someone else?* If no, the moat holds. If yes, you're in trouble.

Warning: MCP is turning every data provider into a plug-in. If your data is available as an agent plugin, the "making it accessible" premium disappears. Companies without truly unique data risk becoming commodity suppliers to agents — competing on price to feed someone else's platform.

**7. Regulatory and Compliance Lock-in → Structural**

HIPAA doesn't care about LLMs. Epic's 18-month implementation cycles, compliance certifications, and hospital billing integrations are unaffected. Regulatory requirements may actually slow LLM adoption in exactly the verticals where compliance lock-in is strongest.

**8. Network Effects → Sticky**

Bloomberg's IB chat is the de facto communication layer for Wall Street — you use it because everyone else does. LLMs don't break this. The information flowing through these networks may become more valuable as training data and context.

**9. Transaction Embedding → Durable**

Software embedded in the money flow (payment processing, loan origination, claims processing) isn't disintermediated by LLMs. The rails remain essential. LLMs may sit on top as a better interface, but can't replace the underlying infrastructure.

**10. System of Record Status → Threatened Long-Term**

LLMs don't directly threaten system of record status today. But agents are quietly building their own — reading Slack, Outlook, SharePoint, accumulating richer context than any single system. Over time, the agent's memory becomes the new source of truth.

---

## The Real Threat: A Pincer Movement

**From below:** Hundreds of AI-native startups entering every vertical. When building a credible financial data product required 200 engineers and $50M in data licensing, markets consolidated to 3-4 players. When it requires 10 engineers and frontier model APIs, the market fragments violently — competition goes from 3 to 300.

**From above:** Horizontal platforms going deep into vertical territory for the first time. Microsoft Copilot inside Excel does AI-powered DCF modeling. Copilot inside Word does contract review. The horizontal tool becomes vertical through AI, not through engineering.

The enabling stack is terrifyingly simple: a general-purpose agent harness (SDK) + pluggable data access (MCP) + domain-specific skills (markdown files). No domain engineers. No years of development.

> "Software is becoming headless. The interface disappears. Everything flows through the agent. What matters isn't the software anymore. It's owning the customer relationship and use cases — which means owning the agent itself."

---

## Framework for Assessing Risk

Ask three questions about any vertical software company:

1. **Is the data proprietary?** If yes, the moat holds. If no, the accessibility layer is collapsing.
2. **Is there regulatory lock-in?** If yes, LLMs don't change the switching cost equation. If no, switching costs are primarily interface-driven and dissolving.
3. **Is the software embedded in the transaction?** If yes, LLMs sit on top of you, not instead of you. If no, you're replaceable.

Zero yes answers: high risk. One: medium risk. Two or three: probably fine.

**High Risk — The Search Layer:** Primary value is making licensable or public data searchable through a specialized interface. Interface lock-in and limited competition are both evaporating.

**Medium Risk — Mixed Portfolio:** Some proprietary business lines alongside repackaged public data. Key question: what percentage of revenue comes from moats LLMs can't touch?

**Lower Risk — Regulatory Fortresses:** Moat is compliance infrastructure and deep integration with mission-critical workflows. May even benefit from disruption elsewhere as customers consolidate around trusted vendors for regulated workflows.

---

## Key Takeaway

The vertical SaaS reckoning isn't about all vertical software dying. It's about the market distinguishing between companies that own something genuinely scarce versus those whose value was always in organizing public data behind a proprietary interface.

The market isn't pricing in a revenue collapse. It's pricing in the end of the premium multiple — because the moats that justified that multiple are dissolving.
