import mysql.connector
from constants import MYSQL_DATABASE, MYSQL_PASSWORD, MYSQL_USER, MYSQL_HOST


class Model:
    def connect_database(self):
        db = mysql.connector.connect(
          host=MYSQL_HOST,
          user=MYSQL_USER,
          password=MYSQL_PASSWORD,
          database=MYSQL_DATABASE
        )
        return db


    def insert_into_table(self, sql_request, values):
        cursor, db = self.connect_cursor()
        # Execute the request
        cursor.execute(sql_request, values)
        db.commit()

    def connect_cursor(self):
        db = self.connect_database()
        cursor = db.cursor()
        return cursor, db

    @staticmethod
    def insert_into_database(sql_request, values, error_message=""):
        model = Model()
        try:
            model.insert_into_table(sql_request, values)
        except Exception as e:
            print(str(e))

    @staticmethod
    def read_all_from_database(sql_request):
        model = Model()
        cursor, db = model.connect_cursor()
        cursor.execute(sql_request)
        # Close the connection
        data = cursor.fetchall()
        cursor.close()
        db.close()
        return data

    @staticmethod
    def read_from_database(sql_request, callback):
        model = Model()
        cursor, db = model.connect_cursor()
        # SQL query
        # Execute the query
        cursor.execute(sql_request)
        # Fetch one row at a time
        row = cursor.fetchone()
        while row is not None:
            row = cursor.fetchone()
            callback(row)
        # Close the connection
        cursor.close()
        db.close()
