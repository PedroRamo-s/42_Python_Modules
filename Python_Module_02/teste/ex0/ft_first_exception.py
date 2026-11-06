#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    return (int(temp_str, 10))


def test_temperature() -> None:
    print("=== Garden Temperature ===")
    print("")
    temp_str_1: str = "25"
    print(f"input data is '{temp_str_1}'")
    try:
        temperature_1: int = input_temperature(temp_str_1)
        print(f"Temperature is now {temperature_1}°C")
    except ValueError:
        print(f"Caught input_temperature error: "
              f"invalid literal for int() with base 10: '{temp_str_1}'")
    print("")
    temp_str_2: str = "abc"
    print(f"input data is '{temp_str_2}'")
    try:
        temperature_2: int = input_temperature(temp_str_2)
        print(f"Temperature is now {temperature_2}°C")
    except ValueError:
        print(f"Caught input_temperature error: "
              f"invalid literal for int() with base 10: '{temp_str_2}'")
    print("")
    print("All tests completed - program didn't crash!")
    return


def main() -> None:
    test_temperature()


if __name__ == "__main__":
    main()
