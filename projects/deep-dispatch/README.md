# Deep Dispatch

A CLI agent powered by Gemini. Type a research question — a PDF appears on your reMarkable.

**Phase: Discover**
**Brief:** [`briefs/project-feature-brief.md`](briefs/project-feature-brief.md)

## What It Does

1. Reads your local NotebookLM sources manifest
2. Uses Gemini to identify which sources are relevant to your question
3. Runs deep research with Google Search grounding
4. Converts the report to a styled PDF
5. Emails it to your reMarkable

## Usage

```bash
python dispatch.py "What is the current state of spatial computing hardware?"
```

## Setup

```bash
pip install -r requirements.txt
brew install pandoc
cp .env.example .env
# Fill in: GEMINI_API_KEY, REMARKABLE_EMAIL, GMAIL_ADDRESS, GMAIL_APP_PASSWORD
```

## Adding Your NotebookLM Sources

Export your NotebookLM project content (PDF, markdown, or text) into the `sources/` directory.
Then add an entry to `sources/manifest.json`:

```json
{
  "id": "my-project",
  "title": "My NotebookLM Project Title",
  "topics": ["brief description of what this covers"],
  "file": "sources/my-project.md"
}
```

The agent reads this manifest on every run and decides which sources to include.
