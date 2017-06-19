class DbClass:
    def __init__(self):
        import mysql.connector as connector

        self.__dsn = {
            "host": "localhost",
            "user": "root",
            "passwd": "Bjarne1021",
            "db": "project"
        }

        self.__connection = connector.connect(**self.__dsn)
        self.__cursor = self.__connection.cursor()

    def getneerslag(self):
        sql = "SELECT neerslag FROM project_db ORDER BY ID DESC LIMIT 1"
        self.__cursor.execute(sql)
        result = self.__cursor.fetchall()
        result = str(result).replace(',)]', '')
        result = str(result).replace('[(', '')
        self.__cursor.close()
        return result

    def gettemperatuur(self):
        sql = "SELECT temp FROM project_db ORDER BY ID DESC LIMIT 1"
        self.__cursor.execute(sql)
        result = self.__cursor.fetchall()
        result = str(result).replace(',)]', '')
        result = str(result).replace('[(', '')
        self.__cursor.close()
        return result

    def getluchtvochtigheid(self):
        sql = "SELECT luchtvochtigheid FROM project_db ORDER BY ID DESC LIMIT 1"
        self.__cursor.execute(sql)
        result = self.__cursor.fetchall()
        result = str(result).replace(',)]', '')
        result = str(result).replace('[(', '')
        self.__cursor.close()
        return result

