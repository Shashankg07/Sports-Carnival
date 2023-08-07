from Controller.IFixtureController import IFixtureController
from Utils.FIleHandler import FileHandler
from Services.FixtureService import FixtureService
from Validations.CustomException import FixtureException


class FixtureController(IFixtureController):
    def __init__(self):
        self.__file_handler = FileHandler()
        self.__fixture_service = FixtureService()

    def create_fixture(self, input_data) -> dict | Exception:
        try:
            return self.__fixture_service.create_fixture(input_data)
        except Exception as err:
            raise err
        except FixtureException as err:
            raise err

    def save_fixture(self, output_file_path: str, data: dict):
        self.__file_handler.write_file(output_file_path, data.__dict__)
