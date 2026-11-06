#!usr/bin/env python3

import sys


def main() -> None:
    print("=== Inventory System Analysis ===")
    inventory = {}
    for argument in sys.argv[1:]:
        current = argument.split(":")
        if len(current) != 2:
            print(f"Error - invalid parameter: '{argument}'")
            continue
        item = current[0]
        quantity = current[1]
        try:
            amount: int = int(quantity)
        except ValueError as e:
            print(f"Quantity error for '{item}': {e}")
            continue
        if item in inventory:
            print(f"Redundant item '{item}' - discarding")
            continue
        inventory.update({item: amount})

    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(inventory.keys())}")
    print(f"Total quantity of the {len(inventory.keys())} items: "
          f"{sum(inventory.values())}")

    if not inventory:
        print("Inventory is empty, no item abundance")
    else:

        for item in inventory:
            percentage = (inventory[item] / sum(inventory.values())) * 100
            print(f"Item {item} represents {round(percentage, 1)}%")

        most_item: str
        most_amount: int = 0
        for item in inventory:
            if inventory[item] > most_amount:
                most_item = item
                most_amount = inventory[item]
        print(f"Item most abundant: {most_item} with quantity {most_amount}")

        least_item: str
        least_amount: int = most_amount
        for item in inventory:
            if inventory[item] < least_amount:
                least_item = item
                least_amount = inventory[item]
        print(f"Item least abundant: {least_item}"
              f"with quantity {least_amount}")


if __name__ == "__main__":
    main()
