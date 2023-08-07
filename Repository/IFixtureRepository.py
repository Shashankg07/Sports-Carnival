from abc import ABC, abstractmethod


class IFixtureRepository(ABC):

    @abstractmethod
    def create_fixture(self, fixture: dict, time_for_one_match: int) -> int:
        pass
