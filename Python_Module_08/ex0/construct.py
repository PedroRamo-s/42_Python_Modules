#!usr/bin/env python3

import sys
import os
import site


def main() -> None:
    if (sys.prefix != sys.base_prefix):
        print("MATRIX STATUS: Welcome to the construct\n")
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
        print("Environment Path: \n", sys.prefix)

        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("The global system.\n")

        print("Package installation path: ")
        print(site.getsitepackages()[0])
    else:
        print("MATRIX STATUS: You're still plugged in")
        print("Virtual Environment: None detected\n")
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install\n")
        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print(r"matrix_env\Scripts\activate # On Windows\n")
        print("Then run this program again")


if __name__ == ("__main__"):
    main()
