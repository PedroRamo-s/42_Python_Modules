#!/usr/bin/env python3

from ex1 import HealingCreatureFactory, TransformCreatureFactory


def main() -> None:
    Healing_Factory = HealingCreatureFactory()
    sproutling = Healing_Factory.create_base()
    print("Testing Creature with healing capability")
    print("base: ")
    sproutling.describe()
    print(f"{sproutling.attack()}")
    sproutling.heal(sproutling)
    print("evolved:")
    bloomelle = Healing_Factory.create_evolved()
    bloomelle.describe()
    print(f"{bloomelle.attack()}")
    bloomelle.heal(bloomelle)
    print("\n")
    print("Testing Creature with transform capability")
    print("base: ")

    Transforming_Factory = TransformCreatureFactory()
    shiftling = Transforming_Factory.create_base()
    shiftling.describe()
    print(f"{shiftling.attack()}")
    shiftling.transform()
    print(f"{shiftling.attack()}")
    shiftling.revert()
    print("Evolved: ")
    morphagon = Transforming_Factory.create_evolved()
    morphagon.describe()
    print(f"{morphagon.attack()}")
    morphagon.transform()
    print(f"{morphagon.attack()}")
    morphagon.revert()


if __name__ == ("__main__"):
    main()
