#!usr/bin/env python3

import sys


def ft_ancient_text() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
    else:
        print("=== Cyber Archives Recovery ===")
        print(f"Accessing file '{sys.argv[1]}'")
        try:
            file = open(sys.argv[1])
            file_contents = file.read()
        except (FileNotFoundError, PermissionError) as e:
            print(f"Error opening file {sys.argv[1]}: {e}")
            return
        print("---\n")
        print(f"{file_contents}\n")
        print("---")
        file.close()
        print(f"File '{sys.argv[1]}' closed.")


def main() -> None:
    ft_ancient_text()


if __name__ == "__main__":
    main()
