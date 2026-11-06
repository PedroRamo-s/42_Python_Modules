from .factory import CreatureFactory
from .creature import Creature
from . import creatures


class FlameFactory(CreatureFactory):
    def create_base(self) -> Creature:
        flameling: creatures.Flameling = creatures.Flameling(
            "flameling",
            "fire"
        )
        return flameling

    def create_evolved(self) -> Creature:
        pyrodon: creatures.Pyrodon = creatures.Pyrodon(
            "pyrodon",
            "Flying/Fire"
        )
        return pyrodon


class WaterFactory(CreatureFactory):
    def create_base(self) -> Creature:
        aquabub: creatures.Aquabub = creatures.Aquabub(
            "aquabub",
            "water"
        )
        return aquabub

    def create_evolved(self) -> Creature:
        torragon: creatures.Torragon = creatures.Torragon(
            "torragon",
            "water"
        )
        return torragon
