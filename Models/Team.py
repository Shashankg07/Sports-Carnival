from Models.PlayerList import PlayerList


class Team:
    def __init__(self, team_id: int, team_name: str, game_type: int, players: list):
        self.team_id = team_id
        self.team_name = team_name
        self.game_type = game_type
        self.players = PlayerList(players)