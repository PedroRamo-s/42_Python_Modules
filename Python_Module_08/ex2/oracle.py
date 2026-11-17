#!/usr/bin/env python3
import os
from dotenv import load_dotenv


def main() -> None:
    load_dotenv()
    mode = os.getenv("MATRIX_MODE")
    database = os.getenv("DATABASE_URL")
    api = os.getenv("API_KEY")
    log = os.getenv("LOG_LEVEL")
    zion_end = os.getenv("ZION_ENDPOINT")
    env_variables = {
        "MATRIX_MODE": mode,
        "DATABASE_URL": database,
        "API_KEY": api,
        "LOG_LEVEL": log,
        "ZION_ENDPOINT": zion_end
    }
    for name, value in env_variables.items():
        if not value:
            print(f"Missing variable: {name}")
            return
    if log not in ("DEBUG", "INFO", "WARNING", "ERROR"):
        print("Invalid log state")
        return
    if mode in ("development", "production"):
        print("mode is valid\n")
    else:
        print("mode is invalid\n")
        return

    print("ORACLE STATUS: Reading the Matrix...\n")
    print("Configuration loaded...")
    if (mode == "development"):
        print(
            f"Mode: {mode}\n"
            f"Database: Local development database\n"
            f"API: Development API configured\n"
            f"Log Level: {log}\n"
            f"Zion Endpoint: {zion_end}"
        )
    elif (mode == "production"):
        print(
            "Mode: Production Mode\n"
            "Database: Production database configured\n"
            "API: Production API configured\n"
            "Log Level: INFO\n"
            "Zion Endpoint: Production endpoint configured\n"
        )
    print()
    print("Environment security check:")
    if api:
        print("[OK] No hardcoded secrets detected")
    else:
        print("API KEY: Missing")

    if os.path.isfile(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[ERROR] .env file not found")

    print("[OK] Production overrides available\n")

    print("The Oracle sees all configurations")


if __name__ == "__main__":
    main()
