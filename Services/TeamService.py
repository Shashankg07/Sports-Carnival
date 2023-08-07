from Models.Team import Team
from Models.TeamsOutput import TeamsOutput
from Repository.PlayerRepository import PlayerRepository
from Repository.TeamRepository import TeamRepository
from Services.ITeamService import ITeamService


class TeamService(ITeamService):
    def __init__(self):
        self.__team_repository = TeamRepository()
        self.__player_repository = PlayerRepository()

    @staticmethod
    def __total_teams(teams_list: list) -> int:
        return len(teams_list)

    @staticmethod
    def __create_team(team_id: int, game_type: int) -> Team | Exception:
        try:
            team_list: Team = Team(team_id, f"Team - {team_id}", game_type, [])
            return team_list
        except Exception as err:
            raise err

    def __create_teams_list(self, game_type: int, details: list) -> list | Exception:
        try:
            teams_list: list = []
            __team_id: int = self.__team_repository.get_last_inserted_team_id()
            for playerIndex in range(self.__total_teams(details)):
                __team_id += 1
                __team: Team = self.__create_team(__team_id, game_type)
                __team.players = details[playerIndex]
                teams_list.append(__team)
            self.__team_repository.create_team(teams_list)
            self.__player_repository.save_team_player(teams_list)
            return teams_list
        except Exception as err:
            raise err

    def create_teams_output(self, game_type: int, details: list) -> TeamsOutput | Exception:
        try:
            __teams_list: list = self.__create_teams_list(game_type, details)
            __total_teams: int = self.__total_teams(__teams_list)
            output_dict: TeamsOutput = TeamsOutput(__teams_list, __total_teams)
            return output_dict
        except Exception as err:
            raise err
