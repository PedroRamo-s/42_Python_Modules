#!usr/bin/env python3

from .light_validator import light_validate_ingredients


def light_spell_allowed_ingredients() -> list:
    list = [
        "earth",
        "air",
        "fire",
        "water"
    ]
    return list


def light_spell_record(spell_name: str, ingredients: str) -> str:
    if ("VALID" in light_validate_ingredients(ingredients)):
        return ("Recorded")
    return ("Rejected")
