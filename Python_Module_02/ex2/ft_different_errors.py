#!/usr/bin/env python3

def garden_operations(operation_number: int) -> None:
    if (operation_number == 0):
        s: str = "abc"
        int(s)
    if (operation_number == 1):
        10 / 0
    if (operation_number == 2):
        file = open("/non/existent/file")
        _ = file
    if (operation_number == 3):
        "abc" + 2  # type: ignore
    return


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    for operation in range(5):
        print(f"Testing operation {operation}...")
        try:
            garden_operations(operation)
            print("Operation completed successfully")
        except (ValueError, ZeroDivisionError, FileNotFoundError,
                TypeError) as e:
            print(f"Caught {type(e).__name__}: {e}")
    print("\n")
    print("All error types tested successfully!")


def main() -> None:
    test_error_types()


if __name__ == "__main__":
    main()
