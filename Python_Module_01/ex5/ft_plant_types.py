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

    def show(self) -> None:
        print(f"{self._name}: {self._height}cm, "
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


class Flower(Plant):
    def __init__(self, color: str, name: str, height: float,
                 age: int, growth: float) -> None:
        super().__init__(name, height, age, growth)
        self._color = color
        self._bloom_status = 0

    def bloom(self) -> None:
        self._bloom_status = 1

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")
        if (self._bloom_status == 0):
            print("Rose has not bloomed yet")
        if (self._bloom_status == 1):
            print("Rose is blooming beautifully!")


class Tree(Plant):
    def __init__(self, trunk_diameter: float, name: str,
                 height: float, age: int, growth: float) -> None:
        super().__init__(name, height, age, growth)
        self._trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(f"Tree Oak now produces a shade of {self._height}cm long and "
              f"{self._trunk_diameter}cm wide.")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self._trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(self, harvest_season: str, name: str,
                 height: float, age: int, growth: float) -> None:
        super().__init__(name, height, age, growth)
        self._harvest_seasson = harvest_season
        self._nutritional_value = 0

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self._harvest_seasson}\n"
              f"Nutritional value: {self._nutritional_value}")

    def grow_n_age(self, days: int) -> None:
        for day in range(1, 21):
            super().grow()
            super().age()
            self._nutritional_value += 1


def ft_plant_types() -> None:
    print("=== Garden Plant Types ===")
    print("=== Flower")
    flower = Flower("red", "Rose", 15.0, 10, 0.8)
    flower.show()
    print("[asking the rose to bloom]")
    flower.bloom()
    flower.show()
    print("")
    print("=== Tree")
    tree = Tree(5.0, "Oak", 200.0, 365, 0.2)
    tree.show()
    print("[asking the oak to produce shade]")
    tree.produce_shade()
    print("")
    print("=== Vegetable")
    vegetable = Vegetable("April", "Tomato", 5.0, 10, 2.1)
    vegetable.show()
    print("[make tomato grow and age for 20 days]")
    vegetable.grow_n_age(20)
    vegetable.show()


def main() -> None:
    ft_plant_types()


if __name__ == "__main__":
    main()
