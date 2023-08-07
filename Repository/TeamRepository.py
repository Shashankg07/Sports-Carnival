import mysql.connector

from Core.Database.queries.SQLQuery import SQLQuery
from Core.Database.DBConnection import DBConnection
from Repository.ITeamRepository import ITeamRepository


class TeamRepository(ITeamRepository):
    def __init__(self):
        self.__sql_query = SQLQuery()
        self.__db_connection = DBConnection().database_connection()

    def get_last_inserted_team_id(self) -> int | Exception:
        try:
            __get_last_team_id: str = self.__sql_query.get_last_inserted_team_id
            __cursor: mysql.connector.connection.MySQLConnection.cursor = self.__db_connection.cursor()
            __cursor.execute(__get_last_team_id)
            last_team_id: int = 0
            for row in __cursor:
                last_team_id = row[0]
            return last_team_id
        except Exception as err:
            raise err

    def create_team(self, team_details: list) -> int:
        try:
            __cursor: mysql.connector.connection.MySQLConnection.cursor = self.__db_connection.cursor()
            __insert_team_query: str = self.__sql_query.insert_team_query
            for teams in team_details:
                __val: tuple = (teams.team_id, teams.team_name, 1, teams.game_type)
                __cursor.execute(__insert_team_query, __val)
            self.__db_connection.commit()
            return __cursor.rowcount
        except Exception as err:
            raise err
        finally:
            DBConnection().close_connection(self.__db_connection)
