from abc import ABC, abstractmethod


class IPlayerRepository(ABC):

    @abstractmethod
    def save_player(self, players_list: list) -> int:
        pass

    @abstractmethod
    def save_team_player(self, team_details: list) -> int:
        pass
