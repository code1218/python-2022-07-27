import pymysql

class DBConnection:
    host = '127.0.0.1'
    port = 3306
    user = 'root'
    password = 'toor'
    database = 'python_study'

    connection = None

    def __init__(self):
        print("DataBase 객체 생성")

    def connect(self):
        self.connection = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            database=self.database
        )
        return self.connection

    def close(self):
        self.connection.close()

    def getCursor(self):
        return self.connection.cursor(pymysql.cursors.DictCursor)

    def commit(self):
        self.connection.commit()

