#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float,
                 age: int, growth: float) -> None:
        self._name: str = name
        self._height: float = height
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            self._height = 0.0
        else:
            self._height = height
        self._age: int = age
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            self._age = 0
        else:
            self._age = age
        self._growth: float = growth
        print(f"Plant created: {self._name}: {self._height}cm, "
              f" {self._age} days old\n")

    def show(self) -> None:
        print(f"Current state: {self._name}: {self._height}cm, "
              f"{self._age} days old")

    def grow(self) -> None:
        self._height = round((self._growth + self._height), 1)

    def age(self) -> None:
        self._age += 1

    def get_height(self) -> float:
        return self._height

    def set_height(self, new_height: float) -> None:
        if new_height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = new_height
            print(f"Height updated: {self._height}cm")

    def get_age(self) -> int:
        return self._age

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = new_age
            print(f"Age updated: {self._age} days")


def ft_garden_security() -> None:
    print("=== Garden Security System ===")
    plant = Plant("Rose", 15.0, 10, 0.8)
    plant.set_height(25.0)
    plant.set_age(30)
    print("")
    plant.set_height(-10)
    plant.set_age(-10)
    print("")
    plant.show()


def main() -> None:
    ft_garden_security()


if __name__ == "__main__":
    main()
