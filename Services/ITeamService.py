from abc import ABC, abstractmethod


class ITeamService(ABC):

    @abstractmethod
    def create_teams_output(self, game_type: int, details: list) -> dict | Exception:
        pass