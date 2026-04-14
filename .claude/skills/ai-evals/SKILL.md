---
name: ai-evals
description: Help create and run AI evaluations. Use when building evals for LLM products, measuring model quality, creating test cases, designing rubrics, or systematically measuring AI output quality.
---

# AI Evals

Help the user create systematic evaluations for AI products using insights from AI practitioners via Lenny's Podcast.

## How to Help

1. **Understand what they're evaluating** — Ask what AI feature or model they're testing and what "good" looks like
2. **Help design the eval approach** — Suggest rubrics, test cases, and measurement methods
3. **Guide implementation** — Help think through edge cases, scoring criteria, and iteration cycles
4. **Connect to product requirements** — Ensure evals align with actual user needs, not just technical metrics

## Core Principles

### Evals are the new PRD
Brendan Foody: "If the model is the product, then the eval is the product requirement document." Evals define what success looks like in AI products — they're not optional quality checks, they're core specifications.

### Evals are a core product skill
Hamel Husain & Shreya Shankar: "Both the chief product officers of Anthropic and OpenAI shared that evals are becoming the most important new skill for product builders." This isn't just for ML engineers — everyone building AI products needs to master this.

### Binary scores over Likert scales
Hamel Husain: "Force Pass/Fail, not 1-5 scores. Scales produce meaningless averages like '3.7'. Binary forces real decisions."

### Validate your LLM judge
Hamel Husain: "If using LLM-as-judge, you must eval the eval. Measure agreement with human experts. Iterate until it aligns."

### Start with manual review, then automate
You can't write good evals without first understanding failure patterns through manual trace analysis. The workflow: manual review → open coding (write down what's wrong) → cluster failure patterns → create rubrics → automate.

### Start with vibes, evolve to evals
Howie Liu: "For novel products, start with open-ended vibes testing. Only move to formal evals once use cases converge."

## Questions to Ask

- "What does 'good' look like for this AI output?"
- "What are the most common failure modes you've seen?"
- "How will you know if the model got better or worse?"
- "Are you measuring what users actually care about?"
- "Have you manually reviewed enough outputs to understand failure patterns?"

## Common Mistakes

- **Skipping manual review** — You can't write good evals without first understanding failure patterns
- **Using vague criteria** — "The output should be good" isn't an eval; you need specific, measurable criteria
- **LLM-as-judge without validation** — If using an LLM to judge, validate it against human experts first
- **Likert scales over binary** — Force Pass/Fail; 1-5 scales produce meaningless averages

## Lab Context

The AI Build Loop's Tester actor is an eval system: it receives brief + scenarios + output and produces PASS/FAIL with structured feedback. The `acceptance-scenarios.md` template and the Tier 1/Tier 2 scenario system is the lab's eval framework. Use this skill when designing scenarios or when building an AI product that needs its own internal eval loop.
