# Project Feature Brief: Deep Dispatch

> A CLI agent powered by Gemini that takes a research question, incorporates relevant personal sources, runs deep research with live web access, and delivers a formatted PDF to your reMarkable — without any manual steps after the initial prompt.

**Status:** Draft
**Owner:** Wintermute (PM)
**Last updated:** 2026-02-27
**Parent Initiative:** _(none — standalone agent project)_

---

## The Problem

**User:** Nathan
**Pain:** Running deep research via Gemini is valuable, but the workflow is manual end-to-end: open the web app, type the question, remember to include relevant NotebookLM sources, wait for the result, export it, and get it onto the reMarkable. The friction means research happens less often than it should, and personal knowledge (NotebookLM projects) rarely makes it into the output.
**Evidence:** Stated directly. Current workflow requires multiple context switches and manual file handling every time.

## The Proposed Solution

A Python CLI agent powered by the Gemini API. You type a research question in your terminal. The agent reads your local sources manifest, uses Gemini to identify which of your NotebookLM-exported projects are relevant to the question, incorporates their content into the research context, runs Gemini deep research with Google Search grounding for live web access, converts the output to a styled PDF, and emails it to your reMarkable's registered address. The document appears on your device within minutes, unprompted.

The agent uses Gemini's native function calling for its agentic loop — Gemini is the brain. Google Search grounding is used directly (no third-party search API needed).

## Architecture

```
CLI: python dispatch.py "your research question"

Agent loop (Gemini as orchestrator):
  1. list_sources()         → reads sources/manifest.json
  2. select_sources()       → Gemini picks relevant projects, asks for confirmation
  3. read_source(id)        → loads source content into context
  4. deep_research()        → Gemini + Google Search grounding
  5. write_pdf(content)     → pandoc: markdown → styled PDF
  6. send_to_remarkable()   → emails PDF to reMarkable address
```

## NotebookLM Integration (Constraint + Workaround)

NotebookLM has no public API. The workaround: a local `sources/` directory that mirrors your NotebookLM projects. Each project is represented by:
- An exported PDF, markdown file, or text dump of the source material
- An entry in `sources/manifest.json` with title, topic description, and file path

Gemini reads the manifest to decide which sources are relevant to the question. You update the directory when you add new NotebookLM projects. This is the only manual step the architecture cannot eliminate.

## Why Gemini (Not Claude)

- Native Google Search grounding — live web access without a third-party search API
- Deep research capability the user already relies on and trusts
- Learning goal: build familiarity with Gemini's agent patterns alongside Claude's (Research Scout)

## Stack

- Python 3.11+
- `google-generativeai` SDK (Gemini API)
- Model: `gemini-2.0-pro` or `gemini-2.5-pro`
- Google Search grounding (built in)
- `pandoc` for markdown → PDF conversion
- `smtplib` / Gmail app password for reMarkable email delivery
- `python-dotenv` for credentials

## Out of Scope

- Real-time NotebookLM API integration (does not exist)
- Multi-device delivery (reMarkable only)
- Scheduling / recurring research (v1 is on-demand only)
- Web UI

## Setup Requirements (one-time)

| Requirement | Where to get it |
|---|---|
| `GEMINI_API_KEY` | aistudio.google.com |
| `REMARKABLE_EMAIL` | my.remarkable.com → Integrations |
| `GMAIL_ADDRESS` + `GMAIL_APP_PASSWORD` | Google Account → Security → App Passwords |
| `pandoc` installed | brew install pandoc |

## Success Looks Like

1. Running `python dispatch.py "question"` results in a PDF appearing on the reMarkable within 5 minutes, with no other actions required.
2. When relevant sources exist in `sources/`, the agent correctly identifies and incorporates them.
3. The PDF is readable and well-formatted on the reMarkable's e-ink display.

## Biggest Unknowns

1. **Gemini function calling + Search grounding in the same session** — can the model use custom tools (list_sources, send_to_remarkable) and Google Search grounding simultaneously, or do these need to be separate calls?
2. **PDF formatting for e-ink** — what pandoc template / CSS produces the best reading experience on reMarkable's display?
