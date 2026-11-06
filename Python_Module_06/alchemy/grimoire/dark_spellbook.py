#!usr/bin/env python3

from alchemy.grimoire import dark_validate_ingredients


def dark_spell_allowed_ingredients() -> list:
    list = [
        "bats",
        "frogs",
        "arsenic",
        "eyeball"
    ]
    return list


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    if ("VALID" in dark_validate_ingredients(ingredients)):
        return ("Recorded")
    return ("Rejected")
