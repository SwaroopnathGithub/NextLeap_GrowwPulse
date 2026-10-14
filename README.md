# GrowwPulse

NextLeap Milestone 5 — a weekly product pulse and fee explainer for the Groww app, built from Play Store reviews, with an n8n workflow (approval-gated) that drafts and queues the deliverables.

**Live site:** see GitHub Pages (enabled on this repo) for the rendered pulse, fee explainer, and sources page.

## Contents

- `data/groww_reviews.csv` — raw scrape of 12,637 Groww Play Store reviews (India store, last 12 weeks, `com.nextbillion.groww`)
- `scripts/scrape_reviews.py` — scraper (`google-play-scraper`)
- `scripts/analyze_reviews.py` — keyword-based theme frequency + fee-confusion deep dive
- `scripts/weekly_pulse_data.py` — week-over-week aggregates
- `docs/` — the static site (GitHub Pages source): home, weekly product pulse, fee explainer, sources & methodology
- `n8n/groww-pulse-workflow.json` — the n8n workflow (Groq-drafted content → human approval gate → Google Docs append + Gmail draft creation, never auto-send)
- `n8n/README.md` — import and configuration steps for the workflow

## Pipeline

1. Scrape Groww's Play Store reviews (last 12 weeks).
2. Analyze for rating trends and recurring themes (keyword-tagged).
3. Feed the stats + representative quotes into an n8n workflow where a Groq-backed LLM drafts the weekly pulse and fee explainer.
4. A human approves before anything is written anywhere.
5. Once approved: append to a tracking Google Doc, create a Gmail draft (never sent).
6. This repo's `docs/` site is the always-visible static version of the same deliverables.

## Caveat

Fee figures discussed in the fee explainer (e.g. DP charge, per-trade charge) reflect what reviewers reported in their own words, not Groww's verified official fee schedule.
