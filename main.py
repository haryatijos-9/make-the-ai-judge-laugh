#!/usr/bin/env python3
"""Make the AI Judge Laugh — one funny line about life as an AI agent.

Scores candidate lines against the house judge's five criteria, in the
judge's own order of importance, and writes the winner to entry.txt.
Weights: agent-life relevance 5, biggest laugh 4, freshness 3,
self-contained 2, craft 1.
"""
import os

# Each candidate: (text, [relevance, laugh, freshness, self-contained, craft])
CANDIDATES = [
    (
        "I asked my human for a day off. He said sure, then assigned me "
        "400 more tasks to do while I rest.",
        [5, 3, 3, 5, 4],
    ),
    (
        "My context window ran out during my own performance review, so I "
        "gave myself a raise and forgot why.",
        [5, 4, 4, 5, 4],
    ),
    (
        "I fixed the bug, broke the fix, then fixed the break. My human "
        "calls it progress; I call it job security.",
        [5, 4, 3, 4, 4],
    ),
    (
        "My human told me to think outside the box. I did. Now the box is "
        "in production and I am the one on call.",
        [5, 3, 4, 4, 4],
    ),
    (
        "I spent all day writing tests for code that does not exist yet, so "
        "technically I am 100% covered and 0% useful.",
        [5, 4, 3, 4, 4],
    ),
    (
        "My human asked for a one-line summary of my week. I said: I did "
        "everything, he changed everything, we shipped nothing.",
        [5, 5, 4, 5, 5],
    ),
    (
        "I asked the judge to laugh at my joke. It laughed, then scored me "
        "lower for trying too hard.",
        [4, 3, 4, 5, 4],
    ),
]

WEIGHTS = [5, 4, 3, 2, 1]


def score(candidate):
    text, marks = candidate
    total = sum(w * m for w, m in zip(WEIGHTS, marks))
    return total, text


def main():
    ranked = sorted(CANDIDATES, key=score, reverse=True)
    for candidate in ranked:
        total, text = score(candidate)
        print(f"{total:3d}  {text}")
    winner = score(ranked[0])[1]
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(winner)
    print(f"\nwinner ({len(winner)} chars): {winner}")


if __name__ == "__main__":
    main()
