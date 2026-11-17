#!usr/bin/env python3

def secure_archive(filename: str, action: str = "",
                   to_write: str = "") -> tuple:
    if action == "r":
        try:
            with open(filename) as file:
                content = file.read()
                return (True, content)
        except (FileNotFoundError, PermissionError) as e:
            error_message = f"{e}"
            return (False, error_message)
    elif action == "w":
        try:
            with open(filename, "w") as file:
                file.write(to_write)
                return (True, "Content succesfully written to file")
        except (FileNotFoundError, PermissionError) as e:
            error_message2: str = f"{e}"
            return (False, error_message2)
    else:
        return (False, "Invalid input")


def main() -> None:
    print("=== Cyber Archives Security ===\n")
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(f"{secure_archive('nonexistent.txt', 'r')}\n")
    print("Using 'secure_archive' to read from an inaccessible file:")
    print(f"{secure_archive('inaccessible.txt', 'r')}\n")
    print("Using 'secure_archive' to read from a regular file:")
    print(f"{secure_archive('ancient_fragment.txt', 'r')}\n")
    print("Using 'secure_archive' to write previous content to a new file:")
    print(f"{secure_archive('ancient_fragment.txt', 'w', 'ABCDE')}\n")


if __name__ == "__main__":
    main()
