from abc import ABC, abstractmethod


class IFileHandler(ABC):
    @abstractmethod
    def read_file(self, input_file_path: str) -> dict | Exception:
        pass

    @abstractmethod
    def write_file(self, output_file_path: str, data: list):
        pass