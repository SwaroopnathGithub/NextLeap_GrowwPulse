"""Quick keyword-frequency pass over scraped Groww reviews to surface candidate themes."""
import csv
import io
import re
import sys
from collections import Counter

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

IN_PATH = "data/groww_reviews.csv"

THEME_KEYWORDS = {
    "fees_charges": [
        "fee", "fees", "charge", "charges", "charged", "deduct", "deducted",
        "deduction", "hidden charge", "amc", "brokerage", "commission",
        "gst", "stt", "convenience fee", "platform fee",
    ],
    "kyc_account": [
        "kyc", "verification", "verify", "account open", "signup", "sign up",
        "login", "otp", "aadhaar", "pan card",
    ],
    "withdrawal_payout": [
        "withdraw", "withdrawal", "payout", "refund", "money stuck",
        "funds stuck", "not credited",
    ],
    "app_performance": [
        "crash", "crashing", "bug", "glitch", "slow", "lag", "freeze",
        "not loading", "error", "hang",
    ],
    "customer_support": [
        "support", "customer care", "customer service", "response",
        "no reply", "helpline", "complaint",
    ],
    "ui_ux": [
        "interface", "ui", "ux", "design", "easy to use", "user friendly",
        "confusing",
    ],
    "order_execution": [
        "order", "execution", "trade", "buy", "sell", "limit order",
        "stop loss", "delay in order",
    ],
    "ipo": ["ipo", "allotment", "apply"],
    "mutual_funds": ["mutual fund", "sip", "nav"],
}

FEE_SPECIFIC = [
    "amc", "brokerage", "hidden charge", "hidden fee", "unexpected charge",
    "deducted without", "charged without", "convenience fee", "platform fee",
    "demat charge", "annual charge", "maintenance charge",
]


def load_reviews():
    with open(IN_PATH, encoding="utf-8") as f:
        return list(csv.DictReader(f))


def main():
    rows = load_reviews()
    print(f"Loaded {len(rows)} reviews\n")

    scores = Counter(r["score"] for r in rows)
    print("Rating distribution:", dict(sorted(scores.items())))

    low_rating = [r for r in rows if r["score"] in ("1", "2")]
    print(f"\n1-2 star reviews: {len(low_rating)} ({len(low_rating)/len(rows)*100:.1f}%)\n")

    theme_counts = Counter()
    theme_hits = {k: [] for k in THEME_KEYWORDS}
    for r in rows:
        text = (r["content"] or "").lower()
        for theme, kws in THEME_KEYWORDS.items():
            if any(kw in text for kw in kws):
                theme_counts[theme] += 1
                if len(theme_hits[theme]) < 3:
                    theme_hits[theme].append(r["content"][:140])

    print("Theme frequency (review mentions at least one keyword):")
    for theme, count in theme_counts.most_common():
        pct = count / len(rows) * 100
        print(f"  {theme:20s} {count:5d}  ({pct:4.1f}%)")

    print("\n--- Fee/charge confusion deep dive ---")
    fee_reviews = [r for r in rows if any(kw in (r["content"] or "").lower() for kw in FEE_SPECIFIC)]
    print(f"Reviews mentioning specific fee/charge terms: {len(fee_reviews)}")
    fee_low = [r for r in fee_reviews if r["score"] in ("1", "2")]
    print(f"  of which 1-2 star: {len(fee_low)} ({len(fee_low)/max(len(fee_reviews),1)*100:.1f}%)")
    print("\nSample fee/charge complaints:")
    for r in fee_reviews[:10]:
        print(f"  [{r['score']}* | {r['at'][:10]}] {r['content'][:160]}")

    print("\n--- Sample snippets per theme ---")
    for theme, samples in theme_hits.items():
        if samples:
            print(f"\n{theme}:")
            for s in samples:
                print(f"  - {s}")


if __name__ == "__main__":
    main()
