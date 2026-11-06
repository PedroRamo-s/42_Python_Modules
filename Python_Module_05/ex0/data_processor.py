#!usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._data: list[tuple[int, str]] = []
        self._next_rank: int = 0

    def output(self) -> tuple[int, str]:
        return (self._data.pop(0))

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float, list)):
            if isinstance(data, (int, float)):
                return True
            else:
                for item in data:
                    if not isinstance(item, (int, float)):
                        return False
                return True
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not isinstance(data, (int, float, list)):
            raise Exception("Improper numeric data")
        else:
            if isinstance(data, list):
                for item in data:
                    if not isinstance(item, (float, int)):
                        raise Exception("Improper numeric data")
                    else:
                        self._data.append((self._next_rank, str(item)))
                        self._next_rank += 1
            else:
                self._data.append((self._next_rank, str(data)))
                self._next_rank += 1


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (str, list)):
            if isinstance(data, str):
                return True
            else:
                for item in data:
                    if not isinstance(item, str):
                        return False
                return True
        return False

    def ingest(self, data: str | list[str]) -> None:
        if not isinstance(data, (str, list)):
            raise Exception("Invalid data")
        else:
            if isinstance(data, list):
                for item in data:
                    if not isinstance(item, str):
                        raise Exception("Invalid data")
                    else:
                        self._data.append((self._next_rank, item))
                        self._next_rank += 1
            else:
                self._data.append((self._next_rank, data))
                self._next_rank += 1


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (dict, list)):
            if isinstance(data, dict):
                for key, value in data.items():
                    if not isinstance(key, str) or not isinstance(value, str):
                        return False
                return True

            else:
                for dictionary in data:
                    if not isinstance(dictionary, dict):
                        return False
                    else:
                        for key, value in dictionary.items():
                            if (not isinstance(key, str)
                                    or not isinstance(value, str)):
                                return False
                return True
        return False

    def ingest(self, data: dict | list[dict[str, str]]) -> None:
        if not isinstance(data, (dict, list)):
            raise Exception("invalid data")
        else:
            if isinstance(data, list):
                for item in data:
                    if not isinstance(item, dict):
                        raise Exception("Invalid data")
                    else:
                        for key, value in item.items():
                            if (not isinstance(key, str)
                                    or not isinstance(value, str)):
                                raise Exception("invalid data")
                        self._data.append((self._next_rank, str(item)))
                        self._next_rank += 1
            else:
                self._data.append((self._next_rank, str(data)))
                self._next_rank += 1


def main() -> None:
    print("=== Code Nexus - Data Processor ===\n")
    print("Testing Numeric Processor...")
    num_processor: NumericProcessor = NumericProcessor()
    print(f"Trying to validate input '42': {num_processor.validate(42)}")
    print(f"Trying to validate input 'Hello': "
          f"{num_processor.validate('Hello')}")
    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        num_processor.ingest('foo')
    except Exception as e:
        print(f"Got exception: {e}")
    print("Processing data: [1, 2, 3, 4, 5]")
    num_processor.ingest([1, 2, 3, 4, 5])
    print("Extracting 3 values...")
    for i in range(3):
        print(f"Numeric value {i}: {num_processor.output()[1]}")
    print()

    print("Testing Text Processor...")
    txt_processor: TextProcessor = TextProcessor()
    print(f"Trying to validate input '42': {txt_processor.validate(42)}")
    print("Processing data ['Hello', 'Nexux', 'World']")
    txt_processor.ingest(['Hello', 'Nexux', 'World'])
    print("Extracting 1 value...")
    print(f"Text value 0: {txt_processor.output()[1]}\n")

    print("Testing Log processor...")
    log_processor: LogProcessor = LogProcessor()
    print(f"Trying to validate input 'Hello': {log_processor.validate(42)}")
    print("Processing data: [{'log_level': 'NOTICE', 'log_message':"
          " 'Connection to server'}, {'log_level': 'ERROR"
          "', 'log_message': 'Unauthorized access!!'}]")
    input: list = [
        {'log_level': 'NOTICE', 'log_message': 'Connection to server'},
        {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}
    ]
    log_processor.ingest(input)
    print("Extracting 2 values...")
    for i in range(2):
        rank, message = log_processor.output()
        print(f"Log entry {i}: {message}")


if __name__ == "__main__":
    main()
