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
        self._stats = self.Stats()

    class Stats:
        def __init__(self) -> None:
            self._grow_calls: int = 0
            self._age_calls: int = 0
            self._show_calls: int = 0

        def stat_displayer(self) -> None:
            print(f"Stats: {self._grow_calls} grow, "
                  f"{self._age_calls} age, {self._show_calls} show")

    def show(self) -> None:
        print(f"{self._name}: {self._height}cm, "
              f"{self._age} days old")
        self._stats._show_calls += 1

    def grow(self) -> None:
        self._height = round((self._growth + self._height), 1)
        self._stats._grow_calls += 1

    def age(self) -> None:
        self._age += 1
        self._stats._age_calls += 1

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

    @staticmethod
    def age_check(days_old: int) -> bool:
        if days_old > 365:
            return True
        else:
            return False

    @classmethod
    def anon_plant(cls) -> "Plant":
        plant = cls("Anonymous", 0.0, 0, 0.0)
        return plant


class Flower(Plant):
    def __init__(self, color: str, name: str, height: float,
                 age: int, growth: float) -> None:
        super().__init__(name, height, age, growth)
        self._color = color
        self._bloom_status: bool = False

    def bloom(self) -> None:
        self._bloom_status = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")
        if self._bloom_status is False:
            print(f"{self._name} has not bloomed yet")
        elif self._bloom_status is True:
            print(f"{self._name} is blooming beautifully!")


class Seed(Flower):
    def __init__(self, color: str, name: str, height: float,
                 age: int, growth: float) -> None:
        super().__init__(color, name, height, age, growth)
        self._seed_num = 0

    def show(self) -> None:
        super().show()
        if self._bloom_status == 1:
            self._seed_num = 42
        print(f"Seeds: {self._seed_num}")


class Tree(Plant):
    def __init__(self, trunk_diameter: float, name: str,
                 height: float, age: int, growth: float) -> None:
        super().__init__(name, height, age, growth)
        self._trunk_diameter = trunk_diameter
        self._stats: Tree.Stats = Tree.Stats()

    class Stats(Plant.Stats):
        def __init__(self) -> None:
            super().__init__()
            self._prod_shade_calls = 0

        def stat_displayer(self) -> None:
            super().stat_displayer()
            print(f"{self._prod_shade_calls} shade")

    def produce_shade(self) -> None:
        print(f"Tree Oak now produces a shade of {self._height}cm long and "
              f"{self._trunk_diameter}cm wide.")
        self._stats._prod_shade_calls += 1

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
        for day in range(1, days + 1):
            super().grow()
            super().age()
            self._nutritional_value += 1


def show_stats(plant: Plant) -> None:
    plant._stats.stat_displayer()


def ft_garden_analytics() -> None:
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.age_check(30)}")
    print(f"Is 400 days more than a year? -> {Plant.age_check(400)}")
    print("")
    print("=== Flower")
    flower: Flower = Flower("red", "Rose", 15.0, 10, 0.8)
    flower.show()
    print("[statistics for Rose]")
    flower._stats.stat_displayer()
    print("[asking the rose to grow and bloom]")
    flower.grow()
    flower.bloom()
    flower.show()
    print("[statistics for Rose]")
    flower._stats.stat_displayer()
    print("")
    print("=== Tree")
    tree: Tree = Tree(5.0, "Oak", 200.0, 365, 0.2)
    tree.show()
    print("[statistics for Oak]")
    tree._stats.stat_displayer()
    print("[asking the oak to produce shade]")
    tree.produce_shade()
    print("[statistics for Oak]")
    tree._stats.stat_displayer()
    print("=== Seed")
    sunflower: Seed = Seed("yellow", "Sunflower", 80.0, 45, 0.8)
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.age()
    sunflower.bloom()
    sunflower.show()
    print("[statistics for Sunflower]")
    sunflower._stats.stat_displayer()
    print("")
    print("=== Anonymous")
    anon: Plant = Plant.anon_plant()
    anon.show()
    print("[statistics for Unknown plant]")
    anon._stats.stat_displayer()


def main() -> None:
    ft_garden_analytics()


if __name__ == "__main__":
    main()
