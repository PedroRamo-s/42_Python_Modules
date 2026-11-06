#!usr/bin/env python3

import math


def get_player_pos() -> tuple:
    while True:
        values = input("Enter new coordinates as floats in format 'x,y,z':")
        coordinates = values.split(",")
        if len(coordinates) != 3:
            print("Invalid syntax")
            continue
        try:
            for value in coordinates:
                float(value)
        except ValueError as e:
            print(f"Error on parameter '{value}': {e}")
            continue
        tuple = (float(coordinates[0]),
                 float(coordinates[1]), float(coordinates[2]))
        return tuple


def ft_coordinate_system() -> None:
    print("=== Game Coordinate System ===")
    print("Get a first set of coordinates")
    coordinates_1 = get_player_pos()
    x, y, z = coordinates_1
    print(f"Got a first tuple: {coordinates_1}")
    print(f"It include: X={x}, Y={y}, Z={z}")
    distance: float = round(math.sqrt(((x - 0)*(x - 0)) +
                            ((y - 0)*(y - 0)) + ((z - 0)*(z - 0))), 4)
    print(f"Distance to center: {distance}")
    print()
    print("Get a second set of coordinates")
    coordinates_2 = get_player_pos()
    a, b, c = coordinates_2
    distance_2: float = round(math.sqrt(((a - x)*(a - x)) +
                              ((b - y)*(b - y)) + ((c - z)*(c - z))), 4)
    print(f"Distance between the 2 sets of coordinates: {distance_2}")


def main() -> None:
    ft_coordinate_system()


if __name__ == "__main__":
    main()
