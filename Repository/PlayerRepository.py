import mysql.connector.connection

from Core.Database.DBConnection import DBConnection
from Core.Database.queries.SQLQuery import SQLQuery
from Repository.IPlayerRepository import IPlayerRepository


class PlayerRepository(IPlayerRepository):

    def __init__(self):
        self.__db_connection = DBConnection().database_connection()
        self.__sql_query = SQLQuery()

    def __get_last_inserted_player_id(self) -> int | Exception:
        try:
            __get_last_player_id: str = self.__sql_query.get_last_inserted_player_id
            __cursor: mysql.connector.connection.MySQLConnection.cursor = self.__db_connection.cursor()
            __cursor.execute(__get_last_player_id)
            last_player_id = 0
            for row in __cursor:
                last_player_id = row[0]
            return last_player_id
        except Exception as err:
            return err

    def __get_last_inserted_team_player_id(self) -> int | Exception:
        try:
            __get_last_team_player_id: str = self.__sql_query.get_last_inserted_team_player_id
            __cursor: mysql.connector.connection.MySQLConnection.cursor = self.__db_connection.cursor()
            __cursor.execute(__get_last_team_player_id)
            last_team_player_id = 0
            for row in __cursor:
                last_team_player_id = row[0]
            return last_team_player_id
        except Exception as err:
            return err

    def save_player(self, players_list: list) -> int:
        try:
            __cursor: mysql.connector.connection.MySQLConnection.cursor = self.__db_connection.cursor()
            __insert_player_query: str = self.__sql_query.insert_player_query
            __player_id: int = self.__get_last_inserted_player_id()
            for player in range(len(players_list)):
                __player_id += 1
                __val: tuple = (__player_id, players_list[player]['name'])
                __cursor.execute(__insert_player_query, __val)
            self.__db_connection.commit()
            return __cursor.rowcount
        except Exception as err:
            raise err
        finally:
            DBConnection().close_connection(self.__db_connection)

    def save_team_player(self, team_details: list) -> int:
        try:
            __cursor: mysql.connector.connection.MySQLConnection.cursor = self.__db_connection.cursor()
            __insert_team_player_query: str = self.__sql_query.insert_team_player_query
            __team_player_id: int = self.__get_last_inserted_team_player_id()
            for team in range(len(team_details)):
                for players_id in range(len(team_details[team].players)):
                    __team_player_id += 1
                    __val: tuple = (__team_player_id, team_details[team].players[players_id]['playerId'], team_details[team].team_id)
                    __cursor.execute(__insert_team_player_query, __val)
            self.__db_connection.commit()
            return __cursor.rowcount
        except Exception as err:
            raise err
        finally:
            DBConnection().close_connection(self.__db_connection)