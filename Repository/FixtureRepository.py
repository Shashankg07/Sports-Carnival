import mysql.connector.connection

from Core.Database.DBConnection import DBConnection
from Core.Database.queries.SQLQuery import SQLQuery
from Repository.IFixtureRepository import IFixtureRepository


class FixtureRepository(IFixtureRepository):
    def __init__(self):
        self.__db_connection = DBConnection().database_connection()
        self.__sql_query = SQLQuery()

    def __get_last_inserted_fixture_id(self) -> int | Exception:
        try:
            __get_last_fixture_id: str = self.__sql_query.get_last_inserted_fixture_id
            __cursor: mysql.connector.connection.MySQLConnection.cursor = self.__db_connection.cursor()
            __cursor.execute(__get_last_fixture_id)
            last_fixture_id: int = 0
            for row in __cursor:
                last_fixture_id = row[0]
            return last_fixture_id
        except Exception as err:
            raise err

    def create_fixture(self, fixture: dict, time_for_one_match: int) -> int:
        try:
            __cursor: mysql.connector.connection.MySQLConnection.cursor = self.__db_connection.cursor()
            __last_fixture_id: int = self.__get_last_inserted_fixture_id()
            __query: str = self.__sql_query.insert_fixture_query
            for value in fixture['matches']:
                __last_fixture_id += 1
                __val: tuple = (__last_fixture_id, value['date'], value['teamIds'][0], value['teamIds'][1], time_for_one_match)
                __cursor.execute(__query, __val)
            self.__db_connection.commit()
            return __cursor.rowcount
        except Exception as err:
            raise err
        finally:
            DBConnection().close_connection(self.__db_connection)
