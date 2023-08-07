from enum import Enum


class NoOfPlayers(Enum):
    CRICKET = 11
    BADMINTON = 2
    CHESS = 1


class GameType(Enum):
    CRICKET = 1
    BADMINTON = 2
    CHESS = 3


class DatabaseConstraints:
    host = "localhost"
    port = 3306
    user = "root"
    database = "workshop"


class ClientConstraints:
    sourceIp = "127.0.0.1"
    sourcePort = 3308


class ServerConstraints:
    destIp = "127.0.0.1"
    destPort = 3308


class Command:
    trigger = "isc"
    create_team_method = "create_team"
    create_fixture_method = "create_fixture"
    encoding = "utf-8"
    success = "SUCCESS"
    error = "ERROR"
    method_trigger = "-a"
    input_file_trigger = "-i"
    output_file_trigger = "-o"

