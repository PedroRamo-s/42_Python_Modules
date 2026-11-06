#!usr/bin/env python3
import sys


def main() -> None:
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    if len(sys.argv) < 2:
        print("No arguments provided!")
        print(f"Total arguments provided: {len(sys.argv) - 1}")
    else:
        i: int = 1
        args: int = len(sys.argv) - 1
        print(f"Arguments received: {args}")
        for argument in sys.argv[1:]:
            print(f"Argument {i}: {argument}")
            i += 1
    print(f"Total arguments: {len(sys.argv)}")


if __name__ == "__main__":
    main()
