from Controller.ITeamController import ITeamController
from Models.TeamsOutput import TeamsOutput
from Services.PlayerService import PlayerService
from Utils.FIleHandler import FileHandler
from Services.TeamService import TeamService
from Validations.Validate import Validate
from Validations.CustomException import NullValueException


class TeamController(ITeamController):
    def __init__(self):
        self.__player_details = PlayerService()
        self.__file_handler = FileHandler()
        self.__team_service = TeamService()
        self.__validator = Validate()

    def create_team(self, input_data) -> TeamsOutput | Exception:
        try:
            self.__validator.check_null_input(input_data['players'])
            details = self.__player_details.create_players_list(input_data['players'], input_data['gameType'])
            return self.__team_service.create_teams_output(input_data['gameType'], details)
        except NullValueException as err:
            raise err

    def save_team(self, output_file_path: str, data: TeamsOutput):
        temp = []
        for teams in data.teams:
            temp.append(teams.__dict__)
        data.teams = temp
        self.__file_handler.write_file(output_file_path, data.__dict__)
