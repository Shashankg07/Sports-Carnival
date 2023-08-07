import json
from typing import TextIO

from Utils.IFileHandler import IFileHandler


class FileHandler(IFileHandler):
    def read_file(self, input_file_path: str) -> dict | Exception:
        try:
            file: TextIO = open(input_file_path)
            data: dict = json.load(file)
            return data
        except Exception as err:
            raise err

    def write_file(self, output_file_path: str, data: dict):
        try:
            with open(output_file_path, 'w') as file:
                json.dump(data, file)
        except Exception as err:
            raise err
