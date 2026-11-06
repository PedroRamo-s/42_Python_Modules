#!usr/bin/env python3

from alchemy.grimoire import dark_spell_allowed_ingredients


def dark_validate_ingredients(ingredients: str) -> str:
    for ingredient in dark_spell_allowed_ingredients():
        if ingredient.lower() in ingredients.lower():
            return (f"{ingredients} - VALID")
    return (f"{ingredients} - INVALID")
