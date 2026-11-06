from ex0 import factory
from . import creatures


class HealingCreatureFactory(factory.CreatureFactory):
    def create_base(self) -> creatures.Sproutling:
        return creatures.Sproutling("Sproutling", "Grass")

    def create_evolved(self) -> creatures.Bloomelle:
        return creatures.Bloomelle("Bloomelle", "Fairy/Grass")


class TransformCreatureFactory(factory.CreatureFactory):
    def create_base(self) -> creatures.Shiftling:
        return creatures.Shiftling("Shiftling", "Normal")

    def create_evolved(self) -> creatures.Morphagon:
        return creatures.Morphagon("Morphagon", "Normal/Dragon")
