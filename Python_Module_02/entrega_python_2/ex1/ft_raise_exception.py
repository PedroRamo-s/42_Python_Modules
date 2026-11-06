#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    temp: int = int(temp_str, 10)
    if temp < 0:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
    if temp > 40:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
    return (temp)


def test_temperature() -> None:
    print("=== Garden Temperature ===")
    print("")
    temp_str_1: str = "25"
    print(f"input data is '{temp_str_1}'")
    try:
        temperature_1: int = input_temperature(temp_str_1)
        print(f"Temperature is now {temperature_1}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: "
              f"{e}")
    print("")
    temp_str_2: str = "abc"
    print(f"input data is '{temp_str_2}'")
    try:
        temperature_2: int = input_temperature(temp_str_2)
        print(f"Temperature is now {temperature_2}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: "
              f"{e}")
    print("")
    temp_str_3: str = "100"
    print(f"input data is '{temp_str_3}'")
    try:
        temperature_3: int = input_temperature(temp_str_3)
        print(f"Temperature is now {temperature_3}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: "
              f"{e}")
    print("")
    temp_str_4: str = "-50"
    print(f"input data is '{temp_str_4}'")
    try:
        temperature_4: int = input_temperature(temp_str_4)
        print(f"Temperature is now {temperature_4}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: "
              f"{e}")
    print("")
    print("All tests completed - program didn't crash!")
    return


def main() -> None:
    test_temperature()


if __name__ == "__main__":
    main()
