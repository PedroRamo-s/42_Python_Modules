#!/usr/bin/env python3
import importlib
import importlib.metadata

dependencies: dict[str, str] = {
    "pandas": "Data manipulation ready",
    "numpy": "Numerical computation ready",
    "matplotlib": "Visualization ready"
}


def dependency_check(packages: list[str]) -> list[str]:
    missing: list[str] = []
    for package in packages:
        try:
            importlib.import_module(package)
        except ImportError:
            missing.append(package)
    return missing


def pip_poetry() -> None:
    print("DEPENDENCY MANAGER COMPARISON")
    print("PIP:")
    print("- Works by looking into the requirements.txt, and installing the"
          "packages listed there indivdually")
    print("- Uses the the Python environment that is currently active")
    print("- Does not create a venv\n")
    print("POETRY:")
    print("Works by using a pyproject.toml file,"
          "it creates, pins and resolves "
          "all versions into a .lock file, also "
          "creates and manages its own environment\n")


def main() -> None:
    print("LOADING STATUS: Loading programs... \n")
    print("Checking dependencies...\n")
    missing: list[str] = dependency_check(list(dependencies))
    if missing:
        print("Missing Packages: ")
        for package in missing:
            print(f"- {package}")
        print("To install missing packages run: \n")
        print(r"pip install -r requirements.txt, for pip")
        print(r"poetry install, for poetry")
    else:
        pandas = importlib.import_module("pandas")
        numpy = importlib.import_module("numpy")
        plt = importlib.import_module("matplotlib.pyplot")
        for package, description in dependencies.items():
            print(f"[OK] {package} {importlib.metadata.version(package)}"
                  f" - {description}")
        print()
        rng = numpy.random.default_rng()
        matrix_data = rng.integers(0, 1000, 1000)
        data = pandas.DataFrame(matrix_data, columns=["Agents active"])
        pip_poetry()
        print("Analyzing matrix data...\n")
        print("Describe:")
        print(data.describe().round(2))
        print()
        fig, ax = plt.subplots()
        ax.plot(data.index, data["Agents active"])
        ax.set_title("Matrix Analysis")
        ax.set_ylabel("Index")
        ax.set_xlabel("Agents active")
        print("Analysis complete!")
        print("Results saved to matrix_analysis.png")
        plt.savefig("matrix_analysis.png")
        # plt.show()


if __name__ == "__main__":
    main()
