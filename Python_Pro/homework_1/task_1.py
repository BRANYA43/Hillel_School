from sql_handler import SQLHandler

sql_handler = SQLHandler()
sql_handler.set_path_db('chinook.db')


def get_repeated_name_group():
    MIN = 1
    QUANTITY = 0
    repeated_name_groups = sql_handler.execute_query('''
      SELECT COUNT(CustomerId), FirstName
        FROM customers
    GROUP BY FirstName
    ''')
    return [group for group in repeated_name_groups if group[QUANTITY] > MIN]


if __name__ == '__main__':
    print(get_repeated_name_group())
