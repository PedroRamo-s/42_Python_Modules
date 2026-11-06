#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, message: str = "Something went wrong") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)


def plant_checker(plant: str) -> None:
    raise PlantError(f"The {plant} plant is wilting!")


def water_error(amount: int) -> None:
    if amount < 20:
        raise WaterError("Not enough water in the tank!")


def custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===\n")
    print("Testing PlantError...")
    try:
        plant_checker("tomato")
    except PlantError as e:
        print(f"Caught {type(e).__name__}: {e}\n")
    print("Testing WaterError...")
    try:
        water_error(5)
    except WaterError as e:
        print(f"Caught {type(e).__name__}: {e}\n")
    print("Testing catching all garden errors...")
    try:
        plant_checker("tomato")
    except GardenError as e:
        print(f"Caught {type(e).__name__} {e}")
    try:
        water_error(10)
    except GardenError as e:
        print(f"Caught {type(e).__name__}: {e}\n")
    print("All custom error types work correctly!")


def main() -> None:
    custom_errors()


if __name__ == "__main__":
    main()
