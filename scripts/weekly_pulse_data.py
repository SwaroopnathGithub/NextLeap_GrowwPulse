"""Produce weekly aggregates (ratings, theme mentions) for the product pulse doc."""
import csv
import datetime
import io
import sys
from collections import Counter, defaultdict

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


def load_reviews():
    with open(IN_PATH, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    for r in rows:
        r["at_dt"] = datetime.datetime.fromisoformat(r["at"])
    return rows


def week_key(dt):
    iso = dt.isocalendar()
    return f"{iso[0]}-W{iso[1]:02d}"


def main():
    rows = load_reviews()
    rows.sort(key=lambda r: r["at_dt"])

    weekly_scores = defaultdict(list)
    weekly_themes = defaultdict(Counter)
    weekly_count = Counter()

    for r in rows:
        wk = week_key(r["at_dt"])
        weekly_count[wk] += 1
        weekly_scores[wk].append(int(r["score"]))
        text = (r["content"] or "").lower()
        for theme, kws in THEME_KEYWORDS.items():
            if any(kw in text for kw in kws):
                weekly_themes[wk][theme] += 1

    weeks = sorted(weekly_count.keys())
    print(f"{'Week':10s} {'N':>5s} {'AvgScore':>9s}  Top themes")
    for wk in weeks:
        scores = weekly_scores[wk]
        avg = sum(scores) / len(scores)
        top = weekly_themes[wk].most_common(3)
        top_str = ", ".join(f"{t}:{c}" for t, c in top)
        print(f"{wk:10s} {len(scores):5d} {avg:9.2f}  {top_str}")

    print("\n--- Last 4 weeks vs prior period (fees_charges trend) ---")
    last4 = weeks[-4:]
    prior = weeks[:-4]
    last4_fee = sum(weekly_themes[w]["fees_charges"] for w in last4)
    last4_n = sum(weekly_count[w] for w in last4)
    prior_fee = sum(weekly_themes[w]["fees_charges"] for w in prior)
    prior_n = sum(weekly_count[w] for w in prior)
    print(f"Last 4 weeks: {last4_fee}/{last4_n} = {last4_fee/last4_n*100:.2f}%")
    print(f"Prior weeks:  {prior_fee}/{prior_n} = {prior_fee/prior_n*100:.2f}%")


if __name__ == "__main__":
    main()
