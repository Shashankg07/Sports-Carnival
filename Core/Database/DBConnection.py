import mysql.connector
from Configuration.Config import DatabaseConstraints
from Core.Database.IDBConnection import IDBConnection


class DBConnection(IDBConnection):
    def __init__(self):
        self.__host = DatabaseConstraints.host
        self.__port = DatabaseConstraints.port
        self.__user = DatabaseConstraints.user
        self.__database = DatabaseConstraints.database

    def database_connection(self) -> mysql.connector.connection.MySQLConnection:
        try:
            database_connection: mysql.connector.connection.MySQLConnection = mysql.connector.connect(
                host=self.__host,
                port=self.__port,
                user=self.__user,
                database=self.__database
            )
            return database_connection
        except Exception as err:
            raise err

    def close_connection(self, connection: mysql.connector.connection.MySQLConnection):
        connection.close()
