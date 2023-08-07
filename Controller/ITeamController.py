from abc import ABC, abstractmethod


class ITeamController(ABC):

    @abstractmethod
    def create_team(self, input_file_path: str) -> list | Exception:
        pass

    @abstractmethod
    def save_team(self, output_file_path: str, data: list):
        pass
