import mysql.connector
from mysql.connector import connection

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
    def insert_into_database(sql_request, values):
        model = Model()
        try:
            model.insert_into_table(sql_request, values)
        except Exception as e:
            print(str(e))


    @staticmethod
    def read_from_database(sql_request):
        model = Model()
        cursor, db = model.connect_cursor()
        cursor.execute(sql_request)
        # Close the connection
        data = cursor.fetchall()
        cursor.close()
        db.close()
        return data

    @staticmethod
    def read_from_database_and_callback(sql_request, callback):
        model = Model()
        cursor, db = model.connect_cursor()
        # SQL query
        # Execute the query
        cursor.execute(sql_request)
        # Fetch one row at a time
        row = cursor.fetchone()
        while row is not None:
            callback(row)
            row = cursor.fetchone()
        # Close the connection
        cursor.close()
        db.close()

    @staticmethod
    def update_database(sql_update, values):
        model = Model()
        cursor, db = model.connect_cursor()
        # Execute the update
        try:
            cursor.execute(sql_update, values)
            db.commit()
            print("Update successful.")

        except mysql.connector.Error as error:
            print(f"Failed to update entry: {error}")
            db.rollback()  # Roll back if there’s an error

        finally:
            # Close the cursor and connection
            if db.is_connected():
                cursor.close()
                db.close()