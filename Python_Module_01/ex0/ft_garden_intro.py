#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name: str = name
        self.height: float = height
        self.age: int = age


def ft_garden_intro() -> None:
    plant = Plant("Rose", 25, 30)
    print("=== Welcome to My Garden ===")
    print(f"Plant: {plant.name}")
    print(f"Height: {plant.height}cm")
    print(f"Age: {plant.age} days")
    print("=== End of Program ===")


def main() -> None:
    ft_garden_intro()


if __name__ == "__main__":
    main()
