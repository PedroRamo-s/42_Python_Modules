from .creature import Creature


class Flameling(Creature):
    def attack(self) -> str:
        return (f"{self._name} uses Ember!")


class Pyrodon(Creature):
    def attack(self) -> str:
        return (f"{self._name} uses Flamethrower!")


class Aquabub(Creature):
    def attack(self) -> str:
        return (f"{self._name} uses Water Gun!")


class Torragon(Creature):
    def attack(self) -> str:
        return (f"{self._name} uses Hydro Pump!")
