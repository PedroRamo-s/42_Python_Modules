#!usr/bin/env python3

from alchemy.grimoire import dark_spellbook


def main() -> None:
    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directly")
    print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")
    print(f"Testing record dark spell: "
          f"Spell recorded: Dark Fantasy "
          f"{dark_spellbook.dark_spell_record('Evil Fantasy', 'bats and frogs')}")


if __name__ == "__main__":
    main()
