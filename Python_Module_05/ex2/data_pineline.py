#!usr/bin/env python3

from abc import ABC, abstractmethod
import typing


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._data: list[tuple[int, str]] = []
        self._next_rank: int = 0
        self._stats: int = 0

    def output(self) -> tuple[int, str]:
        return (self._data.pop(0))

    @abstractmethod
    def validate(self, data: typing.Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: typing.Any) -> None:
        pass


class ExportPlugin(typing.Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


class CSVExporter:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        exported = [

        ]
        for info in data:
            exported.append(info[1])
        print("CSV Output:")
        print(f"{','.join(exported)}\n")


class JSONExporter:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        exported = [

        ]
        for info in data:
            output: str = f'"item_{info[0]}": "{info[1]}"'
            exported.append(output)
        print("JSON Output:")
        print(f"{{{','.join(exported)}}}\n")


class DataStream(ABC):
    def __init__(self) -> None:
        self._data: list[tuple[int, str]] = []
        self._processors: list = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        for element in stream:
            processed: bool = False
            for processor in self._processors:
                if (processor.validate(element) is True):
                    processor.ingest(element)
                    processed = True
                    break
            if processed is False:
                print("DataStream error - "
                      f"Can't process element on stream: {element}")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if (len(self._processors) != 0):
            for processor in self._processors:
                print(f"{type(processor).__name__}: total {processor._stats} "
                      "items processed, "
                      f"remaining {len(processor._data)} on procesor")
        else:
            print("No processor found, no data\n")

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        to_plugin = [

        ]
        for processor in self._processors:
            if not processor._data:
                pass
            else:
                for i in range(nb):
                    if not processor._data:
                        break
                    else:
                        to_plugin.append(processor.output())
                plugin.process_output(to_plugin)
                to_plugin.clear()


class NumericProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
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
                        self._stats += 1
            else:
                self._data.append((self._next_rank, str(data)))
                self._next_rank += 1
                self._stats += 1


class TextProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
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
                        self._stats += 1
            else:
                self._data.append((self._next_rank, data))
                self._next_rank += 1
                self._stats += 1


class LogProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
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
                        string: str = (
                            f"{item['log_level']}: "
                            f"{item['log_message']}"
                        )
                        self._data.append((self._next_rank, string))
                        self._next_rank += 1
                        self._stats += 1
            else:
                self._data.append((self._next_rank, str(data)))
                self._next_rank += 1
                self._stats += 1


def main() -> None:
    print("=== Code Nexus - Data Pipeline ===\n")
    print("Initialize Data Stream...")
    data_stream: DataStream = DataStream()
    data_stream.print_processors_stats()
    print("Registering Processors\n")
    numeric_processor: NumericProcessor = NumericProcessor()
    data_stream.register_processor(numeric_processor)
    text_processor: TextProcessor = TextProcessor()
    data_stream.register_processor(text_processor)
    log_processor: LogProcessor = LogProcessor()
    data_stream.register_processor(log_processor)
    stream = [
            "Hello world",
            [3.14, -1, 2.71],
            [
                {
                    "log_level": "WARNING",
                    "log_message": "Telnet access! Use ssh instead"
                },
                {
                    "log_level": "INFO",
                    "log_message": "User wil is connected"
                }
            ],
            42,
            ["Hi", "five"]
        ]
    print("Send first batch of data on stream: "
          "['Hello world', [3.14, -1, 2.71], "
          "[{'log_level': 'WARNING', '"
          "log_message': 'Telnet access! Use ssh instead'}, "
          "{'log_level': 'INFO', 'log_message': 'User wil is"
          "connected'}], 42, ['Hi', 'five']]\n")
    data_stream.process_stream(stream)
    data_stream.print_processors_stats()
    print()
    print("Send 3 processed data from each processor to a CVS plugin: ")
    csv_plugin: CSVExporter = CSVExporter()
    json_plugin: JSONExporter = JSONExporter()
    data_stream.output_pipeline(3, csv_plugin)
    data_stream.print_processors_stats()
    new_stream = [
        21,
        [
            'I love AI',
            'LLMs are wonderful',
            'Stay healthy'
        ],
        [
            {
               'log_level': 'ERROR', 'log_message': '500 server crash'
            },
            {
                'log_level': 'NOTICE', 'log_message':
                'Certificate expires in 10 days'
            }
        ],
        [
            32, 42, 64, 84, 128, 168
        ],
        'World hello'
    ]
    print()
    print("Send another batch of data: "
          "[21, ['I love AI', 'LLMs are wonderful', 'Stay healthy'], "
          "[{'log_level': 'ERROR', 'log_message': '500 server crash'}, "
          "{'log_level': 'NOTICE', 'log_message': "
          "'Certificate expires in 10 days'}, "
          "[32, 42, 64, 84, 128, 168], 'World hello']\n")
    data_stream.process_stream(new_stream)
    data_stream.print_processors_stats()
    print()
    print("Send 5 processed data from each processor to a JSON plugin: ")
    data_stream.output_pipeline(5, json_plugin)
    print()
    data_stream.print_processors_stats()


if __name__ == ("__main__"):
    main()
