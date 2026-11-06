#!usr/bin/env python3

import alchemy.grimoire as grimoire


def main() -> None:
    print("=== Kaboom 0 ===")
    print("Using grimoire module directly")
    print(f"Testing record light spell: "
          f"Spell recorded: Fantasy "
          f"{grimoire.light_spell_record('Fantasy', 'earth, wind, fire')}")


if __name__ == "__main__":
    main()
