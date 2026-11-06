#!usr/bin/env python3

from alchemy.potions import strenght_potion
from ..elements import create_air
import elements


def lead_to_gold() -> str:
    return (f"Recipe transmuting Lead to Gold:"
            f" brew '{create_air()}' and '{strenght_potion()}'"
            f"mixed with '{elements.create_fire()}'")
