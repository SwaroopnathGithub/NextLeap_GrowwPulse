# Groww — Weekly Product Pulse

**Period covered:** 2026-07-21 to 2026-10-14 (12 weeks) · **Source:** Google Play Store reviews, `com.nextbillion.groww` (India) · **Sample:** 12,637 reviews · **Generated:** 2026-10-14

## Headline

Overall sentiment stays strong (avg rating hovering 4.3–4.5/5 every week), but a consistent minority of reviewers — just over 1 in 8 — leave a 1 or 2-star review, and the same five themes keep resurfacing week over week. Nothing in the last 12 weeks looks like a new or emerging problem; these are long-running friction points, not a fresh regression.

## Rating distribution (12 weeks)

| Rating | Count | Share |
|---|---|---|
| 5★ | 9,765 | 77.3% |
| 4★ | 1,004 | 7.9% |
| 3★ | 345 | 2.7% |
| 2★ | 212 | 1.7% |
| 1★ | 1,311 | 10.4% |

12.1% of all reviews are 1-2 star.

## Top themes, ranked by mention frequency

| Rank | Theme | Mentions | Share of reviews |
|---|---|---|---|
| 1 | UI/UX | 558 | 4.4% |
| 2 | Fees & charges | 382 | 3.0% |
| 3 | Order execution / trading | 379 | 3.0% |
| 4 | Customer support | 337 | 2.7% |
| 5 | App performance (crashes/lag) | 297 | 2.4% |
| 6 | Mutual funds / SIP | 214 | 1.7% |
| 7 | IPO / allotment | 89 | 0.7% |
| 8 | Withdrawal / payout | 88 | 0.7% |
| 9 | KYC / account opening | 73 | 0.6% |

*UI/UX mentions are mostly positive ("easy to use," "clean interface"); the other themes skew negative — see quotes below.*

## Week-over-week theme volume

| Week | Reviews | Avg score | Top 3 themes (mentions) |
|---|---|---|---|
| 2026-W30 | 465 | 4.48 | order_execution:17, ui_ux:16, fees:13 |
| 2026-W31 | 1,117 | 4.53 | ui_ux:54, order_execution:30, fees:29 |
| 2026-W32 | 1,224 | 4.40 | ui_ux:52, fees:43, order_execution:41 |
| 2026-W33 | 1,113 | 4.41 | ui_ux:44, support:37, app_perf:28 |
| 2026-W34 | 1,084 | 4.45 | ui_ux:39, fees:27, support:26 |
| 2026-W35 | 1,358 | 4.28 | ui_ux:76, fees:60, order_execution:56 |
| 2026-W36 | 1,198 | 4.39 | ui_ux:55, order_execution:43, fees:37 |
| 2026-W37 | 1,060 | 4.39 | ui_ux:52, fees:29, order_execution:29 |
| 2026-W38 | 1,001 | 4.34 | ui_ux:43, support:37, fees:37 |
| 2026-W39 | 1,057 | 4.34 | ui_ux:46, support:35, app_perf:29 |
| 2026-W40 | 871 | 4.48 | ui_ux:32, order_execution:18, support:18 |
| 2026-W41 | 911 | 4.38 | ui_ux:43, support:31, order_execution:30 |

*W42 excluded from this table — partial week at time of scrape (178 reviews).*

Fee/charge mentions did ease slightly in the most recent 4 weeks (2.7% of reviews) versus the prior 8 weeks (3.1%), but the gap is small and the complaint content hasn't changed — it's the same brokerage-pricing confusion throughout, not a resolved issue.

## What's actually being said

**Fees & charges (382 mentions, 60% of the specific-fee-term subset are 1-2★):**
- "Brokerage fees are too high, Dp charge 24 rupees... when I calculate my monthly brokerage charge I am fully shocked" (1★)
- "This application has the highest brokerage charges compared to other applications" (1★)
- "Here Brokerage charge is very very high. This will finish your hard earned profit." (1★)
- Several reviewers explicitly compare to Zerodha as cheaper.
- A recurring secondary complaint: a flat ₹5/trade charge that surprises beginners who expected free trading.

→ See the companion [Fee Explainer](fee-explainer.md) for the detail and a recommended user-facing fix.

**Order execution / trading (379 mentions):** complaints cluster around slow order fills, FNO glitches, and confusion around stop-loss/limit order behavior.

**Customer support (337 mentions):** mixed — several reviewers praise fast, clear responses, but a recurring complaint thread is "no reply" or slow resolution on fund/withdrawal issues specifically.

**App performance (297 mentions):** crashes and lag reported inconsistently, not concentrated in a single app version in this sample — worth a follow-up cut by `appVersion` if engineering wants to investigate further.

**Withdrawal/payout (88 mentions, low volume but high severity):** a handful of reviews describe funds stuck for multiple days with unresolved support tickets — small in volume but reputationally costly (these tend to be long, detailed 1★ reviews).

## Recommendations

1. **Prioritize fee transparency** — brokerage/DP charges are the single most consistent complaint category across all 12 weeks. A pre-trade cost preview or a simple "what you'll pay" explainer (see companion doc) is the highest-leverage fix available from this data alone.
2. **Audit the withdrawal/support loop** — low volume, but these are the reviews most likely to show up in press or social screenshots. Worth a support-ticket SLA check even though it's only 0.7% of the sample.
3. **No action needed on UI/UX** — it's the top-mentioned theme but mostly positive; don't let mention volume alone trigger a redesign.

## Methodology note

Themes are keyword-matched (see `scripts/analyze_reviews.py` for the keyword lists), not LLM-classified — treat percentages as directional signal, not precise topic counts. A review can match multiple themes. Raw data: `data/groww_reviews.csv`.
