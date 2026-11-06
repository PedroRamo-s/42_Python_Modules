#!usr/bin/env python3

import random
import typing

players = [
    "bob",
    "alice",
    "dylan",
    "charlie"
]

actions = [
    "attack",
    "defend",
    "dodge",
    "parry",
    "run",
    "eat",
    "sleep",
    "grab",
    "move",
    "swim",
    "climb",
    "release"
]


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    while True:
        player = random.choice(players)
        action = random.choice(actions)
        yield (player, action)


def consume_event(
        event_list: list
        ) -> typing.Generator[tuple[str, str], None, None]:
    while (len(event_list) != 0):
        chosen_event = random.choice(event_list)
        event_list.remove(chosen_event)
        yield chosen_event


def ft_data_stream() -> None:
    print("=== Game Data Stream Processor ===")
    event_generator = gen_event()
    for i in range(1000):
        event = next(event_generator)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")
    print()
    event_list = [

    ]
    for i in range(10):
        event = next(event_generator)
        event_list.append(event)
    print(f"Built list of {len(event_list)} events: {event_list}\n")

    for event in consume_event(event_list):
        print(f"Got event from list: {event}\n")
        print(f"Remains in list: {event_list}\n")


def main() -> None:
    ft_data_stream()


if __name__ == "__main__":
    main()
