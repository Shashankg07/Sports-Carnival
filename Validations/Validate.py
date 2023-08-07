from Configuration.Config import Command
from Validations.CustomException import NullValueException, FixtureException
from datetime import datetime, timedelta


class Validate:
    def __init__(self):
        self.null_exception = NullValueException
        self.fixture_exception = FixtureException

    def check_null_input(self, players_list: list):
        try:
            if not players_list:
                raise self.null_exception("player's list cannot be empty")
            for players in players_list:
                if players['playerId'] is None:
                    raise self.null_exception("player id cannot be null")
                if players['name'] is None:
                    raise self.null_exception("player's name cannot be null")
        except self.null_exception as err:
            raise err

    def check_different_game_type(self, game_type: set):
        try:
            if len(game_type) > 1:
                raise self.fixture_exception("there cannot be multiple game type for single fixture")
        except self.fixture_exception as err:
            raise err

    def command_validator(self, command: list) -> bool:
        if command[0] != Command.trigger:
            return True
        if command[1] != Command.method_trigger:
            return True
        if command[3] != Command.input_file_trigger:
            return True
        if command[5] != Command.output_file_trigger:
            return True

    def check_holiday(self, input_data: dict):
        try:
            start_date: datetime = datetime.strptime(input_data['event']['startDate'], "%d-%m-%Y")
            end_date: datetime = datetime.strptime(input_data['event']['endDate'], "%d-%m-%Y")
            date_range: list[datetime] = [start_date + timedelta(n) for n in range(int((end_date - start_date).days) + 1)]
            holiday_dates: list = []
            holiday_list: list = input_data['holidayList']
            for holidays in holiday_list:
                holiday_dates.append(holidays['date'])
            for date in date_range:
                for holiday in holiday_dates:
                    if date.strftime("%d-%m-%Y") == holiday:
                        date_range.remove(date)
            if not date_range:
                raise self.fixture_exception("cannot create fixture on holiday")
        except self.fixture_exception as err:
            raise err
