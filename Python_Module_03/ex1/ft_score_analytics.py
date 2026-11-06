#!usr/bin/env python3
import sys


def main() -> None:
    print("=== Player Score Analytics ===")
    if (len(sys.argv) < 2):
        print("No scores provided. "
              "Usage: python3 ft_score_analytics.py <score1> <score2> ...")
        return
    scores = []
    for score in sys.argv[1:]:
        try:
            scores.append(int(score))
        except ValueError:
            print(f"Invalid parameter: '{score}'")
            continue
    if not scores:
        print("No scores provided. "
              "Usage: python3 ft_score_analytics.py <score1> <score2> ...")
        return
    total_players: int = len(scores)
    average_score: float = sum(scores) / total_players
    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores)}")
    print(f"Total score: {sum(scores)}")
    print(f"Average score: {average_score}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {(max(scores) - min(scores))}")


if __name__ == "__main__":
    main()
