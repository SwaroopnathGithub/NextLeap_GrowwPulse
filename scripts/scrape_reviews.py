"""Scrape Groww app Play Store reviews from the last ~12 weeks and save to CSV."""
import csv
import datetime
import sys

from google_play_scraper import Sort, reviews

APP_ID = "com.nextbillion.groww"
WEEKS_BACK = 12
CUTOFF = datetime.datetime.now() - datetime.timedelta(weeks=WEEKS_BACK)
OUT_PATH = "data/groww_reviews.csv"

FIELDS = [
    "reviewId",
    "userName",
    "score",
    "at",
    "content",
    "thumbsUpCount",
    "appVersion",
    "replyContent",
]


def fetch_all():
    collected = []
    token = None
    batch_size = 200
    max_batches = 100  # safety cap

    for _ in range(max_batches):
        result, token = reviews(
            APP_ID,
            lang="en",
            country="in",
            sort=Sort.NEWEST,
            count=batch_size,
            continuation_token=token,
        )
        if not result:
            break
        collected.extend(result)

        oldest_in_batch = min(r["at"] for r in result)
        print(
            f"Fetched {len(result)} reviews, oldest so far: {oldest_in_batch}",
            file=sys.stderr,
        )
        if oldest_in_batch < CUTOFF:
            break
        if token is None:
            break

    return collected


def main():
    all_reviews = fetch_all()
    filtered = [r for r in all_reviews if r["at"] >= CUTOFF]

    with open(OUT_PATH, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS, extrasaction="ignore")
        writer.writeheader()
        for r in filtered:
            row = {k: r.get(k) for k in FIELDS}
            writer.writerow(row)

    print(f"Total fetched: {len(all_reviews)}", file=sys.stderr)
    print(f"Within last {WEEKS_BACK} weeks (cutoff {CUTOFF.date()}): {len(filtered)}", file=sys.stderr)
    print(f"Saved to {OUT_PATH}", file=sys.stderr)


if __name__ == "__main__":
    main()
