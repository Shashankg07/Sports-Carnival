from abc import ABC, abstractmethod

import mysql.connector


class IDBConnection(ABC):

    @abstractmethod
    def database_connection(self) -> mysql.connector.connection.MySQLConnection:
        pass

    @abstractmethod
    def close_connection(self, connection: mysql.connector.connection.MySQLConnection):
        pass
