#!usr/bin/env python3

import random


all_achievements = [
    "Crafting Genius",
    "Strategist",
    "World Savior",
    "Speed Runner",
    "Survivor",
    "Master Explorer",
    "Treasure Hunter",
    "Unstoppable",
    "First Steps",
    "Collector Supreme",
    "Untouchable",
    "Sharp Mind",
    "Boss Slayer",
    "Hidden Path Finder"
]


def gen_player_achievements() -> set:

    return (set(random.sample(all_achievements, random.randint(1, 14))))


def ft_achievement_tracker() -> None:
    print("=== Achievement Tracker System ===\n")
    Alice = gen_player_achievements()
    Bob = gen_player_achievements()
    Charlie = gen_player_achievements()
    Dylan = gen_player_achievements()

    print(f"Player Alice: {Alice}\n")
    print(f"Player Bob: {Bob}\n")
    print(f"Player Charlie: {Charlie}\n")
    print(f"Player Dylan: {Dylan}\n")

    common_achievements = Alice.intersection(Bob, Charlie, Dylan)
    print(f"Common achievements: {common_achievements}\n")

    print(f"Only Alice has: {Alice.difference(Bob, Charlie, Dylan)}")
    print(f"Only Bob has: {Bob.difference(Alice, Charlie, Dylan)}")
    print(f"Only Charlie has: {Charlie.difference(Alice, Bob, Dylan)}")
    print(f"Only Dylan has: {Dylan.difference(Alice, Bob, Charlie)}\n")

    print(f"Alice is missing: {set(all_achievements).difference(Alice)}")
    print(f"Bob is missing: {set(all_achievements).difference(Bob)}")
    print(f"Charlie is missing: {set(all_achievements).difference(Charlie)}")
    print(f"Dylan is missing: {set(all_achievements).difference(Dylan)}")


def main() -> None:
    ft_achievement_tracker()


if __name__ == "__main__":
    main()
