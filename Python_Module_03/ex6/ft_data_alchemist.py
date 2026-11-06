#!usr/bin/env python3

import random

players = [
    "Alice",
    "bob",
    "Charlie",
    "dylan",
    "Emma",
    "Gregory",
    "john",
    "kevin",
    "Liam",
]


def ft_data_alchemist() -> None:
    print("=== Game Data Alchemist ===\n")
    print(f"Initial list of players: {players}")
    all_capital = [name.capitalize() for name in players]
    print(f"New list with all the names capitalized: {all_capital}")
    some_capital = [name for name in players if name == name.capitalize()]
    print(f"New list of capitalized names only: {some_capital}")

    score_dict = {name: random.randint(1, 1000) for name in all_capital}
    print(f"Score dict: {score_dict}")
    average: float = sum(score_dict.values()) / len(score_dict.keys())
    high_scores = {name: score_dict[name] for name in score_dict
                   if score_dict[name] > average}
    print(f"High scores: {high_scores}")


def main() -> None:
    ft_data_alchemist()


if __name__ == "__main__":
    main()
