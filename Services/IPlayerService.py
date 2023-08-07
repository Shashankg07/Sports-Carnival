from abc import ABCMeta, abstractmethod


class IPLayerService(metaclass=ABCMeta):

    @abstractmethod
    def create_players_list(self, players_list: list, game_type: int) -> list | Exception:
        pass