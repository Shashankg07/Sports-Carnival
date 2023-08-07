from abc import ABC, abstractmethod


class ITeamRepository(ABC):

    @abstractmethod
    def get_last_inserted_team_id(self) -> int | Exception:
        pass

    @abstractmethod
    def create_team(self, team_details: list) -> int:
        pass
