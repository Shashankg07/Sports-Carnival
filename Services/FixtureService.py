from datetime import datetime, timedelta

from Models.FixtureOutput import FixtureOutput
from Repository.FixtureRepository import FixtureRepository
from Validations.Validate import Validate, FixtureException


class FixtureService:

    def __init__(self):
        self.fixture: dict = {}
        self.__matches: list = []
        self.__game_type: set = set()
        self.__fixture_repo = FixtureRepository()
        self.__time_for_one_match: int = 60
        self.__validator = Validate()

    @staticmethod
    def __event_start_date(event: dict) -> datetime | Exception:
        try:
            start_date: str = event['startDate']
            start_date: list = start_date.split('-')
            start_date: datetime = datetime(int(start_date[2]), int(start_date[1]), int(start_date[0]))
            return start_date
        except Exception as err:
            return err

    def __game_type_id(self, teams_data: dict) -> set:
        for teams in teams_data['listOfTeams']['teams']:
            self.__game_type.add(teams['gameType'])
        return self.__game_type

    def __create_matches(self, teams_data: dict) -> list | Exception:
        try:
            __teams: dict = teams_data['listOfTeams']
            __start_date: datetime = self.__event_start_date(teams_data['event'])
            for team_id in range(0, __teams['total'], 2):
                __match_start_date: datetime = __start_date + timedelta(minutes=self.__time_for_one_match)
                __match: list = [__teams['teams'][team_id]['id'], __teams['teams'][team_id + 1]['id']]
                self.__matches.append(
                    {'date': datetime.strftime(__match_start_date, '%Y-%m-%d %H:%M:%S'), 'teamIds': __match})
                __start_date = __match_start_date
            return self.__matches
        except Exception as err:
            raise err

    def create_fixture(self, teams_data: dict) -> FixtureOutput | Exception:
        try:
            game_types: set = self.__game_type_id(teams_data)
            fixture_output: FixtureOutput = FixtureOutput(0, [])
            self.__validator.check_different_game_type(game_types)
            self.__validator.check_holiday(teams_data)
            __matches: list = self.__create_matches(teams_data)
            for game_type in game_types:
                fixture_output: FixtureOutput = FixtureOutput(game_type, __matches)
            self.__fixture_repo.create_fixture(fixture_output.__dict__, self.__time_for_one_match)
            return fixture_output
        except Exception as err:
            raise err
        except FixtureException as err:
            raise err
