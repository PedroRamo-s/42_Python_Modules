#!usr/bin/env python3

from ex0 import FlameFactory, WaterFactory, CreatureFactory

flame_factory = FlameFactory()
water_factory = WaterFactory()


def factory_tester(factory: CreatureFactory) -> None:
    print("Testing Factory")
    creature_1 = factory.create_base()
    creature_1.describe()
    print(f"{creature_1.attack()}")
    creature_2 = factory.create_evolved()
    creature_2.describe()
    # creature_2.attack()
    print(f"{creature_2.attack()}")


def battle_tester(
    flame_factory: FlameFactory,
    water_factory: WaterFactory
) -> None:
    print("Testing Battle")

    flameling = flame_factory.create_base()
    flameling.describe()
    print("vs")
    aquabub = water_factory.create_base()
    aquabub.describe()
    print("Fight!")
    print(f"{flameling.attack()}")
    print(f"{aquabub.attack()}")


def main() -> None:
    fire = FlameFactory()
    water = WaterFactory()
    factory_tester(fire)
    print("\n")
    factory_tester(water)
    print("\n")
    battle_tester(fire, water)


if __name__ == ("__main__"):
    main()
