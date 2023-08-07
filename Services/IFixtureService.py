from abc import ABC, abstractmethod


class FixtureService(ABC):

    @abstractmethod
    def create_fixture(self, teams_data: dict) -> dict | Exception:
        pass
