from Repository.PlayerRepository import PlayerRepository
from Utils.PlayerCount import PlayerCount
from Services.IPlayerService import IPLayerService


class PlayerService(IPLayerService):
    def __init__(self):
        self.__no_of_players = PlayerCount()
        self.list_of_players: list = []
        self.__player_repo = PlayerRepository()

    def create_players_list(self, players_list: list, game_type: int) -> list | Exception:
        try:
            __start_index: int = 0
            __end_index: int = len(players_list)
            __total_players_per_team: int = self.__no_of_players.players_per_team(game_type)
            for each_player_index in range(__start_index, __end_index, __total_players_per_team):
                __first_player_index: int = each_player_index
                self.list_of_players.append(players_list[__first_player_index:__first_player_index + __total_players_per_team])
            self.__player_repo.save_player(players_list)
            return self.list_of_players
        except Exception as err:
            raise err
