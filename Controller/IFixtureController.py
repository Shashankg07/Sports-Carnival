from abc import ABC, abstractmethod


class IFixtureController(ABC):

    @abstractmethod
    def create_fixture(self, input_file_path: str) -> dict | Exception:
        pass

    @abstractmethod
    def save_fixture(self, output_file_path: str, data: list):
        pass
