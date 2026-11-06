#!usr/bin/env python3

def light_validate_ingredients(ingredients: str) -> str:
    from alchemy.grimoire import light_spell_allowed_ingredients
    for ingredient in light_spell_allowed_ingredients():
        if ingredient.lower() in ingredients.lower():
            return (f"{ingredients} - VALID")
    return (f"{ingredients} - INVALID")
