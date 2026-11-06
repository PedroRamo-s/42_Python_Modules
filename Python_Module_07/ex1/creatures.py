from . import capabilities
from ex0 import creature


class Sproutling(creature.Creature, capabilities.HealCapability):
    def attack(self) -> str:
        return (f"{self._name} uses Vine Whip!")

    def heal(self, target: creature.Creature):
        print(f"{self._name} heals {target._name} for a small amount")


class Bloomelle(creature.Creature, capabilities.HealCapability):
    def attack(self) -> str:
        return (f"{self._name} uses Petal Dance!")

    def heal(self, target: creature.Creature):
        print(f"{self._name} heals {target._name} for a large amount")


class Shiftling(creature.Creature, capabilities.TransformCapability):
    def attack(self) -> str:
        if (self._state is False):
            return (f"{self._name} attacks normally")
        else:
            return (f"{self._name} performs a boosted strike!")

    def transform(self):
        print(f"{self._name} shift into a sharper form!")
        self._state = True

    def revert(self):
        print(f"{self._name}  returns to normal.")
        self._state = False


class Morphagon(creature.Creature, capabilities.TransformCapability):
    def attack(self) -> str:
        if (self._state is False):
            return (f"{self._name} attacks normally")
        else:
            return (f"{self._name} unleashes a devastating morph strike!")

    def transform(self):
        print(f"{self._name} morphs into a dragonic battle form!")
        self._state = True

    def revert(self):
        print(f"{self._name} stabilizes its form.")
        self._state = False
