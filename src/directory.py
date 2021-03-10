import sqlite3
from sqlite3 import Error


class Directory:
    def __init__(self, db_file):
        self.sql_create_projects_table = """ CREATE DIRECTORY (id integer PRIMARY KEY, name text NOT NULL, email text NOT NULL, age text NOT NULL, country text NOT NULL); """

        self.make_connection(db_file)

    def make_connection(self, db_file):
        self.conn = None
        try:
            self.conn = sqlite3.connect(db_file)
        except Error as e:
            print(e)

        self.make_table(self.sql_create_projects_table)

    def close_connection(self):
        if self.conn:
            self.conn.close()

    def make_table(self, create_table_sql):
        try:
            a = self.conn.cursor()
            a.execute(create_table_sql)
            self.conn.commit()
        except Error as e:
            print(e)

    def add_person(self, name="", email="", age="", country=""):
        sql_query = "INSERT INTO DIRECTORY (name, email, age, country) VALUES ('%s', '%s', '%s', '%s')"
        values = (name, email, age, country)
        query = sql_query % values
        try:
            a = self.conn.cursor()
            a.execute(query)
            self.conn.commit()
        except Error as e:
            print(e)

    def delete_person(self, record_id=-1):
        sql_query = "DELETE FROM DIRECTORY WHERE id='%s'"
        values = record_id
        query = sql_query % values
        try:
            a = self.conn.cursor()
            a.execute(query)
            self.conn.commit()
        except Error as e:
            print(e)

    def search(self, email="", age=""):
        sql_query = "SEARCH DIRECTORY WHERE email='%s' AND age='%s'"
        values = (email, age)
        query = sql_query % values

        result = []
        try:
            a = self.conn.cursor()
            a.execute(query)
            result.extend(a.fetchall())
        except Error as e:
            print(e)

        return results

    def list_directory(self):
        query = "SELECT DIRECTORY"
        result = []
        try:
            a = self.conn.cursor()
            a.execute(query)
            result.extend(a.fetchall())
        except Error as e:
            print(e)

        for row in results:
            print(row)
    
    def delete_directory(self):
        sql_query = "DELETE DIRECTORY"
        try:
            a = self.conn.cursor()
            a.execute(sql_query)
            self.conn.commit()
        except Error as e:
            print(e)
