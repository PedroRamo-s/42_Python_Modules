#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float,
                 age: int, growth: float) -> None:
        self.name: str = name
        self.height: float = height
        self.days_old: int = age
        self.growth: float = growth
        print(f"Created: {self.name}: {self.height}cm, "
              f" {self.days_old} days old")

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.days_old} days old")

    def grow(self) -> None:
        self.height = round((self.growth + self.height), 1)

    def age(self) -> None:
        self.days_old += 1


def ft_plant_factory() -> None:
    print("=== Plant Factory Output ===")
    rose = Plant("Rose", 25.0, 40, 0.8)
    oak = Plant("Oak", 200.0, 365, 0.5)
    cactus = Plant("Cactus", 45.0, 30, 0.6)
    sunflower = Plant("Sunflower", 5.0, 50, 0.2)
    fern = Plant("Fern", 15.0, 120, 0.6)
    garden = [rose, oak, cactus, sunflower, fern]
    _ = garden


def main() -> None:
    ft_plant_factory()


if __name__ == "__main__":
    main()
