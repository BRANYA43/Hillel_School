import sqlite3
import os


class SQLHandler:
    def __init__(self):
        self._db_pass = None

    def execute_query(self, query: str) -> list[tuple]:
        with sqlite3.connect(self._db_pass) as connection:
            cur = connection.cursor()
            cur.execute(query)
            return cur.fetchall()

    def set_path_db(self, file: str):
        self._db_pass = os.path.join(os.getcwd(), file)


if __name__ == '__main__':
    print('Modul: sql_handler')


