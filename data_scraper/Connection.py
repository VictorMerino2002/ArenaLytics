import mysql.connector
from mysql.connector import Error

class Connection:
    _connection = None

    @staticmethod
    def connect(host, database, user, password):
        if Connection._connection is None:
            try:
                Connection._connection = mysql.connector.connect(
                    host = host,
                    database = database,
                    user = user,
                    password = password
                )

                if Connection.is_connected():
                    print("Connected to the database")
            except Error as e:
                print("Error trying to connect to database", e)

    @staticmethod
    def get_connection():
        if Connection._connection is None:
            print("The connection has not been established.")
        return Connection._connection
    
    @staticmethod
    def close_connection():
        if Connection.is_connected():
            Connection._connection.close()
            Connection._connection = None

    @staticmethod
    def is_connected():
        return Connection._connection is not None and Connection._connection.is_connected()
