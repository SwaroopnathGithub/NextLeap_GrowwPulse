# Understanding Groww's Charges — A Plain-Language Explainer

**Why this exists:** across 12 weeks of Play Store reviews (12,637 reviews, 2026-07-21 to 2026-10-14), fees and charges are the single most consistent complaint theme — 382 mentions, and 60% of reviews using specific fee terms (brokerage, DP charge, AMC, etc.) are 1-2★. The complaint isn't usually that the charges are unfair — it's that users don't know about them until they've already traded and see the deduction. This doc explains what's actually being charged, based on what reviewers are reacting to, and proposes a fix.

## What users are confused about

### 1. Brokerage charges (the #1 complaint)
Reviewers consistently describe being surprised by brokerage deductions after trading, and several directly compare Groww unfavorably to competitors (Zerodha named repeatedly) on this point.

> "Brokerage fees are too high, DP charge 24 rupees, I have switched to another platform, when I calculate my monthly brokerage charge I am fully shocked" — 1★

> "This application has the highest brokerage charges in comparison to other applications." — 1★

> "Brokerage charge is very very high. This will finish your hard earned profit." — 1★

**The underlying issue:** the charge itself may be standard industry pricing, but it isn't surfaced to the user *before* they place the trade — only after, as a deduction they then have to go looking for an explanation of.

### 2. DP (Depository Participant) charges
Mentioned specifically at ₹24 by at least one reviewer — a charge applied per scrip on sell transactions, standard across Indian brokers, but essentially invisible to most retail users until it shows up.

### 3. Flat per-trade charges for beginners
> "Not for beginners, stock purchase/sell — charges ₹5/trade"

New users in particular seem to arrive expecting "free" trading (a common marketing claim across the industry) and are caught off guard by a flat per-trade fee.

### 4. AMC / annual maintenance charges
Lower volume but same pattern — charges that exist but aren't proactively explained at the point where the user would want to know about them (account opening, not account statement).

## What Groww could do (based on review evidence alone)

1. **Pre-trade cost preview**: show the expected brokerage + DP charge + taxes *before* the user confirms a buy/sell, not just in the post-trade contract note.
2. **A persistent, simple "What you'll pay" page**: one page, plain language, no jargon, listing brokerage %, DP charge, AMC, and any per-trade flat fee — linked from the trade confirmation screen itself.
3. **First-trade nudge**: a one-time explainer shown to new users on their first trade, specifically addressing the "is this really free?" expectation gap.
4. **Monthly charge summary notification**: several reviewers only reacted negatively when they "added it all up" at month-end — a proactive monthly summary (via push notification, not buried in a statement) could reframe this from "hidden fee" to "here's what you paid, and why."

## What this is not

This document is a synthesis of review-text patterns, not Groww's actual fee schedule or official policy. Exact rates, GST/STT treatment, and any charge changes should be confirmed against Groww's official charges page before publishing anything fee-specific to end users.

## Source

Derived from `data/groww_reviews.csv` (12,637 Play Store reviews, last 12 weeks) via `scripts/analyze_reviews.py`. See the companion [Weekly Product Pulse](weekly-product-pulse.md) for the full theme breakdown.
