#!usr/bin/env python3

import sys
import typing


def transform(content: str) -> str:
    splitted_contents = content.split("\n")
    for i in range(len(splitted_contents)):
        splitted_contents[i] += "#"
    joined_contents = "\n".join(splitted_contents)
    return (joined_contents)


def save(content: str) -> None:
    print("Enter new file name (or empty):", end=" ")
    sys.stdout.flush()
    new_file = sys.stdin.readline().replace("\n", "")
    if not new_file:
        print("Not saving data")
        return
    try:
        file: typing.IO[str] = open(new_file, "w")
        file.write(content)
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error opening file {new_file}: {e}", file=sys.stderr)
        file.close()
        return
    print(f"Saving data to '{new_file}'")
    print(f"Data saved in file '{new_file}'")
    file.close()


def ft_ancient_text() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
    else:
        print("=== Cyber Archives Recovery ===")
        print(f"Accessing file '{sys.argv[1]}'")
        try:
            file: typing.IO[str] = open(sys.argv[1])
            file_contents = file.read()
        except (FileNotFoundError, PermissionError) as e:
            print(f"Error opening file {sys.argv[1]}: {e}", file=sys.stderr)
            return
        print("---\n")
        print(f"{file_contents}\n")
        print("---")
        file.close()
        print(f"File '{sys.argv[1]}' closed.")
        print("")
        transformed_contents = transform(file_contents)
        print("Transform data: ")
        print("---\n")
        print(f"{transformed_contents}\n")
        print("---")
        save(transformed_contents)


def main() -> None:
    ft_ancient_text()


if __name__ == "__main__":
    main()
