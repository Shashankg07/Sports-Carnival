from Configuration.Config import GameType
from Configuration.Config import NoOfPlayers


class PlayerCount:
    def __init__(self):
        self.game_type = GameType
        self.no_of_players = NoOfPlayers
        self.total_players: int = 0

    def players_per_team(self, game_type: int) -> int | Exception:
        try:
            if game_type == self.game_type.CRICKET.value:
                self.total_players = self.no_of_players.CRICKET.value
            elif game_type == self.game_type.BADMINTON.value:
                self.total_players = self.no_of_players.BADMINTON.value
            elif game_type == self.game_type.CHESS.value:
                self.total_players = self.no_of_players.CHESS.value
            return self.total_players
        except Exception as err:
            raise err
